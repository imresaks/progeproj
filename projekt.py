import random

import pygame

laius=400
kõrgus=400
ruudustiku_suurus=9

def main():
    pygame.init()
    aken=pygame.display.set_mode((laius, kõrgus))
    #aken.fill('white')

    # ruudustiku loomine
    ruudustik=[[0 for i in range(ruudustiku_suurus)] for j in range(ruudustiku_suurus)]

    # täidab random numbritega
    for i in range(ruudustiku_suurus):
        for j in range(ruudustiku_suurus):
            ruudustik[i][j] = int(random.randint(1, 9))

    aken.fill((0, 0, 0))
    for i in range(ruudustiku_suurus):
        for j in range(ruudustiku_suurus):
            pygame.draw.rect(aken, (255, 255, 255), (i * 50, j * 50, 50, 50))
            #if ruudustik[i][j] != 0:
                #pygame.draw.(aken, str(ruudustik[i][j]), (i * 50 +25, j * 50 + 25), (0, 0, 0))
    pygame.display.update()
while True:
    main()