/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class VISA extends Payments {

    /*
     * Constructor to initialize the visa class object
     * initialBalance : initial balance
     */
    public VISA(double initialBalance_USD) {
        super(initialBalance_USD);
    }

    //the overridden paymentInfo method to print the transaction detail
    public void paymentInfo() {
        System.out.println("For VISA:");
        System.out.println("  Initial amount   : " + getInitialBalance_USD() + " USD");
        System.out.println("  Processing Fee   : " + getProcessingFee() + " USD");
        System.out.println("  After conversion : " + convertToCAD() + " CAD");
    }
    //method to get the processing fee
    public double getProcessingFee() {
        return getInitialBalance_USD() * 0.02;
    }

}
