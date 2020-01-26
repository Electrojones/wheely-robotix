import observation
import learning
import servo
from datetime import datetime
import pickle
import numpy
import math

pop_size=30

#create the population
agents=learning.create_pop(pop_size, 5, 6, (2, 12))

print("initiated")

#for explanation read the comment at the bottom
try:
    round=0
    while True:
        print("currently at the "+str(round)+"th cycle")

        #go through every agent
        for i in range(len(agents)):

            score_coll=[]

            print("agent: "+str(i), end='')

            #reset the servos
            servo.set_servos((7, 7, 7, 7, 7, 7))
            servo.pause()
            #print("reset servos")

            #get the starting coordinates
            starting_pos, _ = observation.get_marker_pos()

            #print("saved pos")

            #cycle through all 20 angle sets for 6 times
            servo.set_servos_array(agents[i].get_values(), 0)
            servo.set_servos_array(agents[i].get_values(), 0)
            servo.set_servos_array(agents[i].get_values(), 0)
            servo.set_servos_array(agents[i].get_values(), 0)
            servo.set_servos_array(agents[i].get_values(), 0)
            servo.set_servos_array(agents[i].get_values(), 0)

            #print("cycled through")

            servo.pause()

            #get the end coordinates    
            end_pos, _ = observation.get_marker_pos()

            #print("got new pos")

            #calculate the distance traveled
            distance_vector = numpy.subtract(starting_pos, end_pos)
            distance = math.sqrt(distance_vector[0]**2+distance_vector[1]**2)    
            
            #give the agent object the result
            agents[i].set_score(distance)

            print(" score: "+str(distance))

            score_coll.append(distance)

        #select the best ones
        agents=learning.select(agents, 0.2)

        #breed
        agents=learning.breed(agents, pop_size, 5)

        #mutation
        agents=learning.mutate(agents, 0.4)

        print("the average score was: "+sum(score_coll)/len(score_coll))

        #save it at every 2nd cycle
        if round%2==0:
            dateTimeObj = datetime.now()
            timestamp = dateTimeObj.strftime("%d-%b-%Y_(%H:%M:%S.%f)")
            writer=open("population_pickles/"+timestamp, 'wb')
            pickle.dump(agents, writer)
        
        round+=1

except KeyboardInterrupt:
    #to end the servos
    servo.end()
    #to save the file
    dateTimeObj = datetime.now()
    timestamp = dateTimeObj.strftime("%d-%b-%Y_(%H:%M:%S.%f)")+"_Keyboardinterrupt"
    writer=open("population_pickles/"+timestamp, 'wb')
    pickle.dump(agents, writer)

servo.end()
