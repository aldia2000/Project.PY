import math

# On défini une fonction pour calculer la distance entre deux points géographiques
def distance(lat1, lon1, lat2, lon2):
    # Rayon moyen de la Terre en kilomètres
    R = 6371.0
    
    # On converti des coordonnées degrés en radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Différence des longitudes et latitudes
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Formule de la distance haversine
    #Cette formule permet de calculer la distance entre deux points sur la surface de la Terre en prenant en compte la courbure de la Terre
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

# Fonction pour obtenir les coordonnées et le nom d'un point
def get_point_info():
    name = input("Entrez le nom du point : ")
    lat = float(input("Latitude du point {} : ".format(name)))
    lon = float(input("Longitude du point {} : ".format(name)))
    return name, lat, lon

# Demander les informations pour le premier point
print("Point 1 :")
point1_name, lat1, lon1 = get_point_info()

# Demander les informations pour le deuxième point
print("Point 2 :")
point2_name, lat2, lon2 = get_point_info()

# Calcul de la distance entre les deux points
dist = distance(lat1, lon1, lat2, lon2)

# Afficher le résultat
print("La distance entre les points {} et {} est : {} kilomètres.".format(point1_name, point2_name, dist))
