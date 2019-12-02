import observation
import learning
import servo

#create the population
agents=learning.create_agents(100, 100, 3, (3, 14))

#for explanation read the comment at the bottom
try:
    round=0
    while True:
        print("round "+str(round)+" done")
        #evaluate + set score

        #select the best ones
        agents=learning.select(agents, 0.2)

        #breed
        agents=learning.breed(agents, 100, 30)

        #mutation
        agents=learning.mutate(agents, 0.8)

        #save it every 20 rounds
        if i%20=0:
            
            #save population
        
        i+=1

except KeyboardInterrupt:
    #to end the servos
    servo.end()

servo.end()