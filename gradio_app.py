import gradio as gr
import subprocess

def detect(audio_file):
    if audio_file is None:
        return "Please upload audio"
    result = subprocess.run(["python3", "detector.py", audio_file], capture_output=True, text=True)
    return result.stdout or "Analyzed"

with gr.Blocks(title="🔍 Deepfake Detector") as demo:
    gr.Markdown("# 🔍 Deepfake Detector\n### Detect AI-generated deepfakes")
    audio = gr.Audio(label="Upload Audio", type="filepath")
    detect_btn = gr.Button("🔍 Analyze", variant="primary")
    result = gr.Textbox(label="Result", lines=4)
    detect_btn.click(detect, audio, result)

demo.launch(server_name="0.0.0.0", server_port=7862)
