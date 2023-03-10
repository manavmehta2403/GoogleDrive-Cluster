import caryard
def main():
    choice = 1
    while choice != 5:
        try:
            print('1. Buy a Car')
            print('2. Sell a Car')
            print('3. Search for a Car')
            print('4. Show all cars')
            print('5. Exit')
                             
            choice = int(input('Enter your choice : '))
            if choice == 1:
                caryard.buy_car()
            elif choice == 2:
                caryard.sell_car()
            elif choice == 3:
                caryard.search_car()
            elif choice == 4:
                caryard.list_all_cars()
            elif choice != 5:
                print('Invalid choice')
        except e:
            print(str(e) + "WRONG INPUT FORMT.\n")
            main()

        print('')
    print('Bye!')
if __name__ == "__main__":
    main()   
#end of application.py     
