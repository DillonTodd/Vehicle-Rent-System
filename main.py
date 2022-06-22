from vehicle_rent import Car, Bike, Customer

bike = Bike(100)
car = Car(20)
customer = Customer()

main_menu = True

while True:
    if main_menu:
        print('''
            *** Vehicle Rental Shop ***
            1. Car Rental Shop
            2. Bike Rental Shop
            3. Exit
        ''')
        main_menu = False

        user_input = input('Enter Choice: ')

    if user_input == '1':
        print('''
            *** Car Rental Shop ***
            1. Display Cars Available
            2. Rent A Car By The Hour
            3. Return A Car
            4. Main Menu
            5. Exit
        ''')

        choice = input('Enter Choice: ')

        if choice == '1':
            car.get_stock()
        elif choice == '2':
            customer.time_of_car_rental = car.rent_by_hour(customer.request_vehicle('car'))
            main_menu = True
            print('--------------------')
        elif choice == '3':
            customer.total_price = car.return_vehicle(customer.return_vehicle('car'), 'car')
            customer.cars, customer.time_of_car_rental = 0, 0
        elif choice == '4':
            main_menu = True
        elif choice == '5':
            break
        else:
            print('Please enter a valid input!')
    elif user_input == '2':
        print('''
            *** Bike Rental Shop ***
            1. Display Bikes Available
            2. Rent A Bike By The Hour
            3. Return A Bike
            4. Main Menu
            5. Exit
        ''')

        choice = input('Enter Choice: ')

        if choice == '1':
            bike.get_stock()
        elif choice == '2':
            customer.time_of_bike_rental = bike.rent_by_hour(customer.request_vehicle('bike'))
            main_menu = True
            print('--------------------')
        elif choice == '3':
            customer.total_price = bike.return_vehicle(customer.return_vehicle('bike'), 'bike')
            customer.bikes, customer.time_of_bike_rental = 0, 0
        elif choice == '4':
            main_menu = True
        elif choice == '5':
            break
        else:
            print('Please enter a valid input!')
    elif user_input == '3':
        break
    else:
        print('Please enter a valid input!')
        main_menu = True
    print('Thank you for stopping by!!')