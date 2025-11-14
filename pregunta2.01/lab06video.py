import yt_dlp

def download_video(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# URL del video
video_url = "https://iframe.mediadelivery.net/embed/391119/5901245d-96aa-4d08-a29c-caa234660396?autoplay=false&loop=false&muted=false&preload=false&responsive=true"
download_video(video_url)

