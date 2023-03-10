/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Mehta
 */
class Add {
        
        private int num1;
        private int num2;
    
     int add(int num1, int num2)
    {
        this.num1 = num1;
        this.num2 = num2;
        int result = num1 + num2;
        return result;
    }
    
}   
    
    
    public class Adder
    {
        public static void main(String[] args)
        {
            int num1 = 5;
            int num2 = 6;
            
            Add a = new Add();
            
            int result = a.add(num1,num2);
            
            System.out.println(result);
        }
    }
    
