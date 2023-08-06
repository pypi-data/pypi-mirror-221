import datetime
import pytz
import time
import logging
import sys
import copy
import json
import traceback
import dateutil.parser as dp
from dataclasses import dataclass
from enum import Enum, IntEnum
sys.path.append('../')
from common.azutils import Geom
from common.common_def import MCPUtil

class MCPRE_Config:
    epsilon  =  0.001
    speed_factor = 0.3
    default_delay = 4.0
    min_time_between_positions_entries = 0.025
    calc_nextPoi = True # if True, calc next poi, regardless in nextPoi exist or not, in input

class DroneDelayState(IntEnum):
    Undefined        = 0
    Delay            = 1
    Moving           = 2


# currently for Monitor entry only
# Parse input
# get name, uss, position, velocity ( from positions - if valid), path
# get position from path[0] and next poi location from path[1]
# per each entry update dictionary
# key is uss + drone name
# each entry contains, current record, last record.
# each record contains:
#   a) Current Position
#   b) Position of Next Poi
#   b) Speed  ( 0.5*previous speed + (0.5*(Position - Prev(Current Position))*Dt)
#   b) Distance from next poi
#   c) Delay value ( -1 for moving drones)
#   d) Time ( in s)
#   e) State - Delay/Moving
#   f) Delay_Start - time of delay start if State = Delay. Othewise, irrelevant
#   g) Current POI - reserved only when we are in a delay session. Otherwise does not exist.
#  Algorithm:
#  if Speed > 0.3 *expected speed, then moving = True, State = Moving
#  if State == Moving ( position changed) and not close to next poi Delay = -1
#  if State == moving and close to next poi, Delay = 0, Delay_Start = Now. Current_POI = path[1]
#  if Speed <0.3  and close to prev(current POI):
#        Delay = Expected_Delay - (now - Delay_Start)
#        current_POI = prev(Current POI)
#
#
@dataclass
class Position:
    longitude: float
    latitude:  float
    altitude:  float
    v_total:   float
    vx:        float
    vy:        float
    vz:        float
    time:      int
    timepp:    int
    valid:     bool

    def __init__(self, positions):
        self.longitude = self.latitude = self.altitude = 0.0
        self.vx = self.vy = self.vz = self.v_total = 0.0
        self.valid = True
        if len(positions) >= 2:
            p1 = (positions[0].get('longitude',0.0),
                                  positions[0].get('latitude',0.0),
                                  positions[0].get('altitude',0.0))

            p2 = (positions[1].get('longitude', 0.0),
                                  positions[1].get('latitude', 0.0),
                                  positions[1].get('altitude', 0.0))

            dt = (float(positions[1].get('time', 100) - positions[0].get('time', 0)))/1000.0
            if dt >= MCPRE_Config.min_time_between_positions_entries:
                dp = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
                dpm = Geom.geotuple2tuple(dp,p2[1])
                (vx, vy, vz) = Geom.velvec(dpm, dt)
                self.vx, self.vy, self.vz = (vx, vy, vz)
                self.v_total = Geom.length((self.vx, self.vy, self.vz))
            else:
                self.v_total =  self.vx = self.vy = self.vz = 0
                self.valid = False
            self.longitude= p2[0]
            self.latitude = p2[1]
            self.altitude = p2[2]
            self.time = positions[1].get('time', 100)
            self.timepp = positions[0].get('time', 0)
            
        else:
            self.time = 100
            self.timepp = 0
            self.valid = False

    def is_valid(self):
            return self.valid

    def actual_speed(self):
            return self.v_total


class MCPRE_TrackingRecord:
# record containing either current or previous track data

    def __init__(self,initial_poi_time):
        self.cur_position = 0.0
        self.nextPoi_position = 0.0
        self.currentPoi_position  =0.0 # current POI, including delay at this POI.
        self.speed = 0.0
        self.distance_from_nextPoi = 0.0
        self.delay = 0.0
        self.calc_delay = -1.0 # remaining delay. for now, unknown
        self.time = 0.0
        self.state = DroneDelayState.Undefined
        self.next_poi = -1
        self.flyingState = 100
        self.last_poi_time = initial_poi_time
        self.calc_next_poi = -1
        self.wp = None
        self.origin = None 

    def reset(self):

        self.cur_position = (0.0, 0.0, 0.0)
        self.speed = 0.0
        self.distance_from_nextPoi = 0.0
        self.delay = 0.0
        self.calc_delay = -1.0  # remaining delay. for now, unknown
        self.time = 0.0
        self.state = DroneDelayState.Undefined
        self.next_poi = -1
        self.flyingState = 100
        self.calc_next_poi = -1
        self.wp = None
        self.origin = None
        
        
    def flyingState_as_int(self, flyingState):
        if type(flyingState) == int:
            return (flyingState)
        else:
            result = 0
            try:
                result = int(flyingState)
            except:
                result = 100 # we will not track a badly format flying state
            return result


    # Algoritm:
    #    next poi calculation:
    #    if calc next poi is in config or next_poi = None - perform poi calculation
    #    if next_poi is not None, use it as the "real poi". Otherwise, use the given next_poi
    #    save both the given next poi, and the calc poi.
    #    if calc poi is not calculated, it would be -999
    #
    #
    #


    def set(self, wp, time, position, prev_record, provided_next_poi, flyingState):

        next_poi = provided_next_poi
        fs_int = self.flyingState_as_int(flyingState)
        p0 = (position.longitude, position.latitude, position.altitude)
        if prev_record is None:
            self.origin = (position.longitude, position.latitude, 0.0)
        else:
            self.origin = prev_record.origin

        err_list = []
        if MCPRE_Config.calc_nextPoi or next_poi is None:
            wp_prev = None
            if prev_record is not None:
                wp_prev = prev_record.wp
            self.calc_next_poi,  self.last_poi_time, err_list = \
                MCPUtil.calc_next_poi(wp_prev, wp, p0,  self.calc_next_poi, self.last_poi_time, fs_int)
            if next_poi is None and len(err_list ) == 0: # we have no real next poi. Use the calculated one, if valid.
                next_poi = self.calc_next_poi
        if next_poi is None or next_poi < 0 or next_poi >= len(wp):
            # either still no Next Poi could be produced, or not in a flight
            self.reset()
        else:
            self.next_poi = next_poi
            self.wp = wp
            p1    = (wp[next_poi]["longitude"], wp[next_poi]["latitude"], wp[next_poi]["altitude"])
 
            self.speed      = wp[next_poi]["speed"]
            self.time = time
            self.delay = wp[next_poi]["delay"]
            p0_tr = Geom.sub(p0, self.origin)
            p1_tr = Geom.sub(p1, self.origin)
            self.cur_position = Geom.geotuple2tuple(p0_tr, self.origin[1])
            next_poi_position = Geom.geotuple2tuple(p1_tr, self.origin[1])
            if prev_record is None:
                if position.is_valid():
                    actual_speed = position.actual_speed()
                else:
                    return
            else:
                if position.is_valid():
                    actual_speed = position.actual_speed()
                else:
                    dt = self.time - prev_record.time
                    if (dt > MCPRE_Config.epsilon):
                        actual_speed =  Geom.distance(self.cur_position, prev_record.cur_position)/dt
                    else:
                        actual_speed = self.speed

                if actual_speed > MCPRE_Config.speed_factor *self.speed and next_poi <= prev_record.next_poi:
                    # we are moving, between POIs, so we look for the next poi
                    self.state = DroneDelayState.Moving
                    self.calc_delay = 0.0 # we are moving, no delay
                else:
                    # we are in a delay the current poi is where we standing, not the next poi
                    self.state = DroneDelayState.Delay
                    if prev_record is None and next_poi > 0:
                        self.calc_delay = wp[next_poi -1]["delay"]
                    elif prev_record is None and next_poi == 0:
                        self.calc_delay = 0.0
                    elif prev_record is not None and next_poi > prev_record.next_poi:
                        self.calc_delay = wp[next_poi - 1]["delay"]
                    elif prev_record is not None and prev_record.calc_delay > 0.0:
                        self.calc_delay = max(prev_record.calc_delay - (self.time - prev_record.time)/1000.0, 0.0)
                    else:
                        self.calc_delay = -1.0 # could not resolve
                        self.state = DroneDelayState.Undefined

#  if State == Moving ( position changed) and not close to next poi Delay = -1
#  if State == moving and close to next poi, Delay = 0, Delay_Start = Now. Current_POI = path[1]
#  if Speed <0.3  and close to prev(current POI):
#        Delay = Expected_Delay - (now - Delay_Start)
#        current_POI = prev(Current POI)


class MCPRE_Record:
# a class containing identification data, current and previous tracking records.
    def __init__(self, name, org_id, priority, model,t_in_seconds):
        self.current_record = MCPRE_TrackingRecord(t_in_seconds)
        self.previous_record = MCPRE_TrackingRecord(t_in_seconds)
        self.name = name
        self.org_id = org_id
        self.key = name + '_' + org_id
        self.priority = priority
        self.model    = model
        self.remaining_delay    = -1.0
        self.calc_next_poi = -1

    def set(self, wp, time, position, next_poi, flyingState):
        self.current_record.set(wp, time, position, None, next_poi, flyingState)
        self.remaining_delay = self.current_record.calc_delay
        self.calc_next_poi = self.current_record.calc_next_poi

    def update(self, wp, time, position, next_poi, flyingState):
        if self.current_record.origin is not None:
            self.previous_record =copy.deepcopy(self.current_record)
        self.current_record.set(wp, time, position, self.previous_record, next_poi, flyingState)
        self.remaining_delay = self.current_record.calc_delay
        self.calc_next_poi = self.current_record.calc_next_poi

    def get_remaining_delay(self):
        return self.remaining_delay


class MCPRE_Container:
    def __init__(self):
        self.entities = {}

    def add_entity(self,name, org_id, priority, model, wp, t_in_seconds, position, next_poi, flyingState):
        # add an entity into the dictionary
        mcp_record = MCPRE_Record(name, org_id, priority, model,t_in_seconds)
        key  = mcp_record.key
        self.entities[key] = mcp_record
        mcp_record.set(wp, t_in_seconds, position, next_poi, flyingState)
     
    def update_entity(self, key, wp, time, position, next_poi, flyingState):
        self.entities[key].update(wp, time, position, next_poi, flyingState) # update  an entity

    def remove_entity(self, key):
        if key in self.entities.keys():
            del self.entities[key]

    def get_remaining_delay(self, the_key):
        # returns remaining delay for an entity key:
        # > 0 - drone is in a delay having remaining delay in sec.
        # 0 - if there is no delay (drone is moving)
        # -1 - unknown, or key not found
        the_delay = -1.0
        if the_key in self.entities.keys():
            the_delay = self.entities[the_key].get_remaining_delay()
            #the_delay = self.entities.keys[the_key].get_remaining_delay()
        return the_delay

    def timestamp_str_to_seconds(self, str):
        parsed_t = dp.parse(str)
        t_in_seconds = parsed_t.timestamp()#/(3600.0*24.0*365.24)
        return t_in_seconds


    def convert_data_from_rcs_to_mcpre(self, rcs_data, utm_time=""):

        entities = []

        _nfzs = rcs_data.get("nfzs", {})
        _usses = rcs_data.get("usses", {})

        for org_id, org_data in _usses.items():
            _entities = org_data.get("entities", {})
            for _, drone_data in _entities.items():
                if "data" not in drone_data: 
                    continue

                tmp_drone_data = drone_data["data"]["drone"]
                if tmp_drone_data["flyingState"] in ["101", "100", 100, 101]:
                    continue
                tmp_drone_dict = {}
                tmp_drone_dict["id"] = tmp_drone_data["id"]
                tmp_drone_dict["model"] = tmp_drone_data["model"]
                tmp_drone_dict["name"] = tmp_drone_data["name"]
                tmp_drone_dict["org_id"] = org_id
                tmp_drone_dict["priority"] = tmp_drone_data.get("priority", 0)
                tmp_drone_dict["flyingState"] = tmp_drone_data["flyingState"]
                # Decide the priority
                if "priority" not in tmp_drone_data:
                    if "manned" in tmp_drone_data["descriptors"] or "helicopter" in tmp_drone_data["descriptors"] or "airplane" in tmp_drone_data["descriptors"]:
                        tmp_drone_dict["priority"] = 999
                    # else:
                    #     if tmp_drone_data["descriptors"][0] in ["emulator", "simulator"]:
                    #         tmp_drone_dict["priority"] = 0
                    #     else:
                    #         tmp_drone_dict["priority"] = 10

                tmp_path = {"startTime": None, "wp": None}

                wp = []

                nextPoiIndex =  None # to recognised no nextPoiIndex  case
                # copy also the positions for mcmre
                if "positions" in tmp_drone_data and tmp_drone_data["positions"] is not None:
                    tmp_drone_dict["positions"] = tmp_drone_data["positions"].copy()

                if "path" in tmp_drone_data and tmp_drone_data["path"] is not None \
                        and "poi" in tmp_drone_data["path"]:  # if there is no path its a still drone

                    the_path = tmp_drone_data["path"]

                    

                    if "nextPoiIndex" in the_path and the_path["nextPoiIndex"] is not None:
                            nextPoiIndex = the_path["nextPoiIndex"]  # there is a PoiIndex
                            #if nextPoiIndex == 0:
                            #    tmp_drone_dict["flyingState"] = '102'

                    pois = tmp_drone_data["path"]["poi"]

                    for poi in pois:
                        _poi = {}
                        _poi["altitude"] = poi["altitude"]
                        _poi["latitude"] = poi["latitude"]
                        _poi["longitude"] = poi["longitude"]
                        _poi["speed"] = poi["speed"]
                        _poi["name"] = poi.get("name", "T" + str(pois.index(poi) + 1))
                        if tmp_drone_dict["priority"] == 999:
                            _poi["delay"] = 0
                        else:
                            _poi["delay"] = poi.get("delay", 4)
                        _poi["required"] = poi.get("required", True)
                        wp.append(_poi)

                tmp_path["wp"] = wp.copy()

                if utm_time != "":
                    tmp_path["startTime"] = utm_time
                else:
                    tmp_path["startTime"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

                tmp_path["nextPoiIndex"] =  nextPoiIndex
                tmp_drone_dict["path"] = tmp_path
                # Add the path to the list
                entities.append(tmp_drone_dict)

            for nfz_key, nfz_value in org_data.get("nfzs", {}).items():
                _nfzs[nfz_key] = nfz_value

        parsed_dict = {"airpicture": {"entities": entities, "nfz": _nfzs}}

        return parsed_dict


    def parse_monitor_msg(self, msg):

        try:
            ap = msg['airpicture']
            ent_list = ap['entities']
            for ent in ent_list:
                the_key = ent['name'] + '_' + ent['org_id']
                path = ent['path']
                positions = ent['positions']
                position = Position(positions)
                wp = path['wp']
                flyingState = ent['flyingState']
                start_time_str = path['startTime']
                next_poi = path.get('nextPoiIndex', None)
                name = ent['name']
                t_in_seconds = position.time # this is not correct => self.timestamp_str_to_seconds(start_time_str)
                if next_poi is not None: # we have next poi, use it.
                    if next_poi < 0 or next_poi >= len(wp):  # flight is over, delete and continue
                        self.remove_entity(the_key)
                        wp_current = [{"altitude": position.altitude,
                                   "latitude": position.latitude,
                                   "longitude": position.longitude,
                                   "speed": 5, "name": "current_location",  # speed is not really relevant
                                   "delay": 0, "required": True}]
                        path['wp'] = wp_current
                        if MCPRE_Config.calc_nextPoi:
                            ent["calc_next_poi"] = - 1

                    else:
                        
                        if the_key in self.entities.keys():
                            # update
                            self.entities[the_key].update(wp, t_in_seconds, position, next_poi, flyingState)
                        else:
                            # new key
                            model = ent['model']
                            priority = ent['priority']
                            org_id = ent['org_id']
                            self.add_entity(name, org_id, priority, model, wp, t_in_seconds, \
                                            position, next_poi, flyingState)


                        rd = self.get_remaining_delay(the_key)
                        ent["remaining_delay"] = rd
                        first_delay = rd if rd >=0 else 0

                        wp_current = [{"altitude": position.altitude,
                                       "latitude": position.latitude,
                                       "longitude": position.longitude,
                                       "speed": 5, "name": "current_location",  # speed is not really relevant
                                       "delay": first_delay, "required": True}]
                        wp_current.extend(wp[next_poi:])

                        path['wp'] = wp_current

                        if MCPRE_Config.calc_nextPoi:
                            calc_next_poi = self.entities[the_key].calc_next_poi
                            ent["calc_next_poi"] = calc_next_poi

                else: # next poi is none, we need to calc POI
                    if the_key in self.entities.keys():
                        # update
                        self.entities[the_key].update(wp, t_in_seconds, position, next_poi, flyingState)
                    else:
                        # new key
                        model = ent['model']
                        priority = ent['priority']
                        org_id = ent['org_id']
                        self.add_entity(name, org_id, priority, model, wp, t_in_seconds, position, next_poi, flyingState)

                    if the_key in self.entities.keys():
                        calc_next_poi = self.entities[the_key].calc_next_poi
                    else:
                        calc_next_poi = -1 
                    if calc_next_poi < 0 or calc_next_poi >= len(wp):  # flight is over, remove and continue
                        self.remove_entity(the_key)
                        wp_current = [{"altitude": position.altitude,
                                       "latitude": position.latitude,
                                       "longitude": position.longitude,
                                       "speed": 5, "name": "current_location",  # speed is not really relevant
                                       "delay": 0, "required": True}]
                        path['wp'] = wp_current # no path, except the current location
                        ent["calc_next_poi"] = -1
                    else: # in flight
                        ent["calc_next_poi"] = calc_next_poi
                        rd = self.get_remaining_delay(the_key)
                        ent["remaining_delay"] = rd
                        first_delay = rd if rd >= 0 else 0

                        wp_current = [{"altitude": position.altitude,
                                       "latitude": position.latitude,
                                       "longitude": position.longitude,
                                       "speed": 5, "name": "current_location",  # speed is not really relevant
                                       "delay": first_delay, "required": True}]
                        wp_current.extend(wp[calc_next_poi:])

                        path['wp'] = wp_current

                
        except:
            raise Exception(f"Error while parsing a monitor msg !!\n {traceback.format_exc()}")
            

        return msg


    def start(self, raw_input):
        monitor_entry = self.convert_data_from_rcs_to_mcpre(raw_input)
        return self.parse_monitor_msg(monitor_entry)


if __name__ == "__main__":

    # logging.basicConfig(level = logging.INFO,filename='mcpre.log')
    #mcpre_test_file = "./data/mcpre_test.json"
    mcpre_test_file = "./data/mc_test.json"
    try:

        with open(mcpre_test_file) as f:
            dict = json.load(f)
            entry_list = dict["mcpre_test"]
    except Exception as e:
        raise Exception(f"Error while loading {mcpre_test_file} !!\n {traceback.format_exc()}")
        
    
    container = MCPRE_Container()
    for entry in entry_list:
        monitor_entry = container.convert_data_from_rcs_to_mcpre(entry)
        msg = container.parse_monitor_msg(monitor_entry)
        to_print = msg['airpicture']['entities']
        






