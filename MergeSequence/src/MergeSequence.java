/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
import java.util.ArrayList;

public class MergeSequence {

    // SUPPLIED CODE
    private ArrayList<Integer> values;

    public MergeSequence() {
        values = new ArrayList<Integer>();
    }

    public void add(int x) {
        values.add(x);
    }

    public String toString() {
        return values.toString();
    }
    // END OF SUPPLIED CODE

    public MergeSequence append(MergeSequence other) {
        MergeSequence combined = new MergeSequence();
        //append all values from this sequence
        for (Integer amount : values) {
            combined.add(amount);
        }
        //values accessible from within
        for (Integer val : other.values) {
                /* the same class
                appending all values from the other sequence
                */
            combined.add(val);
        }
        return combined;
    }

}