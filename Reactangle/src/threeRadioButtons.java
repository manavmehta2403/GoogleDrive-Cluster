import java.awt.BorderLayout;

import java.awt.Color;

import java.awt.Container;

import java.awt.Label;

import java.awt.event.ActionEvent;

import java.awt.event.ActionListener;

import java.awt.event.WindowAdapter;

import java.awt.event.WindowEvent;

import javax.swing.JFrame;

import javax.swing.JPanel;

import javax.swing.JRadioButton;



@SuppressWarnings("serial")

public class threeRadioButtons extends JPanel implements ActionListener

{

   JRadioButton redButton = new JRadioButton();

   JRadioButton greenButton = new JRadioButton();

   JRadioButton blueButton = new JRadioButton();



   public threeRadioButtons()

   {
	      
	      JPanel p = new JPanel(new BorderLayout (3,3));
	      p.setSize(200, 100);
	      p.setLocation(50,50);
	      add(BorderLayout.SOUTH,p);

	      setVisible(true);

      add(redButton);

      add(new Label("Red"));

      add(greenButton);

      add(new Label("Green"));

      add(blueButton);

      add(new Label("Blue"));

      redButton.addActionListener(this);

      greenButton.addActionListener(this);

      blueButton.addActionListener(this);



   }



   public void actionPerformed(ActionEvent e)

   {

      Object source = e.getSource();

      //Color color = getBackground();

      if(source == redButton)

      {

    	  setBackground(Color.red);

         blueButton.setSelected(false);

         greenButton.setSelected(false);

      }

      else if(source == greenButton)

      {

    	  setBackground(Color.green);

         blueButton.setSelected(false);

         redButton.setSelected(false);

      }

      else if(source == blueButton)

      {

    	  setBackground(Color.blue);

         redButton.setSelected(false);

         greenButton.setSelected(false);

      }


   }



   @SuppressWarnings("deprecation")

   public static void main(String[] args)

   {

      JFrame frame = new JFrame("Radio");

      frame.setSize(300,200);

      frame.addWindowListener(new WindowAdapter()

            {

         public void windowClosing(WindowEvent c)

         {

            System.exit(0);

         }

            });

      Container content = (Container) frame.getContentPane();

      content.add(new threeRadioButtons());

      frame.show();



   }



}