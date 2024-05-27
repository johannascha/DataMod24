import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

df = gpd.read_file("ne_10m_admin_0_countries.shp")
output = "output"

while True:
    coi = input("Von welchem Land möchtest du seine Nachbarn und Eigenarten kennenleren? \n(Bitte Deutschen Landesnamen angeben)")   # coi: country of interest 
    if not df['NAME_DE'].isin([coi]).any():
        print("Das Land ist nicht in dem Datensatz enthalten. \nBitte versuche es erneut und verwende den Deutschen Landesnamen.")
    else:
        selected_country = df[df['NAME_DE'] == coi]
        df['POP_EST'] = df['POP_EST'].fillna(0)

        #Anzahl der Nachbarländer bestimmen
        neighbors = df[df.touches(selected_country.geometry.iloc[0])]
        num_neighbors = len(neighbors)

        #Namen der Nachbarländer
        neighbors_names_DE = list(neighbors["NAME_DE"])

        #Gesamtfläche der Nachbarländer der Nachbarländer exklusiv des eingegebenen Landes (in km²) 
        neighbors_area = neighbors.geometry.area
        total_neighbors_area = neighbors_area.sum()
        selected_country_area = selected_country.geometry.area.values[0]
        neighbors_neighbors_area = total_neighbors_area - selected_country_area

        #Gesamtbevölkerung der Nachbarländer der Nachbarländer exklusiv des eingegebenen Landes
        neighbors_neighbors = df[df.geometry.touches(neighbors.unary_union)]
        total_population = neighbors_neighbors['POP_EST'].sum()

        #Bevölkerungsdichte der Gesamtfläche (Population / km²) ohne COI
        population_density = total_population / neighbors_neighbors_area

        print("Landesinfo für" , coi)
        print("Anzahl der Nachbarländer der Nachbarländer: \t\t\t\t\t \t \t", num_neighbors)
        print("Namen der Nachbarländer der Nachbarländer (deutschsprachig): \t\t\t\t\t", neighbors_names_DE)
        print("Gesamtfläche der Nachbarländer der Nachbarländer exklusive des eingegebenen Landes (in km²):\t", neighbors_neighbors_area)
        print("Gesamtbevölkerung der Nachbarländer der Nachbarländer exklusive des eingegebenen Landes:\t", int(total_population))
        print("Bevölkerungsdichte der Gesamtfläche exklusive des eigegebenen Landes (Population / km²)\t\t", population_density) 
        break

#Visualisierung
#neues Geopackage erstellen und speichern
gdf_selected = gpd.GeoDataFrame(pd.concat([selected_country, neighbors], ignore_index=True), crs = df.crs)

if not os.path.exists(output):
    os.makedirs(output)

selected_country_name = selected_country['NAME_DE'].values[0]
output = os.path.join(output, f'{selected_country_name}_neigbors.gpkg')
gdf_selected.to_file(output, layer=f'{selected_country_name}_neigbors', driver='GPKG')

#Karte erstellen
gdf = gpd.read_file(output)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
fig, ax = plt.subplots()
world.plot(ax=ax, edgecolor='gray', facecolor='lightgray')
gdf.plot(ax=ax, color='red')
plt.show()


