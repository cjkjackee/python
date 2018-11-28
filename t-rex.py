import pyautogui as gui
import msvcrt
import snp

def getOther(pic):
    return snp.locateOnScreen(pic, region=(pos[0]+pos[2]+50, pos[1]-20, 130, pos[3]+10))

def getThing(pic):
    thing = snp.locateOnScreen(pic, threshold=0.6, region=(pos[0]+pos[2]+20, pos[1]-20, 100, pos[3]+10))
    return thing

# find dino position
pos = snp.locateOnScreen('dino.png')
if (pos == None):
    print('dion not found')
    exit()
gui.click(pos[0]+pos[2]+150,pos[1]-20)

# start game
gui.press('space')
while True:
    if snp.locateOnScreen('over.png',region=(pos[0]+pos[2]+150, pos[1]-50, 200, 40)):
        break
    if getThing('bird.png') or getThing('cactus.png') or getThing('cactus_s.png'):
        gui.press('space')
        if getOther('bird.png') or getOther('cactus.png') or getOther('cactus_s.png'):
            gui.press('down',3)
            gui.press('space')
            print('next')

gui.press('f5')
gui.hotkey('alt','tab')