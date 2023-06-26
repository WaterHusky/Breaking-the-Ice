# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#f90808", image = "mugger")
define a = Character ("Airplane Announcer", color = "#ffffff" , image = "airplane announcer")
define p = Character ("Phone", color = "#5e0101" , image = "phone")
define k = Character("Konrad", color = "#08f1f9" , image = "konrad")
define t = Character("Tai Zhou", color = "#93E9BE" , image = "tai zhou")
define j = Character("Johnny", color = "#8303fb", image = "johnny")



init:
    $ Physical = 0;
    $ Mental = 0;
    $ Emotional = 0;

# The game starts here.

label start:
    jump touchdown
    return
