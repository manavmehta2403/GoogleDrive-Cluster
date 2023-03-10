/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mavenproject;

/**
 *
 * @author StudyMade
 */
//Sandwich class
public class Sandwich {
    private Bread bread;
    private Filling filling;
    
    //As per the UML default constructor is missing
    //I recommond to use it as it a good practise
    /* if you want to use it please delete this line
        public Sandwich ()
        {
            bread = null;
            filling = null;
        }
    */
    
     //parameterized constructor
    public Sandwich(String breadType, int caloriesPerSlice, String fillingType, int caloriesPerServing) 
    {
	bread = new Bread(breadType, caloriesPerSlice);
	filling = new Filling(fillingType, caloriesPerServing);
    }
    
    //mutators and accessors
    public Filling getFilling() 
    {	
        return filling;
    }
    void setFilling(Filling filling)
    {
        this.filling = filling;
    }
    
    public Bread getBread() 
    {	
        return bread;
    }
    void setBread(Bread bread)
    {
        this.bread = bread;
    }
    
    /*
        //Another approach to get the details of
        //filling and bread class variable values
        
        //getters and setters for filling and bread class respectively
    
    public String getFillingType() {	
        return filling.getFillingType();
    }
    public int getFillingCalories() {
	return filling.getCaloriesPerServing();
    }
    
    public String getBreadType() {
	return bread.getBreadType();
    }
    public int getCaloriesPerSlice() {
        return bread.getCaloriesPerSlice();
    }
    */
    
    
    //total method to return the total value of the calories from
    // both the slices of bread ( that's why 2 is multiplied) and 
    //calories from filling
    public int getTotalCalories() {
	return filling.getCaloriesPerServing()+ (bread.getCaloriesPerSlice() * 2);
    }
}