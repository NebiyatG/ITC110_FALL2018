# riders_rating.py
# ITC110
# Fall 2018
# Nebi Gidey
# program to find the best Uber riders with highest TTM.
# Trips * Tips * Multipler Factor
# The bigger the TTM, the bigger the bucks into Uber-Nebi's pocket :)

# When USER is prompted, type in    uber_riders.dat
# for filenanme of data to load into this program


## create the riders 
class  Riders:
    ## the constructor
    def __init__ (self, name, numOfTrips, tipRating):
        # instance variables
        self.name       = name
        self.numOfTrips = float(numOfTrips)
        self.tipRating  = float(tipRating)

    ## accessor methods
    def getName(self):
        return self.name

    def getHours(self):
        return self.numOfTrips

    def getQPoints(self):
        return self.tipRating

    ## simple method / function -- not a mutator 
    def ttm(self):
        return self.numOfTrips * self.tipRating



## make a riders instance from file of information/data
## create a riders object with data from the file
def makeRiders(infoStr):
    # infoStr is tab separated line: name   hours   qpoints

    name, hours, qpoints = infoStr.split("\t") # split on TAB delimiter
    return Riders(name, hours, qpoints)

## main section
def main():
    ## open the file for reading
    filename = input("Enter the file name with uber riders information:  ")
    infile = open(filename, "r")

    ## make a riders oject with info from the file
    best = makeRiders(infile.readline()) # careful, we had "(infile.readline)" without the "()"

    ## loop through each riders; compare with current best and find the best in file
    for line in infile:
        s = makeRiders(line)
        if s.ttm() > best.ttm():
            best = s

    infile.close() ## close the file

    ## print out the best rider and best TTM
    print("The best riders is                  :  ", best.getName())
    print("Number of Trips                     :  ", best.getHours())
    print("Tip Rating                          :  ", best.getQPoints())
    print("The Trips*Tips Multiplier number is :  ", best.ttm())


## call the main
main()


            




    





