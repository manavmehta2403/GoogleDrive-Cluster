class TL:
    color = None
    def __init__(self,color):
        self.color = "Red"
    def setColor(self,color):
        self.color = color
    def ischange(self):
        if (self.color == "Red"):
            self.color = "Green"
        elif (self.color == "Green"):
            self.color = "Yellow"
        else:
            self.color = "Red"
    def display(self):
        print (self.color)

col = TL("Green")
col.display()
col.setColor("Green")
col.ischange()
col.display()

class Light:
    def __init__(self,color):
        self.color = "Red"
        
    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def change(self):
        if(self.color == "RED"):
            self.color = "GREEN"
        elif(self.color == "GREEN"):
            self.color = "YELLOW"
        else:
            self.color = "RED"
            
    def __repr__(self):
        return self.color



def main():
    light = str(input("Enter the color of the trafic light")).upper()
    l = Light(light)
    l.setColor(light)
    l.change()
    print(l.__repr__())
    
            
if __name__ == "__main__":
    main()
