from os import system
from colorama import Fore, Back, Style
from prettytable import PrettyTable
"""Only public attributes and methods will be used in this example to save time by avoiding creation of getters and setters."""

class Vehicle:
    """Class vehicle has make, year, kind of fuel they use and 'aval' as availability"""
    def __init__(self,make:str,year:str,fuel:str,avail:bool):
        self.make = make
        self.year = year
        self.avail = avail


class Driver:
    """Collects needed data from drivers asigned to a certain vehicle"""
    def __init__(self,id:int, name:str, surname:str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.driver_dict[id] = {"name":name,"surname":surname}
        


class TransportCompany(Vehicle,Driver):
    """Holds a list of available vehicles to be used"""
    def __init__(self, make: str, year: str, fuel: str, avail: bool):
        super().__init__(make, year, fuel, avail)
        self.vehicles_dict = dict()
    
    def register_vehicle(self,vehicle:Vehicle):
        """Adds a new vehicle to vehicles list"""
        self.vehicles_list = []
        self.vehicles_dict[vehicle] = {"make":self.make,"year":self.year,"fuel":self.fuel,"avail":self.avail}
        self.vehicles_list.append(self.vehicles_dict)

    def asign_driver(self,id:int):
        pass



