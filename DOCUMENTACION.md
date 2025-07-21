# DOCUMENTACIÓN DEL SISTEMA DE MONITOREO AMBIENTAL

Este documento técnico detalla la instalación, estructura, configuración, uso y validación del sistema de monitoreo ambiental desarrollado con Raspberry Pi y sensor BME280, visualizado mediante Streamlit y desplegable vía Docker.

---

## 1. Manual de instalación

### Requisitos del sistema

- Raspberry Pi (modelo 2 B+ o superior)
- Python 3.11+
- Sensor BME280 (I2C)
- Acceso a internet para instalación de dependencias

### Pasos de instalación

```bash
git clone https://github.com/erneztox/proyecto-monitoreo.git
cd proyecto-monitoreo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
bash run.sh
```

---

## 2. Estructura de archivos

```plaintext
.
├── dashboard.py               # Lógica principal: captura, almacenamiento, visualización
├── registros_ambientales.db   # Base de datos SQLite (se genera automáticamente)
├── config.env                 # Parámetros configurables
├── run.sh                     # Script de ejecución automatizada
├── requirements.txt           # Dependencias del sistema
├── Dockerfile                 # Imagen Docker para despliegue contenedor
├── DOCUMENTACION.md           # Documento técnico del sistema
```

---

## 3. Funciones clave

- `crear_tabla()`: Crea la tabla `registros` si no existe.
- `leer_sensor(sensor)`: Lee temperatura, humedad y presión del BME280.
- `insertar_registro(...)`: Guarda nuevos registros en SQLite.
- `leer_ultimos_registros(limite)`: Recupera los últimos valores para graficar.
- `main()`: Ciclo principal con Streamlit y almacenamiento automático.

---

## 4. Parámetros configurables

Definidos en el archivo `config.env`:

```env
SAMPLE_FREQUENCY=60        # Frecuencia de muestreo en segundos
DASHBOARD_PORT=8501        # Puerto para el dashboard de Streamlit
```

Estas variables se exportan automáticamente al ejecutar `run.sh`.

---

## 5. Ejecución y validación

Una vez iniciado el sistema:

- El sensor es detectado automáticamente mediante la interfaz I2C.
- Se visualizan en tiempo real los datos de temperatura, humedad y presión.
- Cada registro es almacenado con timestamp en una base SQLite local.

### Pruebas recomendadas

- Validar la presencia del sensor con `i2cdetect -y 1`
- Desconectar el sensor para testear tolerancia a fallos.
- Verificar persistencia de datos tras reinicio de la Raspberry Pi.
- Confirmar funcionamiento del dashboard accediendo a `http://<IP>:8501`.

---

## 6. Anexos previstos

- 📷 Fotografía del montaje físico del sensor y la Raspberry Pi (ver Figura 5 en el informe).
- 📂 Esquema de cableado del sensor BME280 vía I2C.
- 📄 Manual completo en formato PDF o Markdown.

---

## 7. Licencia y créditos

Este proyecto fue desarrollado como parte de una actividad universitaria. Código, documentación y diseño son de libre acceso para fines educativos.

Repositorio oficial:  
[https://github.com/erneztox/proyecto-monitoreo](https://github.com/ernextoz/proyecto-monitoreo)

