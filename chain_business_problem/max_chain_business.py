class Business():
    def __init__(self, name, location, _id):
        """Inititlize the obeject with name, location, and
        _id attributes
        """
        self.name = name
        self.location = location
        self._id = _id

    def __repr__(self):
        """String representation of the object"""
        return (f"name: {self.name}, location: {self.location}, id: {self._id}")



businesses = [
    Business("Sturbucks", "SF", 100),
    Business("Sturbucks", "SF", 100),
    Business("Whole Foods", "SF", 101),
    Business("Whole Foods", "SF", 102),
    Business("Whole Foods", "SF", 142),
    Business("Amazon", "SF", 103),
    Business("Amazon", "SF", 110),
    Business("McDonalds", "SF", 104),
    Business("McDonalds", "SF", 104),
    Business("McDonalds", "NYC", 106),
    Business("McDonalds", "NYC", 105)
]


def num_of_chains(list_of_businesses, city):
    
    all_chains = {}
    for business in list_of_businesses:
        if city == business.location and business.name not in all_chains:
            all_chains[business.name] = 1
        elif city == business.location and business.name in all_chains:
            all_chains[business.name] += 1
    return all_chains


def sort_chain(list_of_businesses, city):

    dict_of_chains = num_of_chains(list_of_businesses, city)

    for name, num in dict_of_chains.items():
        print(name, num)

    




    # create dictionary
    # iterate throught the list
    # if the input city matches the busines location
    # append dictionary key = business name, value = how many 
    
    # iterate over the dict
    # print key value pair


print(sort_chain(businesses, "SF"))

