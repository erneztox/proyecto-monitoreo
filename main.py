import time
import board
import sqlite3
import streamlit as st
from adafruit_bme280 import basic as adafruit_bme280
from datetime import datetime

# Ruta del archivo de base de datos SQLite
DB_PATH = "registros_ambientales.db"

def crear_tabla():
    """
    Crea la tabla 'registros' en la base de datos si no existe.
    La tabla almacena timestamp, temperatura, humedad, presión y altitud.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperatura REAL,
            humedad REAL,
            presion REAL,
            altitud REAL
        )
    """)
    conn.commit()
    conn.close()

def insertar_registro(timestamp, temperatura, humedad, presion, altitud):
    """
    Inserta un nuevo registro de datos ambientales en la base de datos.

    Parámetros:
    - timestamp (str): Fecha y hora de la lectura (formato ISO).
    - temperatura (float): Temperatura en grados Celsius.
    - humedad (float): Humedad relativa en porcentaje.
    - presion (float): Presión atmosférica en hPa.
    - altitud (float): Altitud calculada en metros.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO registros (timestamp, temperatura, humedad, presion, altitud)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, temperatura, humedad, presion, altitud))
    conn.commit()
    conn.close()

def leer_ultimos_registros(limite=100):
    """
    Recupera los últimos registros almacenados en la base de datos,
    limitado por el parámetro 'limite'. Retorna los datos en orden
    cronológico ascendente.

    Parámetros:
    - limite (int): Número máximo de registros a recuperar.

    Retorna:
    - List[Tuple]: Lista de tuplas con los campos del registro.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT timestamp, temperatura, humedad, presion, altitud
        FROM registros
        ORDER BY id DESC LIMIT {limite}
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows[::-1]  # Invierte la lista para mostrar en orden cronológico

def leer_sensor(sensor):
    """
    Lee los valores actuales del sensor BME280.

    Parámetros:
    - sensor: instancia del sensor Adafruit_BME280_I2C.

    Retorna:
    - tuple: timestamp, temperatura, humedad, presion, altitud.
    """
    temp = sensor.temperature
    hum = sensor.relative_humidity
    pres = sensor.pressure
    alt = sensor.altitude
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, temp, hum, pres, alt

def main():
    """
    Función principal que orquesta la ejecución del dashboard Streamlit.
    Se encarga de crear la base de datos, leer datos del sensor periódicamente,
    guardar registros y actualizar la interfaz con datos actuales e históricos.
    """
    st.title("Monitoreo Ambiental - Sensor BME280")

    crear_tabla()

    # Inicializa la interfaz I2C y el sensor BME280
    i2c = board.I2C()
    sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    sensor.sea_level_pressure = 1013.25  # Ajustar según altitud local (hPa)

    placeholder = st.empty()

    # Estado para controlar el intervalo de lectura
    if "last_update" not in st.session_state:
        st.session_state.last_update = time.time()

    # Bucle infinito para lecturas y actualizaciones en tiempo real
    while True:
        # Ejecuta lectura y guardado cada 5 segundos
        if time.time() - st.session_state.last_update > 5:
            try:
                timestamp, temp, hum, pres, alt = leer_sensor(sensor)
                insertar_registro(timestamp, temp, hum, pres, alt)
                st.session_state.last_update = time.time()
            except Exception as e:
                st.error(f"Error al leer o guardar datos: {e}")

        # Obtiene y muestra la última lectura registrada
        datos = leer_ultimos_registros(1)
        if datos:
            ts, t, h, p, a = datos[-1]
            placeholder.metric("Temperatura (°C)", f"{t:.1f}")
            placeholder.metric("Humedad (%)", f"{h:.1f}")
            placeholder.metric("Presión (hPa)", f"{p:.1f}")
            placeholder.metric("Altitud (m)", f"{a:.2f}")

        # Visualiza gráficas históricas de las últimas 50 lecturas
        data = leer_ultimos_registros(50)
        if data:
            import pandas as pd
            df = pd.DataFrame(data, columns=["timestamp", "temperatura", "humedad", "presion", "altitud"])
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df = df.set_index("timestamp")

            st.line_chart(df[["temperatura", "humedad", "presion"]])

        time.sleep(1)

if __name__ == "__main__":
    main()
