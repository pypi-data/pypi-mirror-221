from pathlib import Path
import os.path
from common.azutils import Geom, TimeStampAsFloatInSec
import math
import traceback

class CommonConfig:
    CalcNextPoi = True # calculate next Poi, regardless its existance


class MCPUtil:

    dist1 = 100.0 # accepted distance of current location from path (m)
    dist2 =  5.0 # accepted distance between planned POI (m)
    dist3 = 30.0 # accepted distance if time for the segment exceeded
    dtime =  1.5 # accepted delay difference at poi
    dspeed=  0.2 # accepted changes in speed.

    @staticmethod
    def is_same_path(wp1, wp2):
        err_msg = []
        try:

            if wp1 is None and wp2 is None: # we had not and still don't have an alternative path.
                return True, err_msg
            if wp1 is None or wp2 is None:  # only one is none, we should not filter.
                return False, err_msg
            if type(wp1) != list:
                err_msg.append("Error,Illegal type for wp1, not a list!")
                return False, err_msg
            if type(wp2) != list:
                err_msg.append("Error,Illegal type for wp2, not a list!")
                return False,  err_msg

            if len(wp2) > len(wp1): # wp2 has surely  changed.
                return False,  err_msg
            # convert to tupple-meters (x,y,z)
            # find on what segment, the current location is, on wpm1.
            # if it is close enough to the segment, we can compare from this point onward.
            pt = wp1[0]
            origin = (pt["longitude"], pt["latitude"], pt["altitude"])
            wpm1 = Geom.convert_list_geo_2tuplem_origin(wp1, origin)
            wpm2 = Geom.convert_list_geo_2tuplem_origin(wp2, origin)
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
                    ent1m_as_list = Geom.convert_list_geo_2tuplem_origin([ent1], origin)
                    ent2m_as_list = Geom.convert_list_geo_2tuplem_origin([ent2], origin)
                    poi_distance  = Geom.distance(ent1m_as_list[0],ent2m_as_list[0])
                    if poi_distance >    MCPUtil.dist2:
                        poi_diff = True
                        break

                if poi_diff:
                    return False,  err_msg
                else:
                    return True,  err_msg

            else:
                return False, err_msg

        except:
            err_msg.append(f"Error while processing an alert msg !!\n {traceback.format_exc()}")
            raise Exception(f"Error while processing an alert msg !!\n {traceback.format_exc()}")
            return False, err_msg
    #calculate the next poi:
    # Input:
    #    wp1, wp2 - current and previous waypoint list
    #    pos_tuple - current drone position, given as a tuple (lon, lat, alt)
    #    previous_poi -next poi as calculated in previous cycle.
    #    last_poi_time - calculated time where we think drone had advanced to the current poi
    #    flying_state - flying state of the drone as reported.
    # Output:
    #    result - the calculated next poi. -999 -> calculation failed. 0 -> Drone has still not started the path.
    #    start_poi_time - the calculated point in time, where the current poi started
    # Algorithm:
    #    if len of wp2 is 0 or 1, or not in a flying state,  next poi is  -1
    #    if flying state is that of a take off, result is zero
    #    otherwise:
    #       if the new path is different from the old path, start from
    #       the first point, ignoring previous poi
    #       if wp1 == wp2, next poi can only increase, start from previous_poi
    #       find the closest segment,or close enough segment to drone position.
    #       if the distance is acceptable:
    #          if we are still on the same path, but calculated time, shows we should move to the next - do it.
    #       if we moved to the next poi, update the returned start_poi_time.
    @staticmethod
    def calc_next_poi(wp1, wp2, pos_tuple, previous_poi, last_poi_time, flying_state):
        result = -999
        start_poi_time = last_poi_time
        time_now = TimeStampAsFloatInSec()
        err_list = []
        try:
            if wp1 is None:
                if flying_state == 102:
                    
                    result = 0
                elif flying_state in [103,108]:
                
                    result = 0
                    start_poi_time = time_now
                else:
                    result = -1

            elif len(wp2) <=1 or flying_state not in [102,103,108]: # not flying
                result = -1
            elif flying_state == 102: # taking off, drone is in its way to the first wp
                result = 0
            else:
                initial_poi = max(previous_poi, 0)
                same_path, err_list = MCPUtil.is_same_path(wp1, wp2)
                if not same_path: # path has changed, we should start checking with next_poi = 1
                    initial_poi = 0
                    start_poi_time = time_now
                pt = wp2[0]
                origin = (pt["longitude"], pt["latitude"], pt["altitude"])
                wpm2 = Geom.convert_list_geo_2tuplem_origin(wp2, origin)
                dp = Geom.sub(pos_tuple,origin)
                dpm = Geom.geotuple2tuple(dp, pos_tuple[1])
                if initial_poi == 0:
                    d0 = Geom.distance((0,0,0), dpm)
                    if d0 <= MCPUtil.dist2:
                        result =  1
                        start_poi_time = time_now
                    else:
                        result =  0 
                else : # initial_poi >= 1 
                    min_dist = 999.0
                    result = initial_poi 
                    
                    if initial_poi + 1  < len(wpm2):
                        dist1, nearest1 = Geom.pnt2line(dpm, wpm2[initial_poi-1], wpm2[initial_poi])
                        dist2, nearest2 = Geom.pnt2line(dpm, wpm2[initial_poi], wpm2[initial_poi+1])
                        min_dist = min(dist1, dist2) 
                        if min_dist <= MCPUtil.dist3:
                            result = initial_poi
                            if dist2 < dist1 + 1.0 and math.fabs(time_now - start_poi_time) >= 4.0: # if both dist are equal, we are on a wp, so move to the next poi anyway, 
                                                                                        # but we must stay on a segment at least 4.0 second.   
                                result += 1
                
                            else:
                                pass
                            
                            if result > initial_poi: #we moved for any reason to the next poi, update start time
                                start_poi_time = time_now

                        else:
                            msg = "calc_poi: drone seems not to follow its path, calc poi failed!"
                            err_list.append(msg)
                            result = previous_poi
           
        except:
            err_list.append(f"Error while processing an alert msg !!\n {traceback.format_exc()}")
            raise Exception(f"Error while processing an alert msg !!\n {traceback.format_exc()}")
            #return previous_poi, start_poi_time, err_list
        return result,  start_poi_time, err_list

class CommonFiles:
    RCSConfigFileName = ""

    @staticmethod
    def config_file_name():
        import pathlib
        main_dir  = Path(__file__).parents[0]
        sub_dir = 'install'
        fname = 'rcs_config.json'
        CommonFiles.RCSConfigFileName = Path(main_dir, sub_dir, fname)
        if not CommonFiles.RCSConfigFileName.exists():
            raise Exception("Fatal Error! configuration file path is not defined! ")

        return CommonFiles.RCSConfigFileName

if __name__ == "__main__":
    os.environ['RCS_CONFIG_PATH'] = '~/dev/common/install/'
    file_name = CommonFiles.config_file_name()
