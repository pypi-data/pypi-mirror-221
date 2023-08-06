
import datetime
import math
from typing import List, Dict, Tuple, Union
from enum import Enum, IntEnum
from common.azutils import TimeStampStr2Sec, TimeStampAsFloatInSec, Geom
from awz_server_api_test.models import *



"""
Y. Shachar 6/22
data structures to support the new V2.1 protocols, for internal usage by RCS
fields not in use by RCS code, have been omitted. For example: Pilot, ovn, USS contact details etc.

"""

class AccuracyV21:

    Horizontal={"HA1m":1.0,"HA3m":3.0, "HA10m":10.0, "HA30m":30.0, "HA005NM":92.6, "HA01NM": 185.2, "HAUnknown": 5.0}
    Vertical={"VA1m":1 ,"VA3m": 3.0, "VA10m":10.0, "VA25m":25.0, "VA45m":45.0,
              "VA150m":150.0, "VA150mPlus":250.0, "VAUnknown":8.0}

    @staticmethod
    def as_number_horizonal(literal:str) ->float:
        tmp = "HAUnknown"
        if literal in AccuracyV21.Horizontal.keys():
            tmp = literal
        return AccuracyV21.Horizontal[tmp]

    @staticmethod
    def as_number_vertical(literal: str) -> float:
        tmp = "VAUnknown"
        if literal in AccuracyV21.Vertical.keys():
            tmp = literal
        return AccuracyV21.Vertical[tmp]


class V11PathFormat(IntEnum):  # various unjustified formats in V11 which we need to take care :-[
    Requested = 0  # upon requesting a flight path
    AP_FPR = 1  # Air Picture in a flight request
    AP_Reported = 2  # reported path
    AP_Approved = 3  # approved path


class AltitudeV21:

    def __init__(self, value: float, reference = "W84", units = "M"):
        self.value = value
        self.reference = reference
        self.units = units

    @staticmethod
    def from_object(awz_alt):
        if not isinstance(awz_alt, Altitude):
            return None

        alt = AltitudeV21(value=awz_alt.value, reference=awz_alt.reference, units=awz_alt.units)

        return alt



class PositionV21:

    def __init__(self, latitude: float, longitude: float, altitude: AltitudeV21,
                 accuracy_h: str = "HA3m", accuracy_v: str = "VA10m"):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.accuracy_h = accuracy_h
        self.accuracy_v = accuracy_v


    def to_dict(self):

        the_dict = {"latitude": self.latitude, "longitude":self.longitude,  "accuracy_h":self.accuracy_h, \
                    "accuracy_v":self.accuracy_v, "altitude": self.altitude.to_dict()
                    }
        return the_dict

    def to_v11(self):

        the_dict = {"latitude": self.latitude, "longitude":self.longitude,  "accuracy_h":self.accuracy_h, \
                    "accuracy_v":self.accuracy_v, "altitude": self.altitude.to_dict()
                    }
        return the_dict


    @staticmethod
    def from_object(awz_waypoint : Position):

        if isinstance(awz_waypoint , Position):
            
            h = awz_waypoint.accuracy_h
            v = awz_waypoint.accuracy_v
            alt = AltitudeV21.from_object(awz_waypoint.altitude)
            pos = PositionV21(latitude=awz_waypoint.latitude,  longitude=awz_waypoint.longitude,
                              altitude=alt, accuracy_h=h, accuracy_v=v)

            return pos


        return None


class Deviation21:
    def __init__(self, value: float, offset_lr: float):
         self.value = value
         self.offest_lr = offset_lr

    @staticmethod
    def get_default(deviation_type: str):

        offset_lr = 0.0
        if deviation_type == "deviation_h":
            value = 30.0
        else: # vertical, need higher margins
            value = 50.0

        return  Deviation21(value, offset_lr)
    @staticmethod
    def from_object(devitaion : AwzDeviationObject):
        return Deviation21(value=devitaion.value, offset_lr=devitaion.offset)

class Volume3d:

    def __init__(self, low_altitude, high_altitude, polygon: list, center=None, radius=None, geo = True):
        self.low_altitude = low_altitude
        self.high_altitude = high_altitude
        self.center = center
        self.radius = radius
        self.geo = geo
        self.geo_tuple = (0,0,0)
        if type(polygon) == list and len(polygon) > 2:
            self.polygon = polygon
            self.center = None
            self.radius = None
            try:
                poly = polygon[0]
                if self.geo:
                    self.geo_tuple =  (poly["lng"], poly["lat"], 0.0)
                else:
                    self.geo_tuple = (poly[0], poly[1], 0.0)

            except:
                raise Exception("polygon is not a list of lists")
        elif center is not None and radius is not None:
            self.center = center
            self.radius = radius
            self.polygon = None
            if self.geo:
                self.geo_tuple = (self.center["lng"], self.center["lat"], 0.0)
            else:
                self.geo_tuple = (self.center[0], self.center[1], 0.0)
        else:
            raise TypeError("bad polygon format")
    """ polygon must follow the scheme of the below example, wherein the vertices are CW ordered in the X-Y space
     [
        {
            "lng": -118.456,
            "lat": 34.123
        },
        {
            "lng": -118.456,
            "lat": 34.123
        },
        {
            "lng": -118.456,
            "lat": 34.123
        }
    ]
    """

    @staticmethod
    def from_object(awz_volume3d):
        if not isinstance(awz_volume3d, Volume3D):
            return None
            
        low = awz_volume3d.altitude_lower.value 
        high = awz_volume3d.altitude_upper.value 
        center = None
        radius = None
        vertices = []
        if hasattr(awz_volume3d, "outline_polygon") and awz_volume3d.outline_polygon is not None:
            
            for item in awz_volume3d.outline_polygon.vertices:
                vertices.append(item.to_dict())
        elif hasattr(awz_volume3d, "outline_circle") and awz_volume3d.outline_circle is not None:
            center = awz_volume3d.outline_circle.center.to_dict()
            radius = awz_volume3d.outline_circle.radius.value
        else:
            raise TypeError("circle nfz not implemented")

        vol3 = Volume3d(low, high, vertices, center, radius)

        return vol3


    #get accuracy literals, geo location and origin, provide a meter based, vol3 based on input:
    @staticmethod
    def from_accuracy_m(accuracy_h:str, accuracy_v:str, location:tuple, origin:tuple):
        h_val = AccuracyV21.as_number_horizonal(accuracy_h)
        v_val = AccuracyV21.as_number_vertical(accuracy_v)
        lat_for_calc =origin[1]

        origin_m   = Geom.geotuple2tuple(origin, lat_for_calc)

        location_m = Geom.sub(Geom.geotuple2tuple(location,lat_for_calc), origin_m)
        polygon_list = [(location_m[0]-h_val, location_m[1]-h_val), (location_m[0] - h_val, location_m[1] + h_val),
                        (location_m[0] +  h_val, location_m[1] + h_val), (location_m[0] + h_val, location_m[1]-h_val)]

        low  = location_m[2] - v_val
        high = location_m[2] + v_val
        geo  = False
        vol3 = Volume3d(low, high, polygon_list, None, None, geo)

        return vol3

    def from_geo_to_m(self, origin:tuple):
        if self.geo == False: #already metric
            return self
        else:
            geo = False
            lat_for_calc = origin[1]
            origin_m = Geom.geotuple2tuple(origin, lat_for_calc)
            vol3 = None
            if self.center is not None:
                center   = Geom.sub(Geom.geotuple2tuple((self.center["lng"], self.center["lat"], 0), lat_for_calc), origin_m)
                vol3 = Volume3d(self.low_altitude, self.high_altitude, None, center, self.radius, geo)
            elif self.polygon is not None:
                poly2d_m = Geom.convert_volume4d_list_geo_2tuplem_2d(self.polygon, origin_m, lat_for_calc)
                vol3 = Volume3d(self.low_altitude, self.high_altitude, poly2d_m, None, None, geo)
            else:
                raise Exception(f" Illegal volume3 structure encountered, while converting to metric\n")
                geo = True # conversion failed
            return vol3

    # returns binary result - does 2 vol4d intersects or not
    # must be metric, based on the same origin.

    def intersect(self, other_vol3d:'Volume3d'): # must be metric, based on the same origin.
        if self.geo is False and other_vol3d.geo is False:
            result = False
            if (self.low_altitude <= other_vol3d.low_altitude <= self.high_altitude) or \
               (self.low_altitude <= other_vol3d.high_altitude <= self.high_altitude):
                if self.polygon is not None and other_vol3d.polygon is not None:
                    result = Geom.polygon_intersection(self.polygon, other_vol3d.polygon)
                elif self.polygon is not None and other_vol3d.center is not None:
                     result = Geom.polygon_circle_intersection(self.polygon, other_vol3d.center, other_vol3d.radius)
                elif other_vol3d.polygon is not None and self.center is not None:
                    result = Geom.polygon_circle_intersection(other_vol3d.polygon, self.center, self.radius)
                elif other_vol3d.center is not None and self.center is not None:
                    result = Geom.circle_intersection(other_vol3d.polygon, self.center, self.radius)
            return result

        else:
            raise Exception(f" Illegal volume3 geo format, while processing metric\n")


    # calc intersection percentage of a given volume3d in respect to self. Note that this is NOT symmetric relations
    # must be metric, based on the same origin.

    def calc_intersection(self, vol3d: 'Volume3d'):

        result = None
        if self.geo == False and vol3d.geo == False:

            if self.high_altitude < vol3d.low_altitude or self.low_altitude > vol3d.high_altitude:
                result = 0.0

            elif self.low_altitude <= vol3d.low_altitude  and vol3d.high_altitude <= self.high_altitude: #contained
                result = 100.0
            elif self.low_altitude <= vol3d.low_altitude <= self.high_altitude <= vol3d.high_altitude:
                result = 100*(self.high_altitude - vol3d.low_altitude)/(vol3d.high_altitude - vol3d.low_altitude)
            elif vol3d.low_altitude<= self.low_altitude <= self.high_altitude <= vol3d.high_altitude: # anticontainment
                result = 100 * (self.high_altitude - self.low_altitude) / (vol3d.high_altitude - vol3d.low_altitude)
            elif vol3d.low_altitude <= self.low_altitude <= vol3d.high_altitude <= self.high_altitude:
                result = 100 * (vol3d.high_altitude - self.low_altitude) / (vol3d.high_altitude - vol3d.low_altitude)
            else:
                raise Exception(f" opps.. I didn't think such a case is possible... \n")
            # for circles ( area volumes), we just support binary results. 100 or 0.

            if self.polygon is not None and vol3d.polygon is not None:
                result = result * Geom.polygon_calc_intersection(self.polygon, vol3d.polygon)
            elif self.polygon is not None and vol3d.center is not None:
                result = result*int(Geom.polygon_circle_intersection(self.polygon, vol3d.center, vol3d.radius))
            elif vol3d.polygon is not None and self.center is not None:
                result = result*int(Geom.polygon_circle_intersection(vol3d.polygon, self.center, self.radius))
            elif vol3d.center is not None and self.center is not None:
                result = result*int(Geom.circle_intersection(vol3d.polygon, self.center, self.radius))
            else:
                result = 0.0
        else:
            raise Exception(f" Illegal volume3 geo format, while processing metric\n")

        return result

    def calc_volume(self):

        height = max(self.high_altitude - self.low_altitude, 0)
        area = 0.0
        if self.polygon is not None:
            if self.geo is False:
                area = Geom.polygon_calc_area(self.polygon)
            else:
                raise Exception(f" Illegal volume3 geo format, while processing metric\n")

        elif self.center is not None:
            area = self.radius*self.radius*math.pi

        return area*height



class Volume4d:

    def __init__(self, volume3d, time_start_str: str, time_end_str: str, geo = True):
        if isinstance(time_start_str, datetime.datetime):
            time_start_str = datetime.datetime.strftime(time_start_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        if isinstance(time_end_str, datetime.datetime):
            time_end_str = datetime.datetime.strftime(time_end_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        self.volume3 = volume3d

        self.time_start_str = time_start_str
        self.start_end_str = time_end_str

        self.time_start = TimeStampStr2Sec(time_start_str)
        self.time_end = TimeStampStr2Sec(time_end_str)
        self.geo = geo

    def to_v11_nfz_polygon(self, nfz_id: str):

        out_dict = {}
        time_now = TimeStampAsFloatInSec()
        polygon = []
        if self.volume3.center is not None and self.volume3.radius is not None:
            dic = {"circle": {"center":{"latitude": self.volume3.center["lat"],
                                        "longitude":self.volume3.center["lng"],
                                        "altitude": self.volume3.low_altitude},
                              "radius": self.volume3.radius}}
            out_dict ={"name": nfz_id, "height":self.volume3.high_altitude,
            "timestamp": self.time_start_str, "type": "circle", "ctr":{}, "id":nfz_id}
            out_dict.update(dic)
        else:

            for ent in self.volume3.polygon:
                dct = {"altitude": self.volume3.high_altitude, "id":"", "latitude":ent["lat"], "longitude":ent["lng"],
                       "nfz_id": nfz_id}
                polygon.append(dct)
            out_dict ={"name": nfz_id, "height":self.volume3.high_altitude,
                               "timestamp": self.time_start_str, "type": "polygon", "ctr":{}, "polygon":polygon, "id":nfz_id }
        return out_dict

    @staticmethod
    def from_object(awz_volume4d):
        if not isinstance(awz_volume4d, Volume4D):
            return None
        vol3 = Volume3d.from_object(awz_volume4d.volume)
        start = awz_volume4d.time_start.value
        end = awz_volume4d.time_end.value
        vol = Volume4d(vol3, time_start_str=start, time_end_str=end)
        return vol

    def from_geo_to_m(self, origin):

        self.volume3 = self.volume3.from_geo_to_m(origin)
        self.geo = False

    # returns binary result - does 2 vol4d intersects or not
    # must be metric, based on the same origin.
    def intersect(self, other_vol4d:'Volume4d'): # must be metric, based on the same origin.
        if self.geo == False and other_vol4d.geo  == False:
            result = False
            if (self.time_start <= other_vol4d.time_start <= self.time_end) or \
               (self.time_start <= other_vol4d.time_end <= self.time_end):
                result = self.volume3.intersect(other_vol4d.volume3)

        else:
            raise Exception(f" Illegal volume4 geo format, while processing metric\n")

        return result

    # calc intersection percentage of a given volume3d in respect to self. Note that this is NOT symmetric relations
    # must be metric, based on the same origin.

    def calc_intersection(self, vol3d:Volume3d):

        result = self.volume3.calc_intersection(vol3d)
        return result

    def time_within(self, the_time):

        if isinstance(the_time, float):
            return self.time_start <= the_time  <= self.time_end
        else:
            raise Exception(f" Illegal volume4 time format expecting number \n")

    def calc_volume(self, the_time):

        result = 0.0
        if self.time_within(the_time):
            result = self.volume3.calc_volume()

        return result

class WaypointV21:
    def __init__(self, latitude:float, longitude:float, altitude:float, speed: float, delay: float,
                 is_calculated: bool = False, deviation_h: Deviation21 = Deviation21.get_default("deviation_h"),
                 deviation_v: Deviation21 = Deviation21.get_default("deviation_v"), time_e = 0.0, time_l = 0.0):
        self.latitude = latitude
        self.longitude= longitude
        self.altitude = altitude
        self.speed    = speed
        self.delay    = delay
        self.deviation_h = deviation_h
        self.deviation_v = deviation_v
        self.time_e = time_e
        self.time_l = time_l
        self.is_calculated = is_calculated

    def to_v11_waypoint(self, pformat: V11PathFormat,  name = "some wp"):

        dct = {"altitude": self.altitude, "latitude": self.latitude, "longitude": self.longitude,
               "delay": self.delay, "speed": self.speed}

        if pformat == V11PathFormat.AP_FPR or pformat == V11PathFormat.Requested:
            dct |= {"accuracy": 0, "id": -1, "name": name}

        # if pformat == V11PathFormat.Requested:
        #     required = True
        # else:
        required = not self.is_calculated
        dct |= {"required": required}
        # if pformat == V11PathFormat.AP_Reported or pformat == V11PathFormat.AP_Approved:
        #     dct |= {"required": required}

        return dct

    @staticmethod
    def from_object(waypoint : AwzWaypoint):
        
        dh = Deviation21.from_object(waypoint.deviation.horizontal)
        dv = Deviation21.from_object(waypoint.deviation.vertical)
        wp = WaypointV21(latitude=waypoint.latitude, longitude=waypoint.longitude, altitude=waypoint.altitude.value, speed=waypoint.speed, delay=waypoint.delay, is_calculated=waypoint.is_calculated, deviation_h=dh, deviation_v=dv, time_e=waypoint.time_enter, time_l=waypoint.time_leave)
        return wp


class PathAwzV21Header:
    def __init__(self, id:str, time_str:str):
        if isinstance(time_str, datetime.datetime):
            time_str = datetime.datetime.strftime(time_str,"%Y-%m-%dT%H:%M:%S.%fZ")
        self.id = id
        self.time_str = time_str
        self.time = TimeStampStr2Sec(time_str)


class PathAwzV21:

    def __init__(self, id: str, time_str: str, priority: int, the_type="delivery",
                 nextPoiIndex: int = None, waypoints: list[WaypointV21] = []):

        self.format = "awz_v2.1"
        self.path = PathAwzV21Header(id, time_str)
        self.priority = priority
        self.type = the_type
        self.nextPoiIndex = nextPoiIndex
        self.waypoints = waypoints

    @staticmethod
    def from_object(awz_path_object):
        if not isinstance(awz_path_object, AwzPathObject):
            return None
        wp = [] 
        for item in awz_path_object.waypoints:
            pos = WaypointV21.from_object(item)
            if pos is None:
                return None
            wp.append(pos)
        PathAwzV21_object = PathAwzV21(id="", time_str=awz_path_object.time_start.value,
                                       priority=awz_path_object.priority, the_type=awz_path_object.type, waypoints=wp, nextPoiIndex=awz_path_object.next_poi_index)
        return PathAwzV21_object

    def to_v11_path(self, pformat: V11PathFormat, ):

        result = None
        if "awz_" in self.format and len(self.waypoints) > 0:
            time_str = self.path.time_str
            wps = []
            i = 0
            for wp in self.waypoints:
                if isinstance(wp, WaypointV21):
                    the_name = "DroneLocation"
                    if i > 0:
                        the_name = "TA"+ str(i)
                    i = i + 1
                    dct = wp.to_v11_waypoint(pformat, the_name)
                    if dct is not None:
                        wps.append(dct)

            if pformat == V11PathFormat.AP_Reported:
                result = {"nextPoiIndex": self.nextPoiIndex + 1, "poi": wps}
            elif pformat == V11PathFormat.AP_Approved:
                result = {"time": time_str, "poi": wps}
            else:
                result = {"startTime": time_str, "wp": wps}

        return result


class PathAstmF3411Header:
    def __init__(self, idn: str, time_start_str: str, time_end_str: str):
        if isinstance(time_start_str, datetime.datetime):
            time_start_str = datetime.datetime.strftime(time_start_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        if isinstance(time_end_str, datetime.datetime):
            time_end_str = datetime.datetime.strftime(time_end_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        self.id = idn
        self.time_start_str = time_start_str
        self.start_end_str = time_end_str
        self.time_start = TimeStampStr2Sec(time_start_str)
        self.time_end   = TimeStampStr2Sec(time_end_str)


class PathAstmF3411:
    MinimalConformanceScore = 99.0
    def __init__(self, idn: str, time_start_str: str, time_end_str: str, priority: int, state: str,
                 manager:str = "", volumes:list[Volume4d] = [], off_nominal_volumes:list[Volume4d] =[]):
        self.format = "astm_f3411"
        self.path = PathAstmF3411Header(idn, time_start_str, time_end_str)
        self.priority = priority
        self.state = state
        self.manager = manager
        self.volumes = volumes
        self.off_nominal_volumes = off_nominal_volumes
        self.geo = True
        if len(self.volumes) > 0:
            self.geo_tuple = self.volumes[0].volume3.geo_tuple
        else:
            self.geo_tuple = None
    #FIXME MEIR, need to fill this up
    @staticmethod
    def from_object(p : AwzAstmF3411PathObject):
        
        if not isinstance(p, AwzAstmF3411PathObject):
            return None
        # version = p.path.reference.version
        time_start = p.path.reference.time_start.value
        time_end = p.path.reference.time_end.value
        prior = p.path.details.priority
        _volumes = []
        for vol in p.path.details.volumes:
            if isinstance(vol, Volume4D):
                _volumes.append(Volume4d.from_object(vol))
            
        _off = []
        for vol in p.path.details.off_nominal_volumes:
            if isinstance(vol, Volume4D):
                _off.append(Volume4d.from_object(vol))
            
        # THERE IS NOE STATE NEITHER MANAGER 
        PathAstmF3411_object = PathAstmF3411(idn="", time_start_str=time_start, time_end_str=time_end, priority=prior,state=None, manager=None, volumes=_volumes, off_nominal_volumes=_off)
        return PathAstmF3411_object

    #return a value between 0 - 100, showing telemetry conformance with the path.
    def position_conformance(self, telemetry: 'TelemetryV21'):
        result = 0.0
        if isinstance(telemetry, TelemetryV21):
            pos = telemetry.position
            if type(pos.altitude) == AltitudeV21:
                altitude = pos.altitude.value
            else:
                altitude = pos.altitude
            vol3 = Volume3d.from_accuracy_m(pos.accuracy_h, pos.accuracy_v,
                                            (pos.longitude, pos.latitude, altitude),self.geo_tuple)
            if self.geo == True: # we need to convert data to metric :
                for a_volume in self.volumes:
                    a_volume.from_geo_to_m(self.geo_tuple)
                self.geo == False

            if self.path.time_start <= telemetry.time <= self.path.time_end and len(self.volumes) > 0: # otherwise dont bother

                v = 0

                for a_volume in self.volumes:
                    if a_volume.time_within(telemetry.time):
                        break
                    else:
                        v = v+1
                if v < len(self.volumes): #we found a relevant volume4d
                    result = self.volumes[v].calc_intersection(vol3)
                    if result < PathAstmF3411.MinimalConformanceScore and (v+1) < len(self.volumes):
                        #give a chance for the next volume4d, if it is time overlapping
                        if self.volumes[v+1].time_within(telemetry.time):
                            result1 = self.volumes[v+1].calc_intersection(vol3)
                            if result1 > result:
                                result = result1

        else:
            raise Exception(f" Illegal input type for position conformance, expecting TelemetryV21 \n")

        return (result)

    # return a value containing the volume cost of the drone in its current position.

    def volume_cost(self, telemetry: 'TelemetryV21'):
        result = 0.0
        if isinstance(telemetry, TelemetryV21):
            pos = telemetry.position
            if type(pos.altitude) == AltitudeV21:
                altitude = pos.altitude.value
            else:
                altitude = pos.altitude
            if self.geo == True:  # we need to convert data to metric :
                for a_volume in self.volumes:
                    a_volume.from_geo_to_m(self.geo_tuple)
                self.geo == False
            if self.path.time_start <= telemetry.time <= self.path.time_end and len(
                    self.volumes) > 0:  # otherwise dont bother

                v = 0

                for a_volume in self.volumes:
                    if a_volume.time_within(telemetry.time):
                        break
                    else:
                        v = v + 1
                if v < len(self.volumes):  # we found a relevant volume4d
                    result = self.volumes[v].calc_volume(telemetry.time) # get its cost
                    if (v + 1) < len(self.volumes):
                        # if the next one volume is time overlapping - we should consider it as well
                        if self.volumes[v + 1].time_within(telemetry.time):
                            result1 = self.volumes[v + 1].calc_volume(telemetry.time)
                            result = result + result1

                if hasattr(self,"off_nominal_volumes") and self.off_nominal_volumes is not None \
                   and len(self.off_nominal_volumes) > 0:

                    v = 0

                    for a_volume in self.off_nominal_volumes:
                        if a_volume.time_within(telemetry.time):
                            break
                        else:
                            v = v + 1
                    if v < len(self.off_nominal_volumes):  # we found a relevant volume4d
                        result = self.off_nominal_volumes[v].calc_volume(telemetry.time)  # get its cost
                        if (v + 1) < len(self.off_nominal_volumes):
                            # if the next one volume is time overlapping - we should consider it as well
                            if self.off_nominal_volumes[v + 1].time_within(telemetry.time):
                                result1 = self.off_nominal_volumes[v + 1].calc_volume(telemetry.time)
                                result = result + result1



        else:
            raise Exception(f" Illegal input type for position conformance, expecting TelemetryV21 \n")

        return (result)


class TelemetryV21:

    def __init__(self, time_str: str, position:PositionV21, speed, speed_v, dummy=False):
        if isinstance(time_str, datetime.datetime):
            time_str = datetime.datetime.strftime(time_str,"%Y-%m-%dT%H:%M:%S.%fZ")
        self.time_str = time_str
        self.time = TimeStampStr2Sec(time_str)
        self.position = position
        self.velocity = speed
        self.vertical_velocity = speed_v
        self.dummy = dummy
        

    @staticmethod
    def from_object(awz_telemetry_obj):
        if not isinstance(awz_telemetry_obj, VehicleTelemetry):
            return None

        time_str = awz_telemetry_obj.time_measured.value
        pos = PositionV21.from_object(awz_telemetry_obj.position)
        vel = awz_telemetry_obj.velocity.speed
        v_speed = 0 # alwayz zero! see astm doc


        tel_obj = TelemetryV21(time_str=time_str, position=pos, speed=vel, speed_v=v_speed)
        return tel_obj

    def to_v11_positions(self):

        lat = self.position.latitude
        lon = self.position.longitude
        alt = self.position.altitude.value

        return [
                  {"latitude": lat, "longitude": lon, "altitude": alt, "time": self.time*1000, # time here is in ms
                   "alt_isa": 117.6, "altitude_datum": "wgs84"},
                  {"latitude": lat, "longitude": lon, "altitude": alt, "time": self.time*1000,
                   "alt_isa": 117.6, "altitude_datum": "wgs84"}
               ]

# Mair ! Implement ur schisse !
class EnergyV21:

    def __init__(self, distance:float, percentage:float):
        self.distance = distance
        self.percentage = percentage

    @staticmethod
    def from_object(awz_energy_obj):
        if not isinstance(awz_energy_obj, AwzEnergy):
            return None

        distance = awz_energy_obj.distance
        percentage = awz_energy_obj.precentage

        energy_obj = EnergyV21(distance=distance, percentage=percentage)
        return energy_obj


class DroneV21:

    FlyingStateAirborneList = [102,103,104,105,106]
    FlyingStateGroundList = [100,101,107]
    FlyingStateUndefinedList = [108]
    """
    the main data structure of a drone, effective both for flight requests and air pictures
    if reported path is unavailable, an empty list should br provided. Same goes for approved paths
    for flight requests, flight state should be omitted or set to 100, and Telemetry to None.
    """
    #FIXME what in god name is this Union shit?? YS_SAYS: Du dummkopf !
    # -> https://coderslegacy.com/python/union-in-typing/#:~:text=Combining%20together%20Types%20with%20Union,how%20would%20we%20do%20so%3F

    def __init__(self, name: str, org_id: int, idn: str, model: str, model_desc: list[str], descriptors: str,
                 priority, flying_state: int = 100, telemetry: TelemetryV21 = None, energy: EnergyV21 = None , awz_path=None, astm_path=None, approved_awz_path=None, approved_astm_path=None):

        self.name = name
        self.org_id = org_id
        self.id = idn
        self.model = model
        self.model_desc = model_desc
        self.descriptors = descriptors
        self.flying_state = flying_state
        self.priority = priority
        self.awz_path = awz_path
        self.astm_path = astm_path
        self.approved_awz_path = approved_awz_path
        self.approved_astm_path = approved_astm_path
        self.time = int(datetime.datetime.utcnow().timestamp()*1000) # time now in miliseconds
        self.telemetry = telemetry
        self.energy = energy

    # Meir !you need to handle both the cases where the AirPicture is for a non flying object
    # where there is no telemetry, flying state is 100 or 101, but also the case where there
    # is telemetry and flying state. Also, Approved Path is optional and can not be fixed to None !
    @staticmethod
    def from_object(drone_object):
        
        if isinstance(drone_object, AwzUsspToRcsDroneObject):
            _name = drone_object.name
            _id = drone_object.id
            _org_id = drone_object.org_id
            _model = drone_object.model
            _model_desc = "AwzUsspToRcsDroneObject has no _model_desc"
            _descriptors = drone_object.descriptors
            #FIXME YAIR# here will be the path request by the drone 
            # this is a little bit sheisse.. YS_SAYS: HA??
            _awz_path  = None
            _astm_path = None
            _awzpathapp = None
            _astmpathapp = None



            _approved_awz_path = None
            _approved_astm_path = None
            if hasattr(drone_object, "approved_paths") and drone_object.approved_paths is not None:
                
                ap_awzp = drone_object.approved_paths.awz
                ap_astmp = drone_object.approved_paths.astm_f3411
                # _approved_awz_path = PathAwzV21.from_object(ap_awzp)
                # _approved_astm_path = PathAstmF3411.from_object(ap_astmp)
                _awz_path = PathAwzV21.from_object(ap_awzp)
                _astm_path = PathAstmF3411.from_object(ap_astmp)
                _awzpathapp = _awz_path
                _astmpathapp = _astm_path

            _flying_state = drone_object.state
            _telemetry = TelemetryV21.from_object(drone_object.telemetry)
            _energy = EnergyV21.from_object(drone_object.energy)
            _priority = 0
            if hasattr(drone_object.paths, "awz") and hasattr(drone_object.paths.awz, "priority"):
                _priority = drone_object.paths.awz.priority
            elif hasattr(drone_object.paths, "astm_f3411") and hasattr(drone_object.paths.astm_f3411, "priority"):
                _priority = drone_object.paths.astm_f3411.priority


            DroneV21_object = DroneV21(name=_name, org_id=_org_id, model=_model, model_desc=_model_desc,
                                       descriptors=_descriptors, idn=_id, flying_state=_flying_state,
                                       telemetry=_telemetry, energy=_energy, priority=_priority, astm_path=_astm_path,
                                       awz_path=_awz_path, approved_awz_path = _awzpathapp,
                                       approved_astm_path=_astmpathapp)
            
            return DroneV21_object

        if isinstance(drone_object, AwzUsspToRcsFpaRequestObject):
            _name = drone_object.drone.name
            _id = drone_object.drone.id
            _org_id = 0
            _model = drone_object.drone.model
            _model_desc = "ther is no desc"
            _descriptors = drone_object.drone.descriptors
            #FIXME YAIR# here will be the path request by the drone 
            # this is a little bit sheisse.. YS_SAYS: HA??
            
            awzp = drone_object.paths.awz
            astmp = drone_object.paths.astm_f3411
            _awz_path = PathAwzV21.from_object(awzp)
            _astm_path = PathAstmF3411.from_object(astmp)
            _approved_awz_path = None
            _approved_astm_path = None

            _flying_state = 100
            _telemetry = None
            _energy = None
            _priority = 0
            if hasattr(drone_object.paths, "awz") and hasattr(drone_object.paths.awz, "priority"):
                _priority = drone_object.paths.awz.priority
            elif hasattr(drone_object.paths, "astm_f3411") and hasattr(drone_object.paths.astm_f3411, "priority"):
                _priority = drone_object.paths.astm_f3411.priority
            
            DroneV21_object = DroneV21(name=_name, org_id=_org_id, model=_model, model_desc=_model_desc,
                                       descriptors=_descriptors, idn=_id, flying_state=_flying_state, telemetry=_telemetry, energy=_energy, priority=_priority, astm_path=_astm_path, awz_path=_awz_path)
            
            return DroneV21_object

        
        
        return None

    # def find_awz_path(self, path_type:str = "paths"):  # find the path with awz format within V2_1 paths

    #     paths = []
    #     if path_type == "paths":  # reported paths
    #         paths = self.reported_paths
    #     else:
    #         paths = self.approved_paths

    #     index = -1
    #     if paths is not None and len(paths) > 0:

    #         for i in range (0, len(paths)):
    #             if type(paths[i]) == PathAwzV21:
    #                 index = i
    #                 break

    #     return index

    """
    when the Drone is not in the air in V2_1, there is no position.
    So we take it from the path assuming the drone is in the first position on path. 
    """

    def positions_from_path_dict(self, path_dict: dict) -> list:
        
        time = self.time
        

        wp = path_dict["wp"]

        lat = wp[0]["latitude"]
        lon = wp[0]["longitude"]
        alt = wp[0]["altitude"]

        return [
                {"latitude": lat, "longitude": lon, "altitude": alt, "time": time,
                 "alt_isa": 117.6, "altitude_datum": "wgs84"},
                {"latitude": lat, "longitude": lon, "altitude": alt, "time": time,
                 "alt_isa": 117.6, "altitude_datum": "wgs84"}
               ]

    def to_v11_sync_entity(self, include_non_airborne_drones=False):
        # export to V11 drone entity in sync format ( air monitor msg)
        # if flag is set, include non airborne drones as well

        # paths = self.reported_paths
        # index = self.find_awz_path("paths")
        approved_path_dict ={}
        if self.awz_path is not None and self.telemetry is not None:
            
            reported_path_dict = self.awz_path.to_v11_path(V11PathFormat.AP_Reported)
            # paths = self.approved_paths
            # index = self.find_awz_path("approved_paths")
            if self.approved_awz_path is not None: # there is an approved path
                
                approved_path_dict = self.approved_awz_path.to_v11_path(V11PathFormat.AP_Approved)

            #Meir - There is no Attitude in Telemetry ! bug in the 2.1 protocol !

            return {"data": {"drone":{"id":self.id, "model": self.model, "name": self.name, "descriptors": self.descriptors,
                    "isManned": False,
                    # no attitude for now, so fake one:
                    "attitude": {"yaw": -0.890439722379034, "pitch": -0.05, "roll": 0, "time": self.telemetry.time},
                    "priority": self.priority,
                    "path": reported_path_dict,
                    "battery":self.energy.percentage/100.0,
                    "positions": self.telemetry.to_v11_positions(), "org_id": self.org_id,
                    "velocity": {"v_total": self.telemetry.velocity, "vx": 0, "vy": 0, "vz": 0},
                    "flyingState": self.flying_state,
                    "approvedPath": approved_path_dict
                    }}}
        elif self.awz_path is None and \
                (self.flying_state in DroneV21.FlyingStateAirborneList or include_non_airborne_drones) \
                and self.telemetry is not None:

            # obj = {"id": self.id, "model": self.model, "name": self.name, "complianceScore": 0,
            #         "descriptors": self.descriptors, "isManned": False,
            #         "priority": 999,
            #         "position": position, "org_id": self.org_id
            #        }
            # wps = [{"altitude": self.telemetry.position.altitude.value,
            #         "latitude": self.telemetry.position.latitude, 
            #         "longitude": self.telemetry.position.longitude,
            #         "delay": 0, "speed": 5}]
            wps = []
            reported_path_dict = {"nextPoiIndex": 0, "poi": wps, "wp": wps, "startTime": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')}
            
            return {"data": {"drone":{"id":self.id, "model": self.model, "name": self.name, "descriptors": self.descriptors,
                    "isManned": False,
                    # no attitude for now, so fake one:
                    "attitude": {"yaw": 0, "pitch": -0.05, "roll": 0, "time": self.telemetry.time},
                    "path": reported_path_dict,
                    "priority": self.priority,
                    "battery":self.energy.percentage/100.0,
                    "positions": self.telemetry.to_v11_positions(), "org_id": self.org_id,
                    "velocity": {"v_total": self.telemetry.velocity, "vx": 0, "vy": 0, "vz": 0},
                    "flyingState": self.flying_state,
                    "approvedPath": None
                    }}}

        else:
            return {}

    

    def to_v11_fp_air_picture_entity(self, path_format: V11PathFormat):  # various unjustified formats in V11 which we need to take care :-[

        # paths = self.reported_paths
        # index = self.find_awz_path("paths")
        if self.awz_path is not None:
            # the_path = paths[index]
            reported_path_dict = self.awz_path.to_v11_path(V11PathFormat.AP_FPR)

            if self.telemetry is not None:
                position = self.telemetry.to_v11_positions()

            else:
                position = self.positions_from_path_dict(reported_path_dict)

            obj = {"id": self.id, "model": self.model, "name": self.name, "complianceScore": 0,
                    "descriptors": self.descriptors, "isManned": False,
                    "priority": self.priority,
                    "position": position, "org_id": self.org_id
                   }
            if (path_format != V11PathFormat.Requested):
                obj["path"] = reported_path_dict

            return obj
        elif self.flying_state in DroneV21.FlyingStateAirborneList and self.telemetry is not None: # this is a still drone
            position = self.telemetry.to_v11_positions()
            obj = {"id": self.id, "model": self.model, "name": self.name, "complianceScore": 0,
                    "descriptors": self.descriptors, "isManned": False,
                    "priority": 998,
                    "position": position, "org_id": self.org_id
                   }
            # wps = [{"altitude": position[0]["altitude"],
            #         "latitude": position[0]["latitude"], 
            #         "longitude": position[0]["longitude"],
            #         "delay": 0, "speed": 5}]
            wps = []
            obj["path"] = {"nextPoiIndex": 0, "poi": wps, "wp": wps, "startTime": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')}
            return obj
        else:
            return {}


class ConstraintHeaderV21:

    def __init__(self, idn: str, manager: str, time_start_str: str, time_end_str: str):
        if isinstance(time_start_str, datetime.datetime):
            time_start_str = datetime.datetime.strftime(time_start_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        if isinstance(time_end_str, datetime.datetime):
            time_end_str = datetime.datetime.strftime(time_end_str,"%Y-%m-%dT%H:%M:%S.%f%Z")
        self.id = idn
        self.manager = manager
        self.time_start_str = time_start_str
        self.start_end_str = time_end_str
        self.time_start = TimeStampStr2Sec(time_start_str)
        self.time_end = TimeStampStr2Sec(time_end_str)


class ConstraintV21:

    def __init__(self, idn: str, manager: str, time_start_str: str, time_end_str: str,
                 details: list[Volume4d]):

        if type(details) != list:
            raise TypeError("details must be of type list")
        for ent in details:
            if type(ent) != Volume4d:
                raise TypeError("each details entry must be of type Volume4d")
        self.header = ConstraintHeaderV21(idn, manager, time_start_str, time_end_str)
        self.details = details
        self.geo = True
        if len(self.details) > 0:
            self.geo_tuple = self.details[0].volume3.geo_tuple
        else:
            self.geo_tuple = None

    def to_v11_nfz(self):

        i = 0
        result = {}
        for vol in self.details:
            vol_num_str = format(i, '04d')
            the_value = vol.to_v11_nfz_polygon(self.header.id)
            the_key = self.header.id + "_" + vol_num_str
            result[the_key] = the_value
            i = i+1

        return result
    
    @staticmethod
    def from_object(constraint_object):
    
        if constraint_object is None or not isinstance(constraint_object, AwzConstraint) and not isinstance(constraint_object.constraint, Constraint) and constraint_object.constraint is None:
            return None
        
        cr = constraint_object.constraint.reference
        _details = []
        for item in constraint_object.constraint.details.volumes:
            vol = Volume4d.from_object(item)
            _details.append(vol)
        ConstraintV21_object = ConstraintV21(idn=cr.id, manager=cr.manager, time_start_str=cr.time_start.value,
                                             time_end_str=cr.time_end.value, details=_details)
    
        return ConstraintV21_object

    def is_intersecting(self, telemetry: 'TelemetryV21'):
        # return true, if we are intersecting with the given telemetry, with one of our volumes. False otherwise.

        result = False
        if isinstance(telemetry, TelemetryV21):
            pos = telemetry.position
            if type(pos.altitude) == AltitudeV21:
                altitude = pos.altitude.value
            else:
                altitude = pos.altitude

            # build 3d accuracy box around the position, with the same origin as for our Constriants.
            vol3 = Volume3d.from_accuracy_m(pos.accuracy_h, pos.accuracy_v,
                                            (pos.longitude, pos.latitude, altitude),self.geo_tuple)
            # if we are on geo coordinates, convert to metric. origin in the first point in first volume.
            if self.geo == True: # we need to convert data to metric :
                for a_volume in self.details:
                    a_volume.from_geo_to_m(self.geo_tuple)
            self.geo = False

            if self.header.time_start <= telemetry.time <= self.header.time_end and len(self.details) > 0: # otherwise dont bother

                v = 0

                for a_volume in self.details:
                    if a_volume.time_within(telemetry.time):
                        break
                    else:
                        v = v+1
                if v < len(self.details): #we found a relevant volume4d
                    result = self.details[v].volume3.intersect(vol3)
                    if result is False and v+1 < len(self.details):
                        # give a chance for the next volume4d, if it is time overlapping
                        if self.details[v+1].time_within(telemetry.time):
                            result1 = self.details[v+1].volume3.intersect(vol3)
                            result = result or result1

        else:
            raise Exception(f" Illegal input type for position conformance, expecting TelemetryV21 \n")

        return result


class LimitationsV21:

    def __init__(self, time_str: str, constraints: list[ConstraintV21]):

        if isinstance(time_str, datetime.datetime):
            time_str = datetime.datetime.strftime(time_str,"%Y-%m-%dT%H:%M:%S.%fZ")

        self.time_str = time_str
        self.time = TimeStampStr2Sec(time_str)
        self.constraints = constraints

    def to_v11_nfz(self):

        result = {}
        for const in self.constraints:
            dct = const.to_v11_nfz()
            result = result | dct
        return {"nfz": result}

    @staticmethod
    def from_object(_AwzLimitations : AwzLimitations):

        if _AwzLimitations is None:
            return None
        
        # parsing Time object
        _time_str = _AwzLimitations.time_updated.value

        # Parsing list of constraint
        constraints = []
        for item in _AwzLimitations.constraints:
            constraint = ConstraintV21.from_object(item)
            if constraint is not None:
                constraints.append(constraint)

        _constraints = constraints
    
        return LimitationsV21(time_str=_time_str, constraints=_constraints)


class AerialPictureV21:

    def __init__(self, drones: list[DroneV21]):

        if type(drones) != list:
            raise TypeError("drones must be of type list")
        for ent in drones:
            if type(ent) != DroneV21:
                raise TypeError("each drones entry must be of type DroneV21")
        self.drones = drones

    def to_v11_ap(self, path_format : V11PathFormat,include_non_airborne_drones = False):

        ap_list = []
        ap_dict = {}
        for entity in self.drones:
            if (path_format.value == V11PathFormat.AP_FPR.value):
                itm = entity.to_v11_fp_air_picture_entity(V11PathFormat.AP_FPR)
                if len(itm) > 0:
                    ap_list.append(itm)
            else:
                itm = entity.to_v11_sync_entity(include_non_airborne_drones)
                if len(itm) > 0:
                    ap_dict[entity.id] = itm
                
        if (path_format.value == V11PathFormat.AP_FPR.value):
            return {"entities": ap_list}
        return {"entities": ap_dict}

        

    @staticmethod
    def from_object(aeriel_pic_list : AwzUsspToRcsAerialPicture):

        _drones = []

        for item in aeriel_pic_list.drones:
            if isinstance(item, AwzUsspToRcsDroneObject):
                _drones.append(DroneV21.from_object(item))

        return AerialPictureV21(drones=_drones)


class RequestV21:

    """ Note there is inconsistency in V21 definitions where the Drone and Paths structures are separated
        for no good reason. Paths must be part of Drone ! so the following RequestV21 structure, corrects that
        by assuming that the drone contains path.
    """
    def __init__(self, time_str: str,req_id, drone: DroneV21, aerial_picture: AerialPictureV21,
                limitations: LimitationsV21, is_controllable=True):

        if isinstance(time_str, datetime.datetime):
            time_str = datetime.datetime.strftime(time_str,"%Y-%m-%dT%H:%M:%S.%fZ")
        self.time_str = time_str
        self.time = TimeStampStr2Sec(time_str)
        self.req_id = req_id

        self.drone = drone
        self.limitations = limitations
        self.is_controllable = is_controllable
        self.aerial_picture = aerial_picture

    def to_v11_flight_request(self):

        
        entities = self.aerial_picture.to_v11_ap(V11PathFormat.AP_FPR)
        nfz_list = self.limitations.to_v11_nfz()
        airpicture = entities | nfz_list
        entity = self.drone.to_v11_fp_air_picture_entity(V11PathFormat.Requested)
        entity.update({"req_id": self.req_id})
        if self.drone.awz_path is not None:
            path   = self.drone.awz_path.to_v11_path(V11PathFormat.Requested)
            requested_paths = {"requestedPaths":[{"entity":entity, "path":path}]}
            result_dict ={}
            result_dict["airpicture"] = airpicture 
            result_dict.update(requested_paths)

        return result_dict

    @staticmethod
    def from_object(request : AwzUsspToRcsFpaRequestObject):
        if not isinstance(request, AwzUsspToRcsFpaRequestObject):
            return None
        _time_str = "2022-06-21T07:47:20.123057"
        # sending all object because the data is spreaded around
        _drones = DroneV21.from_object(request)

        ap = AerialPictureV21.from_object(request.aerial_picture)
        limit = LimitationsV21.from_object(request.limitations)

        return RequestV21(time_str=_time_str,req_id=request.id, drone=_drones, aerial_picture=ap, limitations=limit)

# Meir! Add ur schisse ":

class AlertV21:

    def __init__(self, time_str: str, alert_type: str):
        self.time_str = time_str
        self.alert_type = alert_type

#FIXME MEIR add from object
class CollisionAlertV21(AlertV21):

    def __init__(self, time_str: str, alert_type: str, drones_ids: List[str], estimated_time_str: str,
                 sugg_paths: List[Union[PathAwzV21, PathAstmF3411]] = None):

        self.estimated_time_str = estimated_time_str
        self.sugg_paths = sugg_paths
        self.drones_ids = drones_ids
        super().__init__(time_str, alert_type)


    @staticmethod
    def from_object(collison_alert : AwzAlert):
        if collison_alert.type != "collision":
            return None

        t = collison_alert.time.value
        est = collison_alert.details.estimated_time
        drones_list = collison_alert.details.drones
        #FIXME i dont want to implemnt
        sugg = None

        coll = CollisionAlertV21(time_str=t, alert_type="collision", drones_ids=drones_list, estimated_time_str=est, sugg_paths=sugg)
        return coll


class CollisionAlertV11:
    def __init__(self, collision_dict: dict):
        pass

#FIXME MEIR add from object
class NfzAlertV21(AlertV21):

    def __init__(self, time_str: str, alert_type: str, drone_id: str, nfz_id: str,
                 sugg_paths: List[Union[PathAwzV21, PathAstmF3411]] = None):

        self.nfz_id = nfz_id
        self.sugg_paths = sugg_paths
        self.drone_id = drone_id
        super().__init__(time_str, alert_type)

#FIXME MEIR add from object
class EmergencyAlertV21(AlertV21):

    def __init__(self, time_str: str, alert_type: str, drone_id: str):

        self.drone_id = drone_id
        self.command = "stop"
        super().__init__(time_str, alert_type)


# RequestsV21 = List[RequestV21]
# AlertsV21 = List[Union[CollisionAlertV21 , NfzAlertV21]]

""" MASTER CLASSES FOR FULL MESSAGES:"""

class FlightsRequestsV21:

    def __init__(self, requests: List[RequestV21] ):

        self.requests = requests

    def to_v11_flight_request(self):
        result = {}
        if len(self.requests) > 0: # we only process 1 request for V1.1 for now.
            result = self.requests[0].to_v11_flight_request()
        return result

    @staticmethod
    def from_object(fpa_list : AwzUsspToRcsFpaRequest):
        if not isinstance(fpa_list, AwzUsspToRcsFpaRequest) or len(fpa_list.requests) == 0:
            return None
        fpa = fpa_list.requests[0]

        r = RequestV21.from_object(fpa)
        return FlightsRequestsV21(requests=[r])


class MonitorRequestV21:

    def __init__(self, system_time_str: str, aerial_picture: AerialPictureV21, limitations: LimitationsV21):

        self.system_time_str = system_time_str
        self.aerial_picture = aerial_picture
        self.limitations = limitations

    def to_v11_monitor_request(self, include_non_airborne_drones = False):
        
        entities = self.aerial_picture.to_v11_ap(V11PathFormat.AP_Reported, include_non_airborne_drones)
        nfz_list = self.limitations.to_v11_nfz()
        result = {"usses": {"0": entities}, "nfzs": nfz_list["nfz"]}
        # the_value = entities | nfz_list
        # result["airpicture"] = the_value
        return result

    @staticmethod
    def from_object(monitor_request : AwzUsspToRcsMonitorRequest):
        if not hasattr(monitor_request, "aerial_picture"):
            return None
        ap = AerialPictureV21.from_object(monitor_request.aerial_picture)
        limit = LimitationsV21.from_object(monitor_request.limitations)
        
        monitor_obj = MonitorRequestV21(system_time_str="2022-06-21T07:47:20.123057",aerial_picture=ap, limitations=limit)
        return monitor_obj
        

#FIXME MEIR add from object
class MonitorResponseV21:

    def __init__(self, system_time_str: str, alerts: List[Union[CollisionAlertV21 , NfzAlertV21]]):

        self.system_time_str = system_time_str
        self.alerts = alerts