import random as rnd
import pygame
import sys
import copy

def create_small():
    grid = []
    
    järjekord = [x for x in range(1,10)]
    rnd.shuffle(järjekord)

    for i in range(3):
        grid.append(järjekord[0+i*3:3+i*3])
    
    return grid


def laienda_ruut(ruut):
    for i in range(len(ruut)):
        for j in range(len(ruut[i])):
            ruut[i].append(ruut[i-1][j])
            
        for j in range(3):
            ruut[i].append(ruut[i-2][j])
    
    return ruut


def laienda_alla(ruut):
    
    for j in range(2):
        for i in range(3):
            külik = []
            for k in range(len(ruut[i])):
                külik.append(ruut[i][k-1-j])
            ruut.append(külik)


    return ruut



def sega_ridu(sisend):
    uus = []
    järjekord = list(range(3))
    rnd.shuffle(järjekord)

    for i in järjekord:
        
        segatud = sisend[0+i*3:3+i*3]
        rnd.shuffle(segatud)

        for j in range(len(segatud)):
            uus.append(segatud[j])
    
    return uus


def counter(pea, alam):
    lugeja = 0
    for i in range(len(pea)):
        if pea[i] == alam:
            lugeja +=1
    
    return lugeja


def sega_tulbad(sisend= 0):
    tulem =[]

    for i in range(9):
        tulem.append([])

    main = list(range(3))
    rnd.shuffle(main)

    for i in main:
        alam = list(range(3))
        rnd.shuffle(alam)

        for j in alam:
            for k in range(len(sisend)):
                tulem[k].append(sisend[k][3*i +j])

    return tulem


raskusastmed = {"lihtne": 24,
                "keskmine": 21,
                "raske": 18
                }


def eemalda_numbreid(lahendus, jätta):

    read_jätmiseks = []
    for i in range(jätta):
        alles = rnd.choice(list(range(9)))
        read_jätmiseks.append(alles)

    for i in range(len(lahendus)):
        valim = rnd.sample(list(range(9)), 9 - counter(read_jätmiseks, i))
        for j in valim:
            lahendus[i][j] = 0

    return lahendus


#valmistab ette põhi-mängulaua(mis on reeglitele vastav) ning mida hakatakse pärast segama, et saada päris-mängulaud
alaruut = laienda_alla(laienda_ruut(create_small()))
segatud = sega_ridu(sega_tulbad(alaruut))

#for i in range(len(segatud)):
   # print(segatud[i])


raskus = "lihtne"   
lahendada = eemalda_numbreid(segatud, raskusastmed[raskus])

print("")

sudoku_laud = []
usr_laud = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]


for i in range(len(lahendada)):
    #print(lahendada[i])
    sudoku_laud.append(lahendada[i])
#usr_laud = sudoku_laud.copy()

kasutaja_laud = copy.deepcopy(sudoku_laud)

def reeglikontroll(nr, grid, rida, veerg):
    
    if nr == 0:
        return True
    
    read = list(range(len(grid)))
    read.pop(rida)
    #kas samas veerus on
    for i in read:
        if grid[i][veerg] == nr:
            return False
    
    veerud = list(range(len(grid[rida])))
    veerud.pop(veerg)
    #kas samas reas on
    for i in veerud:
        if grid[rida][i] == nr:
            return False
    
    #leiame alaruudu, kus nr on
    alarida = rida//3
    alaveerg = veerg//3
    count = 0
    for i in range(len(grid[alarida*3:alarida*3+3])):
        for j in range(len(grid[alarida*3:alarida*3+3][i][alaveerg*3:alarida*3+3])):
            if grid[alarida*3:alarida*3+3][i][alaveerg*3:alarida*3+3][j] == nr:
                count += 1
    if count >= 2:
        return False

    return True


# PyGame-i osa

pygame.init()

LAIUS, KÕRGUS = 540, 540
RUUDU_SUURUS = LAIUS // 9

VALGE = (255, 255, 255)
MUST = (0, 0, 0)
SININE = (43, 140, 200)
LILLA_PUNANE = (153, 1, 71)
HELEPUNANE = (253, 137, 137)



font3 = pygame.font.Font("freesansbold.ttf", 32)
tekst1 = font3.render("Menüü", True, MUST)
tekst2 = font3.render("Start", True, MUST)
tekst3 = font3.render("Quit", True, MUST)


color_light = (170, 170, 170)
color_dark = (100, 100, 100)


# init
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("Sudoku pela in HINDI2025 GTA7LEAK")


def joonista_ruudustik():
    for i in range(10):
        pygame.draw.line(ekraan, MUST, (0, i * RUUDU_SUURUS), (LAIUS, i * RUUDU_SUURUS), 2)
        pygame.draw.line(ekraan, MUST, (i * RUUDU_SUURUS, 0), (i * RUUDU_SUURUS, KÕRGUS), 2)

def joonista_3ruudu_suurus():
    for i in range(0, 10, 3):
        pygame.draw.line(ekraan, SININE, (0, i * RUUDU_SUURUS), (LAIUS, i * RUUDU_SUURUS), 3)
        pygame.draw.line(ekraan, SININE, (i * RUUDU_SUURUS, 0), (i * RUUDU_SUURUS, KÕRGUS), 3)

def joonista_arvud():
    font = pygame.font.SysFont('bahnschrift', 36, bold=False, italic=False)
    font2 = pygame.font.SysFont('blackadderitc', 38, bold=False, italic=False)
    for i in range(9):
        for j in range(9):
            if sudoku_laud[i][j] != 0 and kasutaja_laud[i][j] != 0:
                arv = font.render(str(kasutaja_laud[i][j]), True, MUST)
                x = j * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_width() // 2
                y = i * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_height() // 2
                ekraan.blit(arv, (x, y))
            elif sudoku_laud[i][j] == 0 and kasutaja_laud[i][j] != 0:
                arv = font.render(str(kasutaja_laud[i][j]), True, SININE)
                x = j * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_width() // 2
                y = i * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_height() // 2
                ekraan.blit(arv, (x, y))

    #if valitud_ruut:
        #if vajutus == True:
            #kirjuta_tühja(valitud_ruut, sisend)

def joonista_valitud_ruut(valitud_ruut):
    i, j = valitud_ruut
    pygame.draw.rect(ekraan, LILLA_PUNANE, (j * RUUDU_SUURUS, i * RUUDU_SUURUS, RUUDU_SUURUS, RUUDU_SUURUS), 3)

def kirjuta_tühja(valitud_ruut, sisend):
    if sisend != -1:
        i = valitud_ruut[0]
        j = valitud_ruut[1]
        #font = pygame.font.SysFont('blackadderitc', 38, bold=False, italic=False)
        #if usr_laud[i][j]:
        if sudoku_laud[i][j] == 0:
            kasutaja_laud[i][j] = sisend
            #arv = font.render(str(sisend), True, MUST)
            #x = j * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_width() // 2
            #y = i * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_height() // 2
            #ekraan.blit(arv, (x, y))
        #print(usr_laud)
        sisend = -1
#ekraan.fill(VALGE)



def main():
    
    elusid = 3
    
    vead = []
    kell = pygame.time.Clock()
    valitud_ruut = None
    sisend = -1
    while True:
        vajutus = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hiireX, hiireY = pygame.mouse.get_pos()
                valitud_ruut = (hiireY // RUUDU_SUURUS, hiireX // RUUDU_SUURUS)
                print(valitud_ruut)
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_0 or pygame.K_KP0:
                    #sisend = 0
                if event.key == pygame.K_1:
                    vajutus = True
                    sisend = 1
                    print('Vajutati 1')
                elif event.key == pygame.K_2:
                    vajutus = True
                    sisend = 2
                    print('Vajutati 2')
                elif event.key == pygame.K_3:
                    vajutus = True
                    sisend = 3
                    print('Vajutati 3')
                elif event.key == pygame.K_4:
                    vajutus = True
                    sisend = 4
                    print('Vajutati 4')
                elif event.key == pygame.K_5:
                    vajutus = True
                    sisend = 5
                    print('Vajutati 5')
                elif event.key == pygame.K_6:
                    vajutus = True
                    sisend = 6
                    print('Vajutati 6')
                elif event.key == pygame.K_7:
                    vajutus = True
                    sisend = 7
                    print('Vajutati 7')
                elif event.key == pygame.K_8:
                    vajutus = True
                    sisend = 8
                    print('Vajutati 8')
                elif event.key == pygame.K_9:
                    vajutus = True
                    sisend = 9
                    print('Vajutati 9')
                elif event.key == pygame.K_BACKSPACE:
                    vajutus = True
                    sisend = 0

        ekraan.fill(VALGE)
        
        for i in range(len(vead)):
            pygame.draw.rect(ekraan, HELEPUNANE, (vead[i][1]*RUUDU_SUURUS,vead[i][0]*RUUDU_SUURUS,RUUDU_SUURUS,RUUDU_SUURUS))

        joonista_ruudustik()
        joonista_arvud()
        joonista_3ruudu_suurus()
        if valitud_ruut:
            joonista_valitud_ruut(valitud_ruut)
            if vajutus:
                kirjuta_tühja(valitud_ruut, sisend)
                if not reeglikontroll(kasutaja_laud[valitud_ruut[0]][valitud_ruut[1]],kasutaja_laud, valitud_ruut[0], valitud_ruut[1]):
                    vead.append((valitud_ruut[0],valitud_ruut[1]))
                    elusid -=1
                print(vead)
                if (valitud_ruut[0], valitud_ruut[1]) in vead and kasutaja_laud[valitud_ruut[0]][valitud_ruut[1]] == 0:
                    vead.remove((valitud_ruut[0],valitud_ruut[1]))
                    
        pygame.display.flip()
        kell.tick(60)



def meny():             # genereerib menüü, kui mängu käima paned
    kell1 = pygame.time.Clock()
    while True:
        kell1.tick(60)
        mouse = pygame.mouse.get_pos()

        ekraan.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LAIUS/2 - 40 <= mouse[0] <= LAIUS/2 + 40 and KÕRGUS/2 - 15 <= mouse[1] <= KÕRGUS/2 + 15:
                    main()
                elif 410 <= mouse[0] <= 490 and 335 <= mouse[1] <= 365:
                    pygame.quit()

        # muudab värvi kui hiir "start nupu peal
        if 405 <= mouse[0] <= 490 and 282 <= mouse[1] <= 317:
            pygame.draw.rect(ekraan, color_light, [405, 282, 85, 36], 18, 3)
        else:
            pygame.draw.rect(ekraan, color_dark, [405, 282, 85, 36], 18, 3)

        # muudab värvi kui hiir "quit" nupu peal
        if 405 <= mouse[0] <= 490 and 332 <= mouse[1] <= 367:
            pygame.draw.rect(ekraan, color_light, [405, 332, 85, 36], 18, 3)
        else:
            pygame.draw.rect(ekraan, color_dark, [405, 332, 85, 36], 18, 3)

        # joonistab tekstid menüüle
        ekraan.blit(tekst1, (10, 10))
        ekraan.blit(tekst2, (410, 285))
        ekraan.blit(tekst3, (412, 335))

        pygame.display.update()



# meny()
main()