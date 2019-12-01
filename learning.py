from copy import deepcopy
from numpy import random as np
import random


#every object of the class agent contains its servo values and fitness data
class agent ():

    #length -> number of value pairs; range -> tuple of lower and upper value
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

#returns an array of agents
def create_pop(pop_size, length, number_of_servos, value_range):
    pop=[]
    for _ in range(pop_size):
        pop.append(agent(length, number_of_servos, value_range))

    return pop



#give an array of agents and a mutation coefficient to mutate the population
def mutate(population, mutation_coefficient):
    mutated_agents=[]
    for agent in population:
        for i in range(len(agent)):
            mutation_agent_a=random.choice(population)
            mutation_agent_b=random.choice(population)
            agent.values[i]=agent[i]+mutation_coefficient*(mutation_agent_a[i]-mutation_agent_b[i])
        mutated_agents.append(agent)
    return mutated_agents
            
        

#give an array of agents and a quota of the to keep. The best agents will be selected
def select(population, quota_to_keep):
    score_coll=[]
    for agent in population:
        score_coll.append(agent.get_score())
    
    score_coll.sort()
    threshold=score_coll[(1-quota_to_keep)*len(score_coll)]

    for i in range(len(population)):
        if population[i].get_score() < threshold:
            del population[i]

    return population

#this fills the population with individuals which are a combination of two individuals till the desired amount is reached
def breed(population, desired_pop_size):
    #do it till the population is refilled
    while len(population)<desired_pop_size:
        choosing_index=True
        #create a source for values to choose from
        breed_agents_mix=tuple(zip(random.choice(population).get_values(), random.choice(population).get_values()))
        child=agent()
        #extend child.values
        for i in range(len(breed_agents_mix)):
            child.values.append(deepcopy(breed_agents_mix[i][int(choosing_index)]))
            #flip the source for the values with a 1/30 probability
            if random.randint(1, 30)==2:
                choosing_index = not choosing_index
        population.append(child)

    return population


if __name__ == "__main__":
    pop=create_pop(3, 4, 2, (1, 3))