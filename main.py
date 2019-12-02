import observation
import learning
import servo

#create the population
pop=learning.create_pop(100, 100, 3, (3, 14))

#for explanation read the comment at the bottom
try:
    i=0
    while True:
        print("round "+str(i)+" done")
        #evaluate + set score

        #select the best ones
        pop=learning.select(pop, 0.2)
        #breed
        
        #mutation

        #if condition
            #save population
        
        i+=1

except KeyboardInterrupt:
    #to end the servos
    servo.end()