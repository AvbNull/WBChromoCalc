import math
import random
import statistics

GENE_STATS_LIST = [
    [1, 10, 50, 100, 300],  # 0: Health
    [10, 50, 100],          # 1: Stamina
    [1, 6, 10],             # 2: Damage
    [1, 6, 10],             # 3: Armor
    [1, 2, 5],              # 4: Speed
    [1, 2, 3],              # 5: Diplomacy
    [1, 2, 3],              # 6: Warfare
    [1, 2, 3],              # 7: Stewardship
    [1, 2, 3],              # 8: Intelligence
    [5, 20, 50, 100],       # 9: Lifespan
    [1, 3, 5, 10],          # 10: Offspring
    [1],                    # 11: Birth Rate
    [1],                    # 12: Male Bonus
    [1],                    # 13: Female Bonus
    [1],                    # 14: Mutagenic
    [1]                     # 15: Harmful
]
CUSTOM_GENOME = [
            0,   # 0: health
            0,   # 1: stamina
            0,   # 2: damage
            0,   # 3: armor
            0,   # 4: speed
            0,   # 5: diplomacy
            0,   # 6: warfare
            0,   # 7: stewardship
            0,   # 8: intelligence
            0,   # 9: lifespan
            0,   # 10: offspring
            0,   # 11: birth rate
            0,   # 12: randomsex
            0,   # 13: mutagenic
            0   # 14: harmful
]
CHROMOSOME_SIZES = [
            30,   # 0: big
            24,   # 1: medium
            18,   # 2: small
            12,   # 3: tiny
]
skipcalc = 0
largechromoconstant = 25 #Largest Chromosome: Size Big (30), Min Amplifiers (-1), Min Empty Loci (-4)
smallchromoconstant = 7  #Smallest Chromosome: Size Tiny (12), Max Amplifiers (-2), Max Empty Loci (-3)

def findMinLoci():
    global skipcalc
    skipcalc -= 1
    statindex = 0
    lociamount = 0
    for stat in CUSTOM_GENOME:
        if stat == 0:
            statindex += 1
        else:
            genelevelindex = -1
            savestat = stat
            while savestat != 0 and genelevelindex >= -len(GENE_STATS_LIST[statindex]):
                lociamount += savestat//GENE_STATS_LIST[statindex][genelevelindex]
                lastlociamount = savestat//GENE_STATS_LIST[statindex][genelevelindex]
                savestat = savestat - (lastlociamount*GENE_STATS_LIST[statindex][genelevelindex])
                genelevelindex -= 1
            statindex += 1
    return lociamount

def findMaxLoci():
    global skipcalc
    skipcalc -= 1
    statindex = 0
    lociamount = 0
    for stat in CUSTOM_GENOME:
        if stat == 0:
            statindex += 1
        else:
            genelevelindex = 0
            savestat = stat
            print(f"Index: {statindex} is {stat} stat")
            while savestat != 0:
                lociamount += savestat//GENE_STATS_LIST[statindex][genelevelindex]
                lastlociamount = savestat//GENE_STATS_LIST[statindex][genelevelindex]
                savestat = savestat - (lastlociamount*GENE_STATS_LIST[statindex][genelevelindex])
                genelevelindex += 1
            statindex += 1
    return lociamount

def findNormalLoci():
    global skipcalc
    skipcalc -= 1
    statindex = 0
    lociamount = 0
    priority = 0
    for stat in CUSTOM_GENOME:
        if stat == 0:
            statindex += 1
        else:
            if random.random() < 0.8 or priority == 1:
                priority = 1
                savestat = stat
                genelevelindex = -1
                while savestat != 0  and genelevelindex >= -len(GENE_STATS_LIST[statindex]):
                    lociamount += savestat//GENE_STATS_LIST[statindex][genelevelindex]
                    lastlociamount = savestat//GENE_STATS_LIST[statindex][genelevelindex]
                    savestat = savestat - (lastlociamount*GENE_STATS_LIST[statindex][genelevelindex])
                    genelevelindex -= 1
                statindex += 1
            else:
                savestat = stat
                while savestat != 0:
                    randomchosenlevelindex = random.randint(0, len(GENE_STATS_LIST[statindex])-1)
                    if savestat//GENE_STATS_LIST[statindex][randomchosenlevelindex] >= 1:
                        lociamount += 1
                        lastlociamount = 1
                        savestat = savestat - GENE_STATS_LIST[statindex][randomchosenlevelindex]
                statindex += 1
    return lociamount

def generateChromosome():
    chosenchromoloci = random.choice(CHROMOSOME_SIZES)
    amplifers = 0
    empty_loci = 0
    if chosenchromoloci == 30:
        amplifers = random.randint(1,4)
        empty_loci = random.randint(4,8)
    elif chosenchromoloci == 24:
        amplifers = random.randint(1,3)
        empty_loci = random.randint(3,5)
    elif chosenchromoloci == 18:
        amplifers = random.randint(1,3)
        empty_loci = random.randint(2,4)
    elif chosenchromoloci == 12:
        amplifers = random.randint(0,2)
        empty_loci = random.randint(1,3)
    avalibloci = chosenchromoloci - (amplifers + empty_loci)
    return avalibloci


print("Input genome:")
print("(H) Health")
print("(S) Stamina")
print("(D) Damage")
print("(A) Armor")
print("(Sp) Speed")
print("(Dp) Diplomacy")
print("(Wf) Warfare")
print("(St) Stewardship")
print("(In) Intelligence")
print("(L) Lifespan")
print("(O) Offspring")
print("(B) Birth Rate")
print("(Rg) Random Sex Gene")
print("(Mg) Mutagenic Gene")
print("(Hg) Harmful Gene")

while True:
    # take input from the user         
    choice = input("Enter choice(H/S/D/A...): ")

    # check if choice is one of the four options
    if choice in ('H', 'h', 'S', 's', 'D', 'd', 'A', 'a', 'Sp', 'sp', 'Dp', 'dp', 'Wf', 'wf', 'St', 'st', 'In', 'in', 'L', 'l', 'O', 'o', 'B', 'b', 'Rg', 'Mg', 'Hg', 'ALL', 'skip'):
        
        try:
            if choice == 'H' or choice == 'h':
                CUSTOM_GENOME[0] = int(input("Enter health value: "))
            elif choice == 'S' or choice == 's':
                CUSTOM_GENOME[1] = int(input("Enter stamina value: "))
            elif choice == 'D' or choice == 'd':
                CUSTOM_GENOME[2] = int(input("Enter damage value: "))
            elif choice == 'A' or choice == 'a':
                CUSTOM_GENOME[3] = int(input("Enter armor value: "))
            elif choice == 'Sp' or choice == 'sp':
                CUSTOM_GENOME[4] = int(input("Enter speed value: "))
            elif choice == 'Dp' or choice == 'dp':
                CUSTOM_GENOME[5] = int(input("Enter diplomacy value: "))
            elif choice == 'Wf' or choice == 'wf':
                CUSTOM_GENOME[6] = int(input("Enter warfare value: "))
            elif choice == 'St' or choice == 'st':
                CUSTOM_GENOME[7] = int(input("Enter stewardship value: "))
            elif choice == 'In' or choice == 'in':
                CUSTOM_GENOME[8] = int(input("Enter intelligence value: "))
            elif choice == 'L' or choice == 'l':
                CUSTOM_GENOME[9] = int(input("Enter lifespan value: "))
            elif choice == 'O' or choice == 'o':
                CUSTOM_GENOME[10] = int(input("Enter offspring value: "))
            elif choice == 'B' or choice == 'b':
                CUSTOM_GENOME[11] = int(input("Enter birth rate value: "))
            elif choice == 'Rg':
                CUSTOM_GENOME[12] = int(input("Enter random sex gene amount: "))
            elif choice == 'Mg':
                CUSTOM_GENOME[13] = int(input("Enter mutagenic gene amount: "))
            elif choice == 'Hg':
                CUSTOM_GENOME[14] = int(input("Enter harmful gene amount: "))
            elif choice == "ALL": # made for using source of the Creature Genomes wb wiki page
                allstats = str(input("Enter genes: "))
                parts = allstats.split('|', 15)
                dashzero_parts = [part.replace(' -', '0') for part in parts]
                CUSTOM_GENOME[0] = int(dashzero_parts[1])
                CUSTOM_GENOME[1] = int(dashzero_parts[2])
                CUSTOM_GENOME[2] = int(dashzero_parts[3])
                CUSTOM_GENOME[3] = int(dashzero_parts[4])
                CUSTOM_GENOME[4] = int(dashzero_parts[5])
                CUSTOM_GENOME[5] = int(dashzero_parts[6])
                CUSTOM_GENOME[6] = int(dashzero_parts[7])
                CUSTOM_GENOME[7] = int(dashzero_parts[8])
                CUSTOM_GENOME[8] = int(dashzero_parts[9])
                CUSTOM_GENOME[9] = int(dashzero_parts[10])
                CUSTOM_GENOME[10] = int(dashzero_parts[11])
                CUSTOM_GENOME[11] = int(dashzero_parts[12])
                CUSTOM_GENOME[12] = int(dashzero_parts[13])
                CUSTOM_GENOME[13] = int(dashzero_parts[14])
                CUSTOM_GENOME[14] = int(dashzero_parts[15])
        except ValueError:
            print("Invalid input. Please enter one of the provided choices.")
            continue

    calcChoice = input("Enter choice(MinL/MaxL/MinC/MaxC/SimNormal/SimAdvanced/GeneralChromoSize/add/end): ")

    if calcChoice in ('MinL', 'MaxL', 'MinC', 'MaxC', 'SimNormal', 'SimAdvanced', 'GeneralChromoSize', 'add', 'end'):
        try:
            if calcChoice == 'MinL':
                print(f"Minimum Loci for current genome is {findMinLoci()}")
            if calcChoice == 'MaxL':
                print(f"Maximum Loci for current genome is {findMaxLoci()}")
            if calcChoice == 'MinC':
                lociamount = findMinLoci()
                chromoresult = math.ceil(lociamount/largechromoconstant)
                print(f"Minimum Chromosomes for current genome is {chromoresult}")
            if calcChoice == 'MaxC':
                lociamount = findMaxLoci()
                chromoresult = math.ceil(lociamount/smallchromoconstant)
                print(f"Minimum Chromosomes for current genome is {chromoresult}")
            if calcChoice == 'SimNormal':
                averageFromSims = int(input("Enter choice(times to sim [average]): "))
                averageLoci = 0
                tempnormalloci = 0
                sdlist = []
                for i in range(averageFromSims):
                    tempnormalloci = findNormalLoci()
                    averageLoci += tempnormalloci
                    sdlist.append(tempnormalloci)
                sdlist_sd = statistics.stdev(sdlist)
                print(f"Simulated Average Loci for current genome was {averageLoci/averageFromSims} in this instance\nStandard Deviation was {sdlist_sd}")
            if calcChoice == 'SimAdvanced':
                averageFromSims = int(input("Enter choice(times to sim [average]): "))
                zscoreTarget = int(input("Enter target for z-score: "))
                averageLoci = 0
                tempnormalloci = 0
                sdlist = []
                for i in range(averageFromSims):
                    tempnormalloci = findNormalLoci()
                    averageLoci += tempnormalloci
                    sdlist.append(tempnormalloci)
                sdlist_sd = statistics.stdev(sdlist)
                print(f"Simulated Average Loci for current genome was {averageLoci/averageFromSims} in this instance\nStandard Deviation was {sdlist_sd}\nZ-Score is {(zscoreTarget-(averageLoci/averageFromSims))/sdlist_sd}")
            if calcChoice == 'GeneralChromoSize':
                averageFromGen = int(input("Enter choice(times to sim [average]): "))
                averageChromo = 0
                for i in range(averageFromGen):
                    averageChromo += generateChromosome()
                print(f"Simulated Chromosome Loci Space was {averageChromo/averageFromGen} in this instance [unrelated to inputted genome]")
            if calcChoice == 'add':
                skipcalc = 1
            if calcChoice == 'end':
                break
        except ValueError:
            print("Invalid input. Please enter one of the provided calculations.")
            continue
    
        if skipcalc == 0:
            next_calculation = input("Start a new calculation? (yes/no): ")
            if next_calculation == "no":
                break
    else:
        print("Invalid Input")
