/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
class Manager extends Adult {

    //constructor
    Manager(String name, int year) {
        super(name, year);
    }

    //function return the string
    public String toString() {
        return "Supervisor " + super.toString();
    }
}

