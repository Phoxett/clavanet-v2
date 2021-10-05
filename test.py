
class T:

    name = "A"
    d = 1
    e = 3

    def __init__(self, name):
        self.name = name 


class B(T):

    surname = "T"

    def __init__(self, name, surname):
        super().__init__(name, surname)
        
        self.name = name
        self.surname = surname


b = B()