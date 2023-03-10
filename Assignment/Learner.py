##//Creating the UnoCard
##
class UnoCard:
    def __init__(self,color,value):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value

    def isMatch(self,UnoCard):
        return self.getColor() == UnoCard.getColor() or self.getValue()== UnoCard.getValue() 




def main():
    c1 = UnoCard("Red",0)
    c2 = UnoCard("Yellow",0)
    c3 = UnoCard("",0)
    c3.setColor("Yellow")
    c3.setValue(9)

    print("Card-1: Value:",c1.getValue(),"\tColor:",c1.getColor())
    print("Card-2: Value:",c2.getValue(),"\tColor: ",c2.getColor())
    print("Card-3: Value:",c3.getValue(),"\tColor:",c3.getColor())
    print("\nMatching card-1 with card-2:",c1.isMatch(c2))
    print("Matching card-2 with card-3:",c2.isMatch(c3))
    print("Matching card-1 with card-3:",c1.isMatch(c3))


if __name__ == "__main__":
    main()
