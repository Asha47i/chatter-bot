import streamlit as st
import pyttsx3
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK resources are available
nltk.download('punkt')

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to get chatbot response based on user input
def get_chatbot_response(user_input):
    # Simply return the same input as the response
    return user_input

# Text-based interface
def text_mode():
    st.header("Text Chat Mode")
    user_input = st.text_input("👉 You can type your message here:")

    if user_input:
        response = get_chatbot_response(user_input)
        st.write(f"🤖 Chatbot: {response}")

# Speech-based interface
def speech_mode():
    st.header("Speech Chat Mode")
    st.write("🎤 Listening... Speak clearly into your microphone.")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            st.write(f"🗣️ You said: {user_input}")

            response = get_chatbot_response(user_input)
            st.write(f"🤖 Chatbot: {response}")

            speak(response)

        except sr.UnknownValueError:
            st.write("😕 Sorry, I couldn't understand what you said. Please try again.")
        except sr.RequestError as e:
            st.write(f"🚫 There was an error with the speech recognition service: {e}")

# Main function to choose between text and speech mode
def main():
    st.title("🗣️ Speech-enabled Chatbot 🤖")
    mode = st.radio("Choose your interaction mode:", ("Text", "Speech"))

    if mode == "Text":
        text_mode()
    elif mode == "Speech":
        speech_mode()

if __name__ == "__main__":
    main()

