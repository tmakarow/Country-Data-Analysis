##e.g Nigeria (pop: 11723456, size: 324935) in Africa


from country import Country

name = "Nigeria"
pop = 11723456
area = 324935
continent = "Africa"
#test = Country("Nigeria", 11723456, 324935, "Africa")
test = Country(name, pop, area, continent)
#test.setPopulation(pop)
#test.setArea(area)
#test.setContinent(continent)

#test.getPopulation()
#test.getArea()
#test.getContinent()
final = test.__repr__()
print(final)
#density = test.getPopDensity()
#print(density)
