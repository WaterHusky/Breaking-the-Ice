# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#f90808")
define a = Character ("Airplane Announcer", color = "#ffffff")
define p = Character ("Phone", color = "#5e0101")
define k = Character("Konrad", color = "#08f1f9")
define t = Character("Tai Zhou", color = "#93E9BE")


init:
    $ Physical = 0;
    $ Mental = 0;
    $ Emotional = 0;

# The game starts here.

label start:
        jump touchdown
    return
