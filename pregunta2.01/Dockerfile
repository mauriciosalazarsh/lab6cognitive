FROM python:3.10-slim

# Instalar certificados del sistema y utilidades necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        ffmpeg \
        curl \
        wget && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir yt-dlp==2025.10.14

# Copiar el script
COPY lab06video.py .

# Ejecutar el script automáticamente
CMD ["python", "lab06video.py"]
