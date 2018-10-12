## Section 1
class Place(object):
    ## Section 2
    ## class attrbute: list of places
    places_list = []
    
    @staticmethod
    def locations():
        ## check if list is empty (no places exist)
        ## if not, print message
        ## as long as there are Places in list, we print each one out
        if Place.places_list == []:
            print("No locations exist at this time.")
        else:
            print("The following locations exist:")
            for place in Place.places_list:
                print(place)
        
    
    ## constructor method, takes name and another place (if not give place, default is None)
    def __init__(self, name, location = None):
        ## return message to indicate Place object created
        print(name + " created.")
        ## name and location are private attributes
        self.__name = name
        ## if another Place object given, we store the name of that place in __location, if not we keep the "None"
        if location == None:
            self.__location = location
        else:
            self.__location = location.__name
        ## this public variable indicates if the Place is visited
        self.visited = False
        ## adds Place object to class attribute list to keep track of all existing Places
        Place.places_list.append(self)

    ## to-string method that prints name, where located if valid, and if visted
    def __str__(self):
        reply = self.__name
        if self.__location != None:
            reply += ", located in " + self.__location

        if self.visited == False:
            reply += " (not visited)."
        else:
            reply += " (visited)."

        return reply
    
    ## getter methods for name and location
    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    ## Section 5 Bonus
    def is_located_in(self, other):
        related = []
        for place in Place.places_list:
            if place.__name == self.__location:
                related.append(place)
        if other in related:
            return True

    ## Section 4: visitation
    def visit(self):
        ## check if Place is already visited, if not
        if self.visited == False:
            print("You visit " + self.__name + ".")
            ## make this place visited
            self.visited = True
            ## look through other object in our list of places
            ## if the place's location is in the list, we call the visit method for that location
            ## this will allow all related places to through this method
            for place in Place.places_list:
                if place.__name == self.__location:
                    print("That means... You visit " + place.__name)
                    place.__visited = True
                    place.visit()
##            relate = self.related()
##            if relate:
##                for loc in relate:
##                    print("That means... You visit " + loc.__name)
##                    loc.__visited = True
            
        ## if place is already visited, return message
        else:
            print(self.__name + " has already been visited.")
            
##    rel_places = []
##    def related(self):
##        for place in Place.places_list:
##            if place.__name == self.__location:
##                Place.rel_places.append(place)
##                place.related()
##        return Place.rel_places

class Home(Place):
    ## super calls Place init first, then assigns new attributes
    def __init__(self, name, location, bedrooms, occupancy):
        super().__init__(name, location)
        self.bedrooms = bedrooms
        self.occupancy = occupancy

    ## trying to call the Place str first and then add new information, but doesn't seem to work
    def __str__(self):
        super().__str__()
        reply = "\tThis house has " + str(self.bedrooms) + " bedrooms, " + str(self.occupancy) + " of which are occupied"
        return reply
        

class City(Place):
    ## calls Place init first, then assigns new attributes
    def __init__(self, name, location, population, mayor):
        super().__init__(name, location)
        self.population = population
        self.mayor = mayor
    ## trying to add new reply to the Place str, but doesn't seem to work
    def __str__(self):
        super().__str__()
        reply = "\tThis city has " + str(self.population) + " residents, and the mayor is " + self.mayor + "."
        return reply


## Main Test
## Section 1
##iu = Place("IU Campus")
##library = Place("Wells Library", iu)
##
##print()
##print(iu)
##print(library)

## Section 2
##Place.locations()
##
##iu = Place("IU Campus")
##library = Place("Wells Library", iu)
##
##Place.locations()

## Section 3
##Place.locations()
##indiana = Place("Indiana")
##indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")
##btown = City("Bloomington", indiana, 80405, "John Hamilton")
##iu = Place("IU Campus", btown)
##library = Place("Wells Library", iu)
##rental = Home("Rental House", btown, 5, 4)
##historic = Home("Elias Abel House", btown, 4, 0)
##
##Place.locations()

## Section 4
indiana = Place("Indiana")
indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")
btown = City("Bloomington", indiana, 853173, "Joeseph Hogsett")
iu = Place("IU Campus", btown)
library = Place("Wells Library", iu)
rental = Home("Rental House", btown, 5, 4)
historic = Home("Elias Abel House", btown, 4, 0)

print()
library.visit()
indiana.visit()

## Section 5

print("True or False, Rental House is located in Indiana:", end = ' ')
print(rental.is_located_in(indiana), "\n")
print("True or False, Elias Abel House is located in Indianapolis:", end = ' ')
print(historic.is_located_in(indy), "\n")
