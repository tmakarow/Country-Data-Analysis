##Tara Makarowski, CompSci1026B, Assignment 4

##Task 2
#This class uses two files to build the data structures to hold the information about countries and continent

from country import *

class CountryCatalogue() :

    ## Contructor, Hold info about countries and continents
    # @param file that contains the names of countries and continents (continent.txt)
    # @para file that contains the country information (data.txt)
    #
    def __init__(self, cont_info, country_info):
        #dictionary of countries
        self._countryCat = {}
        #dictionary where the key is the country name and the value is the continent
        self._cDictionary = {}
        info = open(cont_info, "r")
        #skip header
        next(info)
        #process file, add name and continent to dictionary
        for line in info :
            prts = line.strip("\n")
            parts = prts.split(",")
            Country._name = parts[0]
            Country._continent = parts[1]
            self._cDictionary[Country._name] = Country._continent
        data = open(country_info, "r")
        #skip header
        next(data)
        #process file, add name, pop, area, continent to list, add that list to catalog list
        for line in data :
            element = line.strip("\n")
            elmnt = element.split("|")
            name = elmnt[0]
            pop = int(elmnt[1].replace(",", ""))
            are = float(elmnt[2].replace(",", ""))
            area = "%.2f" %are
            #add continent value from dictionary
            continent = self._cDictionary[name]
            #create country object
            obj = Country(name, pop, area, continent)
            #Country._name is the dict key
            #value is the catalog dictionary value
            self._countryCat[obj.getName()] = obj
        info.close()
        data.close()


    ## Looks up information on countries
    # @param country name
    # @return country object, or null object if not in catalog
    #
    def findCountry(self, name):
        if name in self._countryCat :
            return self._countryCat[name]
        else :
            return None


    ## Set the population of the country (if it is in the catalogue) to the value
    # @param country name
    # @param new population
    # @return True if successful, or False​ if it is not(the country isn't in the catalogue)
    #
    def setPopulationOfCountry(self, name, new_pop):
         if name in self._countryCat :
            self._countryCat[name].setPopulation(new_pop)
            return True
         else :
            return False



    ## Set the area of the country (if it is in the catalogue) to the value
    # @param country name
    # @param new area???
    # @return True if successful, or False​ if it is not(the country isn't in the catalogue)
    #
    def setAreaOfCountry(self, name, new_area):
        if name in self._countryCat :
            self._countryCat[name].setArea(new_area)
            return True
        else :
            return False


    ## Provide a way to add a new country to the dictionary of countries and country catalogue
    # @param country name
    # @param country population
    # @param country area
    # @param country continent
    # @return True if successful, or False​ if it is not(the country already exists)
    #
    def  addCountry(self, name, pop, area, continent):
        if name in self._countryCat :
            #country already in catalogue
            return False
        else :
            new_obj = Country(name, pop, "%0.2f" %area, continent)
            self._countryCat[new_obj.getName()] = new_obj
            return True


    ## If country exists, delete from the catalogue and from cDictionary
    # @param country name
    #
    def deleteCountry(self, name):
        if name in self._countryCat :
            del self._countryCat[name]




    ## Display the whole catalogue to the screen, using the default string representation for the Country objects
    #
    def printCountryCatalogue(self):
        for obj in self._countryCat :
            print(self._countryCat[obj])


    ## Find countries on a continent
    # @param continent name
    # @return list of countries on continent
        #Note: the return type is list and the elements of the list are Country objects)
        #if not valid continent, otherwise it returns an empty list
    #
    def getCountriesByContinent(self, continent):
        countries_on_cont = []
        for obj in self._countryCat :
            if self._countryCat[obj].getContinent() == continent :
                #add country names to list
                countries_on_cont.append(self._countryCat[obj].getName())
        return countries_on_cont


    ## Lists countries and their population density in descending order
    # @param lower bound for a population density range #inclusive of endpoints
    # @param upper bound for a population density range
    # @return a list of pairs, (country name, population density) from high to low density
    #
    def filterCountriesByPopDensity(self, low_den, high_den):
        pop_dense = []
        for obj in self._countryCat :
            density = self._countryCat[obj].getPopDensity()
            if density >= low_den and density <= high_den :
                pair = (self._countryCat[obj].getName(), density)
                pop_dense.append(pair)
        return sorted(pop_dense, key=lambda x: x[1], reverse=True)


    ## Enable all the country information in the catalogue to be saved to a file, sorted alphabetically by name
    ##Format​: Name|Continent|Population|AreaSize|PopulationDensity
    ##Example​: Canada|North America|34207999|9976200.00|3.43
    # @param name of file
    # @return number of items written, if fail: return -1
    #
    def saveCountryCatalogue(self, file):
        data = []
        count = 0
        file = open("out.txt", "w")
        for obj in self._countryCat :
            name = self._countryCat[obj].getName()
            continent = self._countryCat[obj].getContinent()
            pop = self._countryCat[obj].getPopulation()
            area = self._countryCat[obj].getArea()
            density = self._countryCat[obj].getPopDensity()
            info = "{}|{}|{}|{}|{}".format(name, continent, pop, "%0.2f" %area, "%0.2f" %density)
            data.append(info)
            count +=1
        file.write(str('\n'.join(sorted(data))))
        file.close()
        if count == 0 :
            return -1
        else :
            return count
