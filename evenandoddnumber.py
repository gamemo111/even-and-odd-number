import streamlit as st
import random

# ==========================
# 🔵 Custom Blue Background
# ==========================
st.markdown("""
    <style>
        .stApp {
            background-color: #D0E7FF; /* Light blue background */
        }
        .stButton > button {
            background-color: #3399FF;
            color: white;
            font-weight: bold;
        }
        .stRadio > div {
            background-color: #E6F2FF;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================
# 🎉 App Title and Menu
# ==========================
st.title("✨ Fun with Numbers and Games!✨😎")

# Sidebar menu
menu = st.sidebar.radio(
    "Choose a section:",
    [
        "Even or Odd Checker",
        "Guess the Game",
        "Pick a Number Game",
        "Rock, Paper, Scissors",
        "Animal Guessing Game"
    ]
)

# ==========================
# 1. Even or Odd Checker
# ==========================
if menu == "Even or Odd Checker":
    st.header("🔢 Even or Odd Checker")
    st.write("Enter a number and click the button to check if it's even or odd.")
    user_input = st.text_input("Type a number:")

    if st.button("Check Number"):
        if user_input == "":
            st.warning("Please type a number!")
        else:
            try:
                number = int(user_input)
                if number % 2 == 0:
                    st.success(f"✅ The number {number} is EVEN!")
                else:
                    st.info(f"ℹ️ The number {number} is ODD!")
            except ValueError:
                st.error("❌ Please enter a valid whole number.")

# ==========================
# 2. Guess Even or Odd Game
# ==========================
elif menu == "Guess the Game":
    st.header("🎲 Guess the Even or Odd Game")
    st.write("I'll give you a random number. Can you guess if it's even or odd?")

    if "random_number" not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)

    guess = st.radio("Your guess:", ["Even", "Odd"])

    if st.button("Submit Guess"):
        number = st.session_state.random_number
        correct = "Even" if number % 2 == 0 else "Odd"

        if guess == correct:
            st.success(f"🎉 You're right! The number was {number}, and it's {correct}.")
        else:
            st.error(f"Oops! The number was {number}, and it's {correct}.")

        st.session_state.random_number = random.randint(1, 100)

# ==========================
# 3. Pick a Number Game
# ==========================
elif menu == "Pick a Number Game":
    st.header("🎯 Pick a Number – Closest to Even Wins")
    st.write("Pick a number. I'll pick one too. Let's see who gets closer to an even number!")

    user_pick = st.number_input("Pick a number (1 to 100):", min_value=1, max_value=100)

    if st.button("Play"):
        app_pick = random.randint(1, 100)

        user_diff = abs(user_pick % 2)
        app_diff = abs(app_pick % 2)

        st.write(f"You picked: {user_pick}")
        st.write(f"I picked: {app_pick}")

        if user_diff == app_diff:
            st.info("😐 It's a tie!")
        elif user_diff < app_diff:
            st.success("🎉 You win! Your number is closer to even.")
        else:
            st.error("😜 I win! My number is closer to even.")

# ==========================
# 4. Rock, Paper, Scissors
# ==========================
elif menu == "Rock, Paper, Scissors":
    st.header("🪨📄✂️ Rock, Paper, Scissors")
    st.write("Choose your move and let's see who wins!")

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.radio("Your choice:", choices)

    if st.button("Play RPS"):
        app_choice = random.choice(choices)

        st.write(f"🤖 I picked: **{app_choice}**")
        st.write(f"🧑 You picked: **{user_choice}**")

        if user_choice == app_choice:
            st.info("😄 It's a tie!")
        elif (
            (user_choice == "Rock" and app_choice == "Scissors") or
            (user_choice == "Paper" and app_choice == "Rock") or
            (user_choice == "Scissors" and app_choice == "Paper")
        ):
            st.success("🎉 You win!")
        else:
            st.error("😜 I win!")

# ==========================
# 5. Animal Guessing Game
# ==========================
elif menu == "Animal Guessing Game":
    st.header("🐾 Animal Guessing Game")
    st.write("Can you guess which animal I'm thinking of? Let's try!")

    animals = ["Cat", "Dog", "Elephant", "Lion", "Rabbit", "Giraffe", "Zebra"]

    if "secret_animal" not in st.session_state:
        st.session_state.secret_animal = random.choice(animals)

    user_guess = st.radio("Your guess:", animals)

    if st.button("Guess Animal"):
        if user_guess == st.session_state.secret_animal:
            st.success(f"🎉 Yes! I was thinking of a **{user_guess}**!")
        else:
            st.error(f"❌ Nope! I was thinking of a **{st.session_state.secret_animal}**.")

        # Pick a new animal for the next round
        st.session_state.secret_animal = random.choice(animals)




