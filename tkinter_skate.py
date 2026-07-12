import random
import tkinter as tk
from tkinter import ttk


class RockPaperScissors:
    WINS = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def __init__(self):
        self.bot_rps = None
        self.setter = None

    def rps_outcome(self, choice):
        self.bot_rps = random.choice(("rock", "paper", "scissors"))

        if choice == self.bot_rps:
            self.setter = "tie"
        elif self.WINS[choice] == self.bot_rps:
            self.setter = "player"
        else:
            self.setter = "bot"


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x600")
        self.window.title("SKATE")
        self.window.config(bg="white")

        self.rps = RockPaperScissors()
        self.game = Game(self)

        self.quit_btn = tk.Button(
            self.window,
            text="X",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.quit
        )
        self.quit_btn.pack(anchor="nw", padx=10, pady=10)

        self.main_menu()

    def quit(self):
        print("THANK YOU FOR PLAYING!")
        self.window.destroy()

    def main_menu(self):
        self.welcome_label = tk.Label(
            self.window,
            text="WELCOME TO SKATE\n************************",
            font=("Arial", 30),
            bg="white",
            fg="black"
        )
        self.welcome_label.pack(side=tk.TOP, pady=20)

        self.start_btn = tk.Button(
            self.window,
            text="START",
            font=("Arial", 25),
            bg="white",
            fg="black",
            command=self.start_window,
            width=15
        )
        self.start_btn.pack(side=tk.TOP, pady=10)

        self.instructions_btn = tk.Button(
            self.window,
            text="HOW TO PLAY",
            font=("Arial", 25),
            bg="white",
            fg="black",
            command=self.instructions,
            width=15
        )
        self.instructions_btn.pack(side=tk.TOP, pady=10)

    def instructions(self):
        self.welcome_label.destroy()
        self.start_btn.destroy()
        self.instructions_btn.destroy()

        self.instructions_frame = tk.Frame(
            self.window,
            bg="white"
        )
        self.instructions_frame.pack()

        self.instructions_text = tk.Label(
            self.instructions_frame,
            text=(
                "1. Flat-ground only\n\n"
                "2. Rock paper scissors decides who sets the first trick\n\n"
                "3. The setter chooses a trick that the defender must replicate if landed\n\n"
                "4. If the defender bails, a letter is given until SKATE is spelled out\n\n"
                "5. If the setter bails, the next player becomes the setter\n\n"
                "6. The first player to spell out SKATE loses\n\n"
                "7. Two attempts to replicate the trick are given on the defender's last letter"
            ),
            font=("Arial", 12),
            bg="white",
            fg="black",
            justify="left"
        )
        self.instructions_text.grid(row=0, column=0, columnspan=3, pady=50)

        self.back_btn = tk.Button(
            self.instructions_frame,
            text="BACK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.instructions_back_menu
        )
        self.back_btn.grid(row=1, column=0, columnspan=3, pady=30)

    def instructions_back_menu(self):
        self.instructions_frame.destroy()

        self.main_menu()

    def start_window(self):
        self.start_btn.destroy()
        self.welcome_label.destroy()
        self.instructions_btn.destroy()
        self.rps_window()

    def rps_window(self):
        self.rps_frame = tk.Frame(
            self.window,
            bg="white"
        )
        self.rps_frame.pack()

        self.rps_label = tk.Label(
            self.rps_frame,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 25),
            bg="white",
            fg="black"
        )
        self.rps_label.grid(row=0, column=0, columnspan=3, pady=30)

        self.rps_outcome_label = tk.Label(
            self.rps_frame,
            font=("Arial", 16),
            bg="white",
            fg="black"
        )
        self.rps_outcome_label.grid(row=1, column=0, columnspan=3, pady=50)

        self.rock_btn = tk.Button(
            self.rps_frame,
            text="ROCK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=lambda: self.player_rps_choice("rock"),
            width=10
        )
        self.rock_btn.grid(row=2, column=0, padx=10, pady=30)

        self.paper_btn = tk.Button(
            self.rps_frame,
            text="PAPER",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=lambda: self.player_rps_choice("paper"),
            width=10
        )
        self.paper_btn.grid(row=2, column=1, padx=10, pady=30)

        self.scissors_btn = tk.Button(
            self.rps_frame,
            text="SCISSORS",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=lambda: self.player_rps_choice("scissors"),
            width=10
        )
        self.scissors_btn.grid(row=2, column=2, padx=10, pady=30)

    def player_rps_choice(self, choice):
        self.rps.rps_outcome(choice)

        if self.rps.setter == "tie":
            self.rps_outcome_label.config(
                text=f"The bot chose {self.rps.bot_rps}!\nIt's a tie! Try again."
            )
        else:
            self.rps_outcome_label.config(
                text=f"The bot chose {self.rps.bot_rps}!\nThe {self.rps.setter} starts!"
            )

            self.rock_btn.destroy()
            self.paper_btn.destroy()
            self.scissors_btn.destroy()
            self.cont_skate()

    def cont_skate(self):
        self.cont_btn = tk.Button(
            self.rps_frame,
            text="CONTINUE",
            font=("Arial", 25),
            bg="white",
            fg="black",
            command=self.skate_window
        )
        self.cont_btn.grid(row=2, column=0, columnspan=3, pady=20)

    def skate_window(self):
        self.rps_label.destroy()
        self.cont_btn.destroy()
        self.rps_frame.destroy()

        self.skate_frame = tk.Frame(
            self.window,
            bg="white"
        )
        self.skate_frame.pack()

        self.player_letters_label = tk.Label(
            self.skate_frame,
            text=f"PLAYER'S LETTERS\n{self.game.player_letters}",
            font=("Arial", 20),
            bg="white",
            fg="black"
        )
        self.player_letters_label.grid(row=0, column=0)

        self.bot_letters_label = tk.Label(
            self.skate_frame,
            text=f"BOT'S LETTERS\n{self.game.bot_letters}",
            font=("Arial", 20),
            bg="white",
            fg="black"
        )
        self.bot_letters_label.grid(row=0, column=2)

        self.gameplay_label = tk.Label(
            self.skate_frame,
            font=("Arial", 20),
            bg="white",
            fg="black"
        )
        self.gameplay_label.grid(row=1, column=0, columnspan=3, pady=80)

        self.tricks_list_label = tk.Label(
            self.skate_frame,
            text="ENTER A TRICK",
            font=("Arial", 16),
            bg="white",
            fg="black"
        )
        self.tricks_list_label.grid(row=2, column=0, columnspan=3)

        self.tricks_list = ttk.Combobox(
            self.skate_frame,
            state="readonly",
            values=self.game.tricks
        )
        self.tricks_list.grid(row=3, column=1, pady=20)

        self.submit_btn = tk.Button(
            self.skate_frame,
            text="SUBMIT",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.submit_trick,
            state=tk.DISABLED
        )
        self.submit_btn.grid(row=4, column=1)
        self.tricks_list.bind(
            "<<ComboboxSelected>>",
            lambda event: self.check_submit()
        )  # Allows the submit button to update after player selects a trick

        self.landed_btn = tk.Button(
            self.skate_frame,
            text="LANDED",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.game.player_landed,
            state=tk.DISABLED
        )
        self.landed_btn.grid(row=5, column=0, pady=50)

        self.bailed_btn = tk.Button(
            self.skate_frame,
            text="BAILED",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.game.player_bailed,
            state=tk.DISABLED
        )
        self.bailed_btn.grid(row=5, column=2, pady=50)

        if self.rps.setter == "player":
            self.game.player_sets()
        elif self.rps.setter == "bot":
            self.game.bot_sets()

    def submit_trick(self):
        self.get_player_trick = self.tricks_list.get()

        self.landed_btn.config(state=tk.NORMAL)
        self.bailed_btn.config(state=tk.NORMAL)
        self.submit_btn.config(state=tk.DISABLED)

    def check_submit(self):
        if self.game.current_setter == "player" and self.tricks_list.get() != "":
            self.submit_btn.config(state=tk.NORMAL)

    def end_screen(self, outcome):
        self.player_letters_label.destroy()
        self.bot_letters_label.destroy()
        self.tricks_list_label.destroy()
        self.tricks_list.destroy()
        self.submit_btn.destroy()
        self.landed_btn.destroy()
        self.bailed_btn.destroy()

        if outcome == "player_lost":
            self.gameplay_label.config(
                text="You have 5 letters. You lose!"
            )
        elif outcome == "bot_lost":
            self.gameplay_label.config(
                text="The bot has 5 letters. You win!"
            )
        elif outcome == "tie":
            self.gameplay_label.config(
                text="There are no available tricks left to set. It's a tie!"
            )

        self.new_game_label = tk.Label(
            self.skate_frame,
            text="Play again?\n***********************",
            font=("Arial", 20),
            bg="white",
            fg="black"
        )
        self.new_game_label.grid(row=2, column=0, columnspan=3)

        self.new_game_yes = tk.Button(
            self.skate_frame,
            text="YES",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.play_yes,
            width=10
        )
        self.new_game_yes.grid(row=3, column=0, pady=10)

        self.new_game_no = tk.Button(
            self.skate_frame,
            text="NO",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.play_no,
            width=10
        )
        self.new_game_no.grid(row=3, column=2, pady=10)

        self.back_main_menu = tk.Button(
            self.window,
            text="Main menu",
            font=("Arial", 16),
            bg="white",
            fg="black",
            command=self.clean_up_end,
            width=10
        )
        self.back_main_menu.pack(side=tk.BOTTOM, pady=50)

    def play_yes(self):
        self.skate_frame.destroy()
        self.back_main_menu.destroy()

        self.rps = RockPaperScissors()
        self.game = Game(self)

        self.rps_window()

    def play_no(self):
        print("THANK YOU FOR PLAYING!")
        self.window.destroy()

    def clean_up_end(self):
        self.back_main_menu.destroy()
        self.skate_frame.destroy()

        self.rps = RockPaperScissors()
        self.game = Game(self)

        self.main_menu()


class Game:
    LOM = ("landed", "bailed")
    WORD = "SKATE"

    TRICKS = [
        "ollie", "fakie ollie", "switch ollie", "nollie",
        "BS shuvit", "fakie BS shuvit", "switch BS shuvit", "nollie BS shuvit",
        "FS shuvit", "fakie FS shuvit", "switch FS shuvit", "nollie FS shuvit",
        "kickflip", "fakie kickflip", "switch kickflip", "nollie kickflip",
        "varial flip", "fakie varial flip", "switch varial flip", "nollie varial flip",
        "treflip", "fakie treflip", "switch treflip", "nollie treflip",
        "varial heelflip", "fakie varial heelflip", "switch varial heelflip", "nollie varial heelflip",
        "heelflip", "fakie heelflip", "switch heelflip", "nollie heelflip",
        "BS 360 shuvit", "fakie BS 360 shuvit", "switch BS 360 shuvit", "nollie BS 360 shuvit",
        "FS 360 shuvit", "fakie FS 360 shuvit", "switch FS 360 shuvit", "nollie FS 360 shuvit",
        "BS 540 shuvit", "fakie BS 540 shuvit", "switch BS 540 shuvit", "nollie BS 540 shuvit",
        "FS 540 shuvit", "fakie FS 540 shuvit", "switch FS 540 shuvit", "nollie FS 540 shuvit",
        "BS bigspin", "fakie BS bigspin", "switch BS bigspin", "nollie BS bigspin",
        "FS bigspin", "fakie FS bigspin", "switch FS bigspin", "nollie FS bigspin",
        "BS bigflip", "fakie BS bigflip", "switch BS bigflip", "nollie BS bigflip",
        "FS bigflip", "fakie FS bigflip", "switch FS bigflip", "nollie FS bigflip",
        "BS bigger spin", "fakie BS bigger spin", "switch BS bigger spin", "nollie BS bigger spin",
        "FS bigger spin", "fakie FS bigger spin", "switch FS bigger spin", "nollie FS bigger spin",
        "BS bigger flip", "fakie BS bigger flip", "switch BS bigger flip", "nollie BS bigger flip",
        "FS bigger flip", "fakie FS bigger flip", "switch FS bigger flip", "nollie FS bigger flip",
        "BS kickflip", "halfcab flip", "switch BS kickflip", "nollie BS kickflip",
        "FS kickflip", "fakie FS kickflip", "switch FS kickflip", "nollie FS kickflip",
        "hardflip", "fakie hardflip", "switch hardflip", "nollie hardflip",
        "inward heel", "fakie inward heel", "switch inward heel", "nollie inward heel",
        "impossible", "fakie impossible", "switch impossible", "nollie impossible",
        "front foot impossible", "fakie front foot impossible", "switch front foot impossible", "nollie front foot impossible",
        "dolphin flip", "fakie dolphin flip", "switch dolphin flip", "nollie dolphin flip",
        "laserflip", "fakie laserflip", "switch laserflip", "nollie laserflip",
        "FS 180", "fakie FS 180", "switch FS 180", "nollie FS 180",
        "BS 180", "halfcab", "switch BS 180", "nollie BS 180"
    ]

    def __init__(self, ui):
        self.ui = ui

        self.current_setter = None

        self.player_letters = []
        self.bot_letters = []

        self.tricks = self.TRICKS.copy()

    def player_sets(self):
        if len(self.player_letters) == 5 or len(self.bot_letters) == 5 or not self.tricks:
            self.game_over()
            return

        self.current_setter = "player"

        self.ui.tricks_list.set("")

        self.ui.submit_btn.config(state=tk.DISABLED)

        self.ui.landed_btn.config(state=tk.DISABLED)
        self.ui.bailed_btn.config(state=tk.DISABLED)

    def bot_sets(self):
        if len(self.player_letters) == 5 or len(self.bot_letters) == 5 or not self.tricks:
            self.game_over()
            return

        self.current_setter = "bot"

        self.get_bot_trick = random.choice(self.tricks)
        self.get_bot_lom = random.choice(self.LOM)

        self.ui.gameplay_label.config(
            text=f"The bot set {self.get_bot_trick}. The bot {self.get_bot_lom}!"
        )

        if self.get_bot_lom == "landed":
            self.ui.submit_btn.config(state=tk.DISABLED)

            self.tricks.remove(self.get_bot_trick)
            self.ui.tricks_list.config(values=self.tricks)

            self.player_defends()
        elif self.get_bot_lom == "bailed":
            self.current_setter = "player"
            self.player_sets()

    def player_defends(self):
        self.ui.landed_btn.config(state=tk.NORMAL)
        self.ui.bailed_btn.config(state=tk.NORMAL)

    def bot_defends(self):
        self.get_bot_lom = random.choice(self.LOM)

        self.ui.gameplay_label.config(
            text=f"The bot {self.get_bot_lom}!"
        )

        if self.get_bot_lom == "bailed":
            self.ui.landed_btn.config(state=tk.DISABLED)
            self.ui.bailed_btn.config(state=tk.DISABLED)

            self.bot_letters.append(self.WORD[len(self.bot_letters)])

            self.ui.bot_letters_label.config(
                text=f"BOT'S LETTERS\n{self.bot_letters}"
            )

        self.player_sets()

    def player_landed(self):
        if self.current_setter == "player":
            self.ui.tricks_list.set("")

            self.ui.submit_btn.config(state=tk.DISABLED)

            self.tricks.remove(self.ui.get_player_trick)
            self.ui.tricks_list.config(values=self.tricks)

            self.bot_defends()
        elif self.current_setter == "bot":
            self.ui.tricks_list.set("")

            self.bot_sets()

    def player_bailed(self):
        if self.current_setter == "player":
            self.ui.tricks_list.set("")

            self.current_setter = "bot"
            self.bot_sets()
        elif self.current_setter == "bot":
            self.player_letters.append(self.WORD[len(self.player_letters)])

            self.ui.player_letters_label.config(
                text=f"PLAYER'S LETTERS\n{self.player_letters}"
            )

            self.bot_sets()

    def game_over(self):
        if len(self.player_letters) == 5:
            self.ui.end_screen("player_lost")
        elif len(self.bot_letters) == 5:
            self.ui.end_screen("bot_lost")
        elif not self.tricks:
            self.ui.end_screen("tie")


app = UI()
app.window.mainloop()
