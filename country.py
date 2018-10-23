##Tara Makarowski, CompSci1026B, Assignment 4

## Task 1
#  Implement class Country that holds the information about a single country
class Country :
    ## Hold info about countries, define instance variables
    #  name: The name of the country (string)
    #  population: The population in the country (integer)
    #  area: The area of the country (float)
    #  continent: The name of the continent to which the country belongs (string)
    #
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent


    #Getter Methods:

    ## Get the name of the country
    #  @return country name
    #
    def getName(self):
        return self._name

    ## Get the population of the country
    #  @return the country population
    #
    def getPopulation(self):
        return int(self._pop)

    ## Get the area of the country
    #  @return the country area
    #
    def getArea(self):
        return float(self._area)

    ## Get the continent the country is on
    #  @return the continent
    #
    def getContinent(self):
        return self._continent


    #Setter Methods:

    ## Set the population for the country
    #  @param number of people in country
    #
    def setPopulation(self, pop):
        self._pop = int(pop)

    ## Set the area for the country
    #  @param area of the land of country
    #
    def setArea(self, area):
        self._area = float("%0.2f" %area)

    ## Set the continent for the country
    #  @param which continent
    #
    def setContinent(self, continent):
        self._continent = continent


    ## Calculate the population density for the country
    # Population density is the population divided by the area rounded to 2 decimal places.
    # @return population density
    #
    def getPopDensity(self):
        density = self.getPopulation() / self.getArea()
        return float("%0.2f" %density)


    ## Generate a string representation for class objects
    # @return string
    # Name (pop: population value, size: area value) in Continent
    def __repr__(self):
        return "{} (pop: {}, size: {}) in {}".format(self._name, self._pop, self._area, self._continent )



