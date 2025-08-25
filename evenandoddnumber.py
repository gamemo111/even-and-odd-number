import streamlit as st
import random
import math

# ==========================
# 🎨 Custom Styling
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

menu = st.sidebar.radio(
    "Choose a section:",
    [
        "Even or Odd Checker",
        "Guess the Game",
        "Pick a Number Game",
        "Rock, Paper, Scissors",
        "Animal Guessing Game",
        "Basic Calculator",
        "Scientific Calculator",
        "Advanced Calculator",
        "Math Quiz Game"
    ]
)

# ==========================
# 1. Even or Odd Checker
# ==========================
if menu == "Even or Odd Checker":
    st.header("🔢 Even or Odd Checker")
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
# 2. Guess the Game
# ==========================
elif menu == "Guess the Game":
    st.header("🎲 Guess the Even or Odd Game")

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

    animals = ["Cat", "Dog", "Elephant", "Lion", "Rabbit", "Giraffe", "Zebra"]

    if "secret_animal" not in st.session_state:
        st.session_state.secret_animal = random.choice(animals)

    user_guess = st.radio("Your guess:", animals)

    if st.button("Guess Animal"):
        if user_guess == st.session_state.secret_animal:
            st.success(f"🎉 Yes! I was thinking of a **{user_guess}**!")
        else:
            st.error(f"❌ Nope! I was thinking of a **{st.session_state.secret_animal}**.")

        st.session_state.secret_animal = random.choice(animals)

# ==========================
# 6. Basic Calculator
# ==========================
elif menu == "Basic Calculator":
    st.header("🧮 Basic Calculator")

    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    operation = st.radio("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("❌ Cannot divide by zero!")

# ==========================
# 7. Scientific Calculator
# ==========================
elif menu == "Scientific Calculator":
    st.header("🔬 Scientific Calculator")

    expression = st.text_input("Enter a math expression (e.g., sqrt(16), sin(45)):")
    if st.button("Evaluate"):
        try:
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

# ==========================
# 8. Advanced Calculator
# ==========================
elif menu == "Advanced Calculator":
    st.header("⚡ Advanced Calculator")
    expression = st.text_area("Enter a complex expression:")

    if st.button("Compute"):
        try:
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

# ==========================
# 9. Math Quiz Game (Difficulty levels)
# ==========================
elif menu == "Math Quiz Game":
    st.header("🧮 Math Quiz Game 🎯")

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question" not in st.session_state:
        st.session_state.question = None

    score = st.session_state.score
    if score < 5:
        difficulty = "Easy"
        num_range = (1, 10)
        ops = ["+", "-"]
    elif score < 10:
        difficulty = "Medium"
        num_range = (1, 50)
        ops = ["+", "-", "*"]
    else:
        difficulty = "Hard"
        num_range = (1, 100)
        ops = ["+", "-", "*", "/"]

    if st.session_state.question is None:
        a = random.randint(*num_range)
        b = random.randint(*num_range)
        op = random.choice(ops)
        if op == "/":
            b = random.randint(1, num_range[1])
        st.session_state.question = (a, b, op)

    a, b, op = st.session_state.question
    st.subheader(f"({difficulty}) ➝  {a} {op} {b} = ?")

    user_answer = st.text_input("Your answer:")

    if st.button("Submit Answer"):
        try:
            correct_answer = eval(f"{a}{op}{b}")
            correct_answer = round(correct_answer, 2)
            if float(user_answer) == correct_answer:
                st.success(f"🎉 Correct! The answer is {correct_answer}.")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer was {correct_answer}.")

            a = random.randint(*num_range)
            b = random.randint(*num_range)
            op = random.choice(ops)
            if op == "/":
                b = random.randint(1, num_range[1])
            st.session_state.question = (a, b, op)

        except:
            st.warning("⚠️ Please enter a valid number.")

    st.info(f"🏆 Your Score: {st.session_state.score}")
