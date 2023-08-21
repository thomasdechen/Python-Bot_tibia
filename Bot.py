from ast import Index
import threading
from time import sleep
import time
import button
import keyboard
import pyautogui
import cv2
import pytesseract
from PIL import Image
import pyscreeze
import win32gui
import winsound
import mouse
import os.path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

tibia_title = "Tibia - [Nickname]" # define o título da janela do jogo tibia

#Não mudar(1600x900)
FOOD1_POS = 529, 630
FOOD2_POS = 569, 632
POS_AMARELA = 1454, 363, 28, 8
POS1_VIDA = 1458, 392, 10, 6
POS1_BATTLE = 1270, 36, 154, 20
BATTLE = 1251, 35, 256, 200
MOB1_BATTLE = 1476, 529
MOB2_BATTLE = 1481, 546
POS3_BATTLE = 1270, 79, 154, 60
POS4_BATTLE = 1270, 97, 117, 60
POS5_BATTLE = 1280, 119, 117, 60
POS_BATTLE = POS4_BATTLE
MOB = False

SAFE = False
#Posições
PLAYER_POS = 714, 379

VIDA_AMARELA = 'pokexgames/vida_amarela.png'
MOB1 = 'pokexgames/elder.png'
DEF_BATTLE = 'pokexgames/def_battle.png'
FOOD_EAT = 'pokexgames/magikarp.png'
VIDA_1 = 'pokexgames/vida1.png'
MOB_BATTLE = ['tibia/execowtioner.png', 'tibia/moohtant.png', 'tibia/mooh.png', 'tibia/blood.png']
CHECK = False

#Configuração

#Waypoints
# HUNT_FOLDER = './tibiamap/flag_{}.png'
HUNT_FOLDER = './tibiamap/flag_{}.png'
REFILL_MAP = './refill_map/flag_{}.png'

#Depot
DEPOT = './tibia/sqm_dp_gray.png'

#Bps
BP_STACK = 'tibia/bp_stack.png'
BP_NONSTACK = 'tibia/bp_nonstack.png'
BP_STACK_ANCHOR = 'tibia/bp_stack_anchor.png'
BP_NONSTACK_ANCHOR = 'tibia/bp_nonstack_anchor.png'
FIRST_SLOT = 15, 25

#Refill
REFILL = True
GO_REFILL = False

GHP = "ultimate health potion"
GHP_QTD = 250
GHP_POS = 197, 673, 29, 30

SMP = "strong mana potion"
SMP_QTD = 1400
SMP_POS = 232, 671, 30, 31

HEALTH_MIN = 80
MANA_MIN = 400

#Target pos
TARGET_POS = (1300, 46)

#Parar e atacar
STOP_ATTACK = False
LURE_ATTACK = True
LURE_ATTACK_JUMP = False
JUMP = False
LURE = False

# Skill em areas?
SKILL_AREA = True
SKILL_TARGET = False
global res
RES = True

#Index escada e rope
RE = (0)

#Número index
N_INDEX = 6
F_INDEX = N_INDEX - 1
N_INDEX_REFILL = 14 + 1

#PAUSAS
SLE = 0.5
LOOT_TIME = 0.07

#variaveis controle
POS4 = False
FOLLOW = False

#Configuração indexes
PORTAS = ['tibia/porta_fechada.png', 'tibia/porta2.png', 'tibia/porta3.png', 'tibia/porta4.png']
HOLES = ['tibia/porta_fechada.png', 'tibia/porta2.png', 'tibia/porta3.png', 'tibia/porta4.png']
CHAVE_PORTA = 'tibia/chave_cult.png'

#Posições
PLAYER_POS = 714, 379

#Config ações especiais
PORTA_NORMAL = False
PORTA_CHAVE = False
ROPE = False
HOLE = False
USE = False
ESCADA = False

def porta_normal():
    #Ver se porta esta aberta e abrir
    print("Checking Doors...")
    for image in PORTAS:
        check_porta = pyautogui.locateOnScreen(image, confidence=0.80)
        if check_porta != None:
            pyautogui.moveTo(check_porta)
            mouse.right_click()
            sleep(3)
        else:
            print("Door is already opened")

def porta_chave():
    #Ver se porta esta aberta e utilizar chave nela duas vezes, sempre checar antes de usar a chave
    print("Checking Doors and using key...")
    for image in PORTAS:
        check_porta = pyautogui.locateOnScreen(image, confidence=0.80)
        if check_porta != None:
            chave = pyautogui.locateOnScreen(CHAVE_PORTA, confidence=0.80, region=[1237, 25, 362, 829])
            pyautogui.moveTo(chave)
            sleep(1)
            mouse.right_click()
            pyautogui.moveTo(check_porta)
            sleep(1)
            mouse.click()
            sleep(2)

            check_porta = pyautogui.locateOnScreen(image, confidence=0.80)
            pyautogui.moveTo(chave)
            sleep(1)
            mouse.right_click()
            pyautogui.moveTo(check_porta)
            sleep(1)
            mouse.click()
        else:
            print("Door is already opened")

def rope():
    print("Rope...")
    pyautogui.press("enter")
    pyautogui.typewrite("exano tera")
    pyautogui.press("enter")
    sleep(1)

def hole():
    print("Hole...")
    for image in HOLES:
        check_hole = pyautogui.locateOnScreen(image, confidence=0.80)
        if check_hole != None:
            pyautogui.moveTo(check_hole)
            mouse.click()
            sleep(3)
        else:
            print("Hole not found")

def use():
    pegaloot()

def escada():
    mouse.move(PLAYER_POS)
    mouse.right_click()

def check_indexes():
    if PORTA_NORMAL == True:
        porta_normal()
    if PORTA_CHAVE == True:
        porta_chave()
    if ROPE == True:
        rope()
    if HOLE == True:
        hole()
    if ESCADA == True:
        escada()
    if USE == True:
        use()

def move(location):
    x, y = pyscreeze.center(location)
    mouse.move(x, y)

def move_and_click(location):
    move(location)
    mouse.click()

def food():
    pyautogui.hotkey('ctrl',  '0')

def make_noise():
    duration = 100  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)

def click_mouse(x, y):
    mouse.move(x, y, absolute=True)
    mouse.right_click()
    sleep(0.05)

def move(location):
    x, y = pyscreeze.center(location)
    pyautogui.moveTo(x, y)

def move_and_click(location):
    move(location)
    pyautogui.click()

def zoomout():
    # global ja_clicou2  # Use a variável global para alterar seu valor
    # ja_clicou2 = False
    # if not ja_clicou2:
    #     pyautogui.moveTo(1558, 84)
    #     pyautogui.click()
    #     pyautogui.moveTo(1300,800)
    #     ja_clicou2 = True  # Atualize o estado do clique após a primeira vez
    sleep(0.5)
    mouse.move(1558, 84)
    mouse.click()
    pyautogui.moveTo(PLAYER_POS)
def zoomin():
    sleep(0.5)
    mouse.move(1560, 109)
    mouse.click()
    pyautogui.moveTo(PLAYER_POS)

def check_ring():
    ring = pyautogui.locateOnScreen('./tibia/ring.png', confidence=0.90)
    if ring != None:
        pyautogui.hotkey("ctrl", "2")

def vial():
    vial1 = pyautogui.locateOnScreen('./tibia/vial1.png', confidence=0.80)
    print(vial1)
    if vial1 != None:
        pyautogui.moveTo(vial1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(713, 375)
        pyautogui.mouseUp(button='left')

    vial2 = pyautogui.locateOnScreen('./tibia/vial2.png', confidence=0.80)
    print(vial2)
    if vial2 != None:
        pyautogui.moveTo(vial2)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(713, 375)
        pyautogui.mouseUp(button='left')

def exeta_res():
    pyautogui.press('=')

def deposit():
    sleep(1)
    dp = pyautogui.locateOnScreen(DEPOT, confidence=0.75)
    pyautogui.moveTo(dp)
    mouse.click()
    sleep(4)
    mouse.move(708, 321)
    mouse.right_click()
    sleep(0.5)
    mouse.move(710, 415)
    mouse.right_click()
    sleep(0.5)
    mouse.move(652, 368)
    mouse.right_click()
    sleep(0.5)
    mouse.move(762, 368)
    mouse.right_click()
    sleep(1)
    depot = pyautogui.locateOnScreen('./tibia/depot.png', confidence=0.80)
    pyautogui.moveTo(depot)
    mouse.right_click()
    sleep(1)
    # X, Y bps anchor
    bp_stack_anchor = pyautogui.locateOnScreen(BP_STACK_ANCHOR, confidence=0.85)
    x_stack, y_stack = pyautogui.center(bp_stack_anchor)
    bp_nonstack_anchor = pyautogui.locateOnScreen(BP_NONSTACK_ANCHOR, confidence=0.85)
    x_nonstack, y_nonstack = pyautogui.center(bp_nonstack_anchor)
    bp_stack_return = x_stack + 133, y_stack
    bp_nonstack_return = x_nonstack + 133, y_nonstack

    #First slot region
    first_slot_stack = x_stack - 10, y_stack, 50, 60
    first_slot_nonstack = x_nonstack - 10, y_nonstack, 50, 60
    pyautogui.moveTo(first_slot_stack)
    pyautogui.moveTo(first_slot_nonstack)

    #First slot bps
    first_slot_stackbp = x_stack+15, y_stack+25
    first_slot_nonstackbp = x_nonstack+15, y_nonstack+25
    pyautogui.moveTo(first_slot_stackbp)
    pyautogui.moveTo(first_slot_nonstackbp)

    #Check if bp is on first slot
    bp_stack = pyautogui.locateOnScreen(BP_STACK, confidence=0.85, region=(first_slot_stack))
    bp_nonstack = pyautogui.locateOnScreen(BP_NONSTACK, confidence=0.85, region=(first_slot_nonstack))

    #Pegar imagem dps
    dp3 = pyautogui.locateOnScreen('./tibia/depot_3.png', confidence=0.90)
    dp4 = pyautogui.locateOnScreen('./tibia/depot_4.png', confidence=0.90)

    depositar_stack = True
    depositar_stack_control = True
    depositar_nonstack = True
    depositar_nonstack_control = True
    nbp_stack = 0
    nbp_nonstack = 0

    while depositar_stack == True:
        if bp_stack != None and nbp_stack == 0:
            print("Sem loot na stack bp")
            depositar_stack = False
            break

        else:
            # if nbp_stack > 0 and depositar_stack_control == False:
            #     print("Sem loot na stack bp")
            #     #Return bps and break while
            #     for _ in range(nbp_stack):
            #         print("Retornando bps...")
            #         pyautogui.moveTo(bp_stack_return)
            #         pyautogui.click()
            #         sleep(1)
            print("Tem loot na stack bp")
            # depositar loot enquanto tem loot
            while bp_stack == None and depositar_stack_control == True:
                bp_stack = pyautogui.locateOnScreen(BP_STACK, confidence=0.85, region=(first_slot_stack))
                pyautogui.moveTo(first_slot_stack)
                pyautogui.mouseDown()
                pyautogui.moveTo(dp4)
                pyautogui.mouseUp()
                pyautogui.moveTo(1300, 800)
                sleep(0.4)
                bp_stack = pyautogui.locateOnScreen(BP_STACK, confidence=0.85, region=(first_slot_stack))
                if bp_stack != None:
                    print("Acabou o loot dessa bp")
                    nbp_stack = nbp_stack + 1
                    pyautogui.moveTo(first_slot_stack)
                    mouse.right_click()
                    pyautogui.moveTo(1300, 800)
                    sleep(0.4)
                    bp_stack = pyautogui.locateOnScreen(BP_STACK, confidence=0.85, region=(first_slot_stack))
                    if bp_stack != None:
                        depositar_stack_control == False
                        print("Acabou loot stack")
                        print("nbp stack number :", nbp_stack)
                        for _ in range(nbp_stack):
                            print("Retornando bps...")
                            pyautogui.moveTo(bp_stack_return)
                            pyautogui.click()
                            sleep(1)
                        break
                    elif bp_stack == None:
                        depositar_stack_control == True
                        print("Tem mais loot loot stack")
        break

    while depositar_nonstack == True:
        if bp_nonstack != None and nbp_nonstack == 0:
            print("Sem loot na nonstack bp")
            depositar_nonstack = False
            break

        else:
            # if nbp_stack > 0 and depositar_stack_control == False:
            #     print("Sem loot na stack bp")
            #     #Return bps and break while
            #     for _ in range(nbp_stack):
            #         print("Retornando bps...")
            #         pyautogui.moveTo(bp_stack_return)
            #         pyautogui.click()
            #         sleep(1)
            print("Tem loot na non stack bp")
            # depositar loot enquanto tem loot
            while bp_nonstack == None and depositar_nonstack_control == True:
                bp_nonstack = pyautogui.locateOnScreen(BP_NONSTACK, confidence=0.85, region=(first_slot_nonstack))
                pyautogui.moveTo(first_slot_nonstack)
                pyautogui.mouseDown()
                pyautogui.moveTo(dp3)
                pyautogui.mouseUp()
                pyautogui.moveTo(1300, 800)
                sleep(0.4)
                bp_nonstack = pyautogui.locateOnScreen(BP_NONSTACK, confidence=0.85, region=(first_slot_nonstack))
                if bp_nonstack != None:
                    print("Acabou o loot dessa bp")
                    nbp_nonstack = nbp_nonstack + 1
                    pyautogui.moveTo(first_slot_nonstack)
                    mouse.right_click()
                    pyautogui.moveTo(1300, 800)
                    sleep(0.4)
                    bp_nonstack = pyautogui.locateOnScreen(BP_NONSTACK, confidence=0.85, region=(first_slot_nonstack))
                    if bp_nonstack != None:
                        depositar_nonstack_control == False
                        print("Acabou loot stack")
                        print("nbp stack number :", nbp_nonstack)
                        for _ in range(nbp_nonstack):
                            print("Retornando bps...")
                            pyautogui.moveTo(bp_nonstack_return)
                            pyautogui.click()
                            sleep(1)
                        break
                    elif bp_nonstack == None:
                        depositar_nonstack_control == True
                        print("Tem mais loot loot stack")
        break            
    print("Fim deposit")

def buy_supply():
    # Define as coordenadas da região da tela a ser capturada
    x1 = 283  # Coordenada X do canto superior esquerdo da região
    y1 = 641  # Coordenada Y do canto superior esquerdo da região
    largura1 = 40  # Largura da região
    altura1 = 15  # Altura da região 283, 641, 40, 15

    x2 = 319  # Coordenada X do canto superior esquerdo da região
    y2 = 639  # Coordenada Y do canto superior esquerdo da região
    largura2 = 37  # Largura da região
    altura2 = 18  # Altura da região 283, 641, 40, 15
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("hi")
    pyautogui.press("enter")
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("trade")
    pyautogui.press("enter")

    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("magic stuff")
    pyautogui.press("enter")

    #sell vials
    sleep(2)
    sell = pyautogui.locateOnScreen('./tibia/sell.png', confidence=0.85)
    pyautogui.moveTo(sell)
    pyautogui.click()
    sleep(1)
    npc_trade = pyautogui.locateOnScreen('./tibia/npc_trade.png', confidence=0.85)
    x, y = pyautogui.center(npc_trade)
    pyautogui.moveTo(x, y+66)
    pyautogui.click()
    ok = pyautogui.locateOnScreen('./tibia/ok.png', confidence=0.85)
    pyautogui.moveTo(ok)
    pyautogui.click()
    ##
    sleep(1)
    npc_trade = pyautogui.locateOnScreen('./tibia/npc_trade.png', confidence=0.85)
    x, y = pyautogui.center(npc_trade)
    pyautogui.moveTo(x, y+66)
    pyautogui.click()
    ok = pyautogui.locateOnScreen('./tibia/ok.png', confidence=0.85)
    pyautogui.moveTo(ok)
    pyautogui.click()

    buy = pyautogui.locateOnScreen('./tibia/buy.png', confidence=0.80)
    pyautogui.moveTo(buy)
    pyautogui.click()

    #Pegar numero de supplys
    mouse.move(213, 690)#283, 641, 40, 15
    sleep(3)
    try:
        # Captura a região da tela
        imagem_capturada = pyautogui.screenshot(region=(x1, y1, largura1, altura1))

        # Salva a imagem capturada em uma pasta
        caminho_hp = "./tibia/hp_amount.png"
        imagem_capturada.save(caminho_hp)
        
        print("Screenshot salvo em:", caminho_hp)

    except Exception as e:
        print("Erro:", e)

    sleep(1)
    mouse.move(1330, 830)
    sleep(1)
    mouse.move(249, 689) #319, 639, 37, 18
    sleep(3)
    try:
        # Captura a região da tela
        imagem_capturada = pyautogui.screenshot(region=(x2, y2, largura2, altura2))

        # Salva a imagem capturada em uma pasta
        caminho_mp = "./tibia/mp_amount.png"
        imagem_capturada.save(caminho_mp)
        
        print("Screenshot salvo em:", caminho_mp)

    except Exception as e:
        print("Erro:", e)
    sleep(1)
    #converte numero da imagem
    try:
    # Realiza o reconhecimento óptico de caracteres (OCR) na imagem capturada
        texto_extraido = pytesseract.image_to_string(caminho_hp)
        texto_extraido2 = pytesseract.image_to_string(caminho_mp)

        # Filtra apenas os números do texto extraído
        numeros = ''.join(filter(str.isdigit, texto_extraido))
        numeros2 = ''.join(filter(str.isdigit, texto_extraido2))

        # Converte a sequência de números para um valor inteiro (se necessário)
        if numeros:
            numero_convertido = int(numeros)
            print("Número extraído:", numero_convertido)
        else:
            print("Nenhum número encontrado na região.")
            numero_convertido = 10
        
        if numeros2:
            numero_convertido2 = int(numeros2)
            print("Número extraído:", numero_convertido2)
        else:
            print("Nenhum número encontrado na região.")
            numero_convertido = 10

    except Exception as e:
        print("Erro:", e)

    #Comprar as potions
    int(numero_convertido)
    int(numero_convertido2)
    hp_comprar = GHP_QTD - numero_convertido
    mp_comprar = SMP_QTD - numero_convertido2
    search = pyautogui.locateOnScreen('./tibia/search_npc.png', confidence=0.85)

        #Comprar health
    if numero_convertido < GHP_QTD:
        print("Interação com caixa de compra de potion")
        search = pyautogui.locateOnScreen('./tibia/search_npc.png', confidence=0.85)
        pyautogui.moveTo(search)
        mouse.click()
        pyautogui.typewrite(GHP)
        sleep(1)
        npc_trade = pyautogui.locateOnScreen('./tibia/npc_trade.png', confidence=0.85)
        x, y = pyautogui.center(npc_trade)
        pyautogui.moveTo(x, y+66)
        pyautogui.click()
        sleep(1)
        amount_npc = pyautogui.locateOnScreen('./tibia/amount_npc.png', confidence=0.85)
        pyautogui.moveTo(amount_npc)
        sleep(1)
        mouse.click()
        sleep(1)
        hp_comprar_str = str(hp_comprar)
        print(hp_comprar_str)
        pyautogui.typewrite(hp_comprar_str)
        sleep(2)
        ok = pyautogui.locateOnScreen('./tibia/ok.png', confidence=0.85)
        pyautogui.moveTo(ok)
        mouse.click()
        search_clean = pyautogui.locateOnScreen('./tibia/search_clean.png', confidence=0.85)
        pyautogui.moveTo(search_clean)
        mouse.click()
    #Comprar mana
    if numero_convertido2 < SMP_QTD:
        sleep(1)
        pyautogui.moveTo(search)
        mouse.click()
        pyautogui.typewrite(SMP)
        sleep(1)
        npc_trade = pyautogui.locateOnScreen('./tibia/npc_trade.png', confidence=0.85)
        x, y = pyautogui.center(npc_trade)
        pyautogui.moveTo(x, y+66)
        pyautogui.click()
        sleep(1)
        amount_npc = pyautogui.locateOnScreen('./tibia/amount_npc.png', confidence=0.85)
        pyautogui.moveTo(amount_npc)
        sleep(1)
        mouse.click()
        sleep(1)
        mp_comprar_str = str(mp_comprar)
        print(mp_comprar_str)
        pyautogui.typewrite(mp_comprar_str)
        ok = pyautogui.locateOnScreen('./tibia/ok.png', confidence=0.85)
        pyautogui.moveTo(ok)
        mouse.click()

def pegaloot():
    sleep(0.2)
    click_mouse(710, 420)
    sleep(LOOT_TIME)
    click_mouse(758, 422)
    sleep(LOOT_TIME)
    click_mouse(758, 368)
    sleep(LOOT_TIME)
    click_mouse(758, 315)
    sleep(LOOT_TIME)
    click_mouse(709, 318)
    sleep(LOOT_TIME)
    click_mouse(659, 319)
    sleep(LOOT_TIME)
    click_mouse(659, 367)
    sleep(LOOT_TIME)
    click_mouse(659, 424)
    sleep(LOOT_TIME)
    click_mouse(714, 379)
    sleep(LOOT_TIME)

def lock_enemy():
    keyboard.press('space')

def player_alert():
        for image in MOB_BATTLE:
            check_enemy = pyautogui.locateOnScreen(image, confidence=0.70)
            print("Monstro na tela: ",check_enemy)
        if check_enemy != None:
                CHECK == False
        curar()
        if CHECK == True:
            print("checando player na tela");
            if check_enemy == None:
                battle = pyautogui.locateOnScreen(
                './tibia/battle.png', confidence=0.70)
                if battle == None:
                    winsound.Beep(2000, 1000)
                    print('player na tela')
        print('Saindo do player alert')

def atualizar_status():
    global vida, mana
    vida90 = pyscreeze.pixel(699, 31)
    vida80 = pyscreeze.pixel(639, 32)
    vida70 = pyscreeze.pixel(587, 31)
    vida60 = pyscreeze.pixel(511, 31)
    vida40 = pyscreeze.pixel(400, 31)
    vida30 = pyscreeze.pixel(360, 31)
    if vida90 == (41, 42, 41):
        vida = 90
    if vida80 == (52, 52, 52):
         vida = 80
    if vida70 == (42, 42, 42):
        vida = 70
    if vida60 == (44, 44, 44):
        vida = 60
    if vida40 == (41, 41, 41):
         vida = 40
    if vida30 == (41, 41, 40):
        vida = 30

    if vida90 != (41, 42, 41):
         vida = 100
    
    mana80 = pyscreeze.pixel(795, 31)
    mana60 = pyscreeze.pixel(825, 31)
    mana30 = pyscreeze.pixel(1016, 31)
    mana20 = pyscreeze.pixel(1167, 31)


    if mana20 == (41, 42, 41):
         mana = 20;
    elif mana30 == (42, 43, 42):
         mana = 40;
    elif mana60 == (36, 37, 36):
        mana = 60;
    elif mana80 == (36, 37, 36):
        mana = 80
    else:
        mana = 100;
 
    print("Vida atual:", vida, "%")
    print("Mana atual:", mana, "%")
    curar()

def ico():
    keyboard.press('f2')
    sleep(0.09)
    keyboard.press('f3')

# Função para curar o personagem
def curar():
        if vida <= 60 and mana > 20:
            keyboard.press('f1')
            sleep(0.09)
            keyboard.press('f3')
            # atacar()

        if vida <= 60:
            keyboard.press('f1')

        if vida >= 60 and mana < 60 and vida < 90:
            ico()

        if vida <= 70 and mana >= 60 and vida >= 50:
            keyboard.press('f3')

        # if mana >= 60  and vida >= 70 and mana < 100:
        #     keyboard.press('f3')
        #     print("Curando mana")

        if mana <= 40 and vida >= 60:
            keyboard.press('f2')
            print("Curando mana")

        if mana < 80:
            keyboard.press('f2')
            print("Curando mana")

        # define a thread de cura
        cura_thread = threading.Timer(1.5, curar)
        cura_thread.start()  
        cura_thread.cancel()                                                                                      

# Função para atacar os inimigos
def atacar():
    if keyboard.press('space'):
        running = not running
        cura_ativa = False
    atualizar_status()
    area_skills = ['5', '8', '0']
    if mana > 20:
        for key in area_skills:
            sleep(0.010)
            keyboard.press(key)
    if keyboard.press('space'):
        running = not running
        cura_ativa = False
                

def pos4_mob():
    for image in MOB_BATTLE:
        check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(POS3_BATTLE))
        print(check_enemy)
        curar()
        if check_enemy != None:
            global POS4
            POS4 = True
            break
        else:
            POS4 = False
        
def follow():
     mouse.move(1581, 175)
     pyautogui.click()
     mouse.move(1400, 800)

def unfollow():
     mouse.move(1581, 153)
     pyautogui.click()
     mouse.move(1400, 800)


def check_mob():
    mob1_check = pyscreeze.pixel(1447, 512)
    # mob2_check = pyscreeze.pixel(1447, 532)
    target = (255, 0, 0)
    print(mob1_check)
    atualizar_status()
    curar()
    # print(mob2_check)
    if mob1_check == (254, 0, 0) or mob1_check == (255, 0, 0):
        print('mob vivo')
        return True
    else:
        return False    
        make_noise()

def check_attack():
    mob1_check = pyscreeze.pixel(1271, 46)
    # mob2_check = pyscreeze.pixel(1447, 532)
    target = (255, 0, 0)
    print(mob1_check)
    atualizar_status()
    curar()
    # print(mob2_check)
    if mob1_check == (254, 0, 0) or mob1_check == (255, 0, 0):
        print('mob vivo')
    else:
        if FOLLOW == True:
            pegaloot()
        mob1_check = pyscreeze.pixel(1271, 46)
        # mob2_check = pyscreeze.pixel(1447, 532)
        target = (255, 0, 0)
        print(mob1_check)
        curar()
        # print(mob2_check)
        if mob1_check == (254, 0, 0) or mob1_check == (255, 0, 0):
            print('mob vivo')
        else:
            target_mob()

# Função para atacar os inimigos
def atacar_low():
    # atualizar_status()
    # find_mob()
    # if MOB == True:
    #      keyboard.press("space")
    #      while MOB == True:
    #           find_mob()
    #           if MOB == False:
    #                break
    keyboard.press("space")

def find_mob():
    for image in MOB_BATTLE:
            check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
            print(check_enemy)
            curar()
            if check_enemy != None:
                MOB = True
                return True
                break  # sair do loop
            else:
                return False
                check_enemy == None
                MOB = False

def find_mob2():
    for image in MOB_BATTLE:
            check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
            print(check_enemy)
            curar()
            if check_enemy is not None:
                MOB = True
                batalha()
                break  # sair do loop
            else:
                check_enemy == None
                MOB = False

def target_mob():
     pyautogui.moveTo(TARGET_POS)
     mouse.click()
     mouse.move(1393, 800)

def batalha_low():
    time_res = 0
    atualizar_status()
    target_mob()
    sleep(SLE)
    for image in MOB_BATTLE:
        check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
        print(check_enemy)
        atualizar_status()
        battle()
        if check_enemy != None:
            break  # sair do loop
        else:
            check_enemy == None
            MOB = False
    while check_enemy != None:
        print('batalha ativada')
        if time_res == 1:
            if RES == True:
                sleep(0.02)
                pyautogui.press('f12')
                time_res = 0
        else:
             time_res += 1
        battle()
        atacar()
        check_attack()
        battle()
        atacar()
        for image in MOB_BATTLE:
            check_enemy = pyautogui.locateOnScreen(image, confidence=0.80, region=(BATTLE))
            if check_enemy != None:
                battle()
                break
            print(check_enemy)
    print('Fora de batalha')
    if find_mob == False:
        atualizar_status()
    if index == N_INDEX:
        vial()
    while mana <= 80:
            atualizar_status()
            battle()

def battle():
                atualizar_status()
                while vida <= 60 and mana >=60:
                    pyautogui.press('1')
                    sleep(0.010)
                    pyautogui.press('3')
                    sleep(0.010)
                    atacar()
                if vida <= 60 and mana > 40:
                    pyautogui.press('1')
                    sleep(0.010)
                    pyautogui.press('3')
                if vida <= 60:
                    pyautogui.press('1')
                elif vida > 60 and mana <= 60 and vida < 100:
                    pyautogui.press('2')
                    sleep(0.010)
                    pyautogui.press('3')
                elif vida > 60 and mana == 100 and vida < 100:
                    pyautogui.press('3')
                elif vida > 60 and mana <= 60:
                    pyautogui.press('2')
                elif mana < 80 and vida == 100:
                    pyautogui.press('2')
                print('MAIN LOOP')
    

def batalha():
    atualizar_status()
    for image in MOB_BATTLE:
                check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
                print(check_enemy)
                if check_enemy is not None:
                    break  # sair do loop
                else:
                    check_enemy == None
                    break
    while check_enemy != None:
        print('batalha ativada')
        atualizar_status()
        curar()
        atacar()
        find_mob()
    print('Fora de batalha')
    if check_enemy == None:
        while vida < 80:
            atualizar_status()
            curar()
    pegaloot()
    atualizar_status()
    curar()
    atualizar_status()

def modes():
    if STOP_ATTACK == True:
        if check_enemy != None:
            print("Parou")
            atualizar_status()
            curar()
            follow()
            curar()
            curar()
            if FOLLOW == False:
                unfollow()
            keyboard.press("s")
            keyboard.release("s")
            keyboard.release("s")
            batalha_low()
            pegaloot()
            food()
            try:
                position_in_map = pyautogui.locateOnScreen(
                    HUNT_FOLDER.format(index), confidence=0.90, region=(1429, 25, 113, 113))
            except:
                pass
            try:
                move_and_click(position_in_map)
            except:
                pass
            pyautogui.moveTo(1379, 800)
            atualizar_status()
            curar()
    if LURE_ATTACK == True:
        if check_enemy_lure != None:
            print("Parou")
            atualizar_status()
            battle()
            if FOLLOW == True:
                follow()
            if FOLLOW == False:
                unfollow()
            keyboard.press("s")
            keyboard.release("s")
            keyboard.release("s")
            batalha_low()
            pegaloot()
            try:
                position_in_map = pyautogui.locateOnScreen(
                    HUNT_FOLDER.format(index), confidence=0.90, region=(1429, 25, 113, 113))
            except:
                pass
            try:
                move_and_click(position_in_map)
            except:
                pass
            pyautogui.moveTo(1379, 800)
    if LURE_ATTACK_JUMP == True:
        if check_enemy_lure != None:
            print("Parou")
            atualizar_status()
            curar()
            follow()
            curar()
            curar()
            if FOLLOW == False:
                unfollow()
            keyboard.press("s")
            keyboard.release("s")
            keyboard.release("s")
            batalha_low()
            pegaloot()
            food()
            pyautogui.moveTo(1379, 800)
            atualizar_status()
            curar()
            JUMP == True

    if LURE == True:
        if check_enemy_lure != None:
            print("Parou")
            # pyautogui.hotkey("s", "w")
            # keyboard.release("s")
            # keyboard.release("w")
            # keyboard.release("s")
            # keyboard.release("w")
            pyautogui.moveTo(PLAYER_POS)
            mouse.right_click()
            atualizar_status()
            battle()
            try:
                position_in_map = pyautogui.locateOnScreen(
                    HUNT_FOLDER.format(index), confidence=0.85, region=(1429, 25, 113, 113))
            except:
                pass
            try:
                move_and_click(position_in_map)
            except:
                pass
            pyautogui.moveTo(1379, 800)
            sleep(1)

def check_refill():
        # Define as coordenadas da região da tela a ser capturada
    x1 = 283  # Coordenada X do canto superior esquerdo da região
    y1 = 641  # Coordenada Y do canto superior esquerdo da região
    largura1 = 40  # Largura da região
    altura1 = 15  # Altura da região 283, 641, 40, 15

    x2 = 319  # Coordenada X do canto superior esquerdo da região
    y2 = 639  # Coordenada Y do canto superior esquerdo da região
    largura2 = 37  # Largura da região
    altura2 = 18  # Altura da região 283, 641, 40, 15

    #Pegar numero de supplys
    mouse.move(213, 690)#283, 641, 40, 15
    sleep(1)
    try:
        # Captura a região da tela
        imagem_capturada = pyautogui.screenshot(region=(x1, y1, largura1, altura1))

        # Salva a imagem capturada em uma pasta
        caminho_hp = "./tibia/hp_amount.png"
        imagem_capturada.save(caminho_hp)
        
        print("Screenshot salvo em:", caminho_hp)

    except Exception as e:
        print("Erro:", e)
    sleep(1)
    mouse.move(1330, 830)
    mouse.move(249, 689) #319, 639, 37, 18
    sleep(1.5)
    try:
        # Captura a região da tela
        imagem_capturada = pyautogui.screenshot(region=(x2, y2, largura2, altura2))

        # Salva a imagem capturada em uma pasta
        caminho_mp = "./tibia/mp_amount.png"
        imagem_capturada.save(caminho_mp)
        
        print("Screenshot salvo em:", caminho_mp)


    except Exception as e:
        print("Erro:", e)
    sleep(1)
    #converte numero da imagem
    numero_convertido = 0
    numero_convertido2 = 0
    try:
    # Realiza o reconhecimento óptico de caracteres (OCR) na imagem capturada
        texto_extraido = pytesseract.image_to_string(caminho_hp)
        sleep(1)
        texto_extraido2 = pytesseract.image_to_string(caminho_mp)

        # Filtra apenas os números do texto extraído
        numeros = ''.join(filter(str.isdigit, texto_extraido))
        numeros2 = ''.join(filter(str.isdigit, texto_extraido2))

        # Converte a sequência de números para um valor inteiro (se necessário)
        if numeros:
            numero_convertido = int(numeros)
            print("Número extraído:", numero_convertido)
        else:
            print("Nenhum número encontrado na região.")
        
        if numeros2:
            numero_convertido2 = int(numeros2)
            print("Número extraído:", numero_convertido2)
        else:
            print("Nenhum número encontrado na região.")


        hp = cv2.imread('./tibia/hp_amount.png', 0)
        mp = cv2.imread('./tibia/mp_amount.png', 0)
        thresh = cv2.threshold(hp, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        thresh2 = cv2.threshold(mp, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        datahp = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
        datamp = pytesseract.image_to_string(thresh2, lang='eng',config='--psm 6')

    except Exception as e:
        print("Erro:", e)

    #Comprar as potions
    # int(numero_convertido)
    # int(numero_convertido2)
    numero_convertido = int(datahp)
    numero_convertido2 = int(datamp)

    if numero_convertido <= HEALTH_MIN or numero_convertido2 <= MANA_MIN:
        print("Supply baixa")
        refill()
        return True
    else:
        print("Supply ok")
        GO_REFILL = False
        return False

def refill():
    global index_refill
    should_stop = False
    for index in range(N_INDEX_REFILL):
                    index_refill = index
                    if index == 0:
                        zoomin()
                        zoomin()
                    if should_stop:  # Se o sinalizador estiver definido como True, saia do loop
                        break  # sair do loop
                    while True:
                        current_index_plus_one = index + 1
                        print('dentro for')
                        # if index == 0:
                        #     zoomout()
                        #     zoomout()
                        if index == 0:
                            try:
                                position_in_map = pyautogui.locateOnScreen(
                                    './refill_map/flag_0.png', confidence=0.90, region=(1429, 25, 113, 113))
                            except:
                                pass
                            if position_in_map == None:
                                break
                            try:
                                move_and_click(position_in_map)
                            except:
                                pass
                            sleep(2)
                        if index != 0:
                            try:
                                position_in_map = pyautogui.locateOnScreen(
                                    REFILL_MAP.format(index), confidence=0.90, region=(1429, 25, 113, 113))
                            except:
                                pass
                            if position_in_map == None:
                                break
                            try:
                                move_and_click(position_in_map)
                            except:
                                pass
                        pyautogui.moveTo(1379, 800)
                        atualizar_status()
                        curar()
                        try:
                            position_in_map2 = pyautogui.locateOnScreen(
                                    REFILL_MAP.format(index), confidence=0.80, region=(1480, 76, 18, 15))
                        except:
                             pass  
                        
                        while position_in_map2 is None and position_in_map != None:
                            if index == N_INDEX_REFILL:
                                should_stop = True
                                sleep(1)
                                batalha_low()
                            for image in MOB_BATTLE:
                                check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(POS1_BATTLE))
                                check_enemy_lure = pyautogui.locateOnScreen(image, confidence=0.70, region=(POS_BATTLE))
                                print(check_enemy) 
                                atualizar_status()
                                battle()
                                position_in_map = pyautogui.locateOnScreen(
                                    REFILL_MAP.format(index), confidence=0.90, region=(1429, 25, 113, 113))
                                try:
                                    modes()
                                except:
                                    pass
                                if check_enemy != None:
                                    batalha_low()
                                    pegaloot()
                            print(position_in_map2)
                            atualizar_status()
                            battle()
                            # player_alert()
                            position_in_map2 = pyautogui.locateOnScreen(
                                REFILL_MAP.format(index), confidence=0.80, region=(1480, 76, 14, 12))
                            position_in_map = pyautogui.locateOnScreen(
                                    REFILL_MAP.format(index), confidence=0.90, region=(1429, 25, 113, 113))
                            # if index == 12:
                            #      keyboard.press("f12")
                            #      move_and_click(711, 376)
                        atualizar_status()
                        if FOLLOW == True:
                            follow()
                        for image in MOB_BATTLE:
                            check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
                            print(check_enemy)
                            atualizar_status()
                            curar()
                            if check_enemy != None:
                                batalha_low()
                                pegaloot()
                                break
                            else:
                                check_enemy == None
                                print("Ações apos andar")
                                # batalha_low()
                                # pegaloot()
                                if index == 0:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomin()
                                    zoomin()
                                    break
                                elif index == 1:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomout()
                                    zoomout()
                                    break
                                elif index == 2:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 3:
                                    deposit()
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 4:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomin()
                                    break
                                elif index == 5:
                                    pyautogui.moveTo(1300, 800)
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomin()
                                    break
                                elif index == 6:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 7:
                                    buy_supply()
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 8:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 9:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomout()
                                    zoomout()
                                    break
                                elif index == 10:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 11:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    break
                                elif index == 12:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    zoomin()
                                    zoomin()
                                    break
                                elif index == 13:
                                    # PORTA_CHAVE = True
                                    # PORTA_NORMAL = True
                                    # ROPE = True
                                    # HOLE = True
                                    # USE = True
                                    # ESCADA = True
                                    check_indexes()
                                    batalha_low()
                                    pegaloot()
                                    should_stop = True
                                    zoomout()
                                    zoomout()
                                    break
                                if index == N_INDEX_REFILL - 1:
                                    batalha_low()
                                    pegaloot()
                                    should_stop = True
                                    break  # sair do loop
                                # PORTA_CHAVE = False
                                # PORTA_NORMAL = False
                                # ROPE = False
                                # HOLE = False
                                # USE = False
                                # ESCADA = False
                                
                        if check_enemy == None:
                            print("saindo ações")
                            break
                        print("Passou ações")
                        batalha_low()
                        pegaloot()
                        if index == N_INDEX:
                            vial()
                    if index == 16:
                        should_stop = True
                        break

while True:
        # inicializa a variável de tempo
    last_f12_press_time = time.monotonic()
    print('comecou')
    sleep(1)
    window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if tibia_title in window_title:
        global index_hunt
        for index in range(N_INDEX):
                    res = 0
                    index_hunt = index
                    while True:
                        if index == 1:
                            if REFILL == True:
                                check_refill()
                                index == 0
                        current_index_plus_one = index + 1
                        print('dentro for')
                        try:
                            position_in_map = pyautogui.locateOnScreen(
                                HUNT_FOLDER.format(index), confidence=0.90, region=(1429, 25, 113, 113))
                        except:
                             pass
                        if position_in_map == None:
                            break
                        try:
                            move_and_click(position_in_map)
                        except:
                            pass
                        check_ring()
                        pyautogui.moveTo(1379, 800)
                        atualizar_status()
                        curar()
                        if position_in_map == None:
                            break
                        try:
                            position_in_map2 = pyautogui.locateOnScreen(
                                    HUNT_FOLDER.format(index), confidence=0.80, region=(1480, 76, 18, 15))
                        except:
                             pass
                        JUMP == False
                        while position_in_map2 == None and position_in_map != None:
                            for image in MOB_BATTLE:
                                check_enemy_lure = pyautogui.locateOnScreen(image, confidence=0.70, region=(POS_BATTLE))
                                check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(POS1_BATTLE))
                                try:
                                    modes()
                                except:
                                    pass
                                # if index == 1:
                                #     if REFILL == True:
                                #         check_refill()
                                #         if GO_REFILL == True:
                                #             refill()
                                #             batalha_low()
                                #             GO_REFILL = False
                                #             index == 0
                            atualizar_status()
                            battle()
                            position_in_map2 = pyautogui.locateOnScreen(
                                HUNT_FOLDER.format(index), confidence=0.80, region=(1480, 76, 38, 35))
                            position_in_map = pyautogui.locateOnScreen(
                                    HUNT_FOLDER.format(index), confidence=0.90, region=(1429, 25, 113, 113))
                            if JUMP == True:
                                    position_in_map == None
                            # if index == 12:
                            #      keyboard.press("f12")
                            #      move_and_click(711, 376)
                        print("Saiu main loop")
                        atualizar_status()
                        if FOLLOW == True:
                            follow()
                        for image in MOB_BATTLE:
                            check_enemy = pyautogui.locateOnScreen(image, confidence=0.70, region=(BATTLE))
                            print(check_enemy)
                            atualizar_status()
                            curar()
                            if check_enemy is not None:
                                break  # sair do loop
                            else:
                                check_enemy == None
                        if check_enemy == None:
                            break
                        atualizar_status()
                        curar()
                        if FOLLOW == False:
                            unfollow()
                        batalha_low()
                        # sleep(0.2)
                        pegaloot()
                        CHECK = True
                        player_alert()
                        CHECK = False
                        atualizar_status()
                        food()
                        check_ring()
                        if index == F_INDEX: 
                            vial()
                        break
