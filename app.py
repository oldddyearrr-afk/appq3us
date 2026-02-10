import requests
from flask import Flask, Response, stream_with_context

app = Flask(__name__)

# ضع الرابط الذي تريد تشغيله هنا
STREAM_URL = "http://line.dream-4k.cc:80/live/9142DC/107CC6/1440477.ts"

@app.route('/stream')
def stream():
    def generate():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'http://line.dream-4k.cc/'
        }
        # فتح اتصال مستمر مع السيرفر الأصلي
        with requests.get(STREAM_URL, headers=headers, stream=True, timeout=10) as r:
            for chunk in r.iter_content(chunk_size=1024*1024): # يمرر 1 ميجا في كل مرة
                if chunk:
                    yield chunk

    return Response(stream_with_context(generate()), mimetype='video/mp2t')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
