from copy import deepcopy
import numpy as np
import random


#every object of the class agent contains its servo values and fitness data
class control_agent:

    #length -> number of value pairs; range -> tuple of lower and upper value; if no arguments were given it creates a "blueprint agent"
    def __init__(self, length=0, number_of_servos=0, range=0):
        self.score=0
        if range is not 0:
            self.values=np.random.random((length, number_of_servos))*(range[1]-range[0])+range[0]
        else:
            self.values=[]

    def set_score(self, new_score):
        self.score = new_score

    def get_score(self):
        return self.score

    def get_values(self):
        return self.values



"""returns an array of new agents"""

def create_pop(pop_size, length, number_of_servos, value_range):
    pop=[]
    for _ in range(pop_size):
        pop.append(control_agent(length, number_of_servos, value_range))

    return pop


#give an array of agents and a mutation coefficient to mutate the population
def mutate(population, mutation_coefficient):
    mutated_agents=[]
    #do it for each individual
    for agent in population:
        #do it for each round
        for i in range(len(agent.values)):
            #choose two mutation "partners" (->DIFFERENTIAL evolut...)
            mutation_agent_a=random.choice(population).values
            mutation_agent_b=random.choice(population).values
            #change the value
            agent.values[i]=agent.values[i]+mutation_coefficient*(mutation_agent_a[i]-mutation_agent_b[i])
        #append the mutated agent
        mutated_agents.append(agent)
    return mutated_agents
            
        

#give an array of agents and a quota of the to keep. The best agents will be selected
def select(population, quota_to_keep):
    #collect all the appearing score values
    score_coll=[]
    for agent in population:
        score_coll.append(agent.get_score())
    
    #select the threshold for "survival"
    score_coll.sort()
    threshold=score_coll[round((1-quota_to_keep)*len(score_coll))]

    #delete all the unlucky ones
    for agent in population:
        if agent.get_score() < threshold:
            population.remove(agent)

    return population


#this is meant to be an alternative to the build-in zip() function because it has problems with multidimensional objects
def altzip(a, b):
    if len(a)!=len(b):
        print("dumbass, they are supposed to have an equal length")
    else:
        result=[]
        for i in range(len(a)):
            result.append([a[i], b[i]])
        return result



"""this fills the population with individuals which are a combination of two individuals till the desired amount is reached"""

def breed(population, desired_pop_size, average_genome_piece_length):
    #do it till the population is refilled
    while len(population)<desired_pop_size:
        choosing_index=True
        #create a source for values to choose from
        breed_agents_mix=altzip(random.choice(population).get_values(), random.choice(population).get_values())
        child=control_agent()
        #extend child.values
        for i in range(len(breed_agents_mix)):
            #choose the values to append and add them
            new_values=deepcopy(breed_agents_mix[i][int(choosing_index)])
            child.values.append(new_values)
            #flip the source for the values with a 1/30 probability
            if random.randint(1, average_genome_piece_length)==2:
                choosing_index = not choosing_index
        child.values=np.array(child.values)
        population.append(child)
    
    return population


if __name__ == "__main__":
    pop=create_pop(3, 4, 2, (1, 3))
    #for i in range(len(pop)):
    #    pop[i].set_score(i+4)
    pop=select(pop, 0.5)

    #for agent in pop:
    #    print(agent.get_values())


    pop=breed(pop, 4, 4)

    for agent in pop:
        print(agent.get_values())

    print("mutate")

    pop=mutate(pop, 0.8)

    for agent in pop:
        print(agent.get_values())