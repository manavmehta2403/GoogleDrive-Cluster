#declaring the class name as Employee
class Employee:

	#initialising the constructor for Employee class
	#with their name, id number, department and job title
	def __init__(self, name, IDnumber, department, job_title):
		self.__name = name
		self.__IDnumber = IDnumber
		self.__department = department
		self.__job_title = job_title

        ##"""Accessor and Mutators| => Remov the comments in case you need this method"""
##	#getter and setter method for name
##	def setName(self, name):
##		self.__name = name
##	def getName(self):
##		return self.__name
##
##	#getter and setter method for Id number
##	def setIDnumber(self, IDnumber):
##		self.__IDnumber = IDnumber
##	def getIDnumber(self):
##		return self.__IDnumber
##	
##	#getter and setter method for department
##	def setDepartment (self, department) : 
##		self.__department = department 
##	def getDepartment (self):
##		return self.__department
##
##	#getter and setter method for job title
##	def setJobtitle(self, job_title): 
##		self.__job_title = job_title
##	def getJobtitle(Eself):
##		self.__job_title
        ##"""Accessor and Mutators"""

	#print method that reterive all the information
	def __str__(self):
		return "Name: "+self.__name +\
                       "\nID Number: " + str(self.__IDnumber) +\
                       "\nDepartment: " + self.__department +\
                       "\nJob Title: " + self.__job_title
#main method
def main():
	#creating four objects of class Employee
	#here are 4 example employees. 3 are from the book and one made up
	emp1 = Employee( 'Susan Meyers', 47899, 'Accounting', 'Vice President') 
	emp2 = Employee( 'Mark Jones', 39119, 'IT', 'Programmer' ) 
	emp3 = Employee( 'Joy Rogers', 81774, 'Manufacturing', 'Engineer' ) 
	emp4 = Employee( 'Britney Mark',  92344, 'HR', 'Admin' )

	#printing the result
	print("Employee 1:")
	print(emp1)
	print("\nEmployee 2:")
	print(emp2)
	print("\nEmployee 3:")
	print(emp3)
	print("\nEmployee 4:")
	print(emp4)

#running the main method
if __name__ == "__main__":
	main()

