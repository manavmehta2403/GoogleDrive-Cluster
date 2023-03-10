/*
 * Assignment 3
 * Author: Ashwinn Balachandran
 * Date: Oct 27th 2019
 */
public class TESTER {
    public static void main(String[] args) {
        //setting the second sequence
        MergeSequence seq2 = new MergeSequence();
        seq2.add(9);
        seq2.add(7);
        seq2.add(4);
        seq2.add(9);
        seq2.add(11);
        //setting the first sequence
        MergeSequence seq1 = new MergeSequence();
        seq1.add(1);
        seq1.add(4);
        seq1.add(9);
        seq1.add(16);

        //printing out the sequences
        System.out.println("Sequence A:" + seq1);
        System.out.println("Sequence B:" + seq2);
        System.out.println("Sequence A+B:" + seq1.append(seq2));
    }
}