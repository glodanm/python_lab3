from .Entertainment import Entertainment, Age


class RiverExcurcion(Entertainment):
    def __init__(self, name: str = "", price: int = 0, height: int = 0, max_people: int = 0,  max_num_of_kids: int = 0,
                 route_length: float = 0, length_of_boat: float = 0):
        super().__init__(Age.ALL_AGES, name, price, height, max_people, max_num_of_kids)
        self.__route_length = route_length
        self.__length_of_boat = length_of_boat

    def __str__(self):
        res2 = super().__str__() + f"\nRoute_length: {self.__route_length}\nLength_of_boat: {self.__length_of_boat}"
        return res2
