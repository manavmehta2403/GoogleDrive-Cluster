public class Patient{
   String firstName;
   String middleName;
   String lastName;
   String address;
   String city;
   String state;
   String zipcode;
   String phone;
   String emergencyName;
   String emergencyPhone;
     
   //This is the constructor.
     
   public Patient(){
       firstName = "";
       middleName = "";
       lastName = "";
       address = "";
       city = "";
       state = "";
       zipcode = "";
       phone = "";
       emergencyName = "";
       emergencyPhone = "";
      
       }
   // This is setter method or mutator
   public void setDetails(String fname,String mname,String lname,String add,String City,
           String State, String Zipcode, String Phone, String ename, String ephone) {
       firstName = fname;
       middleName = mname;
       lastName = lname;
       address = add;
       city = City;
       state = State;
       zipcode = Zipcode;
       phone = Phone;
       emergencyName = ename;
       emergencyPhone = ephone;
         
   }
   // These are getter method or accessors
     
   public String getFname() {
         
       return firstName;
   }
public String getMname() {
         
       return middleName;
   }
public String getLname() {
         
       return lastName;
   }
public String getAddress() {
         
       return address;
      
   }

public String getCity() {
         
       return city;
      
   }
public String getState() {
         
       return state;
      
   }
public String getZip() {
     
   return zipcode;
  
}

public String getphone() {
     
   return phone;
  
}
public String getEname() {
     
   return emergencyName;
     
   }
public String getEphone() {
     
   return emergencyPhone;
  
}  

}