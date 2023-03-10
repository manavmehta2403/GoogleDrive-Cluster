import java.util.ArrayList;
import java.util.Scanner;

//main parent class
class Menu{
	//declaring the variables
	private int menu_item_number;
	private String size;
	//constructor
	public Menu(int menu_itm_no, String size) {
		this.menu_item_number = menu_itm_no;
        this.size = size;
	}
	//to_string method
    public String toString() {
        return this.menu_item_number + " " + this.size;
    }
}

//Base Class Pizza Inheritance Menu
class Pizza extends Menu {
	//declare variables
    private static int menu_item_number;
    private static String size;
    private String base, extra_cheese, extra_garlic;
    //constructor to set values
    public Pizza(int menu_itm_no, String size, String base, String ex_cheese, String ex_garlic) {
        super(menu_item_number, size);
        Pizza.menu_item_number = menu_itm_no;
        Pizza.size = size;
        this.base = base;
        this.extra_cheese = ex_cheese;
        this.extra_garlic = ex_garlic;
    }
    //to_string method
    public String toString() {
        return "Pizza:- "+ Pizza.menu_item_number + ", " + Pizza.size + ", " + this.base + ", " + this.extra_cheese + ", " + this.extra_garlic;
    }
}

//Base Class Curry Inheritance Menu
class Curry extends Menu {
    //declare variables
	private static int menu_item_number;
    private static String size;
	private String curry_type;
    //constructor to set values
    public Curry(int menu_itm_no, String size,String cur_type) {
    	super(menu_item_number, size);
    	Curry.menu_item_number = menu_itm_no;
        Curry.size = size;
        this.curry_type = cur_type;
    }
    //to_string method
    public String toString() {
        return "Curry:- "+ Curry.menu_item_number + ", " + Curry.size + ", " + this.curry_type;
    }
}

//Base Class SoftDrinks Inheritance Menu
class SoftDrink extends Menu {
    //declare variables
	private static int menu_item_number;
    private static String size;
    private String flavour, type;
    //constructor to set values
    public SoftDrink(int menu_itm_no, String size, String flvr, String type) {
    	super(menu_item_number, size);
    	SoftDrink.menu_item_number = menu_itm_no;
        SoftDrink.size = size;
        this.flavour = flvr;
        this.type = type;
    }
    //to_string method
    public String toString() {
        return "Soft Drink:- "+SoftDrink.menu_item_number + ", " + SoftDrink.size + ", " + this.flavour + ", " + this.type;
    }
}

//driver class 
public class TestMenu {
	//setting the Scanner class private to use in this class
	//Scanner object as input
    private static Scanner input = new Scanner(System.in);;

    public static void main(String args[]) {
    	//printing the header
    	System.out.println("Welcome to Great International Food Court\n");
    	
    	//taking the array list as array has the fixed size
    	//array list is used to add multiple values as it is immutable
        ArrayList Order = new ArrayList(); 
        String selection = "";
        //continue loop till exit
        while (selection != "Q" || selection != "q" ) {
        	
            //menu displaying
            System.out.println("MENU: add (P)izza, add (C)urry, add (S)oft drink, (D)elete, (L)ist, (Q)uit");
            
            //choose the selection and converting into lower case
            selection = input.next().toLowerCase();
            
            //if the selection is p
            if (selection.equals("p") || selection.equals("P")) { //this is for pizza
                
            	//prompting the user for the menu item number
            	System.out.println("Enter menu item number");
                int menuItem = input.nextInt();
                
                //prompting the user for the size
                System.out.println("Enter size");
                String size = input.next();
                size = size.substring(0,1).toUpperCase() + size.substring(1).toLowerCase();
                
                //prompting for the base
                System.out.println("Enter the base");
                String base = input.next();
                base = base.substring(0,1).toUpperCase() + base.substring(1).toLowerCase();
                
                //asking user whether they need extra cheese or not
                System.out.println("Enter extra cheese (Yes/No)");
                String Cheese = input.next();
                Cheese = Cheese.substring(0,1).toUpperCase() + Cheese.substring(1).toLowerCase();
                
                //asking user whether they need extra garlic or not
                System.out.println("Enter extra Garlic (true/false)");
                String Garlic = input.next();
                Garlic = Garlic.substring(0,1).toUpperCase() + Garlic.substring(1).toLowerCase();
                
                //creating the pizza object
                Pizza pizza = new Pizza(menuItem, size, base, Cheese, Garlic);
                
                //Creating the unqiue key
                Order.add(menuItem);
                
                //adding the pizza in the array list
                Order.add(pizza);
                
                //when its done
                System.out.println("Done"); 
               
            }
            
            //if the selection is c
            else if (selection.equals("c") || selection.equals("C")) { //this is for curry
                
            	//prompting the user for the menu item number
            	System.out.println("Enter menu item number");
                int menuItem = input.nextInt();
                
                //prompting the user for the size
                System.out.println("Enter size");
                String size = input.next();
                size = size.substring(0,1).toUpperCase() + size.substring(1).toLowerCase();
                
                //prompting for the curry type
                System.out.println("Enter curry type");
                String curryType = input.next();
                curryType = curryType.substring(0,1).toUpperCase() + curryType.substring(1).toLowerCase();
                
                //creating the curry object
                Curry curry = new Curry(menuItem, size, curryType);
                
                //Creating the unqiue key
                Order.add(menuItem);
                
                //adding the curry in the array list
                Order.add(curry);
                
                //when its done
                System.out.println("Done");
                
            } 
            
            //if the selection is s
            else if (selection.equals("s") || selection.equals("S")) { //this is for soft drinks
                
            	//prompting the user for the menu item number
            	System.out.println("Enter menu item number");
                int menuItem = input.nextInt();
                
                //prompting the user for the size
                System.out.println("Enter size");
                String size = input.next();
                size = size.substring(0,1).toUpperCase() + size.substring(1).toLowerCase();
                
                //prompting user to enter the flavour
                System.out.println("Enter flavour");
                String flavour = input.next();
                flavour = flavour.substring(0,1).toUpperCase() + flavour.substring(1).toLowerCase();
                
                //adding the type of the cold-drink
                System.out.println("Enter whether it is a bottle or can");
                String type = input.next();
                type = type.substring(0,1).toUpperCase() + type.substring(1).toLowerCase();
                
                //creating the drink object
                SoftDrink drink = new SoftDrink(menuItem, size, flavour, type);
                
                //Creating the unqiue key
                Order.add(menuItem);
                
                //adding the drink in the array list
                Order.add(drink);
                
                //when its done
                System.out.println("Done");
                
                
            } 
            
            //option to d to remove the record from the list
            else if (selection.equals("d") || selection.equals("D")) { //to delete order
                
            	//asking the user for the number to delete the order list item
            	System.out.println("Enter menu item number to delete");
                int number = input.nextInt();
                
                //getting the index value from the entered number
                int index = Order.indexOf(number);
                
                //if the item is not found to be deleted
                if (index == -1) {
                	System.out.println("Not found");
                }
                
                //otherwise
                else {
                	//removing the number by removing it from the list using index value
                	Order.remove(index);
                    Order.remove(index);
                    System.out.println("Done");
                }
                
            } 
            
            //extracting the records from the list
            else if (selection.equals("l") || selection.equals("L")) { //to show all data
                //System.out.println(Order); //testing
            	
            	//iterating over the list to print the array records
            	for (int i = 0; i < Order.size(); i++) {
            		//not printing the unique key values
            		if (i%2 != 0)
            		{
            			System.out.println(Order.get(i));
            		}
                }
            	//Done statement
            	System.out.println("Done");
            }
            
            //using quit to exit the program
            else if (selection.equals("q") || selection.equals("Q")) { //safely exiting
                System.out.println("Thank you!!");
                break;
            }
            
            //if the selection is the wrong statement
            else {
            	System.out.println("Not found");
            }
        }
    }
}
