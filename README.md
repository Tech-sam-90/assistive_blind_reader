# 🦯 Blind Reader  

**Blind Reader** is a hardware-software solution designed to assist visually impaired individuals by **reading printed text aloud**. It captures text using a camera connected to a Raspberry Pi, processes it with **Microsoft Azure Cognitive Services (OCR)**, and converts it into speech with **Azure Text-to-Speech (TTS)**.  

---

## ✨ Features  

- 📸 Capture text using a Raspberry Pi camera module  
- 🔎 High-accuracy Optical Character Recognition (OCR) with **Azure Computer Vision**  
- 🔊 Text-to-Speech conversion for **real-time audible reading**  
- 🎯 Achieves ~98% text recognition accuracy  
- 💡 Designed for **accessibility and ease of use**  

---

## 🛠️ Tech Stack  

**Hardware**  
- Raspberry Pi (4 recommended)  
- Raspberry Pi Camera Module  
- Speakers / Headphones  

**Software & Services**  
- Python 3.10+  
- Microsoft Azure Cognitive Services:  
  - **Computer Vision (OCR)**  
  - **Speech Services (TTS)**  

**Libraries**  
- `azure-ai-vision` (OCR)  
- `azure-cognitiveservices-speech` (TTS)  
- `python-dotenv` (environment variable management)  
- Other dependencies in `requirements.txt`  

---
