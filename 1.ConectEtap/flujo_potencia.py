#Ejemplo de ejecución de flujo de potencia en ETAP mediante API
import etap.api
import json
import sqlite3
import os

# 1. Conectar con ETAP
baseAddress = "https://localhost:60000"
e = etap.api.connect(baseAddress)

# 2. Ejecutar el flujo de potencia
print("Ejecutando flujo de potencia...")

# -- DATOS DE SISTEMA 04-BARRAS DE IEEE--
response = e.studies.runLF(
    revisionName="Base",
    configName="Normal",
    studyCase="LF",
    presentation="OLV1",
    outputReport="FlujoPrueba",
    getOnlineData=False,
    onlineConfigOnly=False,
    timeoutSecs=30
)

# 3. Obtener la ruta del reporte generado
resultado = json.loads(response)
ruta_reporte = resultado["ReportPath"]

# 4. Consultar los resultados eléctricos
conexion = sqlite3.connect(
    f"file:{ruta_reporte.replace(chr(92), '/')}?mode=ro",
    uri=True
)

try:
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT
            IDFrom AS Barra,
            TYPE AS Tipo,
            kV AS Tension_nominal_kV,
            VoltMag AS Tension_porcentaje,
            VoltAng AS Angulo_grados
        FROM LFR
        WHERE TYPE IN ('Swng', 'Load')
        ORDER BY CAST(IDFrom AS INTEGER);
    """)

    print("\nRESULTADOS DEL FLUJO DE POTENCIA")
    print("-" * 64)
    print(
        f"{'Barra':<10}{'Tipo':<12}"
        f"{'kV nominal':>14}{'Tensión (%)':>14}{'Ángulo (°)':>14}"
    )
    print("-" * 64)

    for barra, tipo, kv, volt, angulo in cursor.fetchall():
        print(
            f"{barra:<10}{tipo:<12}"
            f"{kv:>14.3f}{volt:>14.3f}{angulo:>14.3f}"
        )

finally:
    conexion.close()
