
from abc import ABC, abstractmethod


class Reservation(ABC):
    @property
    @abstractmethod
    def total_cost(self):
        pass


class FlightReservation(Reservation):
    def __init__(self, price):
        self.price = price
    
    @property
    def total_cost(self):
        return self.price


class HotelReservation(Reservation):
    def __init__(self, price_per_night, total_nights):
        self.price_per_night = price_per_night
        self.total_nights = total_nights

    @property
    def total_cost(self):
        return self.price_per_night * self.total_nights


class ItineraryReservation(Reservation):
    def __init__(self, reservations = None):
        self.reservations = [] if reservations is None else reservations

    @property
    def total_cost(self):
        return sum([reservation.total_cost for reservation in self.reservations])


if __name__ == '__main__':
    iti = ItineraryReservation()
    iti.reservations.append(FlightReservation(1001))
    iti.reservations.append(FlightReservation(2001))
    iti.reservations.append(HotelReservation(200, 5))
    print(iti.total_cost)
