# Reversi

## Zadání projektu

Zadání zápočtového programu pro kurz Programování 2 MFF UK.
Program vytváří počítačovou verzi deskové hry Reversi
(též známé pod názvem Othello).

## Pravidla hry

Reversi je hra pro dva hráče. Začíná černý, pak se střídají po tazích.
Cílem je uzavřít co možná nejvíce soupeřových políček ze dvou protilehlých stran a otočit je tak na svou barvu.
Uzavírat lze vodorovně, svisle i diagonálně.
Hraje se na desce s 8x8 políčky, na začátku má uprostřed desky každý hráč 2 políčka své barvy.
Hráč, který je na tahu, obsadí volné (modré) pole tak, aby uzavřel (z obou stran)
souvislou řadu soupeřových políček mezi svým novým a jiným vlastním políčkem.
Všechna takto uzavřená políčka získává hráč na tahu.
Pokud hráč nemá možný tah (neuzavře žádnou řadu) ztrácí tah.
Hra končí, jakmile ani jeden hráč nemá možný tah.
Vítězem je hráč, který má na konci více polí své barvy.

# Uživatelská dokumentace 

## Spuštění programu

Před spuštěním je třeba nainstalovat Python a následně pygame pomocí příkazu `pip install pygame`.
Hra se spustí ve složce `main.py` v adresáři projektu.

## Grafické uživatelské rozhraní

Celý program ovládá uživatel pomocí myši. Program na obrazovku vykresluje tlačíska s různými funkcemi,
které uživatel spustí kliknutím myši na dané tlačítko.
Po spuštění se zobrazí domovská obrazovka.

## Domovská obrazovka

Domovská obrazovka obsahuje následující tlačítka:
1) tlačítko "Hra pro 1" spustí hru proti počítači.
2) tlačítko "Hra pro 2" spustí lokální hru proti druhému hráči.
3) tlačítko "Pravidla" zobrazí obrazovku s pravidly.
4) tlačítko "Ukončit" skončí celý program

Všechny ostatní obrazovky obsahují tlačítko "Zpět", které po kliknutí
vrátí uživatele zpět na domovskou obrazovku. Pokud se na "Zpět" klikne během hry,
tah se hra přeruší.

## Hra proti počítači

Po spuštění hry proti počítači se před samotnou hrou zobrazí dvojice tlačítek:
1) tlačítko "Začíná hráč" zajistí, že první tah ve hře provede hráč.
2) tlačítko "Začíná bot" zajistí, že první tah ve hře provede počítač.

Po zvolení režimu se spustí hra.

## Herní obrazovka

Herní obrazovka je rozdělena na dvě části:
1) vlevo je informační panel
2) vpravo je samotná herní deska

Informační panel obsahuje:
1) tlačítko "Nápověda", které zapíná/vypíná nápovědu.
    Pokud je tato nápověda zapnutá, tak se na políčkách, na které je možno
    táhnout, zobrazují číslo.
    Tyto čísla určují kolik soupeřových políček hráč při daném tahu může získat.
    Nápověda je na začátku každé hry automaticky vypnuta.
2) informace o současném score, to je kolik políček své barvy má v daný moment
    kažký z hráčů.
3) informace o aktivním hráči, to je barva hráče na tahu
    a jestli to je první nebo druhý hráč anebo počítač.
4) tlačítko "Zpět".

Herní deska obsahuje mřížku 8x8, ve které jsou políčka.
Pokud je na tahu hráč, tak po kliknutí na políčko provede tah, pakliže je to 
v souladu s pravidly hry. Jestliže není, nestane se nic.
Pokud je na tahu počítač, tak po krátkém přemýšlení provede automaticky svůj tah.

Po skončení hry se na informačním panelu zobrazí informace o konečném stavu hry
a o případném vítězi.

# Technická dokumentace

Kód je strukturován do 6 modulů, jejichž funkce a obsah jsou popsány níže.
Program navíc využívá built-in modul random a externí knihovnu Pygame.

## Modul class_button

Modul class_button importuje a zároveň inicializuje knihovnu Pygame,
vytváří základní herní display a definuje třídu Button.

Třída Button vytváří tlačítka, která se zobrazují na herním display.

Parametry initoru třídy Button jsou:
- size: dvojice čísel určuje rozměry tlačítka
- pos: dvojice čísel určuje umístění tlačítka na obrazovce
- color: string určuje barvu tlačítka
- text: string určuje text uvnitř tlačítka
- text_size: číslo určuje velikost svého textu
- text_color: string určuje barvu svého textu
- use (nepovinný): klíčové slovo určující co se stane po kliknutí na tlačítko

Metody třídy Button jsou:
- render_text(): 
    Metoda do středu daného tlačítka připojí příslušný text
- show():
    Metoda vykreslí na obrazovku dané tlačítko a jeho text, pokud nějaký má
- update(text):
    Metoda změní text tlačítka a zobrazí ho
- is_clicked(mouse_pos):
    Metoda vrátí True, pokud uživatel klikl myší na dané tlačítko

## Modul set_screen

Modul importuje třídu Button a obsahuje všechny její instance použité v programu.
Tyto instance jsou rozděleny do několika skupin:
- home_screen_buttons jsou tlačítka zobrazená na domovské obrazovce
- rules_screen_buttons jsou tlačítka zobrazená na obrazovce s pravidly
- game_screen_buttons jsou tlačítka zobrazená na herní obrazovce
- bot_choose_buttons jsou tlačítka pro volbu pořadí hráče a počítače
- ostatní jsou # tlačítka informační (mění se v průběhu hry a zobrazuje je až GUI)

Modul navíc obsahuje funkci set_screen, která aktualizuje obrazovku, 
zobrazí zadaná tlačítka a vrátí ty, které mají další využití.

## Modul class_gameboard

Modul class_gameboard importuje funkci random.choice,
obsahuje seznam směrů pohybu po herní desce
a definuje třídu GameBoard, která řídí logiku hry.

Třída Gameboard při inicializaci vytvoří desku (grid) s počátečním rozestavením pro hru Reversi.
Parametrem initoru je barva za kterou hraje počítač.
Pokud počítač nehraje, pak se jedná o prázdný string.
Další atributy třídy jsou:
- active_player: určuje barvu hráče na tahu; na začátku černý
- bot_active: určuje jestli počítač hledá nejlepší tah

Metody třídy GameBoard jsou:
- opponent():
    Metoda vrací barvu soupeře
- score():
    Metoda vrací počet políček bílého/černého hráče
- end_state():
    Metoda určí konečný stav hry a případného výtěze
- value_in_dir():
    Argumenty jsou políčko na desce a směr.
    Metoda určí kolik soupeřových políček v daném směru hráč získá
- value_of_square():
    Argumentem je políčko na desce
    Metoda vrací celkový počet dobytých soupeřových políček po tahu hráče
- legal_move_2_value():
    Metoda vrací slovník možných tahů pro danou pozici a hodnoty tahů
- make_move():
    Argumentem je políčko na desce
    Metoda obsadí zadané políčko a všechny jím ohraničená soupeřova políčka
    Vrátí seznam seznam otočených políček
- undo_move():
    Argumentem je seznam otočených políček
    Metoda zruší důsledky metody make_move
- evaluate():
    Argumentem je barva, za kterou hraje počítač
    Metoda ohodnotí současnou pozici podle počítačové strategie
- minimax_core():
    Pomocná funkce - jádro metody minimax
- minimax():
    Povinné argumenty jsou tah, který chceme provést, a barva, za kterou hraje počítač
    Metoda vrátí cenu zadaného tahu při optimální hře
- best_move():
    Metoda vrátí nejlepší tah v současné pozici
    Pokud je více stejně dobrých tahů, volí náhodně s využitím random.choice

## Modul class_GUI

Modul importuje třídu GameBoard a obsah modulu set_screen.
Modul dále definuje třídu GUI, která propojuje třídu GameBoard s uživatelským rozhraním.

Třída GUI při inicializaci vytvoří instanci třídy Gameboard a svoji vlasní mřížku s instancemi třídy Button,
které budou zobrazovat průběh hry.

Další atributy třídy GUI jsou:
- self.help: určuje, zda se má zobrazovat nápověda,
    na začátku každé automaticky vypnuto
- self.legal_moves_2_value: pomatuje si možné tahy a jejich hodnoty,
    údaje jsou uloženy do proměnné, aby se nemusela nadbytečně volat metoda GameBoard.legal_moves_2_value()

Pokud má první tah hry vykonat počítač, třída GUI ho sama provede během inicializace.

Metody třídy GUI:
- show_board():
    Metoda zobrazí všechna políčka na herní desce
- show_help():
    Metoda zobrazí hodnoty možných tahů
- hide_help():
    Metoda skryje hodnoty možných tahů
- change_help():
    Metoda změní stav nápovědy možných tahů
- show_active_player():
    Metoda zobrazí informaci, který hráč je na tahu
- show_score():
    Metoda zobrazí počet políček bílého/černého hráče
- show_end_state():
    Metoda zobrazí stav na konci hry
- get_buttons():
    Metoda vrací seznam tlačítek, na které může uživatel kliknout během hry
- animate():
    Metoda animuje přebarvení zabraných políček
- show_move():
    Metoda provede a zároveň zobrazí tah hráče
- bot_move():
    Metoda provede a zobrazí tah počítače
- move():
    Metoda provádí tahy hráče a případně počítače
    
## Modul action

Modul action importuje obsah modulu class_GUI a definuje funkci action.

Funkce action po stisknutí učtitého tlačítka dostane klíčové slovo, podle kterého
provede příslušnou akci a vrátí seznam nově použitelných tlačítek

## Modul main

Hlavní modul obsahuje smyčku, ve které běží celý program
Importuje obsah modulu action a zobrazí domovskou obrazovku.
Hlavní smyčka kontroluje činnost uživatele, pokud klikne na nějaké tlačítko,
tak předá jeho klíčové slovo funkci action.

Spuštěním tohoto modulu se zapne hra.