from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

def get_video_transcript(url):
    try:
        video_id = url.split('v=')[-1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ''
        
        for caption in transcript_list:
            if 'text' in caption:
                transcript_text += ' ' + caption['text']
        
        return transcript_text
    except Exception as e:
        return str(e)

# API endpoint to fetch transcript from YouTube URL
@app.route('/get_transcript', methods=['POST'])
def fetch_transcript():
    data = request.get_json()
    video_url = data['video_url']
    
    transcript = get_video_transcript(video_url)
    
    if transcript:
        return jsonify({'transcript': transcript})
    else:
        return jsonify({'error': 'Failed to fetch transcript. Please check the provided URL.'})

if __name__ == '__main__':
    app.run(debug=True)
