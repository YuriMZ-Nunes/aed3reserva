from random import randint

INT_MAX = 2147483647

V = 11

GENES = "ABCDEFGHIJK"

START = 0

POP_SIZE = 10



# 
class individual:
    def __init__(self) -> None:
        self.gnome = ""
        self.fitness = 0
        
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness


# function to return a randon number from start and end
def rand_num(start, end):
    return(randint(start, end - 1))

# function to check if  the character has already occured in the string
def repeat(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return True
    return False

# Function to return a mutate GNOME
# Mutate GNOME is a str w/ a random interchange of two genes to create a variation in species 
def mutatedGene(gnome):
    gnome = list(gnome)
    while True:
        r = rand_num(1, V)
        r1 = rand_num(1, V)
        if r != r1:
            temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return ''.join(gnome)

# Function to return a valid GNOME string
# required to create the population
def create_gnome():
    gnome = "0"
    while True:
        if(len(gnome) == V):
            gnome += gnome[0]
            break
        temp = rand_num(1, V - 1)
        if not repeat(gnome, chr(temp + 48)):
            gnome += chr(temp + 48)
            
    return gnome

# Function to return the fitness value of a gnome
# The fitness value is the path length
def cal_fitness(gnome):
    mp = matrix
    print(mp)
    f = 0
    for i in range(len(gnome) - 1):
        if mp[ord(gnome[i] - 48)][ord(gnome[i + 1]) - 48] == INT_MAX:
            return INT_MAX
        f += mp[ord(gnome[i] - 48)][ord(gnome[i + 1]) - 48]
    
    return f

# Function to return the updated value of the cooling element
def cooldown(temp):
    return (90 * temp) / 100

def TSPUtil(mp):
    gen = 1
    gen_thres = 5
    population = []
    temp = individual()
    
    for i in range(POP_SIZE):
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)
        
    print("\nInitial population: \nGNOME     FITNESS VALUE\n")
    
    for i in range(POP_SIZE):
        print(population[i].gnome. population[i].fitness)
    print()
    
    found = False
    temperature = 10000
    
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nCurrent temp: ", temperature)
        new_population = []
        
        for i in range(POP_SIZE):
            p1 = population[i]
            
            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome)
                
                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break
                else:
                    prob = pow(2.7, -1 * ((float)(new_gnome.fitness - population[i].fitness) / temperature))
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break
        temperature = cooldown(temperature)
        population = new_population
        print("Generation ", gen)
        print("GNOME     FITNESS VALUE")
        
        for i in range(POP_SIZE):
            print(population[i].gnome, population[i].fitness)
        gen += 1
                        
with open('tsp_data/tsp1_253.txt', 'r') as matrixTxt:
    lines = matrixTxt.readlines()
        
matrix = [[0] * len(lines) for _ in range(len(lines))]

for i, line in enumerate(lines):
    values = [int(x) for x in line.split()]
    matrix[i] = values
    
TSPUtil(matrix)