"""Functions which helps the locomotive engineer to keep track of the train."""


from pickle import APPEND


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a,b,c,*d = each_wagons_id
    new_list = [c, *missing_wagons, *d, a, b]
    return new_list   


def add_missing_stops(route, **bananas):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    aux=[]
    for each in bananas.values():
        aux.append(each)

    route["stops"] = aux

    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    # Use o operador ** para combinar os dicionários
    return {**route, **more_route_information}




def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    #====== This is a pmeinhardt's solution  ======
    #return list(map(list, zip(*wagons_rows)))

    #====== This is a Meatball's solution ======
    #[*first_row], [*second_row], [*third_row] = zip(*wagons_rows)
    #return [first_row, second_row, third_row]

    #====== This is a Snooches's solution ======
    #return [list(x) for x in zip(*wagons_rows)]
    x= zip(*wagons_rows)
   
    b=[list(each) for each in x] 

    return b