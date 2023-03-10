/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mavenproject;

import java.util.Scanner;

/**
 *
 * @author StudyMade
 */

//TIp Tokery class
public class TipTopBakery {
    
    public static void main(String[] args) {
        //Creating Scanner object for user input
        Scanner input = new Scanner (System.in);

        //declaring variables
        String bread_type; int bread_calories;

        String filling; int filling_calories;
        
        
        //lopp to ask the details and 
        // if continue is false then program quit
        char continues = 'y';

       while (continues == 'y' || continues == 'Y')
       {
           //prompt user for the input of bread and filling and their calories
           System.out.println("Please enter the bread type: ");
           bread_type = input.next();

           System.out.println("Please enter the calories for slice: ");
           bread_calories = input.nextInt();

           System.out.println("Please enter the stuffing: ");
           filling = input.next();

           System.out.println("Please enter the calories for filling: ");
           filling_calories = input.nextInt();

           //Creating the sandwich object
           Sandwich s_w = new Sandwich(bread_type,bread_calories,filling,filling_calories);


           //Printing the details
           System.out.println("This sandwich has two slices of "+ s_w.getBread().getBreadType() + " bread ("
                              + s_w.getBread().getCaloriesPerSlice() + " calories per slice) with " 
                              + s_w.getFilling().getFillingType() + " filling(" + s_w.getFilling().getCaloriesPerServing() 
                              + " calories per serving).\n"+"The total number of calories for the sandwich is " + s_w.getTotalCalories()+".");
           
           
           /*
            In case of another approach (mentioned in Sandwich class)
           use in the same order
           s_w.getBreadType(), s_w.getCaloriesPerSlice()
           s_w.getFillingType(), s_w.getFillingCalories()
           */
           //checking whether user wants to exit or enter more input
           System.out.println("Do you want to continue?(y/n): ");
           continues = input.next().charAt(0);

       }
   
    }
   
}
