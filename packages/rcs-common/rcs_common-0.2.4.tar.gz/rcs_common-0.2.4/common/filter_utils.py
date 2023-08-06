import numpy as np
import math
from shapely.geometry import Point, Polygon as Shaply_Polygon
from rtree import index


# a simple object containing the minimal representation of 4D polygons.
# the object also contains a unique string identification, preferably derived from a uuid4 object.
#
#
class Polygon4Filter:
    def __init__(self, poly:Shaply_Polygon, id:str, y_min = -10e12, y_max = 10e12, t_min = 0, t_max = 10e12):
        self.poly = poly
        self.id = id # must be a unique string !
        self.y_min  =  y_min
        self.y_max  =  y_max
        self.t_min  = t_min
        self.t_max  = t_max


# this class receives one or more dictionaries containing string ids as keys and Polygon4Filter as
# corresponding objects
# typically, the first dictionary would represent static NFZs, and other dictionaties representations V4 volumes,
# but this is an issue of the caller, not this library.
# then it can get multiple queries of rectangle 2D areas, and return a list of polygon objects, most likely to intersect or to
# be included within the query rectangle areas.
# Future extensions:
# a. 3D and 4D filtersfurthermore
# b. Request a unification set of the polygons, i.e. a set of non intersecting ploygons,
#       wherein each previously intersecting polygons had been unified in a recusive manner.

class GeoFilter:
    def __init__(self):
        self.poly_dict = {}
        self.idx =  index.Index()

    def add_polygons4filters(self, poly_dict):
        if isinstance(poly_dict, dict) and len(poly_dict) > 0:
            index = len(self.poly_dict)
            for key, value in poly_dict.items():
                if isinstance(value, Polygon4Filter):
                    poly = value.poly # for now we are only do 2d filtering

                    self.idx.insert(id=index, coordinates=poly.bounds, obj=key)
                    index += 1
                else:
                    raise TypeError("GeoFilter: input must contain shaply poligons")
            self.poly_dict |= poly_dict
        else:
            raise TypeError("GeoFilter: input must contain a non empty dict")

    def get_filtered_polygons_as_dict(self, min_xy, max_xy,):

        out_dict = {}
        if len (self.poly_dict)> 0:
            objects_list =   [n.object for n in self.idx.intersection((min_xy[0], min_xy[1], max_xy[0], max_xy[1]), objects=True)]
            #indices = list(idx.intersection((min_xy[0], min_xy[1], max_xy[0], max_xy[1])))
            for obj in objects_list:
                if obj is not None:
                    out_dict[obj] = self.poly_dict[obj]
        return out_dict
