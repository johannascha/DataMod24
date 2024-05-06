# Übung2: Objektorientierte Programmierung in Python, Johanna Scharlau
# Aufgabe 01: Implementieren der Klasse „Point“

from math import sqrt

class Point:                                    #Klasse Point inplementieren 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def euclitic_distance(self, other):         #hier implementiere ich ein other im argument
        return sqrt ((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def area(self):
        return 0

p1 = Point(1, 2)                                #hier definiere ich die Punkte
p2 = Point(4, 6)
p3 = Point(3, 3)
p4 = Point(5, 7)

# print(p1.euclitic_distance(p2))
# print(p1.euclitic_distance(p3))
# print(p1.euclitic_distance(p4))

# print(p1.area())
# print(p2.area())
# print(p3.area())
# print(p4.area())


# Aufgabe 02: Implementieren der Unterklasse „Geographic Point“

from math import sin, cos, atan2
class GeographicPoint(Point):
    def __init__(self, x, y, lat, lon):
        super().__init__(x, y)                     #hier definiere ich die Klasse Point
        self.lat = lat
        self.lon = lon

    def distance_Kugeloberffläche(self, other):
        dLat = self.lat - other.lat
        dLon = self.lon - other.lon

        a = sin(dLat/2)**2 + cos(self.lat) * cos(other.lat) * sin(dLon/2)**2 
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = 6371 * c
        
        return d


gpWien = GeographicPoint(1, 2, 16.4, 48.2)
gpTokio = GeographicPoint(4, 6, 139.7, 35.7)
gpNewYork = GeographicPoint(3, 3, 74.0, 40.4)

print(gpWien.distance_Kugeloberffläche(gpTokio))
print(gpWien.distance_Kugeloberffläche(gpNewYork))

# Zugehörigkeit überprüfen 
print(GeographicPoint.mro())


