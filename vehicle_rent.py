import datetime


# parent class of car and bike
class Vehicle:
    # constructor
    def __init__(self, stock):
        self.stock = stock
        self.time = 0

    # getter method to retrieve the amount of vehicles left in stock
    def get_stock(self):
        print('We have {} vehicles available to rent.\n'.format(self.stock))
        return self.stock

    # function to rent a vehicle by the hour
    def rent_by_hour(self, num_of_veh):
        # check if the user entered a valid number of vehicles
        if num_of_veh <= 0:
            print('Please enter a positive integer!')
            return None
        # check if the user wants to rent more vehicles than we have in stock
        elif num_of_veh > self.stock:
            print('We only have {} vehicles in stock.'.format(self.stock))
            return None
        else:
            self.time = datetime.datetime.now()

            if num_of_veh == 1:
                print('You rented 1 vehicle at {}'.format(self.time))
            else:
                print('You rented {} vehicles at {}'.format(num_of_veh, self.time))

            # decrease the number of vehicles in stock
            self.stock -= num_of_veh

            return self.time

    def return_vehicle(self, info, type_of_veh):
        hourly_car_price = 10
        hourly_bike_price = 5

        time_of_rental, num_of_veh = info
        total_price = 0

        if type_of_veh == 'car':
            if time_of_rental and num_of_veh:
                self.stock += num_of_veh
                time_of_return = datetime.datetime.now()
                total_hours = time_of_return - time_of_rental

                total_price = total_hours.seconds / 3600 * hourly_car_price * num_of_veh

                print('Thank you for returning the car!')
                print('Your total price is {}.'.format(total_price))

                return total_price
        elif type_of_veh == 'bike':
            if time_of_rental and num_of_veh:
                self.stock += num_of_veh
                time_of_return = datetime.datetime.now()
                total_hours = time_of_return - time_of_rental

                total_price = total_hours.seconds / 3600 * hourly_bike_price * num_of_veh

                print('Thank you for returning the bike!')
                print('Your total price is {}'.format(total_price))

                return total_price
        else:
            print('You have not rented a vehicle.')
            return None


class Car(Vehicle):
    def __init__(self, stock):
        super().__init__(stock)


class Bike(Vehicle):
    def __init(self, stock):
        super().__init__(stock)


class Customer:
    def __init__(self):
        self.bikes = 0
        self.time_of_bike_rental = 0

        self.cars = 0
        self.time_of_car_rental = 0

    def request_vehicle(self, type_of_veh):
        if type_of_veh == 'car':
            num_of_cars = input('How many cars would you like to rent? ')

            try:
                num_of_cars = int(num_of_cars)
            except ValueError:
                print('Please enter a valid number of cars!')
                return -1

            if num_of_cars < 1:
                print('You must enter a number greater than 0!')
                return -1
            else:
                self.cars = num_of_cars

            return self.cars
        elif type_of_veh == 'bike':
            num_of_bikes = input('How many bikes would you like to rent? ')

            try:
                num_of_bikes = int(num_of_bikes)
            except ValueError:
                print('Please enter a valid number of bikes!')
                return -1

            if num_of_bikes < 1:
                print('You must enter a number greater than 0!')
                return -1
            else:
                self.bikes = num_of_bikes

            return self.bikes
        else:
            print('We only rent cars and bikes!')

    def return_vehicle(self, type_of_veh):
        if type_of_veh == 'car':
            if self.time_of_car_rental and self.cars:
                return self.time_of_car_rental, self.cars
            else:
                return 0, 0
        elif type_of_veh == 'bike':
            if self.time_of_bike_rental and self.bikes:
                return self.time_of_bike_rental, self.bikes
            else:
                return 0, 0
        else:
            print('You must return a car or a bike!')






