
import sys
import etap.api

print("Python:", sys.executable)
print("Biblioteca:", etap.api.__file__)

baseAddress = "https://localhost:60000"

try:
    e = etap.api.connect(baseAddress)
    response = e.application.ping()

    print("Respuesta de ETAP:", response)
    print("Prueba de conexión completada.")

except Exception as error:
    print("Error de conexión:", repr(error))
