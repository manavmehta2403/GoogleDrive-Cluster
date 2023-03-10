from vehicle import Car
carList = []
#def addCar(rego, model, color, price, carList):
def addCar(rego, model, color, price):
    global carList
    #idx = search(rego,carList)
    idx = search(rego)
    if(idx == -1):
        carList.append(Car(rego,model,color,price))
        return True
                             
    return False
                             
#def removeCar(rego,carList):
def removeCar(rego):
    global carList
    #idx = search(rego,carList)
    idx = search(rego)
    if(idx != -1):
        car = carList.pop(idx)
        return car
    else:
        return None
                             
#def all_cars(carList):
def all_cars():
    global carList
    if(len(carList) == 0):
        print('No cars present')
    else:
        for car in carList:
            print(car)
                             
#def search(rego,carList):
def search(rego):
    
    for i in range(len(carList)):
        if carList[i].get_rego() == rego:
            return i
                                            
    return -1                            
#end of cars.py




