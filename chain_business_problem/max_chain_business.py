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
    # listed = []
    for business in list_of_businesses:
        if city == business.location and business.name not in all_chains:
            all_chains[business.name] = 1
        elif city == business.location and business.name in all_chains:
            all_chains[business.name] += 1
    return all_chains

# [
    # {'Sturbucks': 2},
    # {'Whole Foods': 3},
    # {'Amazon': 2},
    # {'McDonalds': 2}
# ]


def sort_output(list_of_businesses, city):
    dict_of_chains = num_of_chains(list_of_businesses, city)
    sorted_dict = sorted(dict_of_chains.items(), key=lambda x: x[1])

    last_indx = len(sorted_dict) - 1
    while last_indx >= 0:
        print(sorted_dict[last_indx])
        last_indx -= 1


    # create dictionary
    # iterate throught the list
    # if the input city matches the busines location
    # append dictionary key = business name, value = how many

    # iterate over the dict
    # print key value pair


print(sort_output(businesses, "SF"))
