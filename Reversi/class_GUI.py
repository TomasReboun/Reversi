# Modul definuje třídu GUI, která propojuje
# třídu GameBoard s uživatelským rozhraním

from class_gameboard import GameBoard
from set_screen import *

class GUI:
    # Třída GUI vytvoří herní desku
    def __init__(self, bot: str = ""):
        set_screen(game_screen_buttons)

        self.GameBoard = GameBoard(bot)
        self.grid = [[Button((64,64),(330 + col*68,30 + row*68),self.GameBoard.grid[row][col],"",30,"White",use = (row,col)) for col in range(8)] for row in range(8)]
        self.legal_moves_2_value = self.GameBoard.legal_moves_2_value()
        self.help = False

        self.show_board()
        self.show_active_player()
        self.show_score()

        if self.GameBoard.bot == "Black":
            self.show_move(self.GameBoard.best_move())

    # Metoda zobrazí všechna políčka na herní desce
    def show_board(self) -> None:
        for i in range(8):
            for j in range(8):
                self.grid[i][j].show()

    # Metoda zobrazí hodnoty možných tahů
    def show_help(self) -> None:
        for square, value in self.legal_moves_2_value.items():
            s1, s2 = square
            self.grid[s1][s2].update(str(value))

    # Metoda skryje hodnoty možných tahů
    def hide_help(self) -> None:
        for square in self.legal_moves_2_value:
            s1, s2 = square
            self.grid[s1][s2].update("")

    # Metoda změní stav nápovědy možných tahů
    def change_help(self) -> None:
        self.help = not self.help
        if self.help: self.show_help()
        else: self.hide_help()
    
    # Metoda zobrazí informaci, který hráč je na tahu
    def show_active_player(self) -> None:
        color = "Bílý" if self.GameBoard.active_player == "White" else "Černý"
        B_active_player_color.update(color)
        if not self.GameBoard.bot:
            name = "(Hráč 2)" if self.GameBoard.active_player == "White" else "(Hráč 1)"
        else:
            name = "(Počítač)" if self.GameBoard.active_player == self.GameBoard.bot else "(Hráč)"
        B_active_player_name.update(name)

    # Metoda zobrazí počet políček bílého/černého hráče
    def show_score(self) -> None:
        w,b = self.GameBoard.score()
        B_score_white.update(str(w))
        B_score_black.update(str(b))

    # Metoda zobrazí stav na konci hry
    def show_end_state(self) -> None:
        state, winner = self.GameBoard.end_state()
        B_endgame.update("Hra skončila")
        B_end_state.update(str(state))
        B_winner_color.update(str(winner))

    # Metoda vrací seznam tlačítek, na které může uživatel kliknout během hry
    def get_buttons(self) -> list[Button]:
        buttons = [B_return, B_help]
        for x,y in self.legal_moves_2_value:
            buttons.append(self.grid[x][y])
        return buttons

    # Metoda animuje přebarvení zabraných políček
    def animate(self, active_player: str, squares: list) -> None:
        speed = 0.4
        r,g,b = 255, 0, 0
        while b <= 255 and r >= 0:
            color = (r,g,b)
            for s1,s2 in squares:
                self.grid[s1][s2].color = color
                self.grid[s1][s2].show()
            pygame.display.flip()
            if active_player == "White":
                b += speed
                g += speed
            else:
                r -= speed

    # Metoda provede a zároveň zobrazí tah hráče
    def show_move(self, squere: tuple[int, int]) -> None:
        self.hide_help()
        active_player = self.GameBoard.active_player
        flipped = self.GameBoard.make_move(squere)
        self.animate(active_player, flipped)

        self.legal_moves_2_value = self.GameBoard.legal_moves_2_value()
        self.show_active_player()
        self.show_score()
        if self.help:
            self.show_help()

        if not self.legal_moves_2_value:
            self.GameBoard.active_player = self.GameBoard.opponent()
            self.legal_moves_2_value = self.GameBoard.legal_moves_2_value()
            if not self.legal_moves_2_value:
                self.show_end_state() # ukončení hry
            else:
                self.show_active_player() # přeskočení tahu
                if self.help:
                    self.show_help()
    
    # Metoda provede a zobrazí tah počítače
    def bot_move(self):
        self.hide_help()
        pygame.display.flip()
        bot_move = self.GameBoard.best_move()
        if bot_move:
            self.show_move(bot_move)
        if self.help:
            self.show_help()

    # Metoda provádí tahy hráče a případně počítače
    def move(self, squere: tuple[int, int]) -> None:
        self.show_move(squere)
        while self.GameBoard.bot == self.GameBoard.active_player and self.legal_moves_2_value:
            self.bot_move()
