/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */

/**
 * This is the super class for all type of the payments
 */
public abstract class Payments implements PaymentInterface {

    //Declaring the instance variable initial balance
    private final double initialBalance_USD;
    //Intitial balance in USD
    public Payments(double initialBalance_USD) {
        this.initialBalance_USD = initialBalance_USD;
    }

    public double getInitialBalance_USD() {
        return initialBalance_USD;
    }
    //conveerting to CAD
    public double convertToCAD() {
        return (getInitialBalance_USD() - getProcessingFee()) * 1.35;
    }

    //method to get the processing fee
    protected abstract double getProcessingFee();

}

