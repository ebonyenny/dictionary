#Module 3 lesson 2
from http.client import TOO_MANY_REQUESTS


class Car:
    def do(self, tyres, seats, door, fuel_dashboard, seat_belts):
      self.tyres=tyres
      self.seats=seats
      self.door=door
      self.fuel_dashboard=fuel_dashboard
      self.seat_belts=seat_belts
    
    def move(self, tyres):
        print("I am moving")

    def reverse(self, seats):
        print("Lets reverse a little")

    def fuel(self, fuel_dashbaord):
        print("I would need some fuel")
    
    def music(self, seat_belts):
        print("ensure you wear your seat belts as I am about to play some rocky music")
    
    def park(self, door):
        print("we just arrived at your destination")



            
    