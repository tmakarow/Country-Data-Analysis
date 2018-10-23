
from catalogue import *

def testFindCountry(countryCatalog):
    print()
    print("Looking up country")
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cntryObj = countryCatalog.findCountry(cntry)
    if cntryObj is None:
        print("-- Country not found in list")
    else:
        print(cntryObj)

def testSetPopulationOfCountry(countryCatalog):
    print()
    print("Setting population of country")
    itemFound = False
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cPop = input("  --  Enter new population: ")
    cPop = cPop.strip()
    cPop = int(cPop.replace(",",""))
    itemFound = countryCatalog.setPopulationOfCountry(cntry,cPop)
    if not itemFound:
        print("  Country " + cntry + " is not in the current list")

def testSetAreaOfCountry(countryCatalog):
    print()
    print("Setting area(size) of country")
    itemFound = False
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cSz = input("  --  Enter new area: ")
    cSz = cSz.strip()
    cSz = float(cSz.replace(",",""))
    itemFound = countryCatalog.setAreaOfCountry(cntry,cSz)
    if not itemFound:
        print("  Country " + cntry + " is not in the current list")

def testAddCountry(countryCatalog):
    print()
    cntry = input("-- Enter name of country to add: ")
    cntry = cntry.strip()
    thePop = input("      Enter the population: ")
    thePop = thePop.strip()
    cPop = int(thePop.replace(",",""))
    theSz = input("      Enter the size(area): ")
    theSz = theSz.strip()
    cSz = float(theSz.replace(",",""))
    theCont = input("      Enter the continent: ")
    theCont = theCont.strip()
    itemFound = countryCatalog.addCountry(cntry,cPop,cSz,theCont)
    if not itemFound:
        print("  Country " + cntry + " is already in the current list")

def testDeleteCountry(countryCatalog):
    print()
    cntry = input("-- Enter name of country to delete: ")
    cntry = cntry.strip()
    countryCatalog.deleteCountry(cntry)

def testGetCountriesByContinent(countryCatalog,theCont):
    lst = countryCatalog.getCountriesByContinent(theCont)
    if len(lst) > 0:
        print()
        print("Countries in "+theCont+" are:")
        for cobj in lst:
            print(cobj)

def testFilterCountriesByPopDensity(countryCatalog):
    print()
    lb = input("-- Enter the lower bound for population density: ")
    lb = float(lb.strip())
    ub = input("-- Enter the upper bound for population density: ")
    ub = float(ub.strip())
    rlst = countryCatalog.filterCountriesByPopDensity(lb,ub)
    if (rlst) == 0 or rlst is None: ####### I added or is None
        print("  No countries with density in that range found.")
    else:
        print("  Countries with density in this range are:")
        for ac in rlst:
            print(ac[0] + ", " + "density = "+ str(ac[1]))

def testSaveCountryCatalogue(cc,fname):
    print()
    print("Saving Country Catalogue")
    nitems = cc.saveCountryCatalogue(fname)
    print(" "+str(nitems)+" items written to file "+fname)


def main():
    cc = CountryCatalogue('continent.txt', 'data.txt')
    # print initial catalogue
    cc.printCountryCatalogue() #works 2
    # find a country
    #testFindCountry(cc) #works 2
    # add a country, delete a country, print the new catalogue and find a country in the new catalogue
    testAddCountry(cc) #seems to work 2
    #testDeleteCountry(cc) #works 2
    cc.printCountryCatalogue() #works 2
    #testFindCountry(cc) #ya tested
    # set the area and population
    testSetAreaOfCountry(cc) #works 2
    testSetPopulationOfCountry(cc) #works 2
    # print various parts of the catalogue
    testGetCountriesByContinent(cc,"Asia") #works 2
    # test filters
    testFilterCountriesByPopDensity(cc) #works 2
    # print final catalogue and then output it to a file
    cc.printCountryCatalogue() #works 2
    testSaveCountryCatalogue(cc,'output.txt') #works! 2

main()
