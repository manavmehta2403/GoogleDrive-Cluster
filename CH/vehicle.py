#declaring the class
class Car:
    #constructor with four arguments and one optional parameter selling_price
    def __init__(self, rego, model, color, purchase_price, selling_price = None):
        self.rego = rego
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.selling_price = self.purchase_price*(1+0.3)

    #get and set methods

    #for rego
    def get_rego(self):
        return self.rego
    def set_rego(self, rego):
        self.rego = rego

    #for model
    def get_model(self):
        return self.model
    def set_model(self):
        self.model = model

    #for color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color

    #for prices
    def get_purchase_price(self):
        return self.purchase_price
    def get_selling_price(self):
        return self.selling_price
    def set_prices(self,purchase_price, selling_price = None):
        self.purchase_price = purchase_price
        self.selling_price = self.purchase_price(1+0.3)

    #print statement
    def __str__(self):
        return "Registration: " + str(self.rego) + " Model: " + str(self.model) + " Color: " + str(self.color) + " Purchase Price: " + str(round(self.purchase_price,2)) + " Selling Price: " + str(round(self.selling_price,2))
    #return statement
    def __repr__(self):
        return "Registration: " + str(self.rego) + " Model: " + str(self.model) + " Color: " + str(self.color) + " Purchase Price: " + str(round(self.purchase_price,2)) + " Selling Price: " + str(round(self.selling_price,2))
                             
#end of vehicle.py                  
