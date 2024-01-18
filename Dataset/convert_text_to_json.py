import json

# Définir le nom du fichier d'entrée et de sortie
input_filename = './Datset_football.txt'
output_filename = 'Dataset_football.json'

# Ouvrir le fichier d'entrée en mode lecture
with open(input_filename, 'r') as file:
    lines = file.readlines()

# Initialiser des listes pour stocker les données des vertices et des arcs
vertices = []
arcs = []

# Parcourir les lignes du fichier
for line in lines:
    if line.startswith('*Vertices'):
        is_vertices = True
        continue
    elif line.startswith('*Arcs'):
        is_vertices = False
        continue

    # Séparer les éléments de la ligne
    elements = line.split()
    
    if is_vertices and len(elements) >= 4:
        vertex_data = {
            'id': int(elements[0]),
            'label': elements[1].strip('"'),
            'x': float(elements[2]),
            'y': float(elements[3]),
            'radius': float(elements[4])
        }
        vertices.append(vertex_data)
    elif not is_vertices and len(elements) == 3:
        arc_data = {
            'source': int(elements[0]),
            'target': int(elements[1]),
            'weight': int(elements[2])
        }
        arcs.append(arc_data)

# Créer un dictionnaire JSON contenant les données
data = {'vertices': vertices, 'arcs': arcs}

# Écrire les données au format JSON dans un fichier de sortie
with open(output_filename, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Conversion terminée. Les données ont été enregistrées dans {output_filename}")
