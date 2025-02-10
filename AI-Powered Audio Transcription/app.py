import streamlit as st
import assemblyai as aai
import os
from dotenv import load_dotenv

# Load API Key from environment variable
load_dotenv()
API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
aai.settings.api_key = API_KEY

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcript = transcriber.transcribe(file_path, config=config)
    return transcript

# Streamlit UI
st.title("🎤 Audio Transcription")
st.write("Upload An Audio File To Get The Transcription And Highlights.")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Transcribing...")
    transcript = transcribe_audio(file_path)
    
    if transcript:
        st.subheader("Transcription:")
        st.write(transcript.text)
        
        if transcript.auto_highlights:
            st.subheader("Key Highlights:")
            for result in transcript.auto_highlights.results:
                st.write(f"- **{result.text}** (Count: {result.count}, Rank: {result.rank})")
        
    os.remove(file_path)
# Footer
st.markdown("------")
st.caption("👨‍💻 Developer >>>> This Project Was Developed And Built By Punjaji Karhale🚀")
