#!/bin/bash

# Construir la imagen Docker (puedes cambiar el tag)
docker build -t monitoreo-bme280 .

# Ejecutar el contenedor, mapeando el puerto 8501 y montando el directorio actual
docker run --rm -it -p 8501:8501 \
  -v "$(pwd):/app" \
  monitoreo-bme280
