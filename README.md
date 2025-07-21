# Proyecto de Monitoreo Ambiental con Raspberry Pi y Sensor BME280

## Descripción General

Sistema modular de monitoreo ambiental desarrollado sobre una Raspberry Pi 2 B+, orientado a condiciones rurales sin acceso a internet. El sistema registra variables ambientales (temperatura, humedad, presión) usando un sensor BME280 conectado por I2C, almacena los datos en SQLite y permite su visualización vía un dashboard local en Streamlit. Todo el sistema puede desplegarse con Docker para facilitar pruebas y portabilidad.

## Características Principales

- Comunicación I2C con sensor BME280.
- Captura automatizada de datos ambientales en intervalos configurables.
- Almacenamiento eficiente mediante SQLite.
- Visualización local vía dashboard en Streamlit.
- Contenerización completa con Docker.
- Scripts documentados y organizados modularmente.


```

## Instalación Manual (sin Docker)

1. Clona el repositorio:

```bash
git clone https://github.com/erneztox/proyecto-monitoreo.git
cd proyecto-monitoreo
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el script de captura:

```bash
python3 src/read_sensor.py
```


## Uso con Docker

```bash
docker-compose up --build
```

## Documentación Técnica

Toda la documentación detallada del sistema (instalación, parámetros configurables, estructura del código, manual de pruebas) está disponible en el archivo:

```
DOCUMENTACION.md
```

## Créditos

Este sistema fue desarrollado como parte de un proyecto académico de ingeniería, orientado a escenarios rurales de monitoreo ambiental en Chile.  
Autor: Ernesto — [github.com/erneztox](https://github.com/erneztox)

