# Video Downloader - Aplicación Flask

Aplicación Flask para descargar videos de YouTube, Instagram y TikTok.

## Requisitos

- Docker
- Docker Compose

## Instalación y Ejecución

### Con Docker (Recomendado)

1. Construir y ejecutar el contenedor:
```bash
docker-compose up --build
```

2. Acceder a la aplicación en: `http://localhost:5001`

3. Para detener la aplicación:
```bash
docker-compose down
```

### Sin Docker

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:
```bash
python app.py
```

## Características

- Descarga de videos desde múltiples plataformas (YouTube, Instagram, TikTok)
- Seguimiento del progreso de descarga en tiempo real
- Limpieza automática de archivos antiguos
- Interfaz web sencilla

## Uso

1. Ingresa la URL del video que deseas descargar
2. Haz clic en "Descargar"
3. Espera a que se complete la descarga
4. Descarga el archivo a tu computadora

## Notas

- Los archivos descargados se almacenan en `static/downloads/`
- Los archivos con más de 1 hora de antigüedad se eliminan automáticamente mediante el endpoint `/cleanup`
