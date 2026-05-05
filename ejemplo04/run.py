import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas004"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc,
        auth=("Lady", "1234"),
    )
    print(f"Insertando {doc['nombre']} | {response.status_code}")
# En el ejemplo 3 se envia todos los documentos en un solo request y en este ejemplo se envia cada documento por separado, tambien para que me cargue tuve que agregar mis credenciales en el archivo local.ini de couchdb, ya que en el ejemplo 3 no se requiere autenticacion y en este ejemplo si.