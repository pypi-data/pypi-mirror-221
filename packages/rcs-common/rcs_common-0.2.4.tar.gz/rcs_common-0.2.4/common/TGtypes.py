import numpy as np
import math


class TGConfig:
    abs_minimal_speed = 0.00000001
    default_min_speed = 5.0
    default_max_speed = 12.0
    manned_speed = 55.0


class TGPosition:
    lon: float
    lat: float
    alt: float

    def __init__(self, lon, lat, alt):
        self.lon = lon
        self.lat = lat
        self.alt = alt

    # calc distance in m between two TGPositions,given in
    # geographic coordinate system.
    def gsc2distance(self,other):
        factor_x = 111111.0 * math.cos(math.pi*self.lat/180.0)
        factor_y = 111111.0
        dlon = math.fabs(self.lon - other.lon)*factor_x
        dlat = math.fabs(self.lat - other.lat)*factor_y
        dalt = math.fabs(self.alt - other.alt)
        return math.sqrt(dlon*dlon + dlat*dlat + dalt*dalt)

    def gsc2distance_xy(self, other):
        factor_x = 111111.0 * math.cos(math.pi * self.lat / 180.0)
        factor_y = 111111.0
        dlon = math.fabs(self.lon - other.lon) * factor_x
        dlat = math.fabs(self.lat - other.lat) * factor_y
        return math.sqrt(dlon * dlon + dlat * dlat)

    def as_point3D(self):
        lon = self.lon*111111.0 * math.cos(self.lon)
        lat = self.lat*111111.0
        alt = self.alt
        return Point3D(lon,lat,alt)


class TGSegment:
    # a container for a segment
    position: TGPosition
    speed: float
    delay: float
    required:bool

    def __init__(self, position:TGPosition, speed, delay, required = True):
        self.position = position
        self.speed = speed
        self.delay = delay
        self.required = required


class  TGTimeTable:

    initial_delay: float # delay before we start the path
    mat: np.array

    def __init__(self,  delay):
        self.initial_delay = delay


    def Generate(self, initial_position:TGPosition, seg_list:list[TGSegment], is_manned = False, in_current_speed = -1.0):

        rel_time  = 0.0
        path_len = len(seg_list)
        if  path_len == 0:
            return None
        else:
            next_seg_speed = True
            # we create a matrix,with the following fields
            # in each row
            # relative time (sec),lon, lat, alt, speed
            # for each segment there are two entries, one
            #    for the delay period, one for the path itself.
            self.mat = np.zeros((2*path_len+1,5))
            current_position = initial_position
            if in_current_speed <= 0.0:
                current_speed = (TGConfig.default_min_speed + TGConfig.default_max_spSeed)/2.0 # default
            else:
                current_speed = max(in_current_speed, TGConfig.abs_minimal_speed)
            if is_manned:
                current_speed = TGConfig.manned_speed
            if next_seg_speed is True:
                current_speed = seg_list[1].speed
            self.mat[0,0] = rel_time
            self.mat[0,1] = initial_position.lon
            self.mat[0,2] = initial_position.lat
            self.mat[0,3] = initial_position.alt
            self.mat[0,4] = current_speed

            for i in range(0, path_len):
                current_speed = max(current_speed, TGConfig.abs_minimal_speed)
                if is_manned:
                    current_speed = TGConfig.manned_speed
                ii = 2*i + 1
                seg_position = seg_list[i].position
                dist = seg_position.gsc2distance(current_position)
                dt   = dist/current_speed
                rel_time += dt
                # build a delay entry
                self.mat[ii,0] = rel_time
                self.mat[ii,1] = seg_list[i].position.lon
                self.mat[ii,2] = seg_list[i].position.lat
                self.mat[ii,3] = seg_list[i].position.alt
                self.mat[ii,4] = 0.0
                # build a segment entry
                rel_time += seg_list[i].delay
                self.mat[ii+1,0] = rel_time
                self.mat[ii+1,1] = seg_list[i].position.lon
                self.mat[ii+1,2] = seg_list[i].position.lat
                self.mat[ii+1,3] = seg_list[i].position.alt
                current_position = seg_list[i].position

                if next_seg_speed is True:
                    if i < path_len - 1:
                        self.mat[ii + 1, 4] = max(seg_list[i+1].speed, TGConfig.abs_minimal_speed)
                        current_speed = seg_list[i+1].speed
                    else:
                        self.mat[ii + 1, 4] = 5.0 # doesnt really matter
                        current_speed = 5.0
                else:
                    self.mat[ii+1,4] = max (seg_list[i].speed, TGConfig.abs_minimal_speed)
                    current_speed = seg_list[i].speed

            return rel_time



    def PositionForRelativeTime(self, dt: float)->TGPosition:
        # return the position and poi index
        # per a given relative time in seconds
        # get a relative time from start point
        # if mat is empty, return None
        # if dt lower than the first time, return initial position
        # if dt higher than the last time, return the last position
        # if dt points into delay entry, return its position
        # if it points to a segment entry, take the point on the segment
        # leading to the next position, based on the delta time between the two positions
        # and the dt - t(entry).
        pos:TGPosition =TGPosition (0,0,0)
        sync_data_delay = 0.0  # remaining delay - initially undefined.
        if self.mat.size > 0:
            dt1 = dt - self.initial_delay
            if dt1 <= self.mat[0, 0]:
                pos = TGPosition(self.mat[0, 1], self.mat[0, 2], self.mat[0, 3])

            else:
                rows = (np.shape(self.mat))[0]
                if dt1 >= self.mat[rows-1, 0]:
                    pos = TGPosition(self.mat[rows-1, 1], self.mat[rows-1, 2], self.mat[rows-1, 3])
                else:
                    ind = 0
                    for i in range(0, rows-1):
                        if dt1 >= self.mat[i, 0] and dt1 < self.mat[i+1, 0]:
                            ind = i
                            break
                    if self.mat[ind, 4] == 0.0:  # a delay entry
                        pos = TGPosition(self.mat[ind, 1], self.mat[ind, 2], self.mat[ind, 3])
                        sync_data_delay = self.mat[i+1, 0] - dt1 # remaining delay
                    else :
                        sync_data_delay = 0.0
                        dt2 = self.mat[ind+1, 0] - self.mat[ind, 0]
                        dt3 = dt1 - self.mat[ind, 0]
                        dt_ratio = dt3/dt2
                        new_lon = self.mat[ind, 1] + dt_ratio*(self.mat[ind+1, 1] - self.mat[ind, 1])
                        new_lat = self.mat[ind, 2] + dt_ratio*(self.mat[ind+1, 2] - self.mat[ind, 2])
                        new_alt = self.mat[ind, 3] + dt_ratio*(self.mat[ind+1, 3] - self.mat[ind, 3])
                        pos = TGPosition(new_lon, new_lat, new_alt)

        return pos, sync_data_delay

    def PositionsForRelativeTimeWithNoise(self, dt: float, angle_noise, speed_noise, micro_dt) -> [TGPosition]:
        # return the 2 positions with added noise
        # dt -relative time for start, angle_noise ( angular noise on the segment, speed_noise (+/- %/100)
        #      micro_dt time in seconds between two positions points
        # get a relative time from start point
        # if mat is empty, return None
        # if dt lower than the first time, return initial position
        # if dt higher than the last time, return the last position
        # if dt points into delay entry, return its position (no noise on delay)
        # if it points to a segment entry, take the point on the segment,
        # leading to the next position, based on the delta time between the two positions
        #  and the dt - t(entry).
        #  add the noise, and calculate
        # its vector to the correct next poi
        pos1: TGPosition = TGPosition(0, 0, 0)
        pos2: TGPosition = TGPosition(0, 0, 0)
        if self.mat.size > 0:

            dt1 = dt - self.initial_delay
            if dt1 <= self.mat[0, 0]:
                pos1 = TGPosition(self.mat[0, 1], self.mat[0, 2], self.mat[0, 3])
                pos2 = pos1
            else:
                rows = (np.shape(self.mat))[0]
                if dt1 >= self.mat[rows - 1, 0]:
                    pos1 = TGPosition(self.mat[rows - 1, 1], self.mat[rows - 1, 2], self.mat[rows - 1, 3])
                    pos2 = pos1

                else:
                    ind = 0
                    for i in range(0, rows - 1):
                        if dt1 >= self.mat[i, 0] and dt1 < self.mat[i + 1, 0]:
                            ind = i
                            break
                    if self.mat[ind, 4] == 0.0:  # a delay entry
                        pos1 = TGPosition(self.mat[ind, 1], self.mat[ind, 2], self.mat[ind, 3])
                        pos2 = pos1
                    else:
                        dt2 = self.mat[ind + 1, 0] - self.mat[ind, 0]
                        speed_noise = min(max(speed_noise,0.0),0.7)
                        dt3 = dt1 - self.mat[ind, 0]
                        dt_ratio_with_noise = dt3 / dt2 + speed_noise*(random()-0.5)
                        angle_noise = min(max(angle_noise,0.0),0.2)
                        d_angle = angle_noise*2*math.pi*(random()-0.5)
                        d_lon   =  (self.mat[ind + 1, 1] - self.mat[ind, 1])
                        d_lat   =  (self.mat[ind + 1, 2] - self.mat[ind, 2])
                        d_alt   =  (self.mat[ind + 1, 3] - self.mat[ind, 3])
                        if math.fabs(d_lon) < 1 * 10**-7:
                            d_lon = 1 * 10**-7
                        ang =  math.atan2(d_lat,d_lon) + d_angle
                        dist1 = math.sqrt(d_lon*d_lon+d_lat*d_lat)
                        dist2 = math.sqrt(d_lon*d_lon+d_lat*d_lat + d_alt*d_alt)
                        d_lon_with_noise = dist1*math.cos(ang)
                        d_lat_with_noise = dist1*math.sin(ang)
                        speed = dist2/dt2

                        new_lon1 = self.mat[ind, 1] + dt_ratio_with_noise * d_lon_with_noise
                        new_lat1 = self.mat[ind, 2] + dt_ratio_with_noise * d_lat_with_noise
                        new_alt1 = self.mat[ind, 3] + dt_ratio_with_noise * (self.mat[ind + 1, 3] - self.mat[ind, 3])

                        d_lon1 = self.mat[ind + 1, 1] - new_lon1
                        d_lat1 = self.mat[ind + 1, 2] - new_lat1
                        d_alt1 = self.mat[ind + 1, 3] - new_alt1

                        dist3  = math.sqrt(d_lon1*d_lon1+d_lat1*d_lat1 + d_alt1*d_alt1)
                        new_lon2 = new_lon1 + micro_dt * speed * d_lon1 / dist3
                        new_lat2 = new_lat1 + micro_dt * speed * d_lat1 / dist3
                        new_alt2 = new_alt1 + micro_dt * speed * d_alt1 / dist3

                        pos1 = TGPosition(new_lon1, new_lat1, new_alt1)
                        pos2 = TGPosition(new_lon2, new_lat2, new_alt2)

        return [pos1, pos2]

    def SpeedForRelativeTime(self, dt: float) -> float:
        # return the speed
        # per a given relative time in seconds
        # get a relative time from start point
        # if mat is empty, return None
        # if dt lower than the first time, return 0.0
        # if dt higher than the last time, return 0.0
        # else, return its speed
        speed = 0.0
        if self.mat.size > 0:

            dt1 = dt - self.initial_delay

            if dt1 <= self.mat[0, 0]:
                speed = 0.0

            else:
                rows = (np.shape(self.mat))[0]
                if dt1 >= self.mat[rows - 1, 0]:
                    speed = 0.0

                else:
                    ind = 0
                    for i in range(0, rows - 1):
                        if dt1 >= self.mat[i, 0] and dt1 < self.mat[i + 1, 0]:
                            ind = i+1 # we look at the next poi for deriving speed. 25/1/2022
                            break
                    speed = self.mat[ind, 4]
        return speed

    def PoiIndexForRelativeTime(self, dt: float)->int:
            # return the p poi index per a given relative time in seconds
            # get a relative time from start point
            # if mat is empty, return None
            # if dt lower than the first time, return index 0
            # if dt higher than the last time, return index n
            # else, calculate what is the active segment, based on time, and returns it
            poi_index:int  = -1
            if self.mat.size > 0:

                dt1 = dt - self.initial_delay
                if dt1 <=  self.mat[0, 0]:
                    poi_index = 0
                else:
                    rows = (np.shape(self.mat))[0]
                    # if we completed the path, poi_index must be -1
                    # see definition of <NextPoiIndex> in Airwayz UTM API
                    if dt1 > self.mat[rows-1, 0]:
                        poi_index = -1
                    else:
                        ind = 0
                        ii = 0
                        for ii in range(1, rows):
                            if dt1 >= self.mat[ii-1, 0] and dt1 < self.mat[ii, 0]:
                                ind = ii
                                break
                        if ind == 0:
                            poi_index = -1
                        else:
                            poi_index = max(int((ind)/2 -1 ) , 0)
            return poi_index
