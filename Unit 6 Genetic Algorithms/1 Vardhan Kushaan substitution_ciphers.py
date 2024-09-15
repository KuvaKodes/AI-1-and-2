import sys 
from math import log
import random

alphabet = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
alphabet_list = list(alphabet)

with open("n_grams.txt") as f:
    line_list = [line.strip().split() for line in f]
    n_gram_dict = dict()
    for n_gram, frequency in line_list:
        n_gram_dict[n_gram] = int(frequency)

def encode(text, cipher):
    output = ""
    text = text.upper()
    for character in text:
        encryption_ind = alphabet.find(character)
        if encryption_ind != -1:
            output += cipher[encryption_ind]
        else:
            output += character
    return output

#print(encode("Hello, Students!", "XRPHIWGSONFQDZEYVJKMATUCLB"))

def decode(text, cipher):
    output = ""
    text = text.upper()
    for character in text:
        decryption_ind = cipher.find(character)
        if decryption_ind != -1:
            output += alphabet[decryption_ind]
        else:
            output += character
    return output

#print(decode("SIQQE, KMAHIZMK!","XRPHIWGSONFQDZEYVJKMATUCLB"))

def fitness(n, encoded_text, candidate):
    fitness_score = 0
    decoded_text = decode(encoded_text, candidate)
    for index in range(0, len(decoded_text)):
        if decoded_text[index:index+n] in n_gram_dict.keys():
            fitness_score = fitness_score + log(n_gram_dict[decoded_text[index:index+n]],2)
    return fitness_score


def hill_climb(encoded_text):
    random_alphabet = list(alphabet)
    random.shuffle(random_alphabet)
    initial_fitness = fitness(4, encoded_text, ''.join(random_alphabet))
    while True: 
        swap_int_1 = random.randint(-1,25)
        swap_int_2 = random.randint(-1,25)
        new_alphabet = random_alphabet.copy()

        temp = new_alphabet[swap_int_1]
        new_alphabet[swap_int_1] = new_alphabet[swap_int_2]
        new_alphabet[swap_int_2] = temp

        new_fitness = fitness(4, encoded_text, ''.join(new_alphabet))
        if new_fitness > initial_fitness:
            initial_fitness = new_fitness
            random_alphabet = new_alphabet.copy()
            print(decode(encoded_text, ''.join(random_alphabet)), new_fitness)

#hill_climb("PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ- SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR.")

POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8

def genetic_algorithm(encoded_text):
    generation = 0 
    population = set()
    for i in range(POPULATION_SIZE):
        temp_list = alphabet_list.copy()
        random.shuffle(temp_list)
        population.add("".join(temp_list))
    while generation < 500:
        weighted_population = list()
        for candidate in population:
            weighted_population.append((fitness(4, encoded_text, candidate), candidate))
        weighted_population = sorted(weighted_population,reverse=True)
        print(decode(encoded_text, weighted_population[0][1]))
        next_gen = set()
        for i in range(NUM_CLONES):
            next_gen.add(weighted_population[i][1])
        while len(next_gen) < 500:
            full_tournament = random.sample(weighted_population, 2*TOURNAMENT_SIZE)
            tournament_1 = sorted(full_tournament[0:TOURNAMENT_SIZE], reverse=True)
            tournament_2 = sorted(full_tournament[TOURNAMENT_SIZE:], reverse=True)
            parent_1 = ""
            parent_2 = ""
            for parent_candidate_1 in tournament_1:
                if random.random() < TOURNAMENT_WIN_PROBABILITY:
                    parent_1 = parent_candidate_1[1]
                    break
                else:
                    continue
            for parent_candidate_2 in tournament_2:
                if random.random() < TOURNAMENT_WIN_PROBABILITY:
                    parent_2 = parent_candidate_2[1]
                    break
                else:
                    continue
            child = [None] * 26
            for i in range(0, CROSSOVER_LOCATIONS):
                crossover = random.randint(-1,25)
                child[crossover] = list(parent_1)[crossover]
            for character in list(parent_2):
                if character in child:
                        continue
                else:
                    for i in range(0,26):
                        if child[i] is None:
                            child[i] = character
                            break
                        else:
                            continue
            if random.random() < MUTATION_RATE:
                swap_index_1, swap_index_2 = random.randint(-1,25), random.randint(-1,25)
                temp = child[swap_index_1]
                child[swap_index_1] = child[swap_index_2]
                child[swap_index_2] = temp
            next_gen.add("".join(child))
        population = next_gen.copy()
        generation = generation + 1
    
genetic_algorithm("PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR QBA'G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR.")


        