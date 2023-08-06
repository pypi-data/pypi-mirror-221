''''
MCPOP

Algorithm for alert filtering:
_______________________________

1) For each rejected drone, a dictionary entry will be opened, based on drone_name + '_' + org_id as a key
2) on entry initiation, its filter flag will be set to off and the alert will not be filter. break
3) after <filter_time> seconds the entry is deleted.  break
4) for each iteration where there is an alert for the same drone + org id:
         if the type of alert has been changed - filter is off
         if the correction type has changed - filter is off ( future code)
         if none of the above, we compare the current and previous suggested path, testing cases in the following order:
            a) both null - filter is on. break.
            b) one null and the other is not, filter is off. break
            c) one of the entry is with size 1, filter is off. break
            d) current entry size > previous entry size,filter is off. break
            e) check that first point of current, is on the path of previous ( allowing DIST1 tolerance) if not, filter
                off, break.
            f) save the next poi as the first point of previous path, removing earlier pois.
            g) insert current location as the first position in previous path.
            h) now compare each poi of current with each poi of previous. if equal ( allowing DIST2 tolerance,
               smaller than DIST1 ). If equal, filter is off, otherwise, filter is on.
5) in any case, set current path as previous path.
6) delete the alert entry from the input alert list, if its filter value is on.

'''

from datetime import datetime
import sys
import copy
import json
import traceback
import math
import dateutil.parser as dp
from dataclasses import dataclass
from enum import Enum, IntEnum
import logging
#sys.path.append('../')
from common.azutils import Geom, TimeStampAsFloatInSec
from common.common_def import MCPUtil

class MCPOP_Config:
    filter_time = 30.0
    nfz_filter_time = 60.0
    speed_factor = 0.3
    default_delay = 4.0
    min_time_between_positions_entries =0.025


class CollisionType(IntEnum):
    Drones = 0
    NFZ = 1
    Other = 2
    NoCol = 3


class CorrectionType(IntEnum):
    Linear = 0
    Delay = 1
    Vertical = 2
    NoSug = 3
    NoCol = 4


class MCPOP_Record:
# record containing  current and previous track data

    def __init__(self, name, org=""):
        self.name = name
        self.org  = org
        self.wp = []
        self.prev_wp = []
        self.collision_type = CollisionType.NoCol
        self.to_filter = False
        self.prev_nfz_id = None
        self.nfz_id = None
        self.time = 0.0
        self.first_time = True
        

    def set(self, wp, time, collision_type, correction_type, nfz_id):

        self.collision_type = collision_type
        self.wp =  copy.deepcopy(wp)
        self.first_time = False
        self.time = time
        self.to_filter = False
        self.nfz_id = nfz_id

    def update(self,wp, time, collision_type, correction_type, nfz_id):
        self.to_filter = False
        
        self.prev_nfz_id = copy.deepcopy(self.nfz_id)
        self.nfz_id = nfz_id
        self.prev_wp = copy.deepcopy(self.wp)
        self.wp = copy.deepcopy(wp)
        # self.time = time # UPDATE time
        if self.collision_type != collision_type:
            self.to_filter = False
        else:
            self.to_filter = self.is_same_sugpath(self.prev_wp, self.wp)
        self.collision_type = collision_type

    def is_old(self, t_in_seconds):
        # if math.fabs(t_in_seconds - self.time) > MCPOP_Config.filter_time:
        #     return True
        if self.collision_type == CollisionType.Drones and math.fabs(t_in_seconds - self.time) > MCPOP_Config.filter_time:
            return True

        elif self.collision_type == CollisionType.NFZ and math.fabs(t_in_seconds - self.time) > MCPOP_Config.nfz_filter_time:
            return True
        else:
            return False

    def is_same_sugpath(self, wp1, wp2):
        try:

            if wp1 is None and wp2 is None: # we had not and still don't have an alternative path.
                return True
            if wp1 is None or wp2 is None:  # only one is none, we should not filter.
                return False
            if type(wp1) != list or type(wp2) != list:                
                return False


            if self.collision_type == CollisionType.NFZ:
                return self.prev_nfz_id == self.nfz_id 

            if len(wp2) > len(wp1): # wp2 has surely  changed.
                return False
            # convert to tupple-meters (x,y,z)
            # find on what segment, the current location is, on wpm1.
            # if it is close enough to the segment, we can compare from this point onward.
            
                
            wpm1 = Geom.convert_list_geo_2tuplem(wp1)
            wpm2 = Geom.convert_list_geo_2tuplem(wp2)
            wpm1_poi_index = 0
            current_loc        = wpm2[0]
            current_loc_geo    = wp2[0]
            dist = 999.0
            nearest = (0,0,0)
            for i in range (0,len(wpm1)-1):

                dist, nearest = Geom.pnt2line(current_loc, wpm1[i], wpm1[i+1])
                if dist <= MCPUtil.dist1:
                    break
                wpm1_poi_index +=1

            poi_diff = False
            if wpm1_poi_index < len(wpm1)-1: # current location is +/- on previous sugg. path.
               # update current location, and compare the two lists.
               wp11  = [current_loc] + wpm1[(wpm1_poi_index+1):]
               wp11_geo  = [current_loc_geo] + wp1[(wpm1_poi_index+1):]
               for ent1, ent2 in zip(wp11_geo, wp2):
                   # check delay, speed, and distance between poi.
                   if math.fabs(ent1["delay"]- ent2["delay"]) > MCPUtil.dtime:
                       poi_diff = True
                       break
                   if math.fabs(ent1["speed"] - ent2["speed"]) > MCPUtil.dspeed:
                       poi_diff = True
                       break
                   ent1m_as_list = Geom.convert_list_geo_2tuplem([ent1])
                   ent2m_as_list = Geom.convert_list_geo_2tuplem([ent2])
                   poi_distance  = Geom.distance(ent1m_as_list[0],ent2m_as_list[0])
                   if poi_distance >    MCPUtil.dist2:
                       poi_diff = True
                       break

               if poi_diff:
                   return False
               else:
                   return True

            else:
               return False


        except:
            raise Exception(f"Error while processing an alert msg !!\n {traceback.format_exc()}")


class MCPOP_Container:
    def __init__(self):
        self.entities = {}

    def add_entity(self,identity, wp, t_in_seconds, rejection_type, correction_type, nfz_id):
        # add an entity into the dictionary
        mcpop_record = MCPOP_Record(identity)
        mcpop_record.set(wp, t_in_seconds, rejection_type, correction_type, nfz_id)
        key  = identity
        self.entities[key] = mcpop_record

    def update_entity(self, key, wp, t_in_seconds, rejection_type, correction_type):
        self.entities[key].update(wp,  t_in_seconds, rejection_type, correction_type) # update  an entity

    def remove_entity(self, key):
        if key in self.entities.keys():
            del self.entities[key]

    def timestamp_str_to_seconds(self, str):
        parsed_t = dp.parse(str)
        t_in_seconds = parsed_t.timestamp()#/(3600.0*24.0*365.24)
        return t_in_seconds


    def parse_monitor_msg(self, alerts):
        try:
            filterd_alerts = []

            if isinstance(alerts, list):# type(alerts) == list:
                
                # # delete all old alerts
                # t_in_seconds = TimeStampAsFloatInSec()
                # key_to_delete = []
                # for the_key, the_value in self.entities.items():
                #     if the_value.is_old(t_in_seconds):
                #         key_to_delete.append(the_key)
                # for key in key_to_delete:
                #     self.remove_entity(key)

                for alert in alerts:
                    identity = None
                    nfz_id = None
                    code_str = alert["type"]
                    details = alert["details"]

                    if code_str == "collision" or code_str == "nfz":
                        rejection_type = CollisionType.Drones if code_str != "nfz" else CollisionType.NFZ
                        correction_type = CorrectionType.Linear # currently we do not use this.

                        if rejection_type == CollisionType.NFZ:
                            identity = details.get("drone_id")
                            nfz_id = details.get("nfz_id")
                        else:
                            drones_list = details.get("drones", [None])
                            if isinstance(drones_list, list) and len(drones_list) > 0:
                                identity = drones_list[0]


                        paths = details.get("suggested_path", {})
                        if "paths" in paths:
                            paths = paths["paths"]
                        path = paths.get("awz", None)

                        if path is not None:
                            wp = []
                            # convert v2.1 path to v1.1
                            for p in path.get("waypoints", []):
                                temp_wp_dict = {}
                                temp_wp_dict["delay"] = p.get("delay", 0.0)
                                temp_wp_dict["speed"] = p.get("speed", 0.0)
                                temp_wp_dict["latitude"] = p.get("latitude", 0.0)
                                temp_wp_dict["longitude"] = p.get("longitude", 0.0)
                                alt_obj = p.get("altitude", {})
                                temp_wp_dict["altitude"] = alt_obj.get("value", 0.0)

                                wp.append(temp_wp_dict)
                            start_time_str = path['time_start']['value']
                            if isinstance(start_time_str, datetime):
                                start_time_str = start_time_str.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                            t_in_seconds = self.timestamp_str_to_seconds(start_time_str)
                            
                        else:
                            wp = None
                            t_in_seconds = TimeStampAsFloatInSec()

                        if identity is not None:
                            the_key = identity
                            if the_key in self.entities.keys():
                                if  self.entities[the_key].is_old(t_in_seconds):
                                    self.remove_entity(the_key)
     
                            if the_key in self.entities.keys():
                                self.entities[the_key].update(wp, t_in_seconds, rejection_type, correction_type, nfz_id)
                            else:
                                self.add_entity(identity, wp, t_in_seconds, rejection_type, correction_type, nfz_id)
    
                                    
                            if self.entities[the_key].to_filter == False:
                                filterd_alerts.append(alert)

        except:
            logging.error("Error while parsing a monitor msg !!")
            trace = traceback.format_exc()
            logging.error(trace)

        return (filterd_alerts)


if __name__ == "__main__":

    logging.basicConfig(level = logging.INFO,filename='mcpop.log')
    mcpop_test_file = "./data/monitor_sample_for_MCPOP.json"
    try:

        with open(mcpop_test_file) as f:
            dict = json.load(f)
            entry_list = dict["mcpop_test"]
    except Exception as e:
        raise Exception("Error while reading the test file")

    container = MCPOP_Container()
    for entry in entry_list:
        body = entry["body"]
        dat  = body["data"]
        msg = container.parse_monitor_msg(dat)
