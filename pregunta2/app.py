from flask import Flask, render_template, request, jsonify, send_file
import os
import yt_dlp
from urllib.parse import urlparse
import time
import threading

app = Flask(__name__)

DOWNLOAD_FOLDER = os.path.join(app.root_path, 'static', 'downloads')
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

download_progress = {}


def detect_platform(url):
    domain = urlparse(url).netloc.lower()

    if 'youtube.com' in domain or 'youtu.be' in domain:
        return 'YouTube'
    elif 'instagram.com' in domain:
        return 'Instagram'
    elif 'tiktok.com' in domain:
        return 'TikTok'
    else:
        return 'Desconocido'


class ProgressHook:
    def __init__(self, download_id):
        self.download_id = download_id

    def __call__(self, d):
        if d['status'] == 'downloading':
            try:
                percent_str = d.get('_percent_str', '0%').strip()
                speed_str = d.get('_speed_str', 'N/A').strip()
                eta_str = d.get('_eta_str', 'N/A').strip()

                download_progress[self.download_id] = {
                    'status': 'downloading',
                    'percent': percent_str,
                    'speed': speed_str,
                    'eta': eta_str
                }
            except:
                pass
        elif d['status'] == 'finished':
            download_progress[self.download_id] = {
                'status': 'processing',
                'percent': '100%',
                'speed': 'N/A',
                'eta': '0s'
            }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get('url', '').strip()

        if not url:
            return jsonify({'success': False, 'error': 'URL no proporcionada'}), 400

        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                return jsonify({'success': False, 'error': 'URL no válida'}), 400
        except:
            return jsonify({'success': False, 'error': 'URL no válida'}), 400

        platform = detect_platform(url)
        download_id = str(int(time.time() * 1000))

        download_progress[download_id] = {
            'status': 'starting',
            'percent': '0%',
            'speed': 'N/A',
            'eta': 'N/A'
        }

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'progress_hooks': [ProgressHook(download_id)],
            'quiet': True,
            'no_warnings': True,
        }

        if platform == 'YouTube':
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

        def download_thread():
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    basename = os.path.basename(filename)

                    download_progress[download_id] = {
                        'status': 'completed',
                        'percent': '100%',
                        'filename': basename,
                        'title': info.get('title', 'Video descargado'),
                        'platform': platform
                    }
            except Exception as e:
                download_progress[download_id] = {
                    'status': 'error',
                    'error': str(e)
                }

        thread = threading.Thread(target=download_thread)
        thread.daemon = True
        thread.start()

        return jsonify({
            'success': True,
            'download_id': download_id,
            'platform': platform
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/progress/<download_id>')
def get_progress(download_id):
    progress = download_progress.get(download_id, {'status': 'unknown'})
    return jsonify(progress)


@app.route('/download_file/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404


@app.route('/cleanup')
def cleanup_downloads():
    try:
        current_time = time.time()
        for filename in os.listdir(DOWNLOAD_FOLDER):
            file_path = os.path.join(DOWNLOAD_FOLDER, filename)
            if os.path.isfile(file_path):
                file_age = current_time - os.path.getmtime(file_path)
                if file_age > 3600:
                    os.remove(file_path)
        return jsonify({'success': True, 'message': 'Limpieza completada'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
