
package test;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Frame extends JFrame {

private double tempNumbers1 = 0;
private double tempNumbers2 = 0;

private byte function = -1;


private JTextField resultJText;

public Frame() {

    JButton[] numberButtons = new JButton[10];

    for ( int i = 9; i >= 0; i--) {
        numberButtons[i] = new JButton(Integer.toString(i));
    }

    JButton enterButton     = new JButton("Enter");
    JButton cButton         = new JButton("C");
    JButton multiplyButton  = new JButton("*");
    JButton divideButton    = new JButton("/");
    JButton addButton       = new JButton("+");
    JButton substractButton = new JButton("-");


    resultJText = new JTextField();
        resultJText.setPreferredSize(new Dimension(160, 20));
        resultJText.setBackground(Color.WHITE);
        resultJText.setEnabled(false);
        resultJText.setHorizontalAlignment(4);
        resultJText.setDisabledTextColor(Color.BLACK);


    JPanel motherPanel = new JPanel();
        motherPanel.setLayout(new BoxLayout(motherPanel, BoxLayout.Y_AXIS));

    JPanel textPanel = new JPanel();
        textPanel.setPreferredSize(new Dimension(160, 20));
        textPanel.add(resultJText);

    JPanel numberButtonsPanel = new JPanel();
        numberButtonsPanel.setPreferredSize(new Dimension(160, 100));

        for(int i = 9; i>=0; i--) {
            numberButtonsPanel.add(numberButtons[i]);
        }

    JPanel functionButtonPanel = new JPanel();
        functionButtonPanel.setPreferredSize(new Dimension(160, 35));
        functionButtonPanel.add(enterButton);
        functionButtonPanel.add(cButton);
        functionButtonPanel.add(multiplyButton);
        functionButtonPanel.add(divideButton);
        functionButtonPanel.add(addButton);
        functionButtonPanel.add(substractButton);
//
//    numberButtonsAction[] numberButtonActions = new numberButtonsAction[10];
//    for ( int i = 0; i < 10; i++ ) {
//        numberButtonActions[i] = new numberButtonsAction(numberButtons[i]);
//        numberButtons[i].addActionListener(numberButtonActions[i]);
//    }
//
//    EnterButton enter = new EnterButton();
//        enterButton.addActionListener(enter);
//
//    CButton c = new CButton();
//        cButton.addActionListener(c);
//
//    MultiplyButton multiply = new MultiplyButton();
//        multiplyButton.addActionListener(multiply);
//
//    DivideButton divide = new DivideButton();
//        divideButton.addActionListener(divide);
//
//    AddButton add = new AddButton();
//        addButton.addActionListener(add);
//
//    SubtractButton subtract = new SubtractButton();
//        substractButton.addActionListener(subtract);

    motherPanel.add(textPanel);
    motherPanel.add(numberButtonsPanel);
    motherPanel.add(functionButtonPanel);
    add(motherPanel);

    setTitle("ButtonTest");
    setSize(180, 290);
    setLocationByPlatform(true);
    setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    setVisible(true);
}
public static void main(String[] args){
    new Frame();
}
}