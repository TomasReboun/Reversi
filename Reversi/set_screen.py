# Modul obsahuje všechny instace třídy Button a funkci set_screen

from class_button import *

# tlačítka zobrazená na domovské obrazovce

B_title = Button((480,140),(210,40),"Blue", "Reversi",150,"White")
B_game_1 = Button((300,80), (300,200),"Blue", "Hra pro 1",70,"White", "GameMode1")
B_game_2 = Button((300,80), (300,300),"Blue", "Hra pro 2",70,"White", "GameMode2")
B_game_rules = Button((300,80), (300,400),"Blue", "Pravidla",70,"White", "Rules")
B_game_end = Button((300,80),(300,500),"Red", "Ukončit", 70,"White", "Quit")

home_screen_buttons = [B_title,B_game_1,B_game_2,B_game_rules,B_game_end]

# tlačítka zobrazená na obrazovce s pravidly

B_return = Button((200,60),(40,505),"Red","Zpět",50,"White", "Return")
B_rules_1 = Button((10,10),(445,30),"Cyan","Pravidla",50,"Black")
B_rules_2 = Button((10,10),(445,80),"Cyan","Reversi je hra pro dva hráče. Začíná černý, pak se střídají po tazích.",30,"Black")
B_rules_3 = Button((10,10),(445,120),"Cyan","Hráč, který je na tahu, obsadí volné (modré) pole tak, aby uzavřel (z obou stran)",30,"Black")
B_rules_4 = Button((10,10),(445,160),"Cyan","souvislou řadu soupeřových políček mezi svým novým a jiným vlastním políčkem.",30,"Black")
B_rules_5 = Button((10,10),(445,200),"Cyan","Uzavírat lze vodorovně, svisle i diagonálně.",30,"Black")
B_rules_6 = Button((10,10),(445,240),"Cyan","Všechna takto uzavřená políčka získává hráč na tahu.",30,"Black")
B_rules_7 = Button((10,10),(445,280),"Cyan","Pokud hráč nemá možný tah (neuzavře žádnou řadu) ztrácí tah.",30,"Black")
B_rules_8 = Button((10,10),(445,320),"Cyan","Hra končí, jakmile ani jeden hráč nemá možný tah.",30,"Black")
B_rules_9 = Button((10,10),(445,360),"Cyan","Vítězem je hráč, který má na konci více polí své barvy.",30,"Black")
B_rules_10 = Button((10,10),(445,400),"Cyan","Zobrazování možných tahů lze zapnout/vypnout tlačítkem Nápověda.",30,"Black")

rules_screen_buttons = [B_return,B_rules_1, B_rules_2, B_rules_3, B_rules_4, B_rules_5, B_rules_6, B_rules_7, B_rules_8, B_rules_9, B_rules_10]

# tlačítka zobrazená na herní obrazovce

B_title_2 = Button((200,60),(40,30),"Blue","Reversi",50,"White")
B_help = Button((200,60),(40,100),"Blue","Nápověda",40,"White", "Help")
B_score_title = Button((200,60),(40,170),"Blue","Score",40,"White")
B_score_color_white = Button((80,40),(70,240),"Cyan","Bílý:   ",40,"Black")
B_score_color_black = Button((80,40),(70,290),"Cyan","Černý:",40,"Black")
B_on_move_is = Button((200,60),(40,340),"Blue","Na tahu je",40,"White")

game_screen_buttons = [B_return, B_title_2, B_score_title,B_score_color_white, B_score_color_black, B_help, B_on_move_is]

# tlačítka pro volbu pořadí hráče a počítače

B_bot_1 = Button((200,60),(40,100),"Blue","Začíná hráč",40,"White", "Bot_White")
B_bot_2 = Button((200,60),(40,170),"Blue","Začíná bot ",40,"White", "Bot_Black")

bot_choose_buttons = [B_return, B_title_2, B_bot_1, B_bot_2]

# tlačítka informační (mění se v průběhu hry a zobrazuje je až GUI)

B_active_player_color = Button((200,40),(40,410),"Cyan", "",40,"Black")
B_active_player_name = Button((200,40),(40,455),"Cyan", "",40,"Black")
B_score_white = Button((40,40),(170,240),"Cyan", "", 40,"Black")
B_score_black = Button((40,40),(170,290),"Cyan", "", 40,"Black")
B_endgame = Button((200,60),(40,340),"Blue", "",40,"White")
B_end_state = Button((200,40),(40,410),"Cyan","",40,"Black")
B_winner_color = Button((200,40),(40,455),"Cyan","",40,"Black")

# funkce zobrazí zadaná tlačítka a vrátí ty, které mají další využití
def set_screen(buttons: list[Button]) -> list[Button]:
    screen.fill("Cyan")
    useful_buttons = []
    for button in buttons:
        button.show()
        if button.use:
            useful_buttons.append(button)
    return useful_buttons