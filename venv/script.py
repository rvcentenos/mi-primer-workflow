import requests

# Realiza una petición HTTP GET a una API de prueba
respuesta = requests.get("https://www.python.org")

# Muestra el código de estado (200 significa éxito)
print(f"Estado de la petición: {respuesta.status_code}")

