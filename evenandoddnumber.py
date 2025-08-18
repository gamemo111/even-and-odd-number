# streamlit_odd_even_checker.py

# Import the streamlit library so we can build the app
import streamlit as st
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

st.title("🔢 Even or Odd Number Checker with Voice (Offline)")

try:
    number = st.number_input("Enter a number", value=0, step=1)

    if st.button("Check"):
        result = "Even" if number % 2 == 0 else "Odd"
        output = f"The number {int(number)} is {result}"
        st.success(output)
        speak(output)

except ValueError:
    st.error("🚫 Please type a valid whole number.")

st.balloons()  # 🎈 for celebration
st.snow()      # ❄️ just for fun 
import streamlit as st

# ✅ Initialize session state variable 'history' if it doesn't exist
if 'history' not in st.session_state:
    st.session_state.history = []  # ← indented under the 'if'

import streamlit as st

# Custom CSS for blue and black background
st.markdown("""
    <style>
        /* Set background color of the main content */
        .stApp {
            background-color: #ADD8E6; /* Light blue */
        }

        /* Optional: style the sidebar */
        section[data-testid="stSidebar"] {
            background-color: black;
            color: white;
        }

        /* Optional: style text */
        .stMarkdown, .stTextInput, .stButton, .stAlert {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)
import streamlit as st
import random

st.set_page_config(page_title="Mini Game Hub 🎮", layout="centered")

# Game selection
game_choice = st.sidebar.selectbox("Choose a Game", [
    "Number Guessing",
    "Rock, Paper, Scissors",
    "Math Quiz",
    "Word Scramble"
])

# Common reset logic
if st.sidebar.button("🔄 Reset All"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

# ========== 1. NUMBER GUESSING ==========
elif game_choice == "Guess the Number":
    st.title("🎯 Guess the Number Game")
    st.write("I'm thinking of a number between 1 and 10...")

    guess = st.number_input("Your guess:", min_value=1, max_value=10, step=1)

    if st.button("Submit Guess"):
        if guess == st.session_state.secret_number:
            st.success("🎉 Correct! You guessed the number!")
            # Reset for next game
            st.session_state.secret_number = random.randint(1, 10)
        else:
            st.warning("❌ Wrong! Try again.")

# ========== 2. ROCK PAPER SCISSORS ==========
elif game_choice == "Rock, Paper, Scissors":
    st.title("✊🖐✌ Rock, Paper, Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.radio("Your choice:", choices)
    if st.button("Play RPS"):
        computer_choice = random.choice(choices)
        st.write(f"Computer chose: **{computer_choice}**")

        win_conditions = {
            ("Rock", "Scissors"),
            ("Scissors", "Paper"),
            ("Paper", "Rock"),
        }

        if user_choice == computer_choice:
            st.info("It's a draw!")
        elif (user_choice, computer_choice) in win_conditions:
            st.success("You win! 🎉")
        else:
            st.error("You lose! 😢")

# ========== 3. MATH QUIZ ==========
elif game_choice == "Math Quiz":
    st.title("➕ Math Quiz")

    if "mq_num1" not in st.session_state:
        st.session_state.mq_num1 = random.randint(1, 20)
        st.session_state.mq_num2 = random.randint(1, 20)

    st.write(f"What is {st.session_state.mq_num1} + {st.session_state.mq_num2}?")
    answer = st.number_input("Your Answer:", key="mq_answer")

    if st.button("Check Answer", key="mq_check"):
        correct = st.session_state.mq_num1 + st.session_state.mq_num2
        if answer == correct:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong. The answer was {correct}.")

        # New question
        st.session_state.mq_num1 = random.randint(1, 20)
        st.session_state.mq_num2 = random.randint(1, 20)

# ========== 4. WORD SCRAMBLE ==========
elif game_choice == "Word Scramble":
    st.title("🔤 Word Scramble")

    words = ["streamlit", "python", "game", "challenge", "code"]
    if "ws_word" not in st.session_state:
        st.session_state.ws_word = random.choice(words)
        st.session_state.ws_scrambled = ''.join(random.sample(st.session_state.ws_word, len(st.session_state.ws_word)))

    st.write(f"Unscramble this word: **{st.session_state.ws_scrambled}**")
    user_input = st.text_input("Your guess:", key="ws_input")

    if st.button("Submit", key="ws_submit"):
        if user_input.lower() == st.session_state.ws_word:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct word was **{st.session_state.ws_word}**")

        del st.session_state["ws_word"]
        del st.session_state["ws_scrambled"]


