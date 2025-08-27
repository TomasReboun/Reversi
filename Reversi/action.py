# Modul obsahuje funkci action

from class_GUI import *

# po stisknutí učtitého tlačítka dostane klíčové slovo
# podle kterého provede příslušnou akci
# a vrátí seznam nově použitelných tlačítek
def action(keyword) -> list[Button]:
    global gui
    match keyword:
        case "GameMode1":
            return set_screen(bot_choose_buttons)
        case "GameMode2":
            gui = GUI()
            return gui.get_buttons()
        case "Bot_White":
            gui = GUI("White")
            return gui.get_buttons()
        case "Bot_Black":
            gui = GUI("Black")
            return gui.get_buttons()
        case "Rules":
            return set_screen(rules_screen_buttons)
        case "Return":
            return set_screen(home_screen_buttons)
        case "Help":
            gui.change_help()
            return gui.get_buttons()
        case _:
            if not gui.GameBoard.bot_active:
                gui.move(keyword)
                return gui.get_buttons()