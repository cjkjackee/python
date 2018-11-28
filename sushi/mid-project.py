import pyautogui as gui
import snp
import time

nori = 5
rice = 10
salmon = 10
roe = 10
eel = 5
shrimp = 5
menu = ['sushi/onigiri.png', 'sushi/roe_maki.png']
customer = [0,0,0,0,0]

def find_ingre(pic, num=1):
    print(pic)
    temp = snp.locateCenterOnScreen(pic, region=(ingredient_x, ingredient_y, 150, 460))
    print(temp)
    gui.click(temp, clicks=num, interval=0.5, pause=0.5, _pause=True)

def click_center(pic):
    temp = snp.locateCenterOnScreen(pic)
    gui.click(temp[0],temp[1])

def order(customer):
    gui.moveTo(customer, customer_y)
    temp = None
    while temp == None:
        for item in menu:
            temp = snp.locateCenterOnScreen(item, region=(customer, customer_y, 50, 50))
            if(temp != None):
                return menu.index(item)+1

def phone():
    if (rice < 7):
        gui.click(phone)
    if (nori < 5):
        gui.click(phone)
    if (roe < 8):
        gui.click(phone)
    if (salmon < 5):
        gui.click(phone)
    if (shrimp < 5):
        gui.click(phone)
    if (eel < 5):
        gui.click(phone)

def sushi(recipes):
    global nori, rice, salmon, roe, eel, shrimp
    if(recipes == 1):
        find_ingre('sushi/rice.png',num=2)
        find_ingre('sushi/nori.png')
        rice -= 2
        nori -= 1
    elif(recipes == 2):
        find_ingre('sushi/rice.png')
        find_ingre('sushi/roe.png')
        rice -= 1
        roe -= 1
    elif(recipes == 3):
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        find_ingre('sushi/roe.png',num=2)
        rice -= 1
        nori -= 1
        roe -= 2
    elif(recipes == 4):
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        find_ingre('sushi/salmon.png')
        rice -= 1
        nori -= 1
        salmon -= 1
    elif(recipes == 5):
        find_ingre('sushi/rice.png')
        find_ingre('sushi/shrimp.png', num=2)
        rice -= 1
        shrimp -= 2
    elif(recipes == 6):
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        find_ingre('sushi/eel.png',num=2)
        rice -= 1
        nori -= 1
        eel -= 2

    gui.click(sushi_done_x, sushi_done_y, pause=2, _pause=True)
    

# enter game 
click_center('sushi/play.png')
time.sleep(0.2)
click_center('sushi/go.png')
time.sleep(0.2)

# init position
print('calculating position')
top = snp.locateOnScreen('sushi/music.png')
phone = snp.locateCenterOnScreen('sushi/phone.png')
ingredient_x = top[0] + 60
ingredient_y = top[1] + 330
sushi_done_x = top[0] + 270
sushi_done_y = top[1] + 395
# customer region: weight = 110, height = 220
customer_y = top[1] + 40
customer_1 = top[0] + 60
customer_2 = top[0] + 180
customer_3 = top[0] + 310
customer_4 = top[0] + 430
customer_5 = top[0] + 550

################   main:  start game     #####################
click_center('sushi/start_game.png')
print('get all 5 people orders')
customer[0] = order(customer_1)
customer[1] = order(customer_2)
customer[2] = order(customer_3)
customer[3] = order(customer_4)
customer[4] = order(customer_5)

for recipe in customer:
    sushi(recipe)
