import random as rnd

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


#for i in range(len(lahendada)):
    #print(lahendada[i])


def reeglikontroll(nr, grid, rida, veerg):
    
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
    for i in range(len(grid[alarida*3:alarida*3+2])):
        for j in range(len(grid[alarida*3:alarida*3+2][i][alaveerg*3:alarida*3+2])):
            if grid[alarida*3:alarida*3+2][i][alaveerg*3:alarida*3+2][j] == nr:
                count += 1
    if count >= 2:
        return False

    return True

ruudustik = [[3, 5, 6, 1, 7, 9, 2, 8, 4],
[1, 7, 9, 8, 4, 2, 6, 3, 5],
[8, 4, 2, 3, 5, 6, 9, 1, 7],
[4, 9, 1, 5, 2, 8, 3, 7, 6],
[7, 6, 3, 4, 9, 1, 8, 5, 2],
[5, 2, 8, 7, 6, 3, 1, 4, 9],
[9, 3, 7, 2, 1, 4, 5, 6, 8],
[6, 8, 5, 9, 3, 7, 4, 2, 1],
[2, 1, 4, 6, 8, 5, 7, 9, 3]]

print(reeglikontroll(3, ruudustik, 0 ,0))
