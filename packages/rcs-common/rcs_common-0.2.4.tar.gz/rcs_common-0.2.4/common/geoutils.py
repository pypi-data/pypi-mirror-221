import math


class AzGeoUtils:
    @staticmethod
    def haversine(coord1, coord2):
        R = 6372800  # Earth radius in meters
        lat1 = coord1[0]
        lon1 = coord1[1]
        lat2 = coord2[0]
        lon2 = coord2[1]

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + \
            math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    @staticmethod
    def bearing(coord1, coord2):
        lat1 = coord1[0]
        lon1 = coord1[1]
        lat2 = coord2[0]
        lon2 = coord2[1]

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dlambda = math.radians(lon2 - lon1)
        y = math.sin(dlambda) * math.cos(phi2)
        x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlambda)
        tet = math.atan2(y, x)
        return (math.degrees(tet) + 360) % 360

    @staticmethod
    def point(origin, coord2):
        distance = AzGeoUtils.haversine(origin, coord2)
        bearing = math.radians(AzGeoUtils.bearing(origin, coord2))
        if len(coord2) == 3:
            return (distance * math.cos(bearing), distance * math.sin(bearing), coord2[2])
        return (distance * math.cos(bearing), distance * math.sin(bearing))

    @staticmethod
    def vector(origin, coord):
        distance = AzGeoUtils.haversine(origin, coord)
        bearing = AzGeoUtils.bearing(origin, coord)
        return (distance, bearing)

    @staticmethod
    def destination(coord1, vector):
        R = 6372800  # Earth radius in meters
        distance, bearing = vector
        tet = math.radians(bearing)
        ang = distance / R
        lat1, lon1 = coord1
        phi1, lam1 = math.radians(lat1), math.radians(lon1)
        phi2 = math.asin(math.sin(phi1) * math.cos(ang) + math.cos(phi1) * math.sin(ang) * math.cos(tet))
        lam2 = lam1 + math.atan2(math.sin(tet) * math.sin(ang) * math.cos(phi1),
                                 math.cos(ang) - math.sin(phi1) * math.sin(phi2))
        return (math.degrees(phi2), math.degrees(lam2))

    @staticmethod
    def geopoint(origin, point):
        bearing = math.atan2(point[1], point[0])
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        res = AzGeoUtils.destination(origin, (distance, math.degrees(bearing)))
        if len(point) == 3:
            res = res + (point[2],)
        return res

#
# def test():
#     s = (32.137504, 34.840042)
#     t = (32.135341, 34.833685)
#     v = AzGeoUtils.vector(s, t)
#     dest = AzGeoUtils.destination(s, v)
#     print ("Distance, Bearing = {v}".format( v=v))
#     print ("Destination: = {dest}".format(dest = dest))
#
# def test2():
#     o = (32.137504, 34.840042)
#     t = (32.135341, 34.833685)
#     p = AzGeoUtils.point(o, t)
#     # 2D
#     gp = AzGeoUtils.geopoint(o, p)
#     print("Geo before = {gb}, After = {ga}".format(gb = t, ga = gp))
#
#     # 3D
#     t = t + (10,)
#     p = AzGeoUtils.point(o, t)
#     gp = AzGeoUtils.geopoint(o, p)
#     print("Geo before = {gb}, After = {ga}".format(gb = t, ga = gp))
#
# test()
# test2()
