"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    # Defina uma lista com as letras dos assentos
    seat_letters = ['A', 'B', 'C', 'D']

    # Crie um loop infinito para gerar as letras dos assentos
    while True:
        # Use um loop for para gerar as letras até que o número desejado seja atingido
        for letter in seat_letters:
            yield letter  # Utilize 'yield' para criar um gerador
            number -= 1
            if number == 0:
                return


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    seat_letter = generate_seat_letters(number)

    seat_number = 1
    aux = 0
    while seat_number <= number:
        for y in range(4):
            aux += 1
            complete_seat = f"{seat_number}{next(seat_letter)}"
            yield complete_seat
            if aux == number: return
        seat_number += 1
        if seat_number == 13:
            seat_number += 1
        



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    comlpete_seat = generate_seats(len(passengers))
    name_seat = {}

    for each in passengers:
        name_seat[each] = next(comlpete_seat)
    
    return name_seat

    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for each in seat_numbers:
        ticket_code = ""
        ticket_code += f"{each+flight_id}"
        fill_zero = 12-len(ticket_code)
        ticket_code += "0"*fill_zero
        yield ticket_code



