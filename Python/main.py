from car import Car
from account import Account
if __name__ == "__main__":
    car = Car("FVS785", Account("Leonardo Vanegass", "JLVP785"))
    print(vars(car))
    print(vars(car.driver))
