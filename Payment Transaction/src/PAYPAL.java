/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class PAYPAL extends Payments {

    /*
     * the constructor to initialize the paypal object
     * initialBalance : initial transaction amount
     */
    public PAYPAL(double initialBalance_USD) {
        super(initialBalance_USD);
    }
    //method to get the processing fee
    protected double getProcessingFee() {
        return getInitialBalance_USD() * 0.01;
    }

    //the overridden payment info method to print detail of the paypal transaction
    public void paymentInfo() {
        System.out.println("For PAYPAL:");
        System.out.println("  Initial amount   : " + getInitialBalance_USD() + " USD");
        System.out.println("  Processing Fee   : " + getProcessingFee() + " USD");
        System.out.println("  After conversion : " + convertToCAD() + " CAD");
    }

}

