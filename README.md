# SimpleGUI
To use simpleGUI in pycharm or other idle:
* Open the command prompt
* Enter and run the following:
  * `python -m pip install --upgrade pip`
  * `python -m tkinter`
  * `pip install pygame`
  * `pip install SimpleGUICS2Pygame`

These install both tkinter (a prerqusite for SimpleGUICS2Pygame)
 and SimpleGUICS2Pygame (a simplegui emulator package) 
 
When using SimpleGUICS2Pygame (simplegui) you want to import it as:


    try:

        import simplegui

    except ImportError:
    
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    

# Requirements
## SimpleGui
See above section about simplegui
## gspread
gspread is used to access a google spreadsheet, in google drive. 
This spreadsheet is the data for the scoreboard. The google account is:

    username: pixel.game.database@gmail.com

    password: Pa$$w0rd12345

To install use cmd to run: 
* `pip install gspread`
* `pip install --upgrade oauth2client`
