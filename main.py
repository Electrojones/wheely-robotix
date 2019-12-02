import observation
import learning
import servo
from datetime import datetime
import pickle

#create the population
agents=learning.create_agents(100, 100, 3, (3, 14))

#for explanation read the comment at the bottom
try:
    round=0
    while True:
        print("round "+str(round)+" done")
        #evaluate + set score

        #for agent in agents:
            #do it 100 times
                #set the servo angles
                #wait a specific time
            #pythagaros the distance
            #set it to the agent


        #select the best ones
        agents=learning.select(agents, 0.2)

        #breed
        agents=learning.breed(agents, 100, 30)

        #mutation
        agents=learning.mutate(agents, 0.8)

        #save it every 20 rounds
        if round%20==0:
            dateTimeObj = datetime.now()
            timestamp = dateTimeObj.strftime("%d-%b-%Y_(%H:%M:%S.%f)")
            writer=open(timestamp, 'wb')
            pickle.dump(agents, writer)
            #save population
        
        round+=1

except KeyboardInterrupt:
    #to end the servos
    servo.end()

servo.end()