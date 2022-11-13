# 0 gene - Has wings 
# 1 gene - Has legs
# 2 gene - Has arms 
# 3 gene - Is stupid

DNALEN = 4
MAXPOWER = 4
MUTATCHANSE = 0.1
POPULATIONLEN = 4
import random
from NEIFP import *
import logging

logging.basicConfig(level=logging.DEBUG)

env = [2,1,1,-2]

  
def view_indivd(individ:list,power:int):
    
    print(f"Has wings  - {bool(individ[0])}")
    print(f"Has legs- {bool(individ[1])}")
    print(f"Has arms  - {bool(individ[2])}")
    print(f"Is stupid - {bool(individ[3])}")
    
    print(f"Total power - {power}")

# now_population = [create_individ() for i in range(4)]
now_population = czbp(POPULATIONLEN,DNALEN)
epoch = 0

while True:  
    #increment epoch
    epoch += 1
    #stores whether there was a mutation
    mutation = False
    #calc power
    powers = [(calc_power(individ,env),index) for index,individ in enumerate(now_population)]
    #sorting tuples usinf 0 element 
    powers.sort(key=lambda tup: tup[0])
    #mutation
    if random.random() < MUTATCHANSE:
        mutation = True
        now_population = mutate_b(now_population)

    new_population = []
    
    #create 1 child
    new_population += pair_i(now_population[0],now_population[1])

    #create 2 child
    new_population += pair_i(now_population[0],now_population[2])
    
    #create 3 child
    new_population += pair_i(now_population[1],now_population[0])

    #create 4 child
    new_population += pair_i(now_population[2],now_population[0])

    now_population = new_population
    #write logs
    logging.debug(f"Epoch - {epoch} Population - {now_population} Top - {now_population[powers[0][1]]} Mutatuion - {mutation}")
        
    
    #check if population is finished
    if powers[0][0] == MAXPOWER:
        break
    
print("Max power population:")
print(now_population)
print("Best individ:")
view_indivd(now_population[powers[0][1]],calc_power(now_population[powers[0][1]],env))