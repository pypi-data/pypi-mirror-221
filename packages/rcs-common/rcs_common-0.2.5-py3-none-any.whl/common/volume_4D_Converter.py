from typing import List

from awz_client_api_test.models import Volume3D, Volume4D, Time, Polygon, LatLngPoint, Altitude, Circle, Radius
from common.geoutils import AzGeoUtils
from datetime import datetime, timedelta
import math
import numpy as np
from scipy.spatial import ConvexHull

from configparser import ConfigParser
from pathlib import Path

#configfile = ConfigParser()
#configfile.read(str(Path(__file__).parent.absolute()) + "/install/converter.ini")
T = 0.0

CONVERTER_VERSION = "2.1.2"

AWZ_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
DEFAULT_EXPANSION_THRESHOLD = 30.0
PRECISION = 10


class awzPoint:

    def __init__(self, altitude=0.0, latitude=0.0, longitude=0.0, speed=0.0, delay=4.0, horizontal_deviation=0.0,
                 vertical_deviation=0.0, time_enter=0.0, time_leave=0.0, is_calculated=False):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.delay = delay
        self.horizontal_deviation = horizontal_deviation
        self.vertical_deviation = vertical_deviation
        self.time_enter = time_enter
        self.time_leave = time_leave
        self.is_calculated = is_calculated


def parse_json_to_vector_object(msg_array):
    _messages = []

    for msg in msg_array:
        _start_time = datetime.strptime(msg["depT"], AWZ_DATETIME_FORMAT)
        _path = []
        for wp in msg["path"]:
            _path.append(awzPoint(altitude=wp['altitude']['value'],
                                  latitude=wp['latitude'],
                                  longitude=wp['longitude'],
                                  speed=wp['speed'],
                                  delay=wp['delay'],
                                  horizontal_deviation=wp['deviation']['horizontal']['value'],
                                  vertical_deviation=wp['deviation']['vertical']['value'],
                                  time_enter=wp['time_enter'],
                                  time_leave=wp['time_leave'],
                                  is_calculated=wp['is_calculated']))
        _messages.append({"start_time": _start_time, "path": _path})
    return _messages


def parse_json_to_astm_object(msg_array):
    messages = []

    for msg in msg_array:
        volumes = []
        for vol in msg:
            time_start = Time(value=datetime.strptime(vol['time_start']['value'], AWZ_DATETIME_FORMAT),
                              _check_type=False)
            time_end = Time(value=datetime.strptime(vol['time_end']['value'], AWZ_DATETIME_FORMAT), _check_type=False)
            altitude_upper = Altitude(value=float(vol['volume']['altitude_lower']['value']))
            altitude_lower = Altitude(value=float(vol['volume']['altitude_upper']['value']))
            volume3d = None
            if 'outline_polygon' in vol['volume']:
                vertices = []
                for vert in vol['volume']['outline_polygon']['vertices']:
                    vertices.append(LatLngPoint(lat=vert['lat'], lng=vert['lng']))

                volume3d = Volume3D(altitude_lower=altitude_lower,
                                    altitude_upper=altitude_upper,
                                    outline_polygon=Polygon(vertices=vertices))
            elif 'outline_circle' in vol['volume']:
                center = LatLngPoint(lat=vol['volume']['outline_circle']['center']['lat'],
                                     lng=vol['volume']['outline_circle']['center']['lng'])
                radius = Radius(value=float(vol['volume']['outline_circle']['radius']['value']))
                circle = Circle(center=center, radius=radius)

                volume3d = Volume3D(altitude_lower=altitude_lower,
                                    altitude_upper=altitude_upper,
                                    outline_circle=circle)

            volume4d = Volume4D(volume=volume3d, time_start=time_start, time_end=time_end)
            volumes.append(volume4d)
        messages.append(volumes)
    return messages


def extend_segment(p1, p2, distance):
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]
    alpha = math.atan2(diff_y, diff_x)
    rad_45 = 45 * math.pi / 180.0

    if distance is None:
        distance = DEFAULT_EXPANSION_THRESHOLD

    ay = p2[1] + (distance * math.sqrt(2) * math.sin(rad_45 + alpha))
    ax = p2[0] + (distance * math.sqrt(2) * math.cos(rad_45 + alpha))
    by = p2[1] + (distance * math.sqrt(2) * math.sin(alpha - rad_45))
    bx = p2[0] + (distance * math.sqrt(2) * math.cos(alpha - rad_45))
    cy = p1[1] - (distance * math.sqrt(2) * math.sin(rad_45 + alpha))
    cx = p1[0] - (distance * math.sqrt(2) * math.cos(rad_45 + alpha))
    dy = p1[1] - (distance * math.sqrt(2) * math.sin(alpha - rad_45))
    dx = p1[0] - (distance * math.sqrt(2) * math.cos(alpha - rad_45))

    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)
    d = (dx, dy)
    return a, b, c, d


def reduce_segment(p1, p2, p3, p4):
    t = ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)
    s = ((p3[0] + p4[0]) / 2.0, (p3[1] + p4[1]) / 2.0)

    diff_x = t[0] - s[0]
    diff_y = t[1] - s[1]

    distance = math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])) / 2.0
    alpha = math.atan2(diff_y, diff_x)
    s1 = (s[0] + distance * math.cos(alpha), s[1] + distance * math.sin(alpha))
    t1 = (t[0] - distance * math.cos(alpha), t[1] - distance * math.sin(alpha))

    return s1, t1, float(round(distance))

class volume4DConverter:

    def __init__(self):
        self.time_start = None
        self.path = []
        self.geo_point = []
        self.volume_4d_array = []
        self.origin = None
        self.time_delay = T if T else 5.0

    @staticmethod
    def calculate_origin_from_path(path):
        # --------- Calculate origin by averaging the points in the path -------
        avg_calc = (0.0, 0.0)  # (latitude, longitude)
        for p in path:
            tup = (p.latitude, p.longitude)
            avg_calc = tuple(map(sum, zip(avg_calc, tup)))

        return tuple(ti / len(path) for ti in avg_calc)

    @staticmethod
    def calculate_origin_from_volumes(volumes):
        origin = (0.0, 0.0)  # (latitude, longitude)
        volume = volumes[0]
        if 'outline_polygon' in volume.volume:
            origin = (volume.volume.outline_polygon.vertices[0].lat, volume.volume.outline_polygon.vertices[0].lng)
        elif 'outline_circle' in volume.volume:
            origin = (volume.volume.outline_circle.center.lat, volume.volume.outline_circle.center.lng)

        return origin

    @staticmethod
    def is_square(p1, p2, p3, p4):
        l1 = math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
        l2 = math.sqrt((p2[0] - p3[0]) * (p2[0] - p3[0]) + (p2[1] - p3[1]) * (p2[1] - p3[1]))
        l3 = math.sqrt((p3[0] - p4[0]) * (p3[0] - p4[0]) + (p3[1] - p4[1]) * (p3[1] - p4[1]))
        l4 = math.sqrt((p4[0] - p1[0]) * (p4[0] - p1[0]) + (p4[1] - p1[1]) * (p4[1] - p1[1]))

        eps = 0.00001
        if abs(l1 - l2) < eps and abs(l2 - l3) < eps and abs(l3 - l4) < eps and abs(l4 - l1) < eps:
            return True
        return False

    def create_square_volume(self):
        altitude = self.geo_point[0][2]
        duration = 10.0
        deviation = self.path[0].horizontal_deviation
        time_end = self.time_start + timedelta(seconds=duration)

        p1 = (self.geo_point[0][0] - deviation, self.geo_point[0][1] - deviation)
        p2 = (self.geo_point[0][0] + deviation, self.geo_point[0][1] - deviation)
        p3 = (self.geo_point[0][0] + deviation, self.geo_point[0][1] + deviation)
        p4 = (self.geo_point[0][0] - deviation, self.geo_point[0][1] + deviation)

        vertices = []
        for p in [p1, p2, p3, p4]:
            pll = AzGeoUtils.geopoint(self.origin, p)
            vertices.append(LatLngPoint(lat=pll[0], lng=pll[1]))

        volume3d = Volume3D(altitude_lower=Altitude(value=float(altitude - self.path[0].vertical_deviation)),
                            altitude_upper=Altitude(value=float(altitude + self.path[0].vertical_deviation)),
                            outline_polygon=Polygon(vertices=vertices))

        volume4d = Volume4D(volume=volume3d,
                            time_start=Time(value=self.time_start, _check_type=False),
                            time_end=Time(value=time_end, _check_type=False)
                            )
        volume4d = volume4d.to_dict()
        volume4d['time_start']['value'] = volume4d['time_start']['value'].strftime(AWZ_DATETIME_FORMAT)
        volume4d['time_end']['value'] = volume4d['time_end']['value'].strftime(AWZ_DATETIME_FORMAT)
        self.volume_4d_array.append(volume4d)
        self.time_start = time_end

    def create_volume(self):
        for i in range(len(self.geo_point) - 1):
            altitude_min = min(self.geo_point[i][2], self.geo_point[i + 1][2])
            altitude_max = max(self.geo_point[i][2], self.geo_point[i + 1][2])
            if self.path[i + 1].speed == 0:
                self.path[i + 1].speed = 0.1
            duration = (math.dist(self.geo_point[i], self.geo_point[i + 1]) / self.path[i + 1].speed) + self.path[
                i].delay + self.time_delay
            time_end = self.time_start + timedelta(seconds=duration)
            p1, p2, p3, p4 = extend_segment(self.geo_point[i], self.geo_point[i + 1], self.path[i].horizontal_deviation)
            vertices = []
            for p in [p1, p2, p3, p4]:
                pll = AzGeoUtils.geopoint(self.origin, p)
                vertices.append(LatLngPoint(lat=pll[0], lng=pll[1]))

            volume3d = Volume3D(
                altitude_lower=Altitude(value=float(altitude_min - self.path[i].vertical_deviation)),
                altitude_upper=Altitude(value=float(altitude_max + self.path[i].vertical_deviation)),
                outline_polygon=Polygon(vertices=vertices))

            volume4d = Volume4D(volume=volume3d,
                                time_start=Time(value=self.time_start, _check_type=False),
                                time_end=Time(value=time_end, _check_type=False)
                                )
            volume4d = volume4d.to_dict()
            volume4d['time_start']['value'] = volume4d['time_start']['value'].strftime(AWZ_DATETIME_FORMAT)
            volume4d['time_end']['value'] = volume4d['time_end']['value'].strftime(AWZ_DATETIME_FORMAT)
            self.volume_4d_array.append(volume4d)
            self.time_start = time_end

    def create_geo_point(self):
        for poi in self.path:
            point = AzGeoUtils.point(self.origin, (poi.latitude, poi.longitude, poi.altitude))
            self.geo_point.append(point)

    def create_trajectory_path_from_volume(self, vertices_array, volume, volumes, time_enter, time_leave):
        p1, p2, p3, p4 = vertices_array[0], vertices_array[1], vertices_array[2], vertices_array[3]
        volume_4d = volume
        delay = 4.0

        enter_p, leave_p, horizontal_deviation = reduce_segment(p1, p2, p3, p4)

        gp1 = AzGeoUtils.geopoint(self.origin, enter_p)
        gp2 = AzGeoUtils.geopoint(self.origin, leave_p)

        duration = (volume_4d.time_end.value - volume_4d.time_start.value).total_seconds()

        takeoff_or_landing = self.is_square(p1, p2, p3, p4)
        try:
            if takeoff_or_landing:
                # calculate speed by altitude lower and upper and not by enter_p and leave_p
                speed = math.dist((enter_p[0], enter_p[1],
                                   (volume_4d.volume.altitude_lower.value + DEFAULT_EXPANSION_THRESHOLD)),
                                  (leave_p[0], leave_p[1],
                                   (volume_4d.volume.altitude_upper.value - DEFAULT_EXPANSION_THRESHOLD))) \
                        / (duration - delay)

            else:
                speed = float(round(math.dist(enter_p, leave_p) / (duration - delay)))
        except ZeroDivisionError:
            speed = 5.0

        altitude = (volume_4d.volume.altitude_lower.value + volume_4d.volume.altitude_upper.value) / 2.0
        vertical_deviation = (volume_4d.volume.altitude_upper.value - volume_4d.volume.altitude_lower.value) / 2

        self.path.append(
            {'altitude': {'value': altitude, 'reference': 'w84', 'unit': 'm'},
             'latitude': round(gp1[0], PRECISION),
             'longitude': round(gp1[1], PRECISION),
             'speed': speed,
             'deviation': {'horizontal': {'value': horizontal_deviation},
                           "vertical": {'value': vertical_deviation}},
             "time_enter": time_enter,
             "time_leave": time_leave})

        if volumes.index(volume_4d) == len(volumes) - 1:
            self.path.append(
                {'altitude': {'value': altitude, 'reference': 'w84', 'unit': 'm'},
                 'latitude': round(gp2[0], PRECISION),
                 'longitude': round(gp2[1], PRECISION),
                 'speed': speed,
                 'deviation': {'horizontal': {'value': horizontal_deviation},
                               "vertical": {'value': vertical_deviation}},
                 "time_enter": time_enter,
                 "time_leave": time_leave})

    def create_area_from_volume(self, vertices_array, st, et, alt_lower, alt_upper, time_e, time_l):
        polygon_pois = []
        for v in vertices_array:
            polygon_pois.append((v.lat, v.lng))

        polygon_area_data = {"type": "area",
                             "time_start": st,
                             "time_end": et,
                             "altitude_lower": alt_lower,
                             "altitude_upper": alt_upper,
                             "pois": polygon_pois}
        polygon_area_data["time_enter"] = time_e
        polygon_area_data["time_leave"] = time_l
        self.path.append(polygon_area_data)

    def create_circle_from_volume(self, volume_4d, st, et, alt_lower, alt_upper, time_e, time_l):
        the_circle_radius = volume_4d.volume.outline_circle.radius.value
        the_circle_center = volume_4d.volume.outline_circle.center
        circle_data = {"type": "circle",
                       'radius': the_circle_radius,
                       'center': the_circle_center,
                       "time_start": st,
                       "time_end": et,
                       "altitude_lower": alt_lower,
                       "altitude_upper": alt_upper}
        circle_data["time_enter"] = time_e
        circle_data["time_leave"] = time_l
        self.path.append(circle_data)

    def is_volume_trajectory(self, vertices_array):
        if len(vertices_array) != 4:
            return False

        p1 = vertices_array[0]
        p2 = vertices_array[1]
        p3 = vertices_array[2]
        p4 = vertices_array[3]

        # check if the trajectory is a rectangle
        len1 = round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 2)
        len2 = round(math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2), 2)
        len3 = round(math.sqrt((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2), 2)
        len4 = round(math.sqrt((p4[0] - p1[0]) ** 2 + (p4[1] - p1[1]) ** 2), 2)
        is_trajectory = math.fabs(len1 - len3) < 2 and math.fabs(len2 - len4) < 2
        return is_trajectory

    def path_to_volume_4d(self, awz_array_request):
        parse_data = parse_json_to_vector_object(awz_array_request)
        response = []
        for d in parse_data:
            self.time_start = d.get('start_time')
            self.path = d.get('path')

            self.origin = self.calculate_origin_from_path(self.path)
            self.volume_4d_array = []
            self.create_geo_point()

            if len(self.path) == 1:
                self.create_square_volume()

            else:
                self.create_volume()

            response.append(self.volume_4d_array)
            self.geo_point = []
            self.volume_4d_array = []
        return response

    def volumes_to_single_volume_4d(self, volumes):
        try:
            start_time = volumes[0].time_start
            end_time = volumes[-1].time_end
            min_altitude = 100000.0
            max_altitude = -10000.0

            self.origin = self.calculate_origin_from_volumes(volumes)
            points = []
            for v in volumes:
                if v.volume.altitude_upper.value > max_altitude:
                    max_altitude = v.volume.altitude_upper.value
                if v.volume.altitude_lower.value < min_altitude:
                    min_altitude = v.volume.altitude_lower.value

                for p in v.volume.outline_polygon.vertices:
                    poi = (p.lat, p.lng)
                    points.append(AzGeoUtils.point(self.origin, poi))

            np_array = np.array(points)
            hull = ConvexHull(np_array)
            back = []

            for i in range(hull.vertices.size):
                poi = AzGeoUtils.geopoint(self.origin, (np_array[hull.vertices[i], 0], np_array[hull.vertices[i], 1]))
                back.append(LatLngPoint(lat=poi[0], lng=poi[1]))
        except Exception as e:
            return e

        _volume_3d = Volume3D(altitude_lower=Altitude(value=float(min_altitude)),
                              altitude_upper=Altitude(value=float(max_altitude)),
                              outline_polygon=Polygon(vertices=back))

        return Volume4D(volume=_volume_3d, time_start=start_time, time_end=end_time)

    def volume_4d_to_path(self, oi_array_request):
        parse_data = parse_json_to_astm_object(oi_array_request)
        response = []
        for d in parse_data:
            start_time = d[0].time_start
            self.origin = self.calculate_origin_from_volumes(d)

            time_enter = 0.0
            time_leave = 0.0

            for volume_4d in d:
                st = volume_4d.time_start.value.strftime(AWZ_DATETIME_FORMAT)  # string
                et = volume_4d.time_end.value.strftime(AWZ_DATETIME_FORMAT)  # stinrg
                altitude_upper = volume_4d.volume.altitude_upper.value
                altitude_lower = volume_4d.volume.altitude_lower.value
                duration = (volume_4d.time_end.value - volume_4d.time_start.value).total_seconds()
                time_leave = time_enter + duration

                if 'outline_polygon' in volume_4d.volume and volume_4d.volume.outline_polygon is not None:
                    ver = volume_4d.volume.outline_polygon.vertices

                    p1 = AzGeoUtils.point(self.origin, (ver[0].lat, ver[0].lng))
                    p2 = AzGeoUtils.point(self.origin, (ver[1].lat, ver[1].lng))
                    p3 = AzGeoUtils.point(self.origin, (ver[2].lat, ver[2].lng))
                    p4 = AzGeoUtils.point(self.origin, (ver[3].lat, ver[3].lng))

                    is_trajectory = self.is_volume_trajectory([p1, p2, p3, p4])
                    if is_trajectory:
                        self.create_trajectory_path_from_volume([p1, p2, p3, p4], volume_4d, d, time_enter, time_leave)

                    else:  # area
                        self.create_area_from_volume(ver, st, et, altitude_lower, altitude_upper, time_enter,
                                                     time_leave)

                elif 'outline_circle' in volume_4d.volume and volume_4d.volume.outline_circle is not None:
                    self.create_circle_from_volume(volume_4d, st, et, altitude_lower, altitude_upper, time_enter,
                                                   time_leave)

                time_enter = time_leave
            response.append({"depT": start_time, "path": self.path})
            self.path = []
        return response