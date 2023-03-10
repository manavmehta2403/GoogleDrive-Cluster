import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

/*
 * (Move a rectangle using mouse) a program that displays a rectangle. 
 * You can point the mouse inside the rectangle and drag (i.e., move with mouse pressed) the rectangle wherever the mouse goes. 
 * The mouse point becomes the center of the rectangle.
*/

//Creating the ShapeMover class on javaFx
public class ShapeMover extends Application {

	//Setting the start method by passing the scene argument
    @Override
    public void start(Stage frame) {
    	// setting the scene width and height
        double width = 1000;
        double height = 1000;
        
        //using inbuilt rectangle class to make rectangle
        //passing parameters are width, height and the co-ordinates x and y for position
        Rectangle rect = new Rectangle(width/2, height/2, 100, 100);
        //filling the color of the react
        rect.setFill(Color.WHITE);
        
        //adding react to the pane
        Pane pane = new Pane(rect);
        
        //Calling the mouse drag event
        rect.setOnMouseDragged(e-> {
        	//maintaining at the center by dividing the width and height by 2
            rect.setX(e.getX() - rect.getWidth() / 2);
            rect.setY(e.getY() - rect.getHeight() / 2);
        });
        
        //Stage setScene method to add pane with the size of the frame and the color
        frame.setScene(new Scene(pane, width, height, Color.BLACK));
        //naming the title of the frame
        frame.setTitle("Shape Mover - Reactangle");
        //calling the frame to pop up
        frame.show();
    }
    
    //main method to run the program
    public static void main(String[] args) {
        launch(args);
    }
}