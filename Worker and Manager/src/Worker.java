/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
class Worker extends Adult {

    //constructor
    Worker(String name, int year) {
        super(name, year);
    }

    //function return the string
    public String toString() {
        return "Engineer " + super.toString();
    }
}

