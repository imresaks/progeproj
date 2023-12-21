import pygame
import random

pygame.init()

sonafail = r"C:\Users\pertk\kood\poomine\sonad.txt" 
# pela kood

LAIUS, KORGUS = 900, 600
FPS = 60
ekraan = pygame.display.set_mode((LAIUS, KORGUS))
pygame.display.set_caption("poomine")

black = (0, 0, 0)
white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)


font = pygame.font.Font("freesansbold.ttf", 32)
tekst1 = font.render("Menüü", True, black)
tekst2 = font.render("Start", True, black)
tekst3 = font.render("Quit", True, black)
# start nupu suurus ja koht = 80 x 30; 410, 285
# quit nupu suurus ja koht = 80 x 30; 410, 335


def sonavalik(fail):            # valib välja suvalise sõna teisest failist
    with open(fail, "r", encoding= "utf-8") as f:
        x = random.choice(f.readlines())
    return x


def mangulopp(x, y):       # vastavalt kui voitsid/kaotasid, lopetab mangu
    kell = pygame.time.Clock()
    tekst4 = font.render(x, True, black)
    tekst5 = font.render(y, True, black)
    while True:
        kell.tick(FPS)
        ekraan.fill((80, 20, 160))
        ekraan.blit(tekst4, (400, 290))
        ekraan.blit(tekst5, (400, 340))

        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        pygame.time.delay(2000)
        meny()


def main():         # main mangu loogika
    kell = pygame.time.Clock()

    s6na = sonavalik(sonafail).rstrip("\n")  # valitud sõna

    lists6na = list(s6na)
    print(s6na)

    arvatudtahed = []
    pakutudtahed = []

    # input kastiga seonduv
    inputbox = pygame.Rect(600, 470, 70, 35)
    active = False  # kas tekstikast aktiivne
    text = ""
    color_active = pygame.Color("dodgerblue2")
    color_inactive = pygame.Color("lightskyblue3")
    color = color_inactive
    pakkumine = ""
    valedpakkumised = 0

    while True:
        kell.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        pakkumine = text
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # vordleb pakkumist sõnaga
        if len(pakkumine) == 1:
            if pakkumine in lists6na:
                if pakkumine not in arvatudtahed:
                    arvatudtahed.append(pakkumine)
                    pakkumine = ""
            else:
                if pakkumine not in pakutudtahed:
                    pakutudtahed.append(pakkumine)
                    valedpakkumised += 1
                pakkumine = ""
        elif len(pakkumine) > 1:
            if pakkumine == s6na:
                mangulopp("võitsid", s6na)
            else:
                valedpakkumised += 1
            pakkumine = ""

        ekraan.fill((255, 255, 255))

        # joonistab kriipsujuku
        # saast kood aga praegu toimib
        if valedpakkumised > 0:
            pygame.draw.line(ekraan, black, (70, 400), (70, 200), 2)
        if valedpakkumised > 1:
            pygame.draw.line(ekraan, black, (70, 200), (120, 200), 2)
        if valedpakkumised > 2:
            pygame.draw.line(ekraan, black, (120, 200), (120, 215), 2)
        if valedpakkumised > 3:
            pygame.draw.circle(ekraan, black, (120, 235), 20)
            pygame.draw.circle(ekraan, white, (120, 235), 18)
        if valedpakkumised > 4:
            pygame.draw.line(ekraan, black, (120, 255), (120, 325), 2)
        if valedpakkumised > 5:
            pygame.draw.line(ekraan, black, (80, 285), (160, 285), 2)
        if valedpakkumised > 6:
            pygame.draw.line(ekraan, black, (90, 355), (120, 325), 2)
        if valedpakkumised > 7:
            pygame.draw.line(ekraan, black, (150, 355), (120, 325), 2)
            pygame.draw.line(ekraan, black, (130, 240), (110, 240), 2)
            pygame.draw.line(ekraan, black, (116, 231), (110, 225), 2)
            pygame.draw.line(ekraan, black, (124, 231), (130, 225), 2)
            pygame.draw.line(ekraan, black, (116, 225), (110, 231), 2)
            pygame.draw.line(ekraan, black, (124, 225), (130, 231), 2)

            pygame.display.update()
            pygame.time.delay(1000)
            mangulopp("kaotasid", s6na)

        txt_surface = font.render(text, True, color)

        width = max(200, txt_surface.get_width() + 10)
        inputbox.w = width

        asukoht = 500
        for taht in pakutudtahed:
            t2ht = font.render(taht, True, black)
            ekraan.blit(t2ht, (asukoht, 100))
            asukoht += 30

        ekraan.blit(txt_surface, (inputbox.x + 5, inputbox.y + 5))
        pygame.draw.rect(ekraan, color, inputbox, 2)

        # joonistab kriipsu iga tähe kohta sõnas
        algus = 70
        for i in range(len(s6na)):
            pygame.draw.line(ekraan, black, (algus, 500), (algus+30, 500))
            algus += 40

        arvatud = 0
        for i, taht in enumerate(lists6na):
            if taht in arvatudtahed:
                t2ht = font.render(taht, True, black)
                pygame.draw.rect(ekraan, white, [70 + i * 40, 470, 40, 40])
                ekraan.blit(t2ht, (70 + i * 40, 470))
                arvatud += 1

        if arvatud == len(lists6na):
            mangulopp("võitsid", s6na)

        pygame.display.update()


def meny():             # genereerib menüü, kui mängu käima paned
    kell1 = pygame.time.Clock()
    while True:
        kell1.tick(FPS)
        mouse = pygame.mouse.get_pos()

        ekraan.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LAIUS/2 - 40 <= mouse[0] <= LAIUS/2 + 40 and KORGUS/2 - 15 <= mouse[1] <= KORGUS/2 + 15:
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


if __name__ == "__main__":
    meny()