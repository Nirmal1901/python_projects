from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ''
        
        for caption in transcript_list:
            if 'text' in caption:
                transcript_text += ' ' + caption['text']
        
        return transcript_text.strip()
    except Exception as e:
        return str(e), 500

@app.route('/get_transcript', methods=['GET'])
def fetch_transcript():
    video_url = request.args.get('video_url')
    if not video_url:
        return "Missing 'video_url' parameter", 400

    transcript = get_video_transcript(video_url)
    
    if transcript:
        return jsonify({"transcript": transcript})
    else:
        return "Failed to fetch transcript. Please check the provided video URL.", 404

if __name__ == '__main__':
    app.run(debug=True)  # This will run the Flask app on http://127.0.0.1:5000/ by default
