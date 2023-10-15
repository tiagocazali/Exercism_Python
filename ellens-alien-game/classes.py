"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created =0

    def __init__(self, x_position, y_position):
        self.x_coordinate = x_position
        self.y_coordinate = y_position
        self.health =3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -=1

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, x_position, y_position):
        self.x_coordinate = x_position
        self.y_coordinate = y_position

    def collision_detection(self, teste_none):
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(aliens_list):
    lista=[]
    
    for each in aliens_list:
        temp = Alien(each[0],each[1])
        lista.append(temp)
    
    return lista
