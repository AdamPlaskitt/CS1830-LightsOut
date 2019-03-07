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
  * `pip install pygame`
  * `pip install SimpleGUICS2Pygame`
  * `pip install PyAutoGUI`
  
To use tkinter, which I think is need but not 100% certain, I now have a copy of it on a memory stick and can give it 
to those who need it. It should come standard with python 3 onwards, to check it is there navigate to 
`C:\Users\Adam Plaskitt\AppData\Local\Programs\Python\Python37-32\Lib` for windows users, and check that a file called 
tkinter exists. As stated above I have copied this file to a memory stick and can give it to anyone who needs it.

pygame is installed as a prerequisite for SimpleGUICS2Pygame, and for the use of pygame.mouse.get_pos(), to get 
the position of the mouse.

These install both PyAutoGUI (a mouse and keyboard handler) and SimpleGUICS2Pygame (a simplegui emulator package) 
 
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