import pygame
import sys

pygame.init()

LAIUS, KÕRGUS = 540, 540
RUUDU_SUURUS = LAIUS // 9

VALGE = (255, 255, 255)
MUST = (0, 0, 0)
SININE = (67, 92, 124)
LILLA_PUNANE = (153, 1, 71)

# init
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("Sudoku pela in HINDI2025 GTA7LEAK")

# tstlaud
sudoku_laud = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

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
    for i in range(9):
        for j in range(9):
            if sudoku_laud[i][j] != 0:
                arv = font.render(str(sudoku_laud[i][j]), True, MUST)
                x = j * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_width() // 2
                y = i * RUUDU_SUURUS + RUUDU_SUURUS // 2 - arv.get_height() // 2
                ekraan.blit(arv, (x, y))

def joonista_valitud_ruut(valitud_ruut):
    i, j = valitud_ruut
    pygame.draw.rect(ekraan, LILLA_PUNANE, (j * RUUDU_SUURUS, i * RUUDU_SUURUS, RUUDU_SUURUS, RUUDU_SUURUS), 3)

kell = pygame.time.Clock()
valitud_ruut = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hiireX, hiireY = pygame.mouse.get_pos()
            valitud_ruut = (hiireY // RUUDU_SUURUS, hiireX // RUUDU_SUURUS)

    ekraan.fill(VALGE)
    joonista_ruudustik()
    joonista_arvud()
    joonista_3ruudu_suurus()

    if valitud_ruut:
        joonista_valitud_ruut(valitud_ruut)

    pygame.display.flip()
    kell.tick(60)
