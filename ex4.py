# This is a python program for learning Variables and Names

#The number of available cars
cars = 100

#The number of seats available in each car
space_in_a_car = 4

#The number of available drivers
drivers = 30

#The total number of passengers to be transported
passengers = 90

#The number of cars that are out of service
cars_not_driven = cars - drivers

#The number of cars that can be driven
cars_driven = drivers

#The total capacity of available seats
carpool_capacity = cars_driven * space_in_a_car

#The numeber of passengers to be transported via each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
