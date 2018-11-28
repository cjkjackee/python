import pyautogui as gui
import snp
import time

nori = 5
rice = 10
salmon = 10
roe = 10
eel = 5
shrimp = 5
menu = ['sushi/onigiri.png', 'sushi/roe_maki.png', 'sushi/gunkan_maki.png', 'sushi/sake_roll.png', 'sushi/unagi_nigiri.png', 'sushi/ebi_nigiri.png']
customer = [0,0,0,0,0]

def find_ingre(pic, num=1):
    temp = snp.locateCenterOnScreen(pic, region=(ingredient_x, ingredient_y, 200, 460))
    gui.click(temp, clicks=num, interval=0.1, pause=0.1, _pause=True)

def click_center(pic):
    temp = snp.locateCenterOnScreen(pic)
    gui.click(temp[0],temp[1])

def order(customer):
    gui.moveTo(customer, customer_y)
    temp = None
    while temp == None:
        for item in menu:
            temp = snp.locateCenterOnScreen(item, region=(customer, customer_y, 100, 100))
            if(temp != None):
                return menu.index(item)+1

def empty_dishes():
    temp = snp.locateAllOnScreen('sushi/empty.png')
    for item in temp:
        gui.click(item[0]+item[2]/2, item[1]+item[3]/2)

def buy_ingre():
    global rice, nori, roe, salmon, shrimp, eel

    if (rice < 7):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_rice.png')
        gui.click(temp)
        gui.click(temp)
        gui.click(temp)
        rice += 10
    if (nori < 5):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        click_center('sushi/phone_nori.png')
        gui.click(temp[0], temp[1]+20)
        nori += 10
    if (roe < 6):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        click_center('sushi/phone_roe.png')
        gui.click(temp[0], temp[1]+20)
        roe += 10 
    if (salmon < 4):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        click_center('sushi/phone_salmon.png')
        gui.click(temp[0], temp[1]+20)
        salmon += 5
    if (shrimp < 4):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        click_center('sushi/phone_shrimp.png')
        gui.click(temp[0], temp[1]+20)
        shrimp += 5
    if (eel < 4):
        gui.click(phone, pause=0.2, _pause=True)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        click_center('sushi/phone_eel.png')
        gui.click(temp[0], temp[1]+20)
        eel += 5


def sushi(recipes):
    print('sushi number {}',recipes)
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
        find_ingre('sushi/salmon.png')
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
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
ingredient_x = top[0] + 20
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

while True:
    print('get all 5 people orders')
    customer[0] = order(customer_1)
    customer[1] = order(customer_2)
    customer[2] = order(customer_3)
    customer[3] = order(customer_4)
    customer[4] = order(customer_5)

    for recipe in customer:
        sushi(recipe)

    time.sleep(15)

    buy_ingre()
    
    time.sleep(2)
    empty_dishes()