import pyautogui as pg 
 
while True:
     a = pg.confirm("Are you a piece of shit?" ,buttons=['Yes', 'No'])
     if a == 'Yes':
         break
