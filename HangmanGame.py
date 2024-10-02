import tkinter as tk
from random import choice

class Hangman:
    def __init__(self):
        # Open window and window name
        self.window = tk.Tk()
        self.window.title("Hangman")
        
        # Word to guess is selected
        self.word_list = ["france", "spain", "india", "germany", "lion", "tiger", "bear", "monkey", "pizza"]
        self.word = choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.tries = 6

        # Introduction label
        self.intro_label = tk.Label(self.window, text=f"\nWelcome to Hangman! Try to guess the word.\n\nWords: {self.word_list}", font=("Arial", 18))
        self.intro_label.pack()

        # Display the word as underscores initially
        self.word_label = tk.Label(self.window, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack()

        # Start button to initiate the game
        self.start_button = tk.Button(self.window, text="Start Game", font=("Arial", 18), command=self.start_game)
        self.start_button.pack()

        # Elements for the actual game, hidden initially
        self.guess_entry = tk.Entry(self.window, font=("Arial", 24))
        self.guess_button = tk.Button(self.window, text="Guess",font=("Arial",18),command=self.guess_letter)
        self.hangman_label = tk.Label(self.window, text=self.display_hangman(), font=("Arial", 24))
        self.result_label = tk.Label(self.window, text="", font=("Arial", 24))

        # Frame for Quit and Play Again buttons (hidden initially)
        self.button_frame = tk.Frame(self.window)
        self.quit_button = tk.Button(self.button_frame, text="Quit", font=("Arial", 18), command=self.window.quit)
        self.play_again_button = tk.Button(self.button_frame, text="Play Again", font=("Arial", 18), command=self.restart_game)

    def start_game(self):
        # Once the start button is clicked, hide the intro label and start button
        self.start_button.pack_forget()
        self.intro_label.pack_forget()  # Hide the welcome message
        self.intro_label = tk.Label(self.window, text="Hangman Game", font=("Arial", 18))
        self.intro_label.pack()

        # Show the entry field, guess button, hangman display, and result label
        self.guess_entry.pack()
        self.guess_button.pack()
        self.hangman_label.pack()
        self.result_label.pack()

    def guess_letter(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            self.result_label['text'] = "Please guess a single letter (a-z)."
            return
        elif guess in self.guessed_word:
            self.result_label['text'] = "You already guessed this letter. Try another one."
            return
        elif guess not in self.word:
            self.result_label['text'] = "Incorrect guess."
            self.tries -= 1
            self.hangman_label['text'] = self.display_hangman()
        else:
            self.result_label['text'] = "Correct guess!"
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed_word[i] = guess
            self.word_label['text'] = " ".join(self.guessed_word)

        # Check if the game is won or lost
        if "_" not in self.guessed_word:
            self.result_label['text'] = "Congratulations! You guessed the word."
            self.end_game()
        elif self.tries == 0:
            self.result_label['text'] = f"Game over. The word was {self.word}. Better luck next time!"
            self.end_game()

    def display_hangman(self):
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[self.tries]

    def end_game(self):
        # Disable further input after the game ends
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

        # Show Quit and Play Again buttons in the frame, side by side
        self.button_frame.pack()
        self.play_again_button.pack(side=tk.LEFT, padx=10)
        self.quit_button.pack(side=tk.LEFT, padx=10)

    def restart_game(self):
        # Reset game state
        self.word = choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.tries = 6

        # Reset the display elements
        self.word_label['text'] = " ".join(self.guessed_word)
        self.hangman_label['text'] = self.display_hangman()
        self.result_label['text'] = ""

        # Enable input fields again
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)

        # Hide Quit and Play Again buttons
        self.quit_button.pack_forget()
        self.play_again_button.pack_forget()
        self.button_frame.pack_forget()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Hangman()
    game.run()
