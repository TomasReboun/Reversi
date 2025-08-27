# Modul obsahuje třídu Gameboard, která řídí logiku hru

from random import choice

directions = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1))

class GameBoard:
    # Třída GameBoard vytvoří mřížku pro herní políčka
    def __init__(self, bot_color: str):
        self.grid = [["Blue"]*8 for _ in range(8)]
        self.grid[3][3] = self.grid[4][4] = "White"
        self.grid[3][4] = self.grid[4][3] = "Black"
        self.active_player = "Black"
        self.bot = bot_color
        self.bot_active = False
    
    # Metoda vrací barvu soupeře
    def opponent(self) -> str:
        return "White" if self.active_player == "Black" else "Black"
    
    # Metoda vrací počet políček bílého/černého hráče
    def score(self) -> tuple[int, int]:
        white = sum(row.count("White") for row in self.grid)
        black = sum(row.count("Black") for row in self.grid)
        return white, black
    
    # Metoda určí konečný stav hry a případného výtěze
    def end_state(self) -> tuple[str, str]:
        w,b = self.score()
        if w == b: return "Remíza",""
        if w > b: return "Zvítězil", "Bílý"
        return "Zvítězil", "Černý"
      
    # Metoda určí kolik soupeřových políček v daném směru hráč získá
    def value_in_dir(self, actual_square: tuple[int, int], dir: tuple[int, int], dir_value: int = 0) -> int:
        new0 = actual_square[0] + dir[0]
        new1 = actual_square[1] + dir[1]
        if new0 in range(8) and new1 in range(8):
            if self.grid[new0][new1] == "Blue": return 0
            if self.grid[new0][new1] == self.active_player: return dir_value
            return self.value_in_dir((new0, new1), dir, dir_value + 1)
        return 0
    
    # Metoda vrací celkový počet dobytých soupeřových políček po tahu hráče
    def value_of_square(self, square: tuple[int, int]) -> int:
        return sum(self.value_in_dir(square, dir) for dir in directions)

    # Metoda vrací slovník možných tahů pro danou pozici a hodnoty tahů
    def legal_moves_2_value(self) -> dict[tuple[int, int], int]:
        moves_2_value = {}
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == "Blue":
                    value = self.value_of_square((i,j))
                    if value:
                        moves_2_value[(i,j)] = value
        return moves_2_value
    
    # Metoda obsadí zadané políčko a všechny jím ohraničená soupeřova políčka a vrátí jejich seznam
    def make_move(self, square: tuple[int,int]) -> list[tuple[int,int]]:
        flipped = [square]
        self.grid[square[0]][square[1]] = self.active_player
        for dir in directions:
            actual_square = square
            for _ in range(self.value_in_dir(square, dir)):
                new0 = actual_square[0] + dir[0]
                new1 = actual_square[1] + dir[1]
                self.grid[new0][new1] = self.active_player
                actual_square = (new0, new1)
                flipped.append(actual_square)
        self.active_player = self.opponent()
        return flipped
    
    # Metoda zruší důsledky metody make_move
    def undo_move(self, flipped: list[tuple[int,int]], mover: str) -> None:
        s1, s2 = flipped[0]
        self.grid[s1][s2] = "Blue"
        opponent = "White" if mover == "Black" else "Black"
        for s1, s2 in flipped[1:]:
            self.grid[s1][s2] = opponent
        self.active_player = mover
    
    # Metoda ohodnotí současnou pozici podle počítačové strategie
    def evaluate(self, bot_color: str) -> int:
        square_values = [
            [100,-20,10,5,5,10,-20,100],
            [-20,-50,-2,-2,-2,-2,-50,-20],
            [10,-2,0,0,0,0,-2,10],
            [5,-2,0,0,0,0,-2,5],
            [5,-2,0,0,0,0,-2,5],
            [10,-2,0,0,0,0,-2,10],
            [-20,-50,-2,-2,-2,-2,-50,-20],
            [100,-20,10,5,5,10,-20,100]]
        value = 0
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == bot_color:
                    value += square_values[i][j]
                elif self.grid[i][j] != "Blue":
                    value -= square_values[i][j]
        return value
    
    # Pomocná funkce - jádro metody minimax
    def minimax_core(self, bot_color:str, depth:int, alfa, beta) -> int:
        func = max if self.active_player == bot_color else min
        value = -float("inf") if func == max else float("inf")

        for move in self.legal_moves_2_value():
            new_value = self.minimax(move, bot_color,depth+1, alfa, beta)
            value = func(value, new_value)
            # alfa-beta ořezávání
            if func == max:
                alfa = max(alfa, value)
            else:
                beta = min(beta, value)
            if beta <= alfa:
                break
        return value

    # Metoda vrátí cenu zadaného tahu při optimální hře
    def minimax(self, move, bot_color:str, depth: int = 0, alfa = -float("inf"), beta = float("inf")) -> int:
        mover = self.active_player
        flipped = self.make_move(move)
        # dosažena maximální hloubka
        if depth == 4:
            value = self.evaluate(bot_color)
            self.undo_move(flipped, mover)
            return value
        # aktuální hráč nemá tahy
        if not self.legal_moves_2_value():
            self.active_player = self.opponent() # přeskočení tahu hráče
            if not self.legal_moves_2_value(): # konec hry
                state, winner = self.end_state()
                value = 0
                if state != "Remíza":
                    winner_color = "White" if winner == "Bílý" else "Black"
                    value = 1000 if winner_color == bot_color else -1000
                self.undo_move(flipped, mover)
                return value
        # jinak
        value = self.minimax_core(bot_color, depth, alfa, beta)
        self.undo_move(flipped, mover)
        return value

    # Metoda vrátí nejlepší tah v současné pozici
    # Pokud je více stejně dobrých tahů, volí náhodně
    def best_move(self) -> tuple[int, int]:
        self.bot_active = True
        best_value = -float("inf")
        best_moves = []
        for move in self.legal_moves_2_value():
            new_value = self.minimax(move, self.bot)
            if new_value > best_value:
                best_value = new_value
                best_moves = [move]
            elif new_value == best_value:
                best_moves.append(move)
        self.bot_active = False
        return choice(best_moves)