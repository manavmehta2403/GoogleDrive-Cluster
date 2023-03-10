import cars
#def buy_car(carList):
def buy_car():
    rego = int(input('Registration number : '))
    model = input('Model : ')
    color = input('Color : ')
    purchase_price = float(input('Purchase price : $'))
    boolean = cars.addCar(rego,model,color,purchase_price)
    #if(cars.addCar(rego,model,color,purchase_price,carList)):
    if(boolean == False):
        print("Car with registration: " + str(rego) + " already added")
  
#def sell_car(carList):
def sell_car():
    rego = int(input('Registration Number : '))
    #car = cars.removeCar(rego,carList)
    car = cars.removeCar(rego)
    if(car == None):
        print("Car with registration: " + str(rego) + " doesn't exists")
    else:
       print("Car sold at price: " + str(round(car.get_selling_price(),2)))
      
#def search_car(carList):
def search_car():
    rego = int(input('Registration Number : '))
    #idx = cars.search(rego,carList)
    idx = cars.search(rego)
    if(idx != -1):
        print(cars.carList[idx])
    else:
        print("Car with registration: " + str(rego) + " doesn't exists")

#def list_all_cars(carList):
def list_all_cars():
    cars.all_cars()
  
#end of caryard.py     
