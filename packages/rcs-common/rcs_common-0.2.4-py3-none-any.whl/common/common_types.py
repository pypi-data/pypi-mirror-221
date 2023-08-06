import sys
import signal,os
from threading import Lock, Thread, Condition
import time
import requests
import json
import sys
import math
import datetime
import pytz
import numpy as np
import hashlib
from dataclasses import dataclass
from enum import Enum, IntEnum
from argparse import ArgumentParser
#sys.path.append('../')
#import logger.logger2csv as log
from azutils import Geom
from TGtypes import TGPosition, TGSegment, TGTimeTable

# from atc.ATCtypes import PoiItem, Position, ReportedPath, ApprovedPath, ZonePoint, Nfz
# from atc.ATCtypes import FState, FlyingState, FlightRecordState, FlightRecord
# from atc.ATCtypes import ATCSync, ConfigATCT, AtcAlert

class ConfigRCS:

    clean_session = True
    server_ap_port = 4006
    server_fr_port = 4007
    server_dv_port = 4008
    server_cv_port = 4009

    broker_address = "185.241.7.203"
    rcs_logger_level = "INFO"     
    #broker_address = "0.0.0.0"

    broker_port = 1883
    AirPictureMC_QoS = 0
    AirPictureATC_QoS = 0
    AirPictureREC_QoS = 0
    AirPictureMC_Res_QoS = 0
    AirPictureATC_Res_QoS = 0
    AirPictureATC_Alerts_QoS = 0
    HighPriorityMC_Res_QoS = 1
    FlightRequest_QoS = 1
    FlightRequestFinal_QoS = 1
    FlightRequestResponse_QoS = 1
    DividerRequest_QoS = 1
    DividerRequestResponse_QoS = 1
    ConverterRequest_QoS = 1
    ConverterResponse_QoS = 1
    ConverterRequestResponse_QoS = 1

    NFZ_QoS = 1
    Config_QoS = 1

    def __init__(self, init_file_path = None):
        self.clean_session =  ConfigRCS.clean_session
        self.server_ap_port = ConfigRCS.server_ap_port
        self.server_fr_port = ConfigRCS.server_fr_port
        self.server_dv_port = ConfigRCS.server_dv_port
        self.server_cv_port = ConfigRCS.server_cv_port
        self.broker_address = ConfigRCS.broker_address
        self.broker_port    = ConfigRCS.broker_port
        self.docker_flg     = False
        self.rcs_logger_level  = "INFO" 
           
        if init_file_path  is not None:
            self.json_setup(init_file_path)

    def json_setup(self, init_file_path):

        try:

            with open(init_file_path, 'r') as f:
                dict = json.load(f)
                self.docker_flg    = bool(dict.get( 'docker_flg',False))
                self.clean_session = bool(dict.get('clean_session',   self.clean_session))
                self.server_ap_port= dict.get('server_ap_port',  self.server_ap_port)
                self.server_fr_port= dict.get('server_fr_port',  self.server_fr_port)
                self.server_dv_port= dict.get('server_dv_port',  self.server_dv_port)
                self.broker_address= dict.get('broker_address',  self.broker_address)
                self.broker_port   = dict.get('broker_port',     self.broker_port)
                self.rcs_logger_level  = dict.get('rcs_logger_level', self.rcs_logger_level)
                if self.rcs_logger_level not in ["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]:
                   self.rcs_logger_level = "INFO"
                

                print(' RCS Configuration, initialized successfully')

        except Exception as e:
            print ('Warning! error in reading RCS config file, using at least some built-in default values. error is:', str(e))


@dataclass
class Lockers:
    lockAP:Lock   # AirPicture
    lockFP:Lock   # Flight Plan Request
    lockFPR:Lock  # FP Request response
    lockDV: Lock  # Divider Request
    lockDVR: Lock  # Divider response
    lockCV: Lock  # Converter Request
    lockCVR: Lock  # Converter response
    lockNFZ:Lock  # NFZ
    lockConfig:Lock  # Config
    lockATC:Lock  # data from ATC
    lockAlerts:Lock  # Alerts from MC
    lockATCAlerts:Lock  # Alerts from ATC
    lockDTE:Lock  # Data Track and Estimator
    lockREC:Lock  # Recorder
    lockSPB:Lock  # scenario playback
    conditionFPR: Condition
    conditionDVR: Condition
    conditionCVR: Condition

    def __init__(self):
        self.lockAP = Lock() # Air picture
        self.lockFP = Lock() # Flight Plan Request
        self.lockFPR = Lock() # FP Request response
        self.lockDV = Lock() # Flight Plan Request
        self.lockDVR = Lock() # FP Request response
        self.lockCV = Lock() # Flight Plan Request
        self.lockCVR = Lock() # FP
        self.lockNFZ = Lock() # NFZ
        self.lockConfig = Lock() # Config
        self.lockATC    = Lock() # data from ATC
        self.lockAlerts = Lock() # Alerts from MC
        self.lockATCAlerts = Lock() # Alerts from ATC
        self.lockDTE    = Lock() #  Data Track and Estimator
        self.lockREC    = Lock() # Recorder
        self.lockSPB    = Lock() # scenario playback
        self.conditionFPR = Condition()
        self.conditionDVR = Condition()
        self.conditionCVR = Condition()


@dataclass
class Conditions:
    conditionFPR:Condition  # FP Request response

    def __init__(self):
        self.conditionFPR = Lock()


@dataclass
class Flags:
    config:bool
    nfz:bool
    fp:bool
    dv:bool
    cv:bool
    cvr:bool
    atc_stat_data:bool
    atc_alerts:bool
    alert_data:bool
    fpr:bool
    dvr:bool
    high_priority_alert_data:bool

    def __init__(self):
        self.config = self.nfz = self.fp = self.dv = self.dvr = self.atc_stat_data = \
            self.atc_alerts = self.fr_resp = self.alert_data = self.high_priority_alert_data = False

@dataclass
class Topics:
    AirPictureMC       = 'AirPictureMC'
    AirPictureATC      = 'AirPictureATC'
    AirPictureREC      = 'AirPictureREC'
    AirPictureMC_Res   = 'AirPictureMC_Res'
    AirPictureATC_Res  = 'AirPictureATC_Res'
    AirPictureATC_Alerts = 'AirPictureATC_Alerts'
    HighPriorityMC_Res   = 'HighPriorityMC_Res'
    FlightRequest      = 'FlightRequest'
    FlightRequestFinal = 'FlightRequestFinal'
    FlightRequestResponse = 'FlightRequestResponse'
    TrafficInormationRequest     = 'TrafficInormationRequest'
    TrafficInormationResponse   = 'TrafficInormationResponse'
    DividerRequest        = 'DividerRequest'
    DividerResponse       = 'DividerResponse'
    ConverterRequest      = 'ConverterRequest'
    ConverterResponse     = 'ConverterResponse'
    NFZ                   = 'NFZ'
    Config                = 'Config'
    ConfigResponse        = 'ConfigResponse'
    AsList = [AirPictureMC, AirPictureATC, AirPictureREC, AirPictureMC_Res, AirPictureATC_Res, \
              AirPictureATC_Alerts, HighPriorityMC_Res, FlightRequest, FlightRequestFinal, \
              FlightRequestResponse, DividerRequest, DividerResponse,  ConverterRequest, \
              ConverterResponse, NFZ, Config ]

@dataclass
class ModuleName:

    proxy = "Proxy"
    mc    = "MC"
    atc   = "ATC"
    divider = "Divider"
    converter = "Converter"

class TrafficSource(IntEnum):

    _1090ES       = 0
    UAT           = 1
    Multi_Radar   = 2
    MLAT          = 3
    SSR           = 4
    PSR           = 5
    Mode_S        = 6
    MRT           = 7
    SSR_PSR_Fused = 8
    ADS_B         = 9
    FLARM         = 10

class AltSourceType(IntEnum):
    Baro          = 0
    Geo          = 1

class TrafficSourceType(IntEnum):
    TRUE          = 0
    FUSED         = 1

class UtmServerType(IntEnum):
    AP            = 0
    FR            = 1
    DV            = 2
    CV            = 3

class Drone_Identification: #  utm to rcs per drone
    org_id: int #Org identifier
    area_id: int #id of current UTM area.
    drone_name: str # Drone Name – Organization Unique
    drone_id: str # Drone ID –   Drone GUID
    model: str #
    descriptors : str # Drone Model Descriptors – Simulator, Operational, Manned,
    traffic_source: TrafficSource # UAS / radar / Fused / Sensor
    pilot_hash: str # (a reference to Pilots Table)

class Telemetry: # utm to rcs per drone
    measurement_timestamp: str # time of measurement ISO
    uss_timestamp: str # time of uss getting measurement ISO
    position: dict # decimal (dict: lon, lat, alt)
    horz_speed: float #m/s float
    ver_speed:  float #m/s float
    heading: float # – deg.Float
    atitude: dict  # {pan, tilt.Zoom}: degrees.
    estimated_error_position: dict #{ee_lat, ee_lon, ee_alt} dict, float dec.dec
    estimated_error_velocity: dict #(X, Y, Z)  float m/s
    alt_type: AltSourceType #  baro / geo
    source_type: TrafficSourceType #  = true / fused.

# class Flight:

#      reported_path: ReportedPath #path as reported by UAV or USS:
#      reported_time: str #Time(ISO) – time of reporting of the latest path NextPoiIndex – Index
#      approved_path: ApprovedPath #  Latest path approved by UTM
#                                 #Time(ISO) – time when UTM approved the path
#                                 # POI – List of POI items( as reported in API 1.1) If there is no reported path, Time
#                                 # would be 1.1 .1970 and POI = []


#      suggested_path: ApprovedPath#Latest Path approved by MC
#                                  #Time(ISO) – when suggested path received by UTM, if any.
#                                  # If suggested path was accepted, this entry should be reset.
#                                  # POI – List of POI items( as reported in API 1.1)
#                                  # If there is no suggested path, Time would be  1.1 .1970 and POI = []
#      priority: int  # - < 0, 10, 20 etc....>


# class ATCFlightData: # from RCS to UTM per flight

#     flight_state: FState  # ATC processed flight state of the flight as follows:
#                           # class FState(IntEnum):
#                           #   OFF = 1
#                           #   IntoFlight = 2
#                           #   Flight     = 3
#                           #   IntoLanding = 4
#     flight_record_state: FlightRecordState # processing state of the flight record, as follows:
#                           #  class FlightRecordState(IntEnum):
#                           #      Undefined = 0
#                           #      InFlight  = 1
#                           #      Completed = 2
#     the_data: FlightRecord #  current data of the flight record.



# class CollisionItem:
#             collision_number: int
#             collision_time: str #Time(ISO)
#             explected_collision_position: tuple #Expected CollisionPosition
#             expected_minimal_collision_distance: float # (3D - m)
#             identification: str # (nameA + Name B + CollisionTime)
#             suggested_path: ApprovedPath #if exists

# class Alerts:

#     collision_items:[CollisionItem] # Collision_Alerts: A list of collision items


#     alert_list: [AtcAlert] #  ATC Alerts: A list of ATC alerts items
#             #Alert Code(200 - 499)
#             #Alert Time
#             #Alert Parameter(specific per alerts)

# class UTMAirPictureItem:
#     drone_identification: Drone_Identification
#     telemetry: Telemetry
#     flight: Flight

# class MCAirPicture:
#     collision_items: [CollisionItem]  # Collision_Alerts: A list of collision items


# class AirPicture:
#     drone_identification: Drone_Identification
#     telemetry: Telemetry
#     flight: Flight
#     atc_flight_data:ATCFlightData
#     alerts: Alerts
#     # Flight_Plan
#     # ApprovedFlight Plan

class Config:

    origin:tuple
    range:tuple

# class Nfz:
#     '''
#     * Every point represnt [longitude, latitude, altitude] EXACTLY!!!
#     * PAY ATTENTION to the order -  longitude and then latitude!!!
#     * First and last point shuold be identical

#     {
#         type : feature,
#         geomtry: {
#             "type" : Polygon,
#             "coordinates" : [[1, 2, 3], [3, 3, 3], [2, 2, 2], [1, 2, 3]]
#         },
#         property : {

#             id
#             name
#             org_id_list : empty list -> general NFZ, else -> a CTR to the listed org_id's in the list.
#             minimum height
#             masximum height

#         }
#     }

#     '''

#     # if is_ISO_6709 is True then (lon, lat, alt) else -> (lat, lon)
#     def __init__(self, nfz_name="NFZ_0", nfz_id=-1, pois=[], minimum=0, maximum=1000, org_id_list=[],
#                  expiration_date=None, is_ISO_6709=False) -> None:
#         self.nfz_name = nfz_name
#         self.nfz_id = nfz_id
#         self.pois = pois
#         self.buttom_height = minimum
#         self.upper_height = maximum
#         self.ctr_org_id = org_id_list  # default -1 mean a nfz else it is a ctr.
#         self.expiration_date = expiration_date
#         self.is_ISO_6709 = is_ISO_6709

#     # Usage:
#     # geojson.loads(instance_obj)

#     @property
#     def __geo_interface__(self):
#         # the standard order in geoJSON is [lon, lat(, alt)] as ISO 6709
#         # also see geoJSON documentation section 3.1.1 - https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
#         if not self.is_ISO_6709:
#             coords = [(lon, lat, alt) for lat, lon, alt in self.pois]
#         else:
#             coords = [(lat, lon, alt) for lat, lon, alt in self.pois]

#         if self.pois[0] != self.pois[-1]:
#             coords.append(self.pois[0])

#         geometry_pois = Polygon(coordinates=coords)
#         nfz_properties = {
#             "id": self.nfz_name,
#             "name": self.nfz_id,
#             "min_height": self.buttom_height,
#             "max_height": self.upper_height,
#             "ctr_list": self.ctr_org_id,
#             "expiration": self.expiration_date}
#         return Feature(id=self.id, geometry=geometry_pois, properties=nfz_properties)


class Versions:
    def __init__(self):
        self.mc_version_str = ''
        self.atc_version_str = ''
        self.div_version_str = ''
        self.conv_version_str = ''
        self.proxy_str = ''
        self.all_set = False

    def update_mc(self, mc_version_str):
        if type(mc_version_str) == str:
            self.mc_version_str == mc_version_str

    def update_atc(self, atc_version_str):
        if type(atc_version_str) == str:
            self.atc_version_str == atc_version_str

    def update_div(self, div_version_str):
        if type(div_version_str) == str:
            self.div_version_str == div_version_str

    def update_conv(self, conv_version_str):
        if type(conv_version_str) == str:
            self.conv_version_str == conv_version_str

    def update_proxy(self, proxy_version_str):
        if type(proxy_version_str) == str:
            self.proxy_version_str == proxy_version_str

    def calc_hash(self):
        result = ''
        if len(self.mc_version_str) > 0 and len(self.atc_version_str) > 0 and \
                len(self.div_version_str) > 0 and len(self.conv_version_str) > 0 and len(self.proxy_str) > 0:
            self.all_set = True
            The_string = self.proxy_str + self.mc_version_str + self.atc_version_str + self.div_version_str + \
                         self.conv_version_str
            # Assumes the default UTF-8
            hash_object = hashlib.md5(The_string.encode())
            result = hash_object.hexdigest()
        return (result)

class VerStatus:

    def __init__(self):
        pass

    # build status and versions info for Config Response, status only for other types of messages
    # version & ip values, are relevant for Conif Response only, otherwise it should be None
    # in case of an exception, building a status descriptor with an appropriate error.
    def add_status_version(self, msg, description, code, version = None, ip = None):
        valid_msg = False
        return_msg = msg # set some default
        config = False
        header = {}
        body   = {}
        request_id = 0
        try:
            if type(msg) == dict and type(description) == str and type(code) == int:
                if ("header" in msg) and ("body" in msg):
                    header = msg["header"]
                    body   = msg["body"]
                    if "request_id" in header:
                        request_id = header["request_id"]
                    if version is None and ip is None: # not a config msg
                       valid_msg = True
                    elif version is not None and ip is not None and type(version) == str and type(ip) == str:
                        config = True
                        valid_msg = True
            if (valid_msg):
                body["status_description"] = description + '<' + str(request_id) +'>'
                body["status_code"] = code
                if config:
                    body ["version_ip"] = version + '_' + ip

        except:
            valid_msg = False
            body["status_description"] = "Error in generating version or status info.  " + '<' + str(request_id) + '>'
            body["status_code"] = code

        return_msg = { "header": header, "body":body }
        return valid_msg, return_msg


class SharedData:

    flags:Flags
    config:dict
    nfz:dict
    ap:dict
    fp:dict
    dv:dict
    cv:dict
    cvr:dict
    dvr:dict
    alerts:dict
    atc_stat:dict
    fr_resp:dict
    atc_alerts:dict
    high_priority_alerts:dict
    def __init__(self, flags:Flags, config, nfz, ap, fp, alerts, high_priority_alerts,
                 atc_stat, fr_resp, atc_alerts, dv, dvr,cv ,cvr):
        self.flags = flags
        self.config = config
        self.nfz = nfz
        self.ap  = ap
        self.fp  = fp
        self.dv  = dv
        self.dvr = dvr
        self.cv = cv
        self.cvr = cvr
        self.alerts = alerts
        self.high_priority_alerts = high_priority_alerts
        self.atc_stat = atc_stat
        self.fr_resp = fr_resp
        self.atc_alerts = atc_alerts
        self.versions = Versions()
