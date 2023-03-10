public class Main {
  
   public static void main(String args[]) {
          
       // Initialisation of patient instance with data
           Patient peter = new Patient();
           peter.setDetails("Peter","Singh","Parker","Near River","Newai","Rajasthan","304021",
                   "+91988765321","Kashif","+919571638289");
          
         
           // Initialisation of procedure instance with sample data
       Procedure procedure1 = new Procedure();
       procedure1.setProcedure("Physical Exam","22 Nov 2019","Dr. Irvine",250.00);
         
       Procedure procedure2 = new Procedure();
       procedure2.setProcedure("X-ray","22 Nov 2019","Dr. Jamison",500.00);
         
       Procedure procedure3 = new Procedure();
       procedure3.setProcedure("Blood test","22 Nov 2019","Dr. Smith",200.00);
         
       //print statements
       System.out.println("<----------PATIENT DETAILS----------->");
       System.out.println("FULL NAME : "+peter.getFname()+" "+peter.getMname()
               +" "+peter.getLname());
       System.out.println("ADDRESS : "+ peter.getAddress());
       System.out.println("CITY : "+peter.getCity());
       System.out.println("STATE : "+peter.getState());
       System.out.println("ZIPCODE : "+peter.getZip());
       System.out.println("PHONE NUMBER : "+peter.getphone());
       System.out.println("Emegency Person's NAME : "+peter.getEname());
       System.out.println("Emergency Person's Contact Number : "+ peter.getEphone());
       System.out.println("\n\n");
         
         
       System.out.println("---> PROCEDURE 1 Details :");
       System.out.println("Procedure Name : " +procedure1.getPname());
       System.out.println("Procedure Date : "+ procedure1.getPdate());
       System.out.println("Practicioner : "+ procedure1.getPpract());
       System.out.println("Charge : " + procedure1.getPcharge());
       System.out.println("\n");
         
         
       System.out.println("---> PROCEDURE 2 Details :");
       System.out.println("Procedure Name : " +procedure2.getPname());
       System.out.println("Procedure Date : "+ procedure2.getPdate());
       System.out.println("Practicioner : "+ procedure2.getPpract());
       System.out.println("Charge : " + procedure2.getPcharge());
       System.out.println("\n");

       System.out.println("---> PROCEDURE 3 Details :");
       System.out.println("Procedure Name : " +procedure3.getPname());
       System.out.println("Procedure Date : "+ procedure3.getPdate());
       System.out.println("Practicioner : "+ procedure3.getPpract());
       System.out.println("Charge : " + procedure3.getPcharge());
       System.out.println("\n\n");
         
       double Total = procedure1.getPcharge() + procedure2.getPcharge() + procedure3.getPcharge();
       System.out.println("<<<<<<<<<<<-----------TOTAL CHARGE : " + Total +
               "------------->>>>>>>>");
      
       }
      
      
   }