#This is a small simulation of Air Traffic Control using 100 planes in python.
#All the measurements of distance are in nautical miles (nm). I have tried using 
#variables which can be understood by reading the names and comments are placed
#through out code explaining it
import random
import math

class flight:
    #Initiate flight with random values first is the number in a sequence
    def __init__(self,num):
        self.num=num
        #Position of flight can be between -128 to 128 
        self.x_pos=random.randint(-128,128)
        self.y_pos=random.randint(-128,128)
        #Velocity can be between 30 and 600
        self.velocity=random.randint(30,600)
        #angle can be between 0 and 360 degrees and adding small value in range [0,1) for float value
        self.angle=random.randrange(0,361)+random.random()
        #rounding off angle to 3 decimal places
        self.angle=round(self.angle,3)
        #here dx and dy are the distance travelled by plane in x and y direction for every 0.5 second
        self.dx=(self.velocity * math.cos(math.radians(self.angle)))/7200
        self.dy=(self.velocity * math.sin(math.radians(self.angle)))/7200
        #altitude can be between 3000 and 6000
        self.altitude=random.randint(3000,6000)
        #x_pos_new and y_pos_new are future plane positions after 0.5 seconds
        self.x_pos_new=self.x_pos+self.dx
        self.y_pos_new=self.y_pos+self.dy
    def flight_trace(self,trace_periods):
        #This runs the planes for trace_periods number of periods and each period is for 8 seconds
        i=0#here i and time_counter are just counters for periods and seconds in this period
        time_counter=0.5
        while i<trace_periods:
            i+=1
            while time_counter<=8:
                #updating positions each 0.5 seconds with dx and dy
                self.x_pos=self.x_pos_new
                self.y_pos=self.y_pos_new
                self.x_pos_new+=self.dx
                self.y_pos_new+=self.dy
                if(self.x_pos_new<=-128 or self.x_pos_new>=128 or self.y_pos_new<=-128  or self.y_pos_new>=128):
                    self.x_pos_new=-self.x_pos_new
                    self.y_pos_new=-self.y_pos_new
                time_counter+=0.5

#Initialize 100 flights with random initial values
Flight=[flight(i) for i in range(100)]

#A function to print some of the parameters of all flights at once, I did not print all parameters just to avoid long output
def print_flights(Flight):
    for i in range(100):
        #Here .3f is used to print only 3 decimal places in output, the value in variable is preserved
        print "{0}, {1:.3f}, {2:.3f}, {3:.3f}".format(Flight[i].num, Flight[i].x_pos, Flight[i].dx, Flight[i].x_pos_new)        

#printing flights
print_flights(Flight)

#running flights
for i in range(100):
    Flight[i].flight_trace(100)

print "\n\n"
#printing flights after running for 100 periods
print_flights(Flight)
print "\n\n"

#detect if any conflict between flight1 and flight2 
#here Flight is a list of objects of type flight where as Flight1, Flight2 are objects of class flight
def conflict_detect(Flight1,Flight2):
    #a conflict is detected if flights are closer than 2000 in altitude
    #and closer than 1.5 nm in both x and y directions abs is function for
    #absolute value in int and math.fabs is absolute values of floats
    if (abs(Flight1.altitude-Flight2.altitude)<2000 and Flight1.num!=Flight2.num):
        if (math.fabs(Flight1.x_pos_new - Flight2.x_pos_new) <= 1.5 and math.fabs(Flight1.y_pos_new - Flight2.y_pos_new) <= 1.5):
            print "Conflict detected between", Flight1.num, "and", Flight2.num
            #if conflict detected returns 1 else 0
            return 1
        else:
            return 0
    else:
        return 0

#conflict avoidance
#I have included output where I could successfully avoid conflict in a seperate ATC_output.txt file.
#conflicts are being detected easily but only some are being avoided. I think this is because we 
#need to turn the flight at a greater angle, but researching online I found that generally the turns are less than 
#6-8 degrees at a time, so i left my program at 10 degrees and occasionally I could avoid conflict 
#breaking out of the code
for i in range(100):
    for j in range(i+1,100):
        #testing each plane against every other
        num_conflict=0
        while (conflict_detect(Flight[i],Flight[j])):
            num_conflict+=1
            if num_conflict <= 10:
                #trying to turn plane in one direction and updating it's future position accordingly
                Flight[i].angle+=10
                Flight[i].dx=(Flight[i].velocity * math.cos(math.radians(Flight[i].angle)))/7200
                Flight[i].dy=(Flight[i].velocity * math.sin(math.radians(Flight[i].angle)))/7200                
                Flight[i].x_pos_new=Flight[i].x_pos+Flight[i].dx
                Flight[i].y_pos_new=Flight[i].y_pos+Flight[i].dy
            if 10 < num_conflict <= 30:
                #if turning in one direction fails attempting to turn in other direction
                #and updating new positions accordingly
                Flight[i].angle-=10
                Flight[i].dx=(Flight[i].velocity * math.cos(math.radians(Flight[i].angle)))/7200
                Flight[i].dy=(Flight[i].velocity * math.sin(math.radians(Flight[i].angle)))/7200                
                Flight[i].x_pos_new=Flight[i].x_pos+Flight[i].dx
                Flight[i].y_pos_new=Flight[i].y_pos+Flight[i].dy
            if num_conflict > 30:
                #if conflict cannot be resolved upto 30 conflicts breaking out to avoid infinite loop
                break
            if not (conflict_detect(Flight[i],Flight[j])):
                #if conflict avoided printing it out
                print "Conflict avoided successfully between", Flight[i].num, Flight[j].num
                