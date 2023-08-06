import numpy as np
import sys
import math
import datetime
import dateutil.parser as dp
import pytz
import time
import traceback
from shapely.geometry import Point as Shapely_Point
from shapely.geometry import Polygon as Shapely_Polygon
from shapely.geometry import LineString as Shaply_LineString
AWZ_TIME_FORMAT_STRING = '%Y-%m-%dT%H:%M:%S.%fZ'

class Geom:
    epsilon = 1e-8

    @staticmethod
    def dot(u, w):
        x, y, z = u
        X, Y, Z = w
        return x * X + y * Y + z * Z

    @staticmethod
    def length(u):
        x, y, z = u
        return math.sqrt(x * x + y * y + z * z)

    @staticmethod
    def vector(b, e):
        x, y, z = b
        X, Y, Z = e
        return (X - x, Y - y, Z - z)

    @staticmethod
    def unit(u):
        x, y, z = u
        mag = Geom.length(u)
        return (x / mag, y / mag, z / mag)

    @staticmethod
    def distance(p0, p1):
        return Geom.length(Geom.vector(p0, p1))

    @staticmethod
    def scale(u, sc):
        x, y, z = u
        return (x * sc, y * sc, z * sc)

    @staticmethod
    def add(u, w):
        x, y, z = u
        X, Y, Z = w
        return (x + X, y + Y, z + Z)

    @staticmethod
    def sub(u, w):
        x, y, z = u
        X, Y, Z = w
        return (x - X, y - Y, z - Z)

    @staticmethod
    def velvec(d, t):
        if t > 0:
            v = Geom.scale(d, 1/t)
            return (v)
        else:
            return(0.0, 0.0, 0.0)

    @staticmethod
    def geo2tuple(lon,lat,alt):
        x = lon * 111111.0 * math.cos(math.pi*lat/180.0)
        y = lat * 111111.0
        z = alt
        return (x, y, z)

    @staticmethod
    def geotuple2tuple(p,lat):

        x = p[0] * 111111.0 * math.cos((math.pi*lat)/180.0)
        y = p[1] * 111111.0
        z = p[2]
        return (x, y, z)

    @staticmethod
    def tuple2geotuple(p, origin):

        lat = (origin[1] + p[1])/111111.0
        org_lat = (origin[1])/111111.0
        _cos = math.cos((math.pi * org_lat) / 180.0)
        if _cos >= Geom.epsilon:
            lon = (origin[0] + p[0])/(111111.0*_cos)
        else:
            lon = 0
        if len(p) == 3 and len(origin) == 3:
            alt = origin[2] + p[2]
        else:
            alt = 0
        return (lon, lat, alt )


    @staticmethod
    def Polygon2d(points: list):
        try:
            poly = Shapely_Polygon(points)
        except:
            poly = None
        return poly


    # returns true if a point is within a given polygon, false otherwise
    @staticmethod
    def WithinPolygon2d(point: tuple, poly: Shapely_Polygon):
        p1 = Shapely_Point(point)
        if p1.within(poly):
            return True
        else:
            return False

    # returns the first intersection point between a 2d line segment and a 2d polygon
    # the first point in the line segment, must be outside the polygon.
    # the second point in the line segment, must be inside the polygon
    # if there is no intersection between the line and the polygon, None is returned.

    @staticmethod
    def Polygon2d_segment_intersection(poly:Shapely_Polygon, points: list):
        res = None
        line = Shaply_LineString(points)
        is_intersect = poly.intersects(line)
        if (is_intersect):
            inters = poly.intersection(line)
            a = (inters.coords.xy[0][0], inters.coords.xy[1][0])
        return a

    @staticmethod
    def Polygon2d_center(poly:Shapely_Polygon):
        coords =  poly.centroid.coords[:]
        return coords[0]

    # Given a line with coordinates 'start' and 'end' and the
    # coordinates of a point 'pnt' the proc returns the shortest
    # distance from pnt to the line and the coordinates of the
    # nearest point on the line.
    #
    # 1  Convert the line segment to a vector ('line_vec').
    # 2  Create a vector connecting start to pnt ('pnt_vec').
    # 3  Find the length of the line vector ('line_len').
    # 4  Convert line_vec to a unit vector ('line_unitvec').
    # 5  Scale pnt_vec by line_len ('pnt_vec_scaled').
    # 6  Get the dot product of line_unitvec and pnt_vec_scaled ('t').
    # 7  Ensure t is in the range 0 to 1.
    # 8  Use t to get the nearest location on the line to the end
    #    of vector pnt_vec_scaled ('nearest').
    # 9  Calculate the distance from nearest to pnt_vec_scaled.
    # 10 Translate nearest back to the start/end line.
    # Malcolm Kesson 16 Dec 2012

    @staticmethod
    def pnt2line(pnt, start, end):
        line_vec = Geom.vector(start, end)
        pnt_vec = Geom.vector(start, pnt)
        line_len = Geom.length(line_vec)
        if (line_len > 0.0):
            line_unitvec = Geom.unit(line_vec)
            pnt_vec_scaled = Geom.scale(pnt_vec, 1.0 / line_len)
            t = Geom.dot(line_unitvec, pnt_vec_scaled)
            if t < 0.0:
                t = 0.0
            elif t > 1.0:
                t = 1.0
            nearest = Geom.scale(line_vec, t)
            dist = Geom.distance(nearest, pnt_vec)
            nearest = Geom.add(nearest, start)
        else:
            nearest = start
            dist = Geom.distance(start,pnt)
        return dist, nearest

    @staticmethod
    def convert_volume4d_list_geo_2tuplem_2d(wp:list, origin_m:tuple, lat_for_calc:float)->list: # convert volume dict list of points to a list of (x,y) tupples
        out_list = []

        try:
            for ent in wp:
                p = (ent["lng"], ent["lat"], 0.0)
                xyz = Geom.sub(Geom.geotuple2tuple(p,lat_for_calc), origin_m)
                xy= (xyz[0],xyz[1])
                out_list.append(xy)
        except:
            raise Exception(f"Error while parsing a volume geo msg !!\n {traceback.format_exc()}")
        return out_list

    @staticmethod
    def convert_list_geo_2tuplem(wp:list)->list: # convert geo dict list of points to a list of (x,y,z) tupples
        out_list = []
        try:
            for ent in wp:
                p = (ent["longitude"], ent["latitude"], ent["altitude"])
                xyz = Geom.geotuple2tuple(p,p[1])
                out_list.append(xyz)
        except:
            raise Exception(f"Error while parsing a geo msg !!\n {traceback.format_exc()}")
        return out_list

    @staticmethod
    def convert_list_geo_2tuplem_origin(wp:list, origin:tuple)->list:
        # convert geo dict list of points to a list of (x,y,z) tupple, around an origin
        out_list = []
        try:
            for ent in wp:
                p = (ent["longitude"], ent["latitude"], ent["altitude"])
                dp =  Geom.sub(p,origin)
                xyz = Geom.geotuple2tuple(dp,p[1])
                out_list.append(xyz)
        except:
            raise Exception(f"Error while parsing a geo msg !!\n {traceback.format_exc()}")
        return out_list

    @staticmethod
    def polygon_calc_area(polygon):
        if isinstance(polygon, list):
            result = 0.0
            try:
                pa = Geom.Polygon2d(polygon)
                result = pa.area

            except:
                raise Exception(f"Error while parsing polygon tupples !!\n {traceback.format_exc()}")

            return result

        else:
            raise Exception(f"illegal format of polygon tupples !!\n {traceback.format_exc()}")

    @staticmethod
    def polygon_calc_intersection(ref_polygon, target_polygon):
        if isinstance(ref_polygon, list) and isinstance(target_polygon, list):
            result = 0.0
            try:
                pa = Geom.Polygon2d(ref_polygon)
                pb = Geom.Polygon2d(target_polygon)


                if pa.intersects(pb):
                    result = pb.intersection(pa).area / pb.area
            except:
                raise Exception(f"Error while parsing polygon tupples !!\n {traceback.format_exc()}")
            return result
        else:
            raise Exception(f"illegal format of polygon tupples !!\n {traceback.format_exc()}")

    @staticmethod
    def polygon_intersection(ref_polygon, target_polygon):
        if isinstance(ref_polygon, list) and isinstance(target_polygon, list):
            result = False
            try:
                pa = Geom.Polygon2d(ref_polygon)
                pb = Geom.Polygon2d(target_polygon)

                if pa.intersects(pb):
                    result = True
            except:
                raise Exception(f"Error while parsing polygon tupples !!\n {traceback.format_exc()}")
            return result
        else:
            raise Exception(f"illegal format of polygon tupples !!\n {traceback.format_exc()}")


    #finds if a a polygon and circle intersect
    @staticmethod
    def polygon_circle_intersection(ref_polygon, target_center, target_radius):
        if isinstance(ref_polygon, list) and isinstance(target_center, tuple):
            result = False
            try:
                pa = Geom.Polygon2d(ref_polygon)
                cr = Shapely_Point(target_center[0],target_center[1]).buffer(target_radius)

                if cr.intersects(pa):
                    result = True
            except:
                raise Exception(f"Error while parsing polygon tupples !!\n {traceback.format_exc()}")
            return result
        else:
            raise Exception(f"illegal format of polygon or circle center tupples !!\n {traceback.format_exc()}")

        # finds if a a polygon and circle intersect

    @staticmethod
    def circle_intersection(ref_center, ref_radius, target_center, target_radius):
        if isinstance(ref_center, tuple) and isinstance(target_center, tuple):
            result = False
            try:
                dist = Geom.distance(ref_center,target_center)
                if dist <= ref_radius + target_radius:
                    result = True
            except:
                raise Exception(f"Error while parsing polygon tupples !!\n {traceback.format_exc()}")
            return result
        else:
            raise Exception(f"illegal format of polygon or circle center tupples !!\n {traceback.format_exc()}")

    # sort key function, returning the CW angle of the point to a ref vector + its vector length
    @staticmethod
    def clockwise_angle_and_distance(point: list, origin: list):
        # Vector between pts and the origin: v = p - o
        refvec = [0, 1]
        vector = [point[0] - origin[0], point[1] - origin[1]]
        # Length of vector: ||v||
        lenvector = math.hypot(vector[0], vector[1])
        # If length is zero there is no angle
        if lenvector == 0:
            return -math.pi, 0
        # Normalize vector: v/||v||
        normalized = [vector[0] / lenvector, vector[1] / lenvector]
        dotprod = normalized[0] * refvec[0] + normalized[1] * refvec[1]  # x1*x2 + y1*y2
        diffprod = refvec[1] * normalized[0] - refvec[0] * normalized[1]  # x1*y2 - y1*x2
        angle = math.atan2(diffprod, dotprod)
        # Negative angles represent counter-clockwise angles so we need to subtract them
        # from 2*pi (360 degrees)
        if angle < 0:
            return 2 * math.pi + angle, lenvector
        # I return first the angle because that's the primary sorting criterium
        # but if two vectors have the same angle then the shorter distance should come first.
        return angle, lenvector

    # sort list of 2d points, representing a CONVEX polygon, into a CW ordered list of points
    # each point must contain at least 2 components, more components are legal, but will be ignored.
    @staticmethod
    def sort_polygon_as_list_cw(pts:list):
        result = []
        try:
            tmp = np.array(pts)
            p1 = (tmp[0,0], tmp[0,1],0)
            n = tmp.shape[0]
            pn = (tmp[n-1,0], tmp[n-1,1],0)
            if Geom.distance(p1,pn) < Geom.epsilon:
                pts.pop()
            origin = (tmp.mean(axis=0)).tolist()
            result = sorted(pts, key=lambda point: Geom.clockwise_angle_and_distance(point, origin))

        except:
            raise Exception(f"Error while sorting polygon tupples !!\n {traceback.format_exc()}")
        return result


def TimeStampAsIntMs() -> int:

    timestamp = int(time.mktime((datetime.datetime.now()).timetuple())*1000.0 +
                                 datetime.datetime.now().microsecond/1000.0)
    return timestamp


def TimeStampAsFloatInSec() -> float:

    timestamp =  (time.mktime((datetime.datetime.now()).timetuple())*1000.0 +
                  datetime.datetime.now().microsecond/1000.0)/1000
    return timestamp

def TimeStampAsStrIsoFormat()-> str:

    timestamp = datetime.datetime.now(pytz.utc).isoformat()
    return timestamp

def TimeStampStr2Sec(str)-> float:
    try:
        
        parsed_t = dp.parse(str)
        t_in_seconds = parsed_t.timestamp()
        return t_in_seconds
    except:
        raise Exception(f"Error while parsing a time stamp msg !!\n {traceback.format_exc()}")

def TimeStampStr2SecSpecific(timestamp_str: str) -> float:
    try:
        parsed_t = datetime.datetime.strptime(timestamp_str, AWZ_TIME_FORMAT_STRING)
        t_in_seconds = parsed_t.timestamp()
        return t_in_seconds
    except Exception as e:
        raise Exception(f"Error while parsing a timestamp: {e}")

#copy into dict, while not changing its reference
# this is needed for cases where dict are e.g. shared between threads.

def CopyDictDeep(source:dict, dest:dict):
    if type(source) == dict and type(dest) == dict:
        dest.clear()
        the_keys = source.keys()
        for a_key in the_keys:
            dest.update({a_key: source[a_key]})


if __name__ == "__main__":
    poly = Geom.Polygon2d([(0,0),(0,1),(1,1),(1,0)])
    line = [(4.0,0.5),(0.5,0.5)]
    a = Geom.Polygon2d_segment_intersection(poly, line)
    
    now1 = datetime.datetime.now(pytz.utc)
    now_plus_setup_delay = now1 + datetime.timedelta(seconds=30.0)
