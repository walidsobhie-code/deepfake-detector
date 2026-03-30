# Deepfake Detector 🔍🛡️

Detect AI-generated audio and video deepfakes. Protect against voice spoofing and face swap fraud.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](Dockerfile)

## Why Deepfake Detection?

With AI deepfakes exploding, security is critical. Every company needs to verify audio/video authenticity.

## ✨ Features

- 🎙️ **Audio Detection** - Detect voice deepfakes using MFCC & spectral analysis
- 🔊 **Feature Extraction** - MFCC, spectral centroid, chroma features
- 📊 **Confidence Scores** - Detailed analysis with indicators
- 🔔 **Batch Processing** - Analyze multiple files at once
- 🌐 **Web UI** - Gradio interface for easy testing
- 🐳 **Docker Ready** - Deploy anywhere with Docker

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Detect audio deepfake
python detector.py --input voice.wav --type audio

# Batch analysis
python detector.py --batch ./audio_samples/

# Interactive mode
python detector.py --interactive
```

## 🌐 Web UI

```bash
python gradio_app.py
# Open http://localhost:7860
```

## 🐳 Docker

```bash
docker build -t deepfake-detector .
docker run -p 7860:7860 deepfake-detector
```

## 📝 License

MIT License

## ⭐ Star for security!