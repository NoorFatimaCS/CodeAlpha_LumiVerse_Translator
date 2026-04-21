# 🌌 LumiVerse Translator - AI Powered Multi-Modal Assistant

## 🚀 Project Overview
This project is an advanced **Language Translation Tool** developed as part of my **Artificial Intelligence Internship at CodeAlpha**. It provides a seamless interface for text and voice translation, designed with a futuristic "Neon-Space" aesthetic.

---

## ✅ Fulfillment of Core Requirements (Task 1)
As per the internship instructions, this project successfully implements:
- **User Interface:** A clean, responsive dashboard built with Streamlit.
- **Language Selection:** Dynamic selection for both Source and Target languages.
- **API Integration:** Powered by the Google Translate API for accurate real-time processing.
- **Clear Output:** Translated text is displayed in a dedicated high-visibility "Neon Output Box."

---

## ✨ Extra "Elite" Features (Beyond the Task)
To enhance usability and demonstrate advanced AI implementation, I have added:

1. **🎤 Voice Interface (Speech-to-Text):**
   Integrated Google Speech Recognition allowing users to translate by speaking directly into the microphone.
   
2. **🔊 Neural Audio Playback (Text-to-Speech):**
   Used `gTTS` to generate natural voice outputs, enabling users to hear the correct pronunciation in the target language.

3. **📝 Roman Urdu Optimization:**
   A specialized feature that understands Urdu written in English alphabets (Roman Urdu) and translates it accurately.

4. **📋 Smart Clipboard (Copy Button):**
   A one-click JavaScript-powered button to instantly copy the translation to the clipboard.

5. **💾 Translation Memory & Export:**
   - Real-time **History Log** to keep track of past translations.
   - **Download Button** to save results as `.txt` files for offline use.

6. **🔄 Smart Swap Logic:**
   Intelligent state management to swap languages instantly while maintaining the context of the translation.

7. **🌌 Futuristic Glassmorphism UI:**
   Custom CSS3 implementation with neon glows and blur effects for a premium "LumiVerse" feel.

---

## 🛠️ Technical Stack
- **Language:** Python 3.9+
- **Core Library:** `streamlit`
- **NLP & Translation:** `googletrans==4.0.0-rc1`
- **Speech Engine:** `SpeechRecognition`, `gTTS`
- **Styling:** Custom CSS with `Orbitron` Google Font


## 📸 Interface Preview
![App Demo Screenshot]





## ⚙️ How to Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/noorfatimaimran/CodeAlpha_LumiVerse_Translator.git](https://github.com/noorfatimaimran/CodeAlpha_LumiVerse_Translator.git)
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
 

  
**Developer: Noor Fatima 
Internship: CodeAlpha AI Program
Task ID: 01 - Language Translation Tool**
