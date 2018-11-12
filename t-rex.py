import pyautogui as gui
import time
import msvcrt
import snp

def drop():
    gui.press('down')

def getThing(pic):
    thing = snp.locateOnScreen(pic, threshold=0.7, region=(pos[0]+pos[2]+50, pos[1]-20, 70, pos[3]+10))
    if thing != None:
        print(thing[0],thing[1])
        return True

# find dino position
pos = snp.locateOnScreen('dino.png')
gui.click(pos[0]+pos[2]+50,pos[1]-20)
print(pos[0]+pos[2]+20, pos[1]-20)
start = time.time()

# start game
gui.press('space')
while True:
    if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
        break
    if getThing('bird.png') or getThing('cactus.png') or getThing('cactus_s.png'):
        gui.press('space')