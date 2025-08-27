# Modul inicializuje knihovnu pygame a tvoří třídu Button

import pygame

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Reversi")



class Button:
    # Třída Button vytvoří tlačítko s danou velikostí, pozicí a barvou
    def __init__(self, size, pos, color, text, text_size, text_color, use = None):
        self.rect = pygame.Rect(*pos, *size)
        self.color = color
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.use = use

        if text: self.render_text()
    
    # Metoda do středu daného tlačítka připojí příslušný text
    def render_text(self) -> None:
        font = pygame.font.Font(None,self.text_size)
        self.text_surface = font.render(self.text, True, self.text_color)
        self.text_pos = self.text_surface.get_rect(center=self.rect.center)
    
    # Metoda vykreslí na obrazovku dané tlačítko a jeho text, pokud nějaký má
    def show(self) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text:
            screen.blit(self.text_surface, self.text_pos)
    
    # Metoda změní text tlačítka a zobrazí ho
    def update(self, text) -> None:
        self.text = text
        self.render_text()
        self.show()

    # Metoda vrátí True, pokud uživatel klikl myší na dané tlačítko
    def is_clicked(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos)