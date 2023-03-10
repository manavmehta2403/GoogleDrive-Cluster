/**
* USLDemo class
*
*/
public class USLDemo {

   /**
   * @param args
   */
   public static void main(String[] args) {
       // TODO Auto-generated method stub
       //USL object
       USL usl=new USL();
      
       //MaleThread objects
       MaleThread maleThread1=new MaleThread(usl);
       Thread thread1=new Thread(maleThread1);
       MaleThread maleThread2=new MaleThread(usl);
       Thread thread2=new Thread(maleThread2);
       MaleThread maleThread3=new MaleThread(usl);
       Thread thread3=new Thread(maleThread3);
       MaleThread maleThread4=new MaleThread(usl);
       Thread thread4=new Thread(maleThread4);
       MaleThread maleThread5=new MaleThread(usl);
       Thread thread5=new Thread(maleThread5);
      
       //FemaleThread objects
       FemaleThread femaleThread1=new FemaleThread(usl);
       Thread thread6=new Thread(femaleThread1);
       FemaleThread femaleThread2=new FemaleThread(usl);
       Thread thread7=new Thread(femaleThread2);
       FemaleThread femaleThread3=new FemaleThread(usl);
       Thread thread8=new Thread(femaleThread3);
       FemaleThread femaleThread4=new FemaleThread(usl);
       Thread thread9=new Thread(femaleThread4);
       FemaleThread femaleThread5=new FemaleThread(usl);
       Thread thread10=new Thread(femaleThread5);
      
       //start threads
       thread1.start();
       thread2.start();
       thread3.start();
       thread4.start();
       thread5.start();
       thread6.start();
       thread7.start();
       thread8.start();
       thread9.start();
       thread10.start();      
   }

}