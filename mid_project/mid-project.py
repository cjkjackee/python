import pyautogui as gui
import snp
import time

nori = 5
rice = 10
salmon = 10
roe = 10
eel = 5
shrimp = 5
score = 0
menu = ['sushi/onigiri.png', 'sushi/roe_maki.png', 'sushi/gunkan_maki.png', 'sushi/sake_roll.png', 'sushi/unagi_nigiri.png', 'sushi/ebi_nigiri.png']

def find_ingre(pic, num=1):
    temp = snp.locateCenterOnScreen(pic, region=(ingredient_x, ingredient_y, 200, 460))
    gui.click(temp, clicks=num, interval=0.1, pause=0.1, _pause=True)

def click_center(pic, threshold=0.87):
    temp = snp.locateCenterOnScreen(pic, threshold=threshold)
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
    first = True
    for pos in customer_pos:
        count = 0
        temp = None
        while not temp:
            temp = snp.locateCenterOnScreen('sushi/empty.png', threshold=0.9, region=(pos, customer_y+150, 120, 80))
            count += 1
        time.sleep(1)
        gui.click(temp)

def buy_ingre(ingrediant=None, emergency=False):
    global rice, nori, roe, salmon, shrimp, eel, score

    trig = False

    if emergency:
        gui.click(phone)
        time.sleep(0.2)
        if (ingrediant == 'rice'):
            temp = snp.locateCenterOnScreen('sushi/phone_rice.png')
            gui.click(temp)
            item = None
            while item == None:
                item = snp.locateCenterOnScreen('sushi/phone_rice_2.png',threshold=0.9)
            gui.click(item)
            gui.click(temp)
            rice += 10
            score -= 100
        else:
            if (ingrediant == 'nori'):
                nori += 10
                score -= 100
                pic = 'sushi/phone_nori.png'
            elif (ingrediant == 'roe'):
                roe += 10
                score -= 200
                pic = 'sushi/phone_roe.png'
            elif (ingrediant == 'salmon'):
                salmon += 5
                score -= 300
                pic = 'sushi/phone_salmon.png'
            elif (ingrediant == 'shrimp'):
                shrimp += 5
                pic = 'sushi/phone_shrimp.png'
            elif (ingrediant == 'eel'):
                eel += 5
                pic = 'sushi/phone_eel.png'
            else:
                pass
            temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
            gui.click(temp)
            item = None
            while item == None:
                item = snp.locateCenterOnScreen(pic)
            gui.click(item)
            gui.click(temp[0], temp[1]+80)
            time.sleep(6)
        return True
    
    if (nori < 5):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_nori.png')
        gui.click(item)
        gui.click(temp[0], temp[1]+20)
        nori += 10
        score -= 100
        trig = True
    if (roe < 6):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_roe.png')
        gui.click(item)
        gui.click(temp[0], temp[1]+20)
        roe += 10 
        score -= 200
        trig = True
    if (salmon < 4):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_salmon.png')
        gui.click(item)
        gui.click(temp[0], temp[1]+20)
        salmon += 5
        score -= 300
        trig = True
    if (shrimp < 4):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_shrimp.png')
        gui.click(item)
        gui.click(temp[0], temp[1]+20)
        shrimp += 5
        trig = True
    if (eel < 4):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_topping.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_eel.png')
        gui.click(item)
        gui.click(temp[0], temp[1]+20)
        eel += 5
        trig = True
    if (rice < 8):
        gui.click(phone)
        time.sleep(0.2)
        temp = snp.locateCenterOnScreen('sushi/phone_rice.png')
        gui.click(temp)
        item = None
        while item == None:
            item = snp.locateCenterOnScreen('sushi/phone_rice_2.png',threshold=0.9)
        gui.click(item)
        gui.click(temp)
        rice += 10
        score -= 100
        trig = True

    return trig

def sushi(recipes):
    global nori, rice, salmon, roe, eel, shrimp, score
    if(recipes == 1):
        if (rice < 2):
            buy_ingre(ingrediant='rice', emergency=True)
        if (nori < 1):
            buy_ingre(ingrediant='nori', emergency=True)
        find_ingre('sushi/rice.png',num=2)
        find_ingre('sushi/nori.png')
        rice -= 2
        nori -= 1
        score += 50
    elif(recipes == 2):
        if (rice < 1):
            buy_ingre(ingrediant='rice', emergency=True)
        if (roe < 1):
            buy_ingre(ingrediant='roe', emergency=True)
        find_ingre('sushi/rice.png')
        find_ingre('sushi/roe.png')
        rice -= 1
        roe -= 1
        score += 80
    elif(recipes == 3):
        if (rice < 1):
            buy_ingre(ingrediant='rice', emergency=True)
        if (nori < 1):
            buy_ingre(ingrediant='nori', emergency=True)
        if (roe < 2):
            buy_ingre(ingrediant='roe', emergency=True)
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        find_ingre('sushi/roe.png',num=2)
        rice -= 1
        nori -= 1
        roe -= 2
        score += 120
    elif(recipes == 4):
        if (rice < 1):
            buy_ingre(ingrediant='rice', emergency=True)
        if (nori < 1):
            buy_ingre(ingrediant='nori', emergency=True)
        if (salmon < 1):
            buy_ingre(ingrediant='salmon', emergency=True)
        find_ingre('sushi/salmon.png')
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        rice -= 1
        nori -= 1
        salmon -= 1
        score += 150
    elif(recipes == 5):
        if (rice < 1):
            buy_ingre(ingrediant='rice', emergency=True)
        if (shrimp < 2):
            buy_ingre(ingrediant='shrimp', emergency=True)
        find_ingre('sushi/rice.png')
        find_ingre('sushi/shrimp.png', num=2)
        rice -= 1
        shrimp -= 2
    elif(recipes == 6):
        if (rice < 1):
            buy_ingre(ingrediant='rice', emergency=True)
        if (nori < 1):
            buy_ingre(ingrediant='nori', emergency=True)
        if (eel < 2):
            buy_ingre(ingrediant='eel', emergency=True)
        find_ingre('sushi/rice.png')
        find_ingre('sushi/nori.png')
        find_ingre('sushi/eel.png',num=2)
        rice -= 1
        nori -= 1
        eel -= 2

    gui.click(sushi_done_x, sushi_done_y, pause=2, _pause=True)
    

    
###########################   main    #############################

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

customer_y = top[1] + 40
customer_pos = []
customer_pos.append(top[0] + 60)
customer_pos.append(top[0] + 180)
customer_pos.append(top[0] + 310)
customer_pos.append(top[0] + 430)
customer_pos.append(top[0] + 550)

# start game
start = time.time()
customer = []
click_center('sushi/start_game.png')

while True:
    customer.clear()
    print('waiting orders')
    for pos in customer_pos:
        customer.append(order(pos))

    for recipe in customer:
        sushi(recipe)

    buy_ingre()
    
    empty_dishes()

    if (score > 1000):
        end = time.time()
        print('run time ', end-start)
    print(score)