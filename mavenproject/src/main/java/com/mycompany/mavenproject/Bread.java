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

//Bread class
public class Bread {
    
    //instance variable
    private  String breadType;
    private  int caloriesPerSlice;
    
    //As per the UML default constructor is missing
    //I recommond to use it as it a good practise
    /* if you want to use it please delete this line
        public Bread ()
        {
            breadType = null;
            caloriesPerSlice = null;
        }
    */
    
    //parameterized constructor
    public Bread (String breadType, int caloriesPerSlice)
    {
        this.breadType = breadType;
        this.caloriesPerSlice = caloriesPerSlice;
    }
    
    //mutators and accessors
    String getBreadType()
    {
        return breadType;
    }
    void setBreadType(String breadType)
    {
        this.breadType = breadType;
    }
    
    int getCaloriesPerSlice()
    {
        return caloriesPerSlice;
    }
    void setCaloriesPerSlice(int caloriesPerSlice)
    {
        this.caloriesPerSlice = caloriesPerSlice;
    }
    
}
