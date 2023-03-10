#declaring the class name as Patient
class Patient:
    
    #initialising the constructor for Patient class
    #with their first name,middle name,last name,address,city,state,zipcode,phone,emergency name,emergency phone    
    def __init__(self,first_name,middle_name,last_name,address,city,state,zipcode,phone,emergency_name,emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

      ##"""Accessor and Mutators| => Remove the comments in case you need this method"""
        
##    #getter and setter method for first name
##    def getFirstName(self):
##        return self.first_name
##    def setFirstName(self,first_name):
##        self.first_name=first_name
##        
##    #getter and setter method for middle name
##    def getMiddleName(self):
##        return self.middle_name
##    def setMiddleName(self,middle_name):
##        self.middle_name=middle_name
##
##    #getter and setter method for first name
##    def getLastName(self):
##        return self.last_name
##    def setLastName(self,last_name):
##        self.last_name=last_name
##
##    #getter and setter method for middle name    
##    def getAddress(self):
##        return self.address
##    def setAddress(self,address):
##        self.address=address
##
##    #getter and setter method for first name
##    def getCity(self):
##        return self.city
##    def setCity(self,city):
##        self.city=city
##
##    #getter and setter method for first name
##    def getState(self):
##        return self.state
##    def setState(self,state):
##        self.state=state
##
##    #getter and setter method for first name
##    def getZipcode(self):
##        return self.zipcode
##    def setZipcode(self,zipcode):
##        self.zipcode=zipcode
##  
##    #getter and setter method for first name
##    def getPhone(self):
##        return self.phone
##    def setPhone(self,phone):
##        self.phone=phone
##
##    #getter and setter method for first name
##    def getEmergencyName(self):
##        return self.emergency_name
##    def setEmergencyName(self,emergency_name):
##        self.emergency_name=emergency_name
##
##    #getter and setter method for first name
##    def getEmergencyPhone(self):
##        return self.emergency_phone
##    def setEmergencyPhone(self,emergency_phone):
##        self.emergency_phone=emergency_phone
  
     ##"""Accessor and Mutators"""
        
    #print method that reterive all the information
    def __str__(self):
        return "First Name: "+self.first_name+\
               "\nMiddle Name: "+self.middle_name+\
               "\nLast Name: "+self.last_name+\
               "\nAddress: "+self.address+\
               "\nCity:  "+self.city+\
               "\nState: "+self.state+\
               "\nZip: "+str(self.zipcode)+\
               "\nPhone: "+self.phone+\
               "\nEmergency Contact: "+self.emergency_name+\
               "\nEmergency Phone: "+self.emergency_phone

#declaring the class name as Procedure
class Procedure():

    #initialising the constructor for Patient class
    #with their procedure,date,practitioner,charges
    def __init__(self,procedure,date,practitioner,charges):
        self.procedure=procedure
        self.date=date
        self.practitioner=practitioner
        self.charges=charges
        
    """Accessors and Mutators"""
    
    #getter and setter method for procedure
    def getProcedure(self):
        return self.procedure
    def setProcedure(self,procedure):
        self.procedure=procedure
        
    #getter and setter method for date
    def getDate(self):
        return self.date
    def setDate(self,date):
        self.date=date
        
    #getter and setter method for practioner
    def getPractioner(self):
        return self.practitioner
    def setPractioner(self,practitioner):
        self.practitioner=practitioner
        
    #getter and setter method for charges
    def getCharges(self):
        self.charges
    def setCharges(self,charges):
        self.charges=charges

    #print method that reterive all the information
    def __str__(self):
        return "Procedure: "+self.procedure+\
               "\nDate: "+self.date+\
               "\nPractitioner: "+self.practitioner+\
               "\nCharges: "+str(self.charges)
#main method
def main():

    #Creating 1st Patient object and it's procedure.
    patient1 = Patient("James","Edward", "Jones","123 Main Street","Billings","Montana",59000,"406-555-1212","Jenny Jones","406-555-1213");
    print("1.Patient Details: \n")
    print(patient1)
    #procedure objects for 1st Patient
    patient1_procedure1 = Procedure("Physical Exam","8-24-2019","Dr. Irvine",250.00)
    patient1_procedure2 = Procedure("X-ray","8-24-2019","Dr. Jamison",500.00)
    patient1_procedure3 = Procedure("Blood Test","8-24-2019","Dr. Smith",200.00)
    print()
    print(patient1_procedure1)
    print()
    print(patient1_procedure2)
    print()
    print(patient1_procedure3)
    #calculating the total for 1st Patient
    total = patient1_procedure1.charges+patient1_procedure2.charges+patient1_procedure3.charges
    print("\nTotal charge for patient 1 = "+str(total))

    #Creating 1st Patient object and it's procedure.
    patient2 = Patient("Carol","Thomas", "Smith","456 South Street","Wise","Virginia",24215,"214-555-1234","Will Smith","213-555-1234");
    print("\n\n\n2.Patient Details: \n")
    print(patient1)
    #procedure objects for 1st Patient
    patient2_procedure1 = Procedure("Stool Test","8-24-2019","Dr. Will",575.00)
    patient2_procedure2 = Procedure("Sonography","8-24-2019","Dr. John",250.00)
    patient2_procedure3 = Procedure("Ultra Sound","8-24-2019","Dr. Alexander",155.00)
    print()
    print(patient2_procedure1)
    print()
    print(patient2_procedure2)
    print()
    print(patient2_procedure3)
    #calculating the total for 1st Patient
    total = patient2_procedure1.charges+patient2_procedure2.charges+patient2_procedure3.charges
    print("\nTotal charge for patient 2 = "+str(total))

if __name__ == "__main__":
    main()
