# Usamos imagen Python slim para ARM (compatible Raspberry Pi)
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos requirements.txt y luego instalamos dependencias
COPY requirements.txt .

# Instalamos dependencias sin cache para reducir tamaño
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente completo al contenedor
COPY . .

# Puerto expuesto para Streamlit
EXPOSE 8501

# Comando para lanzar Streamlit con la configuración correcta
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
