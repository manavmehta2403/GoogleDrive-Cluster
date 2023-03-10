import java.util.Scanner;

class Square {

	 public static void main(String args[]) {

	}

	      /**
		 * @uml.property  name="height"
		 */
	    private double height;

	      /**
		 * @uml.property  name="width"
		 */
	    private double width;



	      public Square(double side)

	      {

	            height = side;

	            width = side;

	      }



	      public double computeSurfaceArea()

	      {

	            return (height*width);

	      }



	      public double computerPerimeter()

	      {

	            return(2*(height+width));

	      }

	}
class Cube extends Square{

	 public static void main(String args[]) {

	}



	      /**
		 * @uml.property  name="depth"
		 */
	    private double depth ;



	      public Cube(double side)

	      {

	            super(side);

	            depth = side;

	      }



	      public double computeSurfaceArea()

	      {

	            return(6*super.computeSurfaceArea());

	      }



	      public double computeVolume()

	      {

	            return(super.computeSurfaceArea()*depth);

	      }

	}



	//ShowSquareCube
public class ShowSquareCube {

      public static void main(String[] args) {



            double side;



            Scanner scan = new Scanner(System.in);

            System.out.print("Please enter the dimension for a square : ");

            side = scan.nextDouble();



            Square square = new Square(side);

            Cube cube = new Cube(side);



            System.out.println("The surface area of Square : "+square.computeSurfaceArea());

            System.out.println("The perimeter of Square : "+square.computerPerimeter());

            System.out.println("The surface area of Cube : "+cube.computeSurfaceArea());

            System.out.println("The volume of Cube : "+cube.computeVolume());

            scan.close();

      }

}