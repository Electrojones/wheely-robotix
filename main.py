import observation
import learning
import servo
from datetime import datetime
import pickle
import numpy
import math

#create the population
agents=learning.create_pop(100, 20, 6, (2, 12))

#for explanation read the comment at the bottom
try:
    round=0
    while True:
        print("round "+str(round)+" done")

        #go through every agent
        for i in range(len(agents)):

            #get the starting coordinates
            starting_pos, _ = observation.get_marker_pos()

            #cycle through all 20 angle sets
            servo.set_servos_array(agents[i].get_values(), 0.1)

            #get the end coordinates    
            end_pos, _ = observation.get_marker_pos()

            #calculate the distance traveled
            distance_vector = numpy.subtract(starting_pos, end_pos)
            distance = math.sqrt(distance_vector[0]**2+distance_vector[1]**2)    
            
            #give the agent object the result
            agents[i].set_score(distance)


        #select the best ones
        agents=learning.select(agents, 0.2)

        #breed
        agents=learning.breed(agents, 100, 5)

        #mutation
        agents=learning.mutate(agents, 0.8)

        #save it at every 20th cycle
        if round%20==0:
            dateTimeObj = datetime.now()
            timestamp = dateTimeObj.strftime("%d-%b-%Y_(%H:%M:%S.%f)")
            writer=open(timestamp, 'wb')
            pickle.dump(agents, writer)
        
        round+=1

except KeyboardInterrupt:
    #to end the servos
    servo.end()
    dateTimeObj = datetime.now()
    timestamp = dateTimeObj.strftime("%d-%b-%Y_(%H:%M:%S.%f)")+"_Keyboardinterrupt"
    writer=open(timestamp, 'wb')
    pickle.dump(agents, writer)

servo.end()