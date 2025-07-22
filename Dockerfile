FROM python:3.11-slim

WORKDIR /app

# Instala herramientas necesarias (solo si algún paquete no tiene wheel)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libatlas-base-dev \
    libffi-dev \
    libusb-1.0-0-dev \
    libi2c-dev \
    zlib1g-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalación optimizada de dependencias: usar wheels si existen
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
