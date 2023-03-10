/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
class Adult {

    //properties
    private final String name;
    private final int yearOfBirth;

    //constructor
    Adult(String name, int year) {
        this.name = name;
        this.yearOfBirth = year;
    }

    public String toString() {
        return name + ", born " + yearOfBirth;
    }

    public String getName() {
        return name;
    }

    public int getYearOfBirth() {
        return yearOfBirth;
    }

}


