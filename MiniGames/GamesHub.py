
import tkinter as tk
import random
import json
from pathlib import Path

# ---------- SETTINGS ----------

BG = "#121826"
CARD = "#202B3D"
PURPLE = "#8B5CF6"
WHITE = "#FFFFFF"
MUTED = "#B8C2D6"
GREEN = "#34D399"

SAVE_FILE = Path(__file__).with_name("games_scores.json")

root = tk.Tk()
root.title("Mini Games Hub")
root.geometry("650x600")
root.configure(bg=BG)
root.minsize(500, 500)

wins = 0
played = 0


# ---------- SAVE SCORES ----------

def load_scores():
    global wins, played

    try:
        data = json.loads(SAVE_FILE.read_text())
        wins = data.get("wins", 0)
        played = data.get("played", 0)
    except (FileNotFoundError, ValueError, OSError):
        pass


def save_scores():
    try:
        SAVE_FILE.write_text(
            json.dumps({"wins": wins, "played": played})
        )
    except OSError:
        print("Could not save scores.")


def finish_game(won):
    global wins, played

    played += 1

    if won:
        wins += 1

    save_scores()


# ---------- INTERFACE HELPERS ----------

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def label(text, size=16, color=WHITE):
    widget = tk.Label(
        root,
        text=text,
        font=("Arial", size, "bold"),
        bg=BG,
        fg=color,
        wraplength=550,
        justify="center"
    )
    widget.pack(pady=12)
    return widget


def button(text, command, color=CARD):
    widget = tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 14, "bold"),
        bg=color,
        fg=WHITE,
        activebackground=PURPLE,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        width=25,
        pady=10
    )
    widget.pack(pady=6)
    return widget


def entry():
    field = tk.Entry(
        root,
        font=("Arial", 18),
        bg=CARD,
        fg=WHITE,
        insertbackground=WHITE,
        justify="center",
        relief="flat"
    )
    field.pack(pady=12, ipady=8)
    field.focus_set()
    return field


def game_header(title):
    clear_screen()
    label(title, 25, GREEN)


def back_button():
    button("← Back to Menu", main_menu, PURPLE)


# ---------- MAIN MENU ----------

def main_menu():
    clear_screen()

    label("🎮 MINI GAMES HUB", 28, GREEN)
    label("Choose a game to play!", 14, MUTED)

    label(f"🏆 Wins: {wins}  |  Games Played: {played}", 14)

    button("🔢 Number Guesser", number_guesser)
    button("✊ Rock Paper Scissors", rock_paper_scissors)
    button("📖 Interactive Story", interactive_story)
    button("🧠 Python Trivia", trivia_quiz)
    button("🔤 Word Scramble", word_scramble)

    button("Exit", root.destroy, PURPLE)


# ---------- GAME 1: NUMBER GUESSER ----------

def number_guesser():
    game_header("🔢 NUMBER GUESSER")

    target = random.randint(1, 100)
    attempts = 0
    maximum = 7
    finished = False

    label("Guess a number between 1 and 100!")
    label("You have 7 attempts.", 13, MUTED)

    guess_entry = entry()
    result = label("Good luck!", 15)

    def check_guess():
        nonlocal attempts, finished

        if finished:
            return

        try:
            guess = int(guess_entry.get())
        except ValueError:
            result.config(text="Enter a valid number!")
            return

        if not 1 <= guess <= 100:
            result.config(text="Choose between 1 and 100.")
            return

        attempts += 1

        if guess == target:
            finished = True
            result.config(
                text=f"🎉 Correct! You won in {attempts} guesses!",
                fg=GREEN
            )
            finish_game(True)

        elif attempts >= maximum:
            finished = True
            result.config(
                text=f"Game over! The number was {target}."
            )
            finish_game(False)

        elif guess < target:
            result.config(
                text=f"📈 Higher! {maximum - attempts} attempts left."
            )

        else:
            result.config(
                text=f"📉 Lower! {maximum - attempts} attempts left."
            )

        guess_entry.delete(0, tk.END)

    button("Submit Guess", check_guess, PURPLE)
    button("Play Again", number_guesser)
    back_button()


# ---------- GAME 2: ROCK PAPER SCISSORS ----------

def rock_paper_scissors():
    game_header("✊ ROCK PAPER SCISSORS")

    label("First to 2 wins!")

    player_score = 0
    computer_score = 0
    finished = False

    score_label = label("You: 0  |  Computer: 0")
    result = label("Choose your move!", 15)

    choices = ["rock", "paper", "scissors"]

    def play(player):
        nonlocal player_score, computer_score, finished

        if finished:
            return

        computer = random.choice(choices)

        if player == computer:
            message = "It's a tie!"

        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            player_score += 1
            message = "You win this round!"

        else:
            computer_score += 1
            message = "Computer wins this round!"

        result.config(
            text=f"Computer chose {computer}.\n{message}"
        )

        score_label.config(
            text=f"You: {player_score}  |  Computer: {computer_score}"
        )

        if player_score == 2:
            finished = True
            result.config(text="🏆 YOU WON THE MATCH!")
            finish_game(True)

        elif computer_score == 2:
            finished = True
            result.config(text="Computer won the match!")
            finish_game(False)

    button("🪨 Rock", lambda: play("rock"))
    button("📄 Paper", lambda: play("paper"))
    button("✂️ Scissors", lambda: play("scissors"))

    button("Play Again", rock_paper_scissors, PURPLE)
    back_button()


# ---------- GAME 3: INTERACTIVE STORY ----------

def interactive_story():
    game_header("📖 THE LOST PYTHON KINGDOM")

    label(
        "You discover a mysterious castle "
        "with two glowing doors."
    )

    def blue_door():
        game_header("🔵 THE BLUE DOOR")

        label(
            "You meet a robot guarding "
            "an ancient Python computer."
        )

        label("Which keyword creates a Python function?")

        button(
            "def",
            lambda: ending(
                True,
                "🏆 Correct! The robot crowns you Python Champion!"
            )
        )

        button(
            "function",
            lambda: ending(
                False,
                "The robot sends you back to coding school!"
            )
        )

        back_button()

    def red_door():
        game_header("🔴 THE RED DOOR")

        label(
            "You discover a sleeping dragon "
            "guarding a treasure chest."
        )

        label("What will you do?")

        button(
            "Ask the dragon politely",
            lambda: ending(
                True,
                "🏆 The dragon rewards your kindness!"
            )
        )

        button(
            "Sneak past the dragon",
            lambda: ending(
                False,
                "The dragon wakes up! You escape safely."
            )
        )

        back_button()

    button("🚪 Blue Door", blue_door)
    button("🚪 Red Door", red_door)
    back_button()


def ending(won, message):
    game_header("📖 THE END")

    label(message, 20)

    finish_game(won)

    button("Play Again", interactive_story, PURPLE)
    back_button()


# ---------- GAME 4: PYTHON TRIVIA ----------

def trivia_quiz():
    game_header("🧠 PYTHON TRIVIA")

    questions = [
        (
            "Which keyword defines a function?",
            ["def", "func", "function"],
            0
        ),
        (
            "Which symbol starts a comment?",
            ["//", "#", "--"],
            1
        ),
        (
            "What does print() do?",
            ["Deletes text", "Displays text", "Saves files"],
            1
        ),
        (
            "Which type stores True or False?",
            ["bool", "str", "int"],
            0
        ),
        (
            "Which function gives the length of a list?",
            ["size()", "count()", "len()"],
            2
        )
    ]

    random.shuffle(questions)

    question_number = 0
    score = 0

    def show_question():
        nonlocal question_number, score

        game_header("🧠 PYTHON TRIVIA")

        if question_number >= len(questions):
            label(f"Final Score: {score}/5", 24, GREEN)

            if score >= 3:
                label("🏆 You passed!")
                finish_game(True)
            else:
                label("Keep practicing!")
                finish_game(False)

            button("Play Again", trivia_quiz, PURPLE)
            back_button()
            return

        question, options, correct = questions[question_number]

        label(f"Question {question_number + 1}/5", 14, MUTED)
        label(question, 18)

        def answer(selected):
            nonlocal question_number, score

            if selected == correct:
                score += 1

            question_number += 1
            show_question()

        for index, option in enumerate(options):
            button(
                option,
                lambda i=index: answer(i)
            )

        label(f"Current Score: {score}", 13, MUTED)
        back_button()

    show_question()


# ---------- GAME 5: WORD SCRAMBLE ----------

def word_scramble():
    game_header("🔤 WORD SCRAMBLE")

    words = {
        "python": "A programming language",
        "browser": "Used to visit websites",
        "keyboard": "Used for typing",
        "variable": "Stores a value",
        "function": "A reusable block of code",
        "computer": "Runs programs"
    }

    word = random.choice(list(words.keys()))
    hint = words[word]

    letters = list(word)
    random.shuffle(letters)

    while "".join(letters) == word:
        random.shuffle(letters)

    scrambled = "".join(letters)

    attempts = 0
    finished = False

    label(f"Unscramble: {scrambled.upper()}", 23, GREEN)
    label(f"Hint: {hint}", 14, MUTED)

    answer_entry = entry()
    result = label("You have 3 attempts.", 14)

    def check_answer():
        nonlocal attempts, finished

        if finished:
            return

        answer = answer_entry.get().lower().strip()

        if not answer:
            result.config(text="Please enter an answer.")
            return

        attempts += 1

        if answer == word:
            finished = True
            result.config(text="🎉 Correct! You win!", fg=GREEN)
            finish_game(True)

        elif attempts >= 3:
            finished = True
            result.config(
                text=f"Game over! The word was {word}."
            )
            finish_game(False)

        else:
            result.config(
                text=f"Try again! {3 - attempts} attempts left."
            )

        answer_entry.delete(0, tk.END)

    button("Submit Answer", check_answer, PURPLE)
    button("New Word", word_scramble)
    back_button()


# ---------- START APP ----------

load_scores()
main_menu()

root.mainloop()
