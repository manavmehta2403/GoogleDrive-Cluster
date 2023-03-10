/**
* FemaleThread class
*
*/
public class FemaleThread implements Runnable {

   USL usl; // USL instance

   /**
   * constructor
   */
   public FemaleThread(USL usl) {
       // TODO Auto-generated constructor stub
       this.usl = usl;
   }

   /*
   * (non-Javadoc)
   *
   * @see java.lang.Runnable#run()
   */
   @Override
   public void run() {
       // TODO Auto-generated method stub
       for (int i = 1; i <= 10; i++) {
           int interval = (int) (Math.random() * (10 - 4) + 4);
           try {
               Thread.sleep(interval * 1000);
               boolean result = usl.femaleEnters();
               if (result) {
                   int waitInterval = (int) (Math.random() * (5 - 2) + 2);
                   // wait(waitInterval*1000);
                   Thread.sleep(waitInterval * 1000);
                   usl.femaleExits();
                   // notifyAll();
               }
           } catch (InterruptedException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
           }
       }

   }
}





