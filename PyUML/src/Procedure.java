public class Procedure{
   String procedureName,procedureDate,procedurePractcioner;
   double procedureCharge;
  
   //This is constructor
   public Procedure(){
       procedureName = "";
       procedureDate = "";
       procedurePractcioner = "";
       procedureCharge = 0.00;
       }
   //this is mutator
   public void setProcedure(String pName,String pDate,String pPractcioner,double Charge) {
       procedureName = pName;
       procedureDate = pDate;
       procedurePractcioner = pPractcioner;
       procedureCharge = Charge;
      
      
   }
   //These are accessors or getter methods
  
   public String getPname() {
      
       return procedureName;
   }  
      
public String getPdate() {
      
       return procedureDate;
   }
public String getPpract() {
  
   return procedurePractcioner;
}
public double getPcharge() {
  
   return procedureCharge;
}
  

}

