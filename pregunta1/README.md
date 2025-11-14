# Buscador de Pokémon - Dockerizado

Una aplicación Flask simple para buscar información de Pokémon usando la PokeAPI.

## Requisitos previos

- Docker instalado en tu sistema
- Docker Compose instalado (generalmente viene con Docker Desktop)

## Instrucciones de uso

### Opción 1: Usando Docker Compose (Recomendado)

1. Construir y ejecutar la aplicación:
```bash
docker-compose up --build
```

2. Abrir tu navegador en:
```
http://localhost:5000
```

3. Para detener la aplicación:
```bash
docker-compose down
```

### Opción 2: Usando Docker directamente

1. Construir la imagen:
```bash
docker build -t pokemon-app .
```

2. Ejecutar el contenedor:
```bash
docker run -p 5000:5000 pokemon-app
```

3. Abrir tu navegador en:
```
http://localhost:5000
```

4. Para detener el contenedor:
```bash
docker ps  # Ver el CONTAINER ID
docker stop <CONTAINER_ID>
```

## Características

- Búsqueda de Pokémon por nombre
- Muestra información detallada: ID, tipos, movimientos
- Visualización de sprites (normal y shiny)
- Sin necesidad de instalar dependencias localmente

## Tecnologías

- Python 3.11
- Flask 3.0.0
- PokeAPI
- Docker

## Estructura del proyecto

```
pregunta1/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias de Python
├── templates/
│   └── index.html        # Interfaz de usuario
├── Dockerfile            # Configuración de Docker
├── docker-compose.yml    # Configuración de Docker Compose
├── .dockerignore         # Archivos a ignorar en el build
└── README.md             # Este archivo
```
