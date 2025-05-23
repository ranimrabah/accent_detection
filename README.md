# accent_detection

This is a modular proof-of-concept tool designed for the REM Waste challenge. The project showcases how LangChain agents can be orchestrated to automate real-world tasks such as video processing and accent analysis.

## 🔧 Architecture & Approach

This app uses an agent-based structure:

- **Agent 1 – Audio Extractor**: Extracts audio from a video URL (MP4 or Loom) using FFmpeg.
- **Agent 2 – Accent Classifier (Planned)**: Designed to classify accents using a pretrained model. Below is an example using Hugging Face's `huggingsound` package.
- **Agent 3 – Explanation LLM (Planned)**: Will interpret the classifier's output and explain the accent in natural language using an LLM.


User Input (URL)
↓
Audio Extraction Agent
↓
Accent Classifier Agent (Planned)
↓
Explanation Agent (Planned)


## 🧠 Accent Classifier Agent (Planned)

A simple accent classification pipeline can use automatic speech recognition (ASR) to transcribe speech, then analyze it further for accent cues.

Example using [huggingsound](https://huggingface.co/docs/huggingsound):

```python
from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")
audio_paths = ["C:/Users/rabah/Documents/notebooks/technique/application_accent/audio_outputs/6eab0feea2f94c3e938dbe360c013033.wav"]

transcriptions = model.transcribe(audio_paths)
This transcription result can then be passed to an LLM agent to interpret the speaker's accent and generate a human-readable explanation and confidence score.

✅ Current Status
The agent structure and frontend UI are operational using Streamlit.

Audio extraction from public video links is working.

Accent classification and explanation agents are designed but not fully integrated due to time constraints.

📌 Note
This submission demonstrates:

Mastery of modular agent structure using LangChain.

Clear planning for audio and language processing pipelines.

Ability to expand and integrate ML/LLM components with more time.

🚀 Run Locally:
git clone https://github.com/ranimrabah/accent_detection.git
cd accent_detection
pip install -r requirements.txt
streamlit run app.py
yaml