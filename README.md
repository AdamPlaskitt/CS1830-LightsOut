# LightsOut 🔦
LightsOut is a game with a simple premise, survive the dark. 
In a world devoid of light monsters evolved to thrive in the dark and now they are hunting you!
How long can you survive?

Navigate though this new world with your wits and trusty flash light, 
but be careful of what you might find.  

## Requirements
### SimpleGUI
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

```python
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
```
  
### gspread
To install use cmd to run: 
* `pip install gspread`
* `pip install --upgrade oauth2client`

gspread is used to access a google spreadsheet, in google drive. 
This spreadsheet is the data for the scoreboard. The google account is:

    username: pixel.game.database@gmail.com

    password: Pa$$w0rd12345

gspread is used to provide access to the online scoreboard, if this is inaccessible due
to any reason *(eg. gspread isn't install properly or there is a connection issue)* a local scoreboard
 will be used instead.