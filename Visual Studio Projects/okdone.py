from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time

'''
'''


class Building:  # defines class building
    number_of_floors = 0  # sets number_of_floors variable to 0
    customer_list = []  # creates an empty list for customers in building
    customer_list2 = []
    waiting_list = []  # creates an empty list for customers waiting on elevator
    waiting_list2 = []
    finished_list = []  # creates an empty list for customers finished with the elevator and who have reached their destination
    finished_list2 = []
    in_elevator_list = []  # creates an empty list for customers currently in the elevator
    in_elevator_list2 = []

    def __init__(self, floors, customers):  # initialize Building
        self.number_of_floors = floors  # assigns fl
        # oors entered to number_of_floors
        for ID in range(1, customers + 1):  # assigns number of customers entered to customer_list in order
            new = Customer(ID,
                           self.number_of_floors)  # creates an instance called new of Customer class for number of customers entered in input
            new2 = Customer(ID, self.number_of_floors)
            self.customer_list.append(new)  # appends new instance of customer to customer_list
            self.customer_list2.append(new2)
            self.waiting_list.append(new)
            self.waiting_list2.append(new2)

        self.customer_list.sort(key=lambda x: x.current_floor)  # sorts customer_list by current_floor customer is on
        self.customer_list2.sort(key=lambda x: x.current_floor)
        self.elevator = Elevator(floors,
                                 self.customer_list)  # creates instance of elevator with inputted floors and assigns customer_list to register_list
        self.elevator2 = Elevator(floors, self.customer_list2)


'''
I created my elevator class below which would be used mainly as an indicator as to what floor the elevator was on which would then match
up with the customer current floor and destination floor during the programs execution.
'''


class Elevator:
    number_of_floors = 0  # the number of floors
    register_list = []  # the list of customers in the elevator
    current_floor = 0  # the current floor of the elevator

    def __init__(self, number_of_floors, register_list):  # initilizes elevator class
        self.number_of_floors = number_of_floors  # assigns self.numbers_of_floors to number_of_floors
        self.register_list = register_list  # assigns self.register_list to register_list


'''
Customer class is described below where variables are assigned to each customer
i.e. current floor, destination floor, customer ID, whether they are in the elevator,
whether they are finished with the elevator and the direction they want to go in.
'''


class Customer:
    current_floor = 0  # the current floor of the customer
    destination_floor = 0  # the destination floor of the customer
    ID = 0  # the customers ID
    in_elevator = False  # denotes whether customer is in the elevator                                                                                                  # denotes whether customer has reached the destination floor
    finished = False  # denotes whether customer has reached the destination floor
    customer_direction = 0  # customer direction in which they are headed UP (1) or DOWN (1)
    customer_time = 0
    customer_time_total = 0

    '''
    Each customers was designated a random floor which is coded below. The customer coudln't have their destination floor the same as their
    current floor and from these random floors we could then determine which direction they needed to go in. If destination was higher than current floor
    customer would need to move up (1) and if destination was lower the customer would need to go down (-1). This would link in with my first strategy on whether to pick the customer
    up on the way up or on the way down.
    '''

    def __init__(self, ID, floors):  # initilize Customer class
        self.ID = ID  # assigns self.customerID to customerID
        self.current_floor = random.randint(1,
                                            floors)  # assigns self.current_floor to random int between 1 and floors entered
        self.destination_floor = random.randint(1,
                                                floors)  # assigns self.destination_floor to random int between 1 and floors entered
        while self.destination_floor == self.current_floor:  # while dest floors equals current floor
            self.destination_floor = random.randint(1, floors)  # if current floors is less than destination floor
        if self.current_floor < self.destination_floor:  # customer floor is above them
            self.customer_direction = 1  # then direction is UP (1)
        elif self.current_floor > self.destination_floor:  # customer floor is below them
            self.customer_direction = -1  # then direction is DOWN (-1)


class GUI(Building, Elevator, Customer):
    def __init__(self, parent):
        super().__init__(floors=0, customers=0)
        self.parent = parent
        self.parent.title("Elevator Simulation")
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

        main_frame = Frame(self.parent, padx=100, pady=100)
        main_frame.grid(row=0, column=0)

        def show_data():
            text.delete(0.0, 'end')
            result = choice.get()
            floor_result = enter_floors_box.get()
            customer_result = enter_customers_box.get()

            final = result, floor_result, customer_result
            text.insert(0.0, final)

        def showResults():
            text.delete(0.0, 'end')
            result = choice.get()
            num_floors = int(enter_floors_box.get())
            cust_result = int(enter_customers_box.get())

            if result == 1:
                num_floors = int(enter_floors_box.get())
                cust_result = int(enter_customers_box.get())
                building = Building(num_floors, cust_result)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print("Default Strategy Running")
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                self.run()

            # results = "Strategy choice: ", result, "\nNumber of floors: ", num_floors, "\nNumber of customers: ", cust_result
            # results = ("Strategy choice: {}\nNumber of floors: {}\nNumber of customers: {}".format(result, num_floors, cust_result))
            # text.insert(0.0, results)

        choice = IntVar()
        radio1 = Radiobutton(main_frame, text="Run Default Strategy", variable=choice, value=1)
        radio2 = Radiobutton(main_frame, text="Run Second Strategy", variable=choice, value=2)
        radio3 = Radiobutton(main_frame, text="Run Both Strategies", variable=choice, value=3)
        radio1.grid(row=0, column=0, columnspan=2, sticky=W)
        radio2.grid(row=1, column=0, columnspan=2, sticky=W)
        radio3.grid(row=2, column=0, columnspan=2, sticky=W)

        enter_floors_label = Label(main_frame, padx=5, pady=5, text="Enter amount of floors")
        enter_customers_label = Label(main_frame, padx=5, pady=5, text="Enter amount of customers")
        enter_floors_label.grid(row=3, column=0, sticky=W)
        enter_customers_label.grid(row=4, column=0, sticky=W)

        enter_floors_box = Entry(main_frame)
        enter_customers_box = Entry(main_frame)
        enter_floors_box.grid(row=3, column=1, sticky=W)
        enter_customers_box.grid(row=4, column=1, sticky=W)

        start_btn = Button(main_frame, text="Start Simulation", padx=5, pady=5, bg="red", fg="white",
                                command=showResults)
        start_btn.grid(row=5, column=0, columnspan=2, sticky=W + E)

        text = Text(main_frame, width=60, height=30, wrap=WORD)
        text.grid(row=6, columnspan=2, sticky=W)

    def run(self):  # method to operate the elevator
        print('++++++++++++++++++++++++++ELEVATOR IS NOW STARTING+++++++++++++++')  # prints
        print('There are %d customers in the building' % (len(self.customer_list)))  # prints
        self.output()  # runs output method below

    def run2(self):
        print('++++++++++++++++++++++++++ELEVATOR IS NOW STARTING+++++++++++++++')  # prints
        print('There are %d customers in the building' % (len(self.customer_list)))  # prints
        self.output2()

    def output(self):  # produces output to terminal and starts elevator
        start_time = time.time()  # this is used for the comparision between strategies on which executes quicker
        for customer in self.customer_list:
            print("Customer", customer.ID, "is on floor", customer.current_floor, "and wants to go to",
                  customer.destination_floor)  # prints lists of customers in building and their details ID, Current Floor, Destination Floor
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints

        # ELEVATOR MOVING UP LOOP
        while (
                self.elevator.current_floor != self.number_of_floors):  # starts the elevator moving up loop while elevator current floor is not equal to the amount of floors in building
            for customer in self.customer_list:
                if customer.in_elevator == True:
                    print('Customer', customer.ID,
                          'is in the lift')  # prints customer ID of customer currently in the lift
                    customer.customer_time += 1
            self.elevator.current_floor += 1  # moves the elevator up one floor after each loop of customers and once to start the elevator
            print(len(self.customer_list) - len(self.finished_list),
                  'customers still not delivered to destination.')  # prints amount of customers who have not yet reached their destination floor
            print('ELEVATOR MOVING UP')  # prints
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints
            print('FLOOR', self.elevator.current_floor)  # prints elevator current floor
            time.sleep(1)

            for customer in self.customer_list:  # loop through customers
                if (self.elevator.current_floor == customer.current_floor) & (customer.customer_direction == 1) & (
                        customer.finished == True):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = False  # customer goes into elevator
                if (self.elevator.current_floor == customer.current_floor) & (customer.customer_direction == 1) & (
                        customer.finished == False):  # if elevator and customer floor are the same and customer is moving UP (1) and customer is not finished customer goes into elevator
                    customer.in_elevator = True  # customer goes into elevator
                if (self.elevator.current_floor == self.number_of_floors) & (
                        customer.customer_direction == -1 or customer.customer_direction == 1) & (
                        customer.finished == False):  # when customers is on top floor of building and are going either up or down and customer is not finished
                    customer.in_elevator = True  # they are put into the elevator
                if (self.elevator.current_floor == customer.destination_floor) & (customer.in_elevator == True) & (
                        customer.finished == False) & (
                        customer.customer_direction == 1 or customer.customer_direction == -1):  # if elevator current floor is the same as customer destination floor and customer is in lift  and customer is not finished
                    customer.in_elevator = False  # customer leaves the elevator at their destination
                    customer.finished = True  # customer is then finished with the elevator
                    customer.current_floor = customer.destination_floor  # customer current floor remains same as destination as they have exited the lift
                    self.finished_list.append(customer)  # customer who leaves is added to the finished list
                    self.waiting_list.remove(customer)  # removes customer from waiting list
                    print('Customer', customer.ID,
                          'has reached their destination and exiting the lift.')  # prints customer has reached their destination
                    print('Customer', customer.ID, 'was in the lift for', customer.customer_time, 'floors')

        # ELEVATOR MOVING DOWN LOOP
        while (self.elevator.current_floor <= self.number_of_floors) & (
                self.elevator.current_floor != 0):  # while elevator current floor is less than or equal to number of floors in building and elevator floor not 0
            for customer in self.customer_list:
                if customer.in_elevator == True:
                    print('Customer', customer.ID, 'is in the lift')  # prints customer is in lift if true
                    customer.customer_time += 1
            self.elevator.current_floor -= 1  # moves the elevator down one floor after each loop of customers and once when it reaches the top of building
            print(len(self.customer_list) - len(self.finished_list),
                  'customers still not delivered to destination.')  # prints amount of customers who have not reached their destination floor
            print('ELEVATOR MOVING DOWN')  # prints
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints
            print('FLOOR', self.elevator.current_floor)  # prints elevator current floor
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            time.sleep(1)

            for customer in self.customer_list:  # loop through customers
                if (self.elevator.current_floor == customer.current_floor) & (customer.customer_direction == -1) & (
                        customer.finished == True):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = False  # customer goes into elevator
                if (self.elevator.current_floor == customer.current_floor) & (customer.customer_direction == -1) & (
                        customer.finished == False):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = True  # customer goes into elevator
                if (self.elevator.current_floor == customer.current_floor) & (
                        customer.customer_direction == -1):  # if elevator current floor equals customer current floor and directions is DOWN (-1)
                    customer.in_elevator = True  # customer is in the elevator
                if (self.elevator.current_floor == customer.destination_floor) & (customer.in_elevator == True) & (
                        customer.customer_direction == -1):  # if elevator current floor is the same as customer destination floor and customer is in lift
                    customer.in_elevator = False  # customer leaves the elevator at their destination
                    customer.finished = True
                    customer.current_floor = customer.destination_floor
                    self.finished_list.append(customer)  # customer who leaves is added to the finished list
                    self.waiting_list.remove(customer)  # removes customer from waiting list
                    print('Customer', customer.ID, 'has reached their destination and exited the lift.')  # prints
                    print('Customer', customer.ID, 'was in the lift for', customer.customer_time, 'floors')
            for customer in self.customer_list:
                customer.customer_time_total += customer.customer_time

        # PRINTS SUMMARY OF ELEVATOR RUN
        print('++++++++++++++++++++++ELEVATOR RUN SUMMARY+++++++++++++++++++++++')  # prints elevator run summary
        print(len(self.finished_list),
              'customers have reached there destination.')  # prints the amount of customers placed onto the finished list
        print(len(self.customer_list) - len(self.finished_list),
              'customers are awaiting collection.')  # prints the amount of customers awaiting collection
        print(len(self.waiting_list),
              'customers on the waiting list.')  # prints the amount of customers on the waiting list
        self.customer_list.sort(key=lambda x: x.ID)  # sorts customers by ID
        self.finished_list.sort(key=lambda x: x.ID)  # sorts customers by ID
        for finished in self.finished_list:
            print('Customer ID:', finished.ID, '          Customer in Elevator:', finished.in_elevator,
                  '          Customer Finished in Elevator:',
                  finished.finished)  # prints customers details after lift run
        for customer in self.customer_list:
            print("Customer", customer.ID, "is on floor", customer.current_floor, "and their destination was floor",
                  customer.destination_floor)  # prints lists of customers in building and their details ID, Current Floor, Destination Floor after lift run
        self.process_time1 = (time.time() - start_time)
        self.total_floors1 = customer.customer_time_total
        print(('Lift run took', (self.process_time1 * self.total_floors1) / 60), 'human minutes')
        print(('Lift run took', (self.process_time1), 'processing seconds'))
        print(('Total floors visited by all customers', customer.customer_time_total))

        '''
        ALTERNATE STRATEGY IS TOO JUST PICK CUSTOMERS UP IN THE LIFT ALONG THE WAY WHETHER THEY ARE GOING UP OR DOWN
        '''

    def output2(self):
        start_time = time.time()
        for customer in self.customer_list2:
            print("Customer", customer.ID, "is on floor", customer.current_floor, "and wants to go to",
                  customer.destination_floor)  # prints lists of customers in building and their details ID, Current Floor, Destination Floor
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints

        # ELEVATOR MOVING UP LOOP
        while (
                self.elevator2.current_floor != self.number_of_floors):  # starts the elevator moving up loop while elevator current floor is not equal to the amount of floors in building
            for customer in self.customer_list2:
                if customer.in_elevator == True:
                    print('Customer', customer.ID,
                          'is in the lift')  # prints customer ID of customer currently in the lift
                    customer.customer_time += 1
            self.elevator2.current_floor += 1  # moves the elevator up one floor after each loop of customers and once to start the elevator
            print(len(self.customer_list2) - len(self.finished_list2),
                  'customers still not delivered to destination.')  # prints amount of customers who have not yet reached their destination floor
            print('ELEVATOR MOVING UP')  # prints
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints
            print('FLOOR', self.elevator2.current_floor)  # prints elevator current floor
            time.sleep(1)

            for customer in self.customer_list2:  # loop through customers
                if (self.elevator2.current_floor == customer.current_floor) & (
                        customer.finished == True):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = False  # customer goes into elevator
                if (self.elevator2.current_floor == customer.current_floor) & (
                        customer.finished == False):  # if elevator and customer floor are the same and customer is moving UP (1) and customer is not finished customer goes into elevator
                    customer.in_elevator = True  # customer goes into elevator
                if (self.elevator2.current_floor == self.number_of_floors) & (
                        customer.finished == False):  # when customers is on top floor of building and are going either up or down and customer is not finished
                    customer.in_elevator = True  # they are put into the elevator
                if (self.elevator2.current_floor == customer.destination_floor) & (customer.in_elevator == True) & (
                        customer.finished == False):  # if elevator current floor is the same as customer destination floor and customer is in lift  and customer is not finished
                    customer.in_elevator = False  # customer leaves the elevator at their destination
                    customer.finished = True  # customer is then finished with the elevator
                    customer.current_floor = customer.destination_floor  # customer current floor remains same as destination as they have exited the lift
                    self.finished_list2.append(customer)  # customer who leaves is added to the finished list
                    self.waiting_list2.remove(customer)  # removes customer from waiting list
                    print('Customer', customer.ID,
                          'has reached their destination and exiting the lift.')  # prints customer has reached their destination
                    print('Customer', customer.ID, 'was in the lift for', customer.customer_time, 'floors')

        for customer in self.customer_list2:
            if customer.in_elevator == True:
                self.in_elevator_list2.append(customer)

        reaches_top = (len(self.in_elevator_list2) + len(
            self.finished_list2))  # shows that all customers are in either in or have entered and left by time elevator reaches the top therefore showing all customers collected on way to the top

        # ELEVATOR MOVING DOWN LOOP
        while (self.elevator2.current_floor <= self.number_of_floors) & (
                self.elevator2.current_floor != 0):  # while elevator current floor is less than or equal to number of floors in building and elevator floor not 0
            for customer in self.customer_list2:
                if customer.in_elevator == True:
                    print('Customer', customer.ID, 'is in the lift')  # prints customer is in lift if true
                    customer.customer_time += 1
            self.elevator2.current_floor -= 1  # moves the elevator down one floor after each loop of customers and once when it reaches the top of building
            print(len(self.customer_list2) - len(self.finished_list2),
                  'customers still not delivered to destination.')  # prints amount of customers who have not reached their destination floor
            print('ELEVATOR MOVING DOWN')  # prints
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')  # prints
            print('FLOOR', self.elevator2.current_floor)  # prints elevator current floor
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            time.sleep(1)

            for customer in self.customer_list2:  # loop through customers
                if (self.elevator2.current_floor == customer.current_floor) & (
                        customer.finished == True):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = False  # customer goes into elevator
                if (self.elevator2.current_floor == customer.current_floor) & (
                        customer.finished == False):  # if elevator and customer floor are the same and customer is moving UP (1) customer goes into elevator
                    customer.in_elevator = True  # customer goes into elevator
                if (self.elevator2.current_floor == customer.destination_floor) & (
                        customer.in_elevator == True):  # if elevator current floor is the same as customer destination floor and customer is in lift
                    customer.in_elevator = False  # customer leaves the elevator at their destination
                    customer.finished = True
                    customer.current_floor = customer.destination_floor
                    self.finished_list2.append(customer)  # customer who leaves is added to the finished list
                    self.waiting_list2.remove(customer)  # removes customer from waiting list
                    print('Customer', customer.ID, 'has reached their destination and exited the lift.')  # prints
                    print('Customer', customer.ID, 'was in the lift for', customer.customer_time, 'floors')
            for customer in self.customer_list2:
                customer.customer_time_total += customer.customer_time

        # PRINTS SUMMARY OF ELEVATOR RUN
        print('++++++++++++++++++++++ELEVATOR RUN SUMMARY+++++++++++++++++++++++')  # prints elevator run summary
        print(len(self.finished_list2),
              'customers have reached there destination.')  # prints the amount of customers placed onto the finished list
        print(len(self.customer_list2) - len(self.finished_list),
              'customers are awaiting collection.')  # prints the amount of customers awaiting collection
        print(len(self.waiting_list2),
              'customers on the waiting list.')  # prints the amount of customers on the waiting list
        self.customer_list2.sort(key=lambda x: x.ID)  # sorts customers by ID
        self.finished_list2.sort(key=lambda x: x.ID)  # sorts customers by ID
        for finished in self.finished_list2:
            print('Customer ID:', finished.ID, '          Customer in Elevator:', finished.in_elevator,
                  '          Customer Finished in Elevator:',
                  finished.finished)  # prints customers details after lift run
        for customer in self.customer_list2:
            print("Customer", customer.ID, "is on floor", customer.current_floor, "and their destination was floor",
                  customer.destination_floor)  # prints lists of customers in building and their details ID, Current Floor, Destination Floor after lift run
        print("Amount of customers that were in or left the elevator when it reached the top floor:", reaches_top)
        self.process_time2 = (time.time() - start_time)
        self.total_floors2 = customer.customer_time_total
        print(('Lift run took', (self.process_time2 * self.total_floors2) / 60), 'human minutes')
        print(('Lift run took', (self.process_time2), 'processing seconds'))
        print(('Total floors visited by all customers', customer.customer_time_total))


    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()


if __name__ == "__main__":
    # header()
    root = Tk()
    GUI = GUI(root)
    root.mainloop()
