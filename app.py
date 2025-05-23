import streamlit as st
from agent.download_agent import download_audio_as_wav

st.title("🎙️ Audio Downloader - WAV Mono 16kHz")

url = st.text_input("Enter YouTube or direct video URL:")

if url:
    try:
        st.info("Downloading audio and converting to WAV...")
        audio_path = download_audio_as_wav(url)
        st.success(f"Audio saved to: {audio_path}")

        st.audio(audio_path)
    except Exception as e:
        st.error(f"An error occurred: {e}")
