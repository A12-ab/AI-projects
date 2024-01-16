import importlib
import tkinter as tk
from tkinter import ttk

class GameSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI PROJECT")

        # Set a custom color scheme
        self.root.configure(bg="#2D3250")  # Set background color


        # Create a style for buttons
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", background="#11009E", foreground="#11235A")

        # Main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=120, pady=120)

        # Header label
        self.header_label = ttk.Label(self.main_frame, text="Select a game to play", font=("Helvetica", 16), foreground="#7D0A0A")
        self.header_label.pack(pady=10)
 
        # Game buttons
        self.button_game1 = ttk.Button(self.main_frame, text="pong game", command=lambda: self.run_game('main.py'))
        self.button_game1.pack(pady=10)

        self.button_game2 = ttk.Button(self.main_frame, text="Tic Tac Toe", command=lambda: self.run_game('tic_tac_toe.py'))
        self.button_game2.pack(pady=10)

        # Quit button
        self.quit_button = ttk.Button(self.main_frame, text="Quit", command=root.destroy)
        self.quit_button.pack(pady=10)

    def run_game(self, game_module):
        try:
            game = importlib.import_module(game_module)
            game.run_game_logic()
        except ImportError:
            print(f"Error: Module {game_module} not found.")
        except AttributeError:
            print(f"Error: Module {game_module} does not have a 'run_game_logic' function.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameSelectorApp(root)
    root.mainloop()
