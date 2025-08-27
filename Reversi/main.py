# Hlavní modul obsahuje smyčku, ve které běží celý program

from action import *

# Nastavení domovské obrazovky
buttons = set_screen(home_screen_buttons)

# Hlavní smyčka
running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for button in buttons:
                if button.is_clicked(pos):
                    if button.use == "Quit": running = False
                    else: buttons = action(button.use)

     pygame.display.flip()
pygame.quit()