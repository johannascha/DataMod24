
### ÜBUNG 3: Shapefile-Header, Byte für Byte (Johanna Scharlau) ###
### AUFGABE 01: Shape File Header ###
# Funktion erstellen die eine .shp als Argument einließt und den header gelayouted ausgibt
            # Layoutvorgabe: 
            # Header of ...shp 
            # Filecode         =
            # File Lenght       =
            # Version           =
            # Shape Type        =
            # BBox              =
            # Zmin, Zmax        =
            # Mmin, Mmax        = 

from struct import unpack

def shapefile_header(path: str):
    print("Header of ", path)                                   # pring Überschrift
    with open(path, 'rb') as f:                                 #'rb': read binary
        filecode = f.read(4)
        filecode_int = unpack('>i', filecode)[0]
        print("Filecode: \t=",  filecode_int)                  #filecode augeben
        
        f.seek(24)
        file_lenght = f.read(4)
        file_lenght_int = unpack('>i', file_lenght)[0]
        print("File Lenght: \t=",  file_lenght_int)             #file_lenght ausgben

        version = f.read(4)
        version_int = unpack("<i", version)[0]
        print("Version: \t=",  version_int)                 #version ausgeben

        shape_type = f.read(4)
        shape_type_int = unpack("<i", shape_type)[0]
        print("Shape Type: \t=",  shape_type_int)               #shape type ausgeben

        x_min = f.read(8)
        x_min_int = unpack("<q", x_min)[0]
        y_min = f.read(8)
        y_min_int = unpack("<q", y_min)[0]
        x_max = f.read(8)
        x_max_int = unpack("<q", x_max)[0]
        y_max = f.read(8)
        y_max_int = unpack("<q", y_max)[0]
        print("BBox:  \t \t=", "[", x_min_int,",", x_max_int,",", y_min_int,",", y_max_int, "]")

        z_min = f.read(8)
        z_min_int = unpack("<q", z_min)[0]
        z_max = f.read(8)
        z_max_int = unpack("<q", z_max)[0]
        m_min = f.read(8)
        m_min_int = unpack("<q", m_min)[0]
        m_max = f.read(8)
        m_max_int = unpack("<q", m_max)[0]
        print("Zmin, Zmax: \t=", "(", z_min_int, ",", z_max_int, ")")
        print("Mmin, Mmax \t=", "(", m_min_int, ",", m_max_int, ")")

#calling my funtion 
shapefile_header(r"C:\Daten_Johanna\HCU\4_SO24_hcu\DataMod\UE3\data\ne_10m_populated_places.shp")



### AUFGABE 02: las Header ###
def las_header(path: str):
    print("Header of ", path)
    with open(path, 'rb') as f:
        f.seek(14)
        version_major = f.read(1)
        version_major_int = unpack("<b", version_major)[0]
        version_minor = f.read(1)
        version_minor_int = unpack("<b", version_minor)[0]
        f.seek(79)
        creation_date = f.read(2)
        creation_date_int = unpack("<H", creation_date)[0]
        print("Version: \t \t=",  version_minor_int,".",version_minor_int)
        print("Datum der Erzeugung: \t=",  creation_date_int)                       #hier weiß ich nicht wie ich das Datum im Format DD.MM.YYYY ausgebe

#calling my funtion 
las_header(r"C:\Daten_Johanna\HCU\UPV\modelos_cartograficos_ambientales\PR_2\2009\dunes09_so_g4.las")






