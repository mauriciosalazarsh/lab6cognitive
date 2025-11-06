import os
import sys
from urllib.parse import urlparse

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp no está instalado.")
    print("Por favor instala las dependencias con: pip install -r requirements.txt")
    sys.exit(1)


class VideoDownloader:
    def __init__(self, output_folder='downloads'):
        self.output_folder = output_folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def detect_platform(self, url):
        """Detecta la plataforma del video basándose en la URL"""
        domain = urlparse(url).netloc.lower()

        if 'youtube.com' in domain or 'youtu.be' in domain:
            return 'YouTube'
        elif 'instagram.com' in domain:
            return 'Instagram'
        elif 'tiktok.com' in domain:
            return 'TikTok'
        else:
            return 'Desconocido'

    def download_video(self, url):
        """Descarga el video desde la URL proporcionada"""
        platform = self.detect_platform(url)

        print(f"\n{'='*60}")
        print(f"Plataforma detectada: {platform}")
        print(f"URL: {url}")
        print(f"{'='*60}\n")

        if platform == 'Desconocido':
            print("Advertencia: No se pudo detectar la plataforma.")
            print("Intentando descargar de todas formas...\n")

        # Configuración de yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(self.output_folder, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'quiet': False,
            'no_warnings': False,
        }

        # Configuraciones específicas por plataforma
        if platform == 'YouTube':
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

        elif platform == 'Instagram':
            ydl_opts['format'] = 'best'

        elif platform == 'TikTok':
            ydl_opts['format'] = 'best'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("Obteniendo información del video...")
                info = ydl.extract_info(url, download=False)
                print(f"\nTítulo: {info.get('title', 'Sin título')}")
                print(f"Duración: {info.get('duration', 0) // 60} minutos {info.get('duration', 0) % 60} segundos")

                print("\nIniciando descarga...")
                ydl.download([url])

                print(f"\n{'='*60}")
                print(f"Descarga completada exitosamente!")
                print(f"Archivo guardado en: {self.output_folder}/")
                print(f"{'='*60}\n")
                return True

        except Exception as e:
            print(f"\n{'='*60}")
            print(f"Error al descargar el video: {str(e)}")
            print(f"{'='*60}\n")
            return False

    def progress_hook(self, d):
        """Hook para mostrar el progreso de descarga"""
        if d['status'] == 'downloading':
            try:
                percent = d.get('_percent_str', 'N/A')
                speed = d.get('_speed_str', 'N/A')
                eta = d.get('_eta_str', 'N/A')
                print(f"\rDescargando: {percent} | Velocidad: {speed} | ETA: {eta}", end='')
            except:
                pass
        elif d['status'] == 'finished':
            print(f"\n\nDescarga finalizada. Procesando archivo...")


def main():
    print("="*60)
    print(" "*15 + "DESCARGADOR DE VIDEOS")
    print(" "*10 + "YouTube | Instagram | TikTok")
    print("="*60)

    downloader = VideoDownloader()

    while True:
        print("\nOpciones:")
        print("1. Descargar video")
        print("2. Salir")

        choice = input("\nSelecciona una opción (1-2): ").strip()

        if choice == '1':
            url = input("\nIngresa la URL del video: ").strip()

            if not url:
                print("Error: Debes ingresar una URL válida.")
                continue

            # Validar que la URL sea válida
            try:
                result = urlparse(url)
                if not all([result.scheme, result.netloc]):
                    print("Error: La URL no es válida.")
                    continue
            except:
                print("Error: La URL no es válida.")
                continue

            downloader.download_video(url)

        elif choice == '2':
            print("\nGracias por usar el descargador de videos!")
            break

        else:
            print("Opción no válida. Por favor selecciona 1 o 2.")


if __name__ == '__main__':
    main()
