# Laboratorio 06 - API

Laboratorio de Cognitive Computing sobre consumo de APIs y descarga de videos.

## Contenido

- **Pregunta 1**: Aplicación Flask para búsqueda de Pokémon
- **Pregunta 2**: Aplicación Python para descarga de videos de YouTube, Instagram y TikTok

---

## Pregunta 1: Buscador de Pokémon

Aplicación web desarrollada con Flask que permite buscar información de Pokémon usando la PokéAPI.

### Características

- Formulario de búsqueda por nombre de Pokémon
- Muestra los tipos del Pokémon
- Lista de los primeros 10 movimientos
- 4 imágenes: frente normal, frente shiny, espalda normal, espalda shiny
- Interfaz atractiva y responsive

### Instalación y Ejecución

```bash
# Navegar a la carpeta
cd pregunta1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

### Uso

1. Abre tu navegador en `http://127.0.0.1:5000`
2. Ingresa el nombre de un Pokémon (ej: pikachu, charizard, mewtwo)
3. Presiona "Buscar"
4. Verás la información completa del Pokémon

### Ejemplos de Pokémon

- pikachu
- charizard
- mewtwo
- bulbasaur
- eevee
- gengar
- dragonite

---

## Pregunta 2: Descargador de Videos

Aplicación de consola que permite descargar videos desde YouTube, Instagram y TikTok.

### Características

- Descarga de videos desde YouTube
- Descarga de videos desde Instagram
- Descarga de videos desde TikTok
- Detección automática de la plataforma
- Muestra progreso de descarga
- Interfaz de consola interactiva

### Instalación y Ejecución

```bash
# Navegar a la carpeta
cd pregunta2

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

```bash
# Navegar a la carpeta
cd pregunta2.01

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
docker build -t video-downloader . --no-cache

Para Mac o linux:
docker run -v "$(pwd)":/app video-downloader


Para Windows:
docker run -v "%cd%":/app video-downloader
```

### Uso

1. Ejecuta el programa
2. Selecciona la opción 1 para descargar un video
3. Ingresa la URL completa del video
4. El video se descargará en la carpeta `downloads/`

### Plataformas Soportadas

- **YouTube**: Videos individuales y shorts
  - Ejemplo: `https://www.youtube.com/watch?v=VIDEO_ID`

- **Instagram**: Reels, posts con video, IGTV
  - Ejemplo: `https://www.instagram.com/reel/ID/`

- **TikTok**: Videos de TikTok
  - Ejemplo: `https://www.tiktok.com/@usuario/video/ID`

### Notas Importantes

- Los videos se guardan en la carpeta `downloads/` que se crea automáticamente
- La calidad del video descargado es la mejor disponible
- Algunos videos pueden tener restricciones de descarga según la plataforma

---

## Estructura del Proyecto

```
lab06/
├── README.md
├── pregunta1/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── pregunta2/
    ├── video_downloader.py
    └── requirements.txt
```

---

## Requisitos Generales

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a Internet

---

## Dependencias

### Pregunta 1
- Flask 3.0.0
- requests 2.31.0

### Pregunta 2
- yt-dlp 2024.10.7

---

## Troubleshooting

### Pregunta 1
- Si obtienes error de conexión, verifica tu conexión a Internet
- Si un Pokémon no se encuentra, verifica que el nombre esté en minúsculas y sin acentos

### Pregunta 2
- Si la descarga falla, verifica que la URL sea correcta y pública
- Algunos videos privados o con restricciones no se pueden descargar
- Si yt-dlp falla, intenta actualizar: `pip install --upgrade yt-dlp`

---

## Autor

Laboratorio realizado para el curso de Cognitive Computing - UTEC

## Licencia

Este proyecto es para fines educativos.
