

/**
* USL (UniSex Lounge) class
*
*/
public class USL {

   // enum for state of lounge
   public enum STATE {
       Empty, WomenPresent, MenPresent
   }

   // data members
   private STATE loungeState; // state of lounge
   private int malesInside; // males inside lounge
   private int malesWaiting; // males waiting to get inside lounge
   private int femalesInside; // females inside lounge
   private int femalesWaiting; // females waiting to get inside lounge

   /**
   * default constructor
   */
   public USL() {
       // TODO Auto-generated constructor stub
       loungeState = STATE.Empty;
       malesInside = 0;
       malesWaiting = 0;
       femalesInside = 0;
       femalesWaiting = 0;
   }

   /**
   * @return the state
   */
   STATE getState() {
       return loungeState;
   }

   /**
   * @param state
   *            the state to set
   */
   void setState(STATE state) {
       this.loungeState = state;
   }

   /**
   * @return the malesInside
   */
   int getMalesInside() {
       return malesInside;
   }

   /**
   * @param malesInside
   *            the malesInside to set
   */
   void setMalesInside(int malesInside) {
       this.malesInside = malesInside;
   }

   /**
   * @return the malesWaiting
   */
   int getMalesWaiting() {
       return malesWaiting;
   }

   /**
   * @param malesWaiting
   *            the malesWaiting to set
   */
   void setMalesWaiting(int malesWaiting) {
       this.malesWaiting = malesWaiting;
   }

   /**
   * @return the femalesInside
   */
   int getFemalesInside() {
       return femalesInside;
   }

   /**
   * @param femalesInside
   *            the femalesInside to set
   */
   void setFemalesInside(int femalesInside) {
       this.femalesInside = femalesInside;
   }

   /**
   * @return the femalesWaiting
   */
   int getFemalesWaiting() {
       return femalesWaiting;
   }

   /**
   * @param femalesWaiting
   *            the femalesWaiting to set
   */
   void setFemalesWaiting(int femalesWaiting) {
       this.femalesWaiting = femalesWaiting;
   }

   /**
   * maleEnters method
   *
   * @throws InterruptedException
   */
   public synchronized boolean maleEnters() throws InterruptedException {
       boolean maleEntered = false;
       STATE state = getState();
       if (state == STATE.Empty) {
           malesInside++;
           if (malesWaiting != 0)
               malesWaiting--;
           maleEntered = true;
           setState(STATE.MenPresent);
       } else if (state == STATE.MenPresent) {
           malesInside++;
           if (malesWaiting != 0)
               malesWaiting--;
           maleEntered = true;
       } else {
           malesWaiting++;
           int waitInterval = (int) (Math.random() * (10 - 4) + 4);
           // wait(waitInterval);
           Thread.sleep(waitInterval * 1000);
       }
       displayLoungeStatus();
       notifyAll();
       return maleEntered;
   }

   /**
   * femaleEnters method
   *
   * @throws InterruptedException
   */
   public synchronized boolean femaleEnters() throws InterruptedException {
       boolean femaleEntered = false;
       STATE state = getState();
       if (state == STATE.Empty) {
           femalesInside++;
           if (femalesWaiting != 0)
               femalesWaiting--;
           femaleEntered = true;
           setState(STATE.WomenPresent);
       } else if (state == STATE.WomenPresent) {
           femalesInside++;
           if (femalesWaiting != 0)
               femalesWaiting--;
           femaleEntered = true;
       } else {
           femalesWaiting++;
           int waitInterval = (int) (Math.random() * (10 - 4) + 4);
           // wait(waitInterval);
           Thread.sleep(waitInterval * 1000);
       }
       displayLoungeStatus();
       notifyAll();
       return femaleEntered;
   }

   /**
   * maleExits method
   *
   * @return
   */
   public synchronized void maleExits() {
       malesInside--;
       if (malesInside == 0) {
           setState(STATE.Empty);
       }
       notifyAll();
       displayLoungeStatus();
   }

   /**
   * femaleExits method
   */
   public synchronized void femaleExits() {
       femalesInside--;
       if (femalesInside == 0) {
           setState(STATE.Empty);
       }
       notifyAll();
       displayLoungeStatus();
   }

   /**
   * display lounge status
   */
   public synchronized void displayLoungeStatus() {
       String state = "";
       STATE name = getState();
       if (name == STATE.Empty)
           state = "Empty";
       else if (name == STATE.MenPresent)
           state = "Men Present";
       else if (name == STATE.WomenPresent)
           state = "Women Present";

       System.out.println("Lounge status:" + state);
       System.out.println("Men inside:" + malesInside);
       System.out.println("Men waiting:" + malesWaiting);
       System.out.println("Women inside:" + femalesInside);
       System.out.println("Women waiting:" + femalesWaiting);
   }
}


