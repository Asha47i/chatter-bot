# mirror_bot.py

import streamlit as st
import speech_recognition as sr

# Initialize session state
if "recording" not in st.session_state:
    st.session_state.recording = False
if "captured_text" not in st.session_state:
    st.session_state.captured_text = ""
if "recorded" not in st.session_state:
    st.session_state.recorded = False

# Function to capture speech and convert to text
def get_speech_input():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("🎤 Listening... Speak now.")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            st.session_state.captured_text = text
            st.session_state.recorded = True
            st.success("Speech captured successfully!")
    except sr.UnknownValueError:
        st.warning("Couldn't understand your speech.")
    except sr.RequestError:
        st.error("Speech recognition service is unavailable.")
    except Exception as e:
        st.error(f"Error: {e}")

# Main app
def main():
    st.title("🗣️ Chatter Bot 🤖")
    st.markdown("**Speech to Text or Text to Text. Everything to Text 😏**")

    mode = st.radio("Choose Input Mode:", ("Text", "Speech"))

    if mode == "Speech":
        if st.button("▶️ Start Recording"):
            st.session_state.recording = True
            get_speech_input()

        if st.button("⏹ Stop Recording"):
            st.session_state.recording = False

        if st.session_state.recorded:
            if st.button("📋 Show My Words"):
                st.write("📝 You said:")
                st.code(st.session_state.captured_text)

    else:
        user_input = st.text_input("Type something:")
        if user_input:
            st.write("📝 You typed:")
            st.code(user_input)

if __name__ == "__main__":
    main()
