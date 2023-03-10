import java.util.Arrays;
import java.util.Comparator;

/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class Driver {

    public static void main(String[] args) {

        //array of the objects
        Worker[] w = new Worker[5];
        Manager[] m = new Manager[5];

        //filled the array
        w[0] = new Worker("Ashwinn Bala", 1999);
        w[1] = new Worker("Kawhi Leonard", 1991);
        w[2] = new Worker("Kobe Bryant", 1978);
        w[3] = new Worker("LeBron James", 1984);
        w[4] = new Worker("Joseph Vijay", 1974);

        //filled the array
        m[0] = new Manager("Will Smith", 1968);
        m[1] = new Manager("Jackie Chan", 1954);
        m[2] = new Manager("Arnold Schwarzenegger", 1947);
        m[3] = new Manager("Bruce Lee", 1940);
        m[4] = new Manager("Zakir Hussain", 1951);

        //sorting.........
        Arrays.sort(w, Comparator.comparing(Adult::getYearOfBirth));
        Arrays.sort(m, Comparator.comparing(Adult::getName));

        // printing out list
        System.out.println("Sorted Workers by year of birth:");
        for (int k = 0; k < 5; k++) {
            System.out.println("  " + w[k]);
        }

        System.out.println();

        //printing out list
        System.out.println("Sorted Managers by name:");
        for (int k = 0; k < 5; k++) {
            System.out.println("  " + m[k]);
        }

    }
}
