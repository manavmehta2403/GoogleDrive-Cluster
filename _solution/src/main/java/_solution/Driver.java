/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package _solution;

/**
 *
 * @author Mehta
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import javax.swing.JOptionPane;

/**
 *
 * @Author :
 * @Date : 19 Feb, 2017,1:57:19 AM
 */
public class Driver {
    public static void main(String[] args) {
        List<Toy> toys = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        String option=null;
        String name;
        int age;
        String toyName;
        // Displays welcome message
        JOptionPane.showMessageDialog(null,"Welcome to Gift World.");
        do{
            // Accepts name and age
            name = JOptionPane.showInputDialog(null, " Enter Name: ");
            age = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter Age (between 1 - 10): "));
            
            //Rubrics of the age
            System.out.println("Age Range:");
            System.out.println(" plushie: 0 to 2 years");
            System.out.println(" book: 4 to 7 years");
            System.out.println(" block: 3 to 5 years");

            //Accept the toy name
            toyName  = JOptionPane.showInputDialog(null, " Choose a toy: plushie, blocks, or book:  ");
            Toy toy = new Toy(toyName,age);
            while (!toy.ageOK()){
                age = Integer.parseInt(JOptionPane.showInputDialog(null, "change the Age:"));
                toy.setAge(age);
            }
            
            //Checking the additional items
            String flag;
            flag = JOptionPane.showInputDialog(null, "You want to add card?yes/no:");
            toy.addCard(flag);
            flag = JOptionPane.showInputDialog(null, "You want to add balloon?yes/no:");
            toy.addBalloon(flag);
            toys.add(toy);
            
            //If want more toys
            option = JOptionPane.showInputDialog(null, "you want to purchase More?yes/no:");
        }while (!option.equalsIgnoreCase("no"));

        int orderId = 100000 + new Random().nextInt(900000);

        System.out.println("------------------- Yor Order --------------------------");
        System.out.println("--------------------------------------------------------");
        System.out.println("Order Number :"+orderId);
        double orderTotal=0;
        System.out.print(String.format("%-15s%-15s%-15s\n","Name","Toy Name","Cost"));
        for (Toy toy:toys){
            System.out.print(String.format("%-15s%-15s%-13.2f\n",name,toy.getToy(),toy.getCost()));
            orderTotal+=toy.getCost();
        }
        System.out.println("---------------------------------------------------------");
        System.out.print(String.format("%-15s%-13.2f\n","Order total:",orderTotal));
    }
}