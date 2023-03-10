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
//Filling class
public class Filling {
//instance variable
    private  String fillingType;
    private  int caloriesPerServing;
    
    //As per the UML default constructor is missing
    //I recommond to use it as it a good practise
    /* if you want to use it please delete this line
        public Filling ()
        {
            fillingType = null;
            caloriesPerServing = null;
        }
    */
    
    //parameterized constructor
    public Filling (String fillingType, int caloriesPerServing)
    {
        this.fillingType = fillingType;
        this.caloriesPerServing = caloriesPerServing;
    }
    
    //mutators and accessors
    String getFillingType()
    {
        return fillingType;
    }
    void setFillingType(String fillingType)
    {
        this.fillingType = fillingType;
    }
    
    int getCaloriesPerServing()
    {
        return caloriesPerServing;
    }
    void setCaloriesPerServing(int caloriesPerServing)
    {
        this.caloriesPerServing = caloriesPerServing;
    }
    
}

