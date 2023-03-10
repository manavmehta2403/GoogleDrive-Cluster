/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class Driver {

    public static void main(String[] args) {
        //instance of visa class, mastercard class and paypal class
        Payments[] payments = {
                new VISA(50),
                new MASTERCARD(100),
                new PAYPAL(120),
        };

        //total CAD
        double totalCAD = 0.0;
        for (Payments payment : payments) {
            totalCAD += payment.convertToCAD();
            payment.paymentInfo();
            System.out.println();
        }

        //Printing the total transaction amount of all the transactions
        System.out.println( "Total amount of money spent in CAD for all types of payments: " + totalCAD + " CAD");

    }
}
