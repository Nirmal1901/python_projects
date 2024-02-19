import os
from fastapi import FastAPI, HTTPException
import replicate

replicate.api_key = os.environ.get("r8_aopmOULLm121C8KKjUBOTp9osw9j0iM1JviB6")

app = FastAPI()

def get_drive_file_transcript(file_id):
    try:
        output = replicate.run(
            "openai/whisper:4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2",
            input={"audio": f"https://drive.google.com/uc?id={file_id}"}
        )

        if 'transcription' in output:
            transcript_text = output['transcription']
            return transcript_text.strip()
        else:
            raise HTTPException(status_code=500, detail="Internal Server Error: 'transcription' property not found in Replicate API response")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/get_transcript/{file_id}')
async def fetch_transcript(file_id: str):
    transcript = get_drive_file_transcript(file_id)
    
    if transcript:
        return {"transcript": transcript}
    else:
        raise HTTPException(status_code=404, detail="Failed to fetch transcript. Please check the provided file ID.")
