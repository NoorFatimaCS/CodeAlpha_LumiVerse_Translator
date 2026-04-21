import streamlit as st

from googletrans import Translator

from gtts import gTTS

from io import BytesIO

from datetime import datetime

import tempfile

import os

import speech_recognition as sr

import base64

import urllib.parse



st.set_page_config(page_title="LumiVerse Translator", page_icon="🌌", layout="wide")



st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

.stApp {

    background:

        radial-gradient(circle at 15% 25%, rgba(171, 104, 255, 0.22), transparent 20%),

        radial-gradient(circle at 85% 25%, rgba(244, 63, 94, 0.20), transparent 20%),

        radial-gradient(circle at 50% 85%, rgba(59, 130, 246, 0.16), transparent 25%),

        linear-gradient(135deg, #0a0a1a 0%, #1a0d2e 35%, #1e1b4b 100%);

    color: #e5e7eb;

    font-family: 'Orbitron', monospace;

}



.title-glow {

    font-family: 'Orbitron', monospace;

    font-size: 3.2rem;

    font-weight: 900;

    text-align: center;

    background: linear-gradient(135deg, #ab68ff, #f43f5e, #3b82f6);

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    background-clip: text;

    animation: glow 2s ease-in-out infinite alternate;

    letter-spacing: 2px;

    margin-bottom: 0.3rem;

}



@keyframes glow {

    from { filter: drop-shadow(0 0 20px rgba(171,104,255,0.6)); }

    to { filter: drop-shadow(0 0 30px rgba(244,63,94,0.6)); }

}



.subtitle {

    text-align: center;

    color: #a78bfa;

    font-size: 1.1rem;

    font-weight: 500;

    margin-bottom: 2rem;

    letter-spacing: 1px;

}



.neon-card {

    background: rgba(15, 23, 42, 0.85);

    border: 1px solid rgba(171, 104, 255, 0.30);

    border-radius: 24px;

    padding: 28px;

    box-shadow:

        0 0 0 1px rgba(171,104,255,0.15),

        0 20px 50px rgba(0,0,0,0.40),

        inset 0 1px 0 rgba(255,255,255,0.05);

    backdrop-filter: blur(20px);

    transition: all 0.3s ease;

}



.neon-card:hover {

    border-color: rgba(244, 63, 94, 0.5);

    box-shadow:

        0 0 0 1px rgba(244,63,94,0.25),

        0 25px 60px rgba(0,0,0,0.45),

        0 0 40px rgba(244,63,94,0.15);

}



.section-title {

    color: #ffffff;

    font-family: 'Orbitron', monospace;

    font-weight: 800;

    font-size: 1.25rem;

    margin-bottom: 1rem;

    text-shadow: 0 0 10px rgba(171,104,255,0.5);

}



label, .stSelectbox label, .stTextArea label {

    color: #e2e8f0 !important;

    font-weight: 700 !important;

    font-family: 'Orbitron', monospace;

}



/* DROPDOWN (SELECTBOX) FIX - Isko purane Selectbox CSS ki jagah replace karein */

div[data-testid="stSelectbox"] div[data-baseweb="select"] {

    background: rgba(255,255,255,0.08) !important;

    color: #ffffff !important;

    border: 1px solid rgba(171,104,255,0.25) !important;

    border-radius: 16px !important;

    font-family: 'Orbitron', monospace;

    

    /* Text ko center karne ke liye fixes */

    height: 45px !important; 

    display: flex !important;

    align-items: center !important;

    padding: 0 10px !important;

}



/* Isse text ki position mazeed behtar ho jayegi */

div[data-testid="stSelectbox"] [data-testid="stMarkdownContainer"] p {

    margin: 0 !important;

    padding: 0 !important;

    line-height: 1.2 !important;

    display: flex !important;

    align-items: center !important;

}



button {

    background: linear-gradient(135deg, #ab68ff, #f43f5e) !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 16px !important;

    font-weight: 700 !important;

    font-family: 'Orbitron', monospace;

    box-shadow: 0 0 25px rgba(171,104,255,0.35) !important;

    padding: 12px 24px !important;

    min-height: 48px !important;

    transition: all 0.3s ease !important;

}



button:hover {

    transform: translateY(-2px);

    box-shadow: 0 0 35px rgba(244,63,94,0.45) !important;

}



.output-box {

    background: rgba(10, 10, 26, 0.95);

    border: 1px solid rgba(171,104,255,0.30);

    border-radius: 20px;

    padding: 24px;

    color: #ffffff;

    font-size: 1.1rem;

    line-height: 1.8;

    box-shadow: 

        inset 0 0 20px rgba(171,104,255,0.08),

        0 0 40px rgba(0,0,0,0.5);

    font-family: 'Orbitron', monospace;

}



.copy-btn {

    background: linear-gradient(135deg, #1e1b4b, #2d1b69) !important;

    color: #a78bfa !important;

    border: 1px solid rgba(167,139,250,0.4) !important;

    padding: 12px 24px !important;

    border-radius: 16px !important;

    font-weight: 700 !important;

    font-family: 'Orbitron', monospace !important;

    cursor: pointer;

}



.history-item {

    background: rgba(255,255,255,0.03);

    border: 1px solid rgba(171,104,255,0.15);

    border-radius: 16px;

    padding: 16px;

    margin: 8px 0;

}
button[kind="secondary"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}


.sidebar .css-1d391kg {

    background: rgba(15, 23, 42, 0.95) !important;

    border-right: 1px solid rgba(171,104,255,0.2) !important;

}

</style>

""", unsafe_allow_html=True)



def copy_button(text):

    encoded = urllib.parse.quote(text)

    html = f"""

    <button class="copy-btn" onclick="navigator.clipboard.writeText('{text}');this.innerText='✅ Copied!';setTimeout(() => this.innerText='📋 Copy Text', 2000);">

        📋 Copy Text

    </button>

    """

    st.markdown(html, unsafe_allow_html=True)



def speak_text(text, lang):

    try:

        tts = gTTS(text=text, lang=lang)

        fp = BytesIO()

        tts.write_to_fp(fp)

        return fp.getvalue()

    except:

        return None



def transcribe_audio(audio_bytes):
    recognizer = sr.Recognizer()
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
        with sr.AudioFile(tmp_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        os.unlink(tmp_path)
        return text
    except Exception as e:
        return None


def perform_translation(text, src, dest):
    try:
        translator = Translator()
        src_code = languages[src]
        dest_code = languages[dest]
        result = translator.translate(text, src=src_code, dest=dest_code)
        st.session_state.translated_text = result.text
        st.session_state.history.insert(0, {
            "time": datetime.now().strftime("%H:%M:%S"),
            "source": src,
            "target": dest,
            "input": text[:100] + "..." if len(text) > 100 else text,
            "output": result.text[:100] + "..." if len(result.text) > 100 else result.text
        })
        st.session_state.history = st.session_state.history[:20]
        return True
    except Exception as e:
        st.error(f"❌ Translation error: {str(e)}")
        return False
# Animated Header

st.markdown('<div class="title-glow">🌌 LumiVerse Translator</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">A futuristic language assistant for seamless text translation, voice interaction, and multilingual playback.</div>', unsafe_allow_html=True)



languages = {

    "Auto Detect": "auto",

    "English": "en",

    "Urdu": "ur",
    "Roman Urdu": "ur",
    "Hindi": "hi",

    "Arabic": "ar",

    "French": "fr",

    "German": "de",

    "Spanish": "es",

    "Turkish": "tr",

    "Chinese": "zh-cn",

    "Japanese": "ja"

}



if "history" not in st.session_state:

    st.session_state.history = []

if "translated_text" not in st.session_state:

    st.session_state.translated_text = ""

if "recognized_text" not in st.session_state:

    st.session_state.recognized_text = ""
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "src_lang" not in st.session_state:
    st.session_state.src_lang = "English"  # Pehli baar khulne par English hogi
if "targ_lang" not in st.session_state:
    st.session_state.targ_lang = "Urdu"    # Pehli baar khulne par Urdu hogi



# Sidebar

with st.sidebar:

    st.markdown("### 📊 LumiVerse Stats")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Translations", len(st.session_state.history))

    with col2:

        st.metric("Languages", len(languages)-1)

    st.markdown("---")

    st.markdown("### ✨ Features")

    st.markdown("• **Instant Translation**")

    st.markdown("• **Voice Input**") 

    st.markdown("• **Voice Output**")

    st.markdown("• **Smart History**")

    st.markdown("• **Clipboard Copy**")




col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="neon-card">
        <div class="section-title">⚡ Instant Translation</div>
        <div>Transform text across 10+ languages instantly.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="neon-card">
        <div class="section-title">🎤 Voice Capture</div>
        <div>Speak naturally, get perfect text conversion.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="neon-card">
        <div class="section-title">🔊 Audio Output</div>
        <div>Listen to translations in natural voice.</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")



# Main Panels
left, right = st.columns([2.2, 1])

with left:
    # Card ke andar content ko wrap kiya gaya hai
    st.markdown("""
    <div class="neon-card" style="height: 100%;">
        <div class="section-title">⚡ Translation Engine</div>
        <div style="margin-bottom: 20px; color: #a78bfa;">Input your text below for instant multi-language processing.</div>
    </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        source_lang = st.selectbox("From Language", list(languages.keys()), 
                                   index=list(languages.keys()).index(st.session_state.src_lang))
    with col_lang2:
        target_lang = st.selectbox("To Language", list(languages.keys()), 
                                   index=list(languages.keys()).index(st.session_state.targ_lang))

    input_text = st.text_area(
        "Enter text to translate",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type your message here, or use voice input on the right...",
        key="main_text_area"
    )

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    translate_btn = col_btn1.button("🌐 Translate")
    swap_btn = col_btn2.button("↔️ Swap")
    clear_btn = col_btn3.button("🗑️ Clear")

    if swap_btn:
        st.session_state.src_lang = target_lang
        st.session_state.targ_lang = source_lang
        st.rerun()

# Voice Interface block (with proper clear recording fix)
if "voice_input_key_counter" not in st.session_state:
    st.session_state.voice_input_key_counter = 0

with right:
    st.markdown("""
    <div class="neon-card" style="height: 100%;">
        <div class="section-title">🎤 Voice Interface</div>
        <div style="margin-bottom: 20px; color: #a78bfa;">Capture audio and translate in real-time.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    voice_key = f"voice_input_{st.session_state.voice_input_key_counter}"
    audio_value = st.audio_input("🎙️ Record Voice", key=voice_key)

    clear_recording = st.button("🗑️ Clear Recording", key="clear_recording_btn")
    
    if clear_recording:
        if voice_key in st.session_state:
            del st.session_state[voice_key]
        st.session_state.voice_input_key_counter += 1
        st.session_state.recognized_text = ""
        st.session_state.input_text = ""
        st.rerun()

    if audio_value is not None:
        if st.session_state.input_text == "":
            with st.spinner("🔄 Processing..."):
                recognized = transcribe_audio(audio_value.read())
                if recognized:
                    st.session_state.input_text = recognized
                    # YAHAN FIX HAI: source_lang aur target_lang wahi use hongi jo swap ke baad select hui hain
                    perform_translation(recognized, source_lang, target_lang)
                    st.rerun()



if clear_btn:

    st.session_state.history = []

    st.session_state.translated_text = ""

    st.session_state.recognized_text = ""
    st.session_state.input_text = ""

    st.rerun()






if translate_btn:
    if not input_text.strip():
        st.warning("⚠️ Please enter text...")
    else:
        perform_translation(input_text, source_lang, target_lang)
        st.rerun()
# --- Output Section ---
if st.session_state.translated_text:
    st.markdown("## ✨ Translation Result")
    
    # HTML ko render karne ke liye st.markdown use karein
    st.markdown(f"""
    <div class="output-box">
        <div style="font-size: 1.3rem; font-weight: 700; margin-bottom: 12px;">
            {st.session_state.translated_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_copy, col_download = st.columns(2)
    with col_copy:
        copy_button(st.session_state.translated_text)
    with col_download:
        st.download_button(
            "💾 Download",
            data=st.session_state.translated_text,
            file_name=f"lumiverse-translation-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt",
            mime="text/plain"
        )
    
    # Audio Playback
    try:
        audio_lang = languages[target_lang] if languages[target_lang] != "auto" else "en"
        audio_bytes = speak_text(st.session_state.translated_text, audio_lang)
        if audio_bytes:
            st.markdown("### 🔊 Audio Playback")
            st.audio(audio_bytes, format="audio/mp3")
    except:
        st.warning("⚠️ Audio not available for this language")


# History
st.markdown("## 📜 Translation Memory")

if st.session_state.history:
    for item in st.session_state.history:
        with st.expander(f"**{item['time']}** • {item['source']} ➜ {item['target']}"):
            # HTML ko clean format mein likha hai
            st.markdown(f"""
            <div class="history-item" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px;">
                <div style="color: #a78bfa; margin-bottom: 5px;"><strong>Input:</strong> {item['input']}</div>
                <div style="color: #ffffff;"><strong>Output:</strong> {item['output']}</div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("👆 Start translating to build your history")


st.markdown("---")

st.markdown("<p style='text-align: center; color: #a78bfa; font-size: 0.9rem;'>Built for <strong>CodeAlpha AI Internship</strong> | LumiVerse Translator © 2026</p>", unsafe_allow_html=True)