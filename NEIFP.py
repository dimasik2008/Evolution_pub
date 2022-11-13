import random
import numpy

def crbp(size:int,dnas:int) -> list:
    o = []
    o = numpy.random.randint(2, size=(size,dnas))
    return o.tolist()

def czbp(size:int,dnas:int) -> list:
    o = []
    o = numpy.zeros((size,dnas),dtype=int)
    return o.tolist()
    

def cobp(size:int,dnas:int) -> list:
    o = []
    o = numpy.ones((size,dnas),dtype=int)
    return o.tolist()
    

def mutate_b(population:list,) -> list:
    mutdivid = random.randint(1,len(population)-1)
    mutgene = random.randint(0,len(population[0])-1)
    population[mutdivid][mutgene] = 1 if population[mutdivid][mutgene] == 0 else 0
    return population

def calc_power(individ:list,env:list) -> int:
    if len(individ) != len(env):
        raise IndexError
    o = 0
    for index,item in enumerate(individ):
        if item:
            o += env[index]
    return o

def pair_i(individ0:list,individ1:list) -> list:
    if len(individ0) != len(individ1):
        raise IndexError
    dnalen = len(individ0)-1
    new = []
    rand_slice = random.randint(0,dnalen)
    new.append(individ0[:rand_slice] + individ1[rand_slice:])
    
    rand_slice = random.randint(0,dnalen)
    new.append(individ1[:rand_slice] + individ0[rand_slice:])
    
    return new

