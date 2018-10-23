# coding=utf-8
from assingnment3 import *

class CountryCatalogue:
    def __init__(self, cont_info, country_info):
        #dictionary of countries
        self._countryCat = {}
        #dictionary where the key is the country name and the value is the continent
        self._cDictionary = {}
        country = []
        cDictfile = open(cont_info, "r")
        content = cDictfile.readlines()

        for line in content:
            # before reading the lines with content make sure to skip lines with headers

            data = line.split(",")
            self.cDictionary[data[0]] = data[1]

        cDictfile.close()

        catalogueFile = open(country_info, "r")
        fileContent = catalogueFile.readlines()
        for line in fileContent:
            # before reading the lines with content make sure to skip lines with headers

            # i have assumed that data.txt has country name, country population, area, continent
            # from the way we save we used | to separate items so i have further assumed to split using |
            data = line.split("|")
            newCountry = Country(data[0], data[1], data[2], data[3]) # also figure out position of name, continent, area and population after split()
            self.catalogue.append(newCountry)

        catalogueFile.close()

        self.cDictionary = dict()
        self.catalogue = [] #the catalogue should contain the Country


    def filterCountriesByContinent(self):
        continent = input("Enter name of the continent: ")
        for i in self.catalogue:
            if i.getContinent() == continent: #assuming continent is valid
                print (i.getName())


    def printCountryCatalogue(self):
        for i in self.catalogue:
            print (i.__repr__())


    def findCountry(self):
        cName = input("Enter the country name: ")
        for i in self.catalogue:
            if i.getName() == cName:
                print (i.__repr__())
                return

        print ("Country not found")


    def deleteCountry(self):
        cName = input("Enter the country name: ")
        for i in self.catalogue:
            if i.getName() == cName:
                self.catalogue.remove(i)
                print("Country was deleted successfully")
                return

        print ("Country not found")

    def addCountry(self):

        while True:
            cName = input("Enter the country name: ")
            population = float(input("Enter the population: "))
            area = float(input("Enter the area: "))
            continent = input("Enter the continent: ")

            country = Country(cName, population, area, continent)
            if country in self.catalogue:
                print("You can't add an already existing country in the catalogue")
                continue
            else:
                self.catalogue.append(country)
                self.cDictionary[cName] = continent
                print("Country was added successfully")
                break


    def setPopulationOfASelectedCountry(self):
        countryName = input("Enter country name: ")
        for i in self.catalogue:
            if i.getName() == countryName:
                population = float(input("Enter new population: "))
                i.setPopulation(population)
                print (i.getPopDensity())
                break


    def saveCountryCatalogue(self, filename):
        sorted_catalog = sorted(self.catalogue, key=lambda x: x.getName())

        save_file = open(filename, "a")
        for country in sorted_catalog:
            save_file.write(country.formatToSave() + "\n")

        save_file.close()
        print ("Countries were saved successfully")


    def findCountryWithLargestPop(self):
        max_pop = self.catalogue[0]
        for country in self.catalogue:
            if country.getPopulation() > max_pop.getPopulation():
                max_pop = country
        print (max_pop.getName())

    def findCountryWithSmallestArea(self):
        min_area = self.catalogue[0]
        for country in self.catalogue:
            if country.getArea() < min_area.getArea:
                min_area = country
        print (min_area.getName())


    def findMostPopulousContinent(self):
        continent_population = {}
        for country in self.catalogue:
            if not country.getContinent() in continent_population:
                continent_population[country.getContinent()] = country.getPopulation()
            else:
                continent_population[country.getContinent()] += country.getPopulation()

        print (max(continent_population))



    def filterCountriesByPopDensity(self):
        lower = float(input("Enter lower bound population density: "))
        upper = float(input("Enter upper bound population density: "))

        for country in self.catalogue:
            if country.getPopDensity() > lower and country.getPopDensity() <= upper:
                print (country)


