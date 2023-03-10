/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class MASTERCARD extends Payments {

    /*
     * constructor to initialize the mastercard object
     * initialBalance : initial balance of the transaction
     */
    public MASTERCARD(double initialBalance_USD) {
        super(initialBalance_USD);
    }
    //method to get the processing fee
    protected double getProcessingFee() {
        return getInitialBalance_USD() * 0.025;
    }

    //overridden payment info method to print the detail of the transaction
    public void paymentInfo() {
        System.out.println("For Mastercard:");
        System.out.println("  Initial amount   : " + getInitialBalance_USD() + " USD");
        System.out.println("  Processing Fee   : " + getProcessingFee() + " USD");
        System.out.println("  After conversion : " + convertToCAD() + " CAD");
    }

}
