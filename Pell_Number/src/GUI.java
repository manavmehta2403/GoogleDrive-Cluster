import java.io.FileWriter;
import java.io.IOException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

public class GUI {
	/**
	 * 
	 */
	// Variables declaration - do not modify
	private javax.swing.ButtonGroup buttonGroup1;
	private javax.swing.JButton jButton1;
	private javax.swing.JLabel jLabel1;
	private javax.swing.JLabel jLabel2;
	private javax.swing.JLabel jLabel3;
	private javax.swing.JRadioButton jRadioButton1;
	private javax.swing.JRadioButton jRadioButton2;
	private javax.swing.JTextField jTextField1;
	private javax.swing.JTextField jTextField2;
	private javax.swing.JTextField jTextField3;
	private javax.swing.JFrame jFrame1;
	// End of variables declaration

	private static Sequence Sequence;

	/**
	 * Creates new form GUI
	 */
	public GUI() {
		// creating components in it
		initComponents();
		// Setting the jRadioButton is true
		jRadioButton1.setSelected(true);
	}

	/**
	 * This method is called from within the constructor to initialize the form.
	 */

	private void initComponents() {

		// Creating the variables
		buttonGroup1 = new javax.swing.ButtonGroup();
		jRadioButton1 = new javax.swing.JRadioButton();
		jRadioButton2 = new javax.swing.JRadioButton();
		jLabel1 = new javax.swing.JLabel();
		jLabel2 = new javax.swing.JLabel();
		jLabel3 = new javax.swing.JLabel();
		jTextField1 = new javax.swing.JTextField();
		jTextField2 = new javax.swing.JTextField();
		jTextField3 = new javax.swing.JTextField();
		jButton1 = new javax.swing.JButton();
		jFrame1 = new javax.swing.JFrame();

		// Creating all the close and minimize operations
		jFrame1.setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

		// WindowsLister Events on Frame
		jFrame1.addWindowListener(new java.awt.event.WindowListener() {
			public void windowClosed(java.awt.event.WindowEvent evt) {
				try {
					jFrame1WindowClosed(evt);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			@Override
			public void windowActivated(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub

			}

			@Override
			public void windowClosing(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub
				try {
					jFrame1WindowClosed(evt);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			@Override
			public void windowDeactivated(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub

			}

			@Override
			public void windowDeiconified(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub

			}

			@Override
			public void windowIconified(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub

			}

			@Override
			public void windowOpened(java.awt.event.WindowEvent evt) {
				// TODO Auto-generated method stub

			}
		});

		// ActionListener Event on Radio Buttons
		buttonGroup1.add(jRadioButton1);
		jRadioButton1.setText("Iterative");
		jRadioButton1.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jRadioButton1ActionPerformed(evt);
			}
		});

		buttonGroup1.add(jRadioButton2);
		jRadioButton2.setText("Recursive");
		jRadioButton2.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jRadioButton2ActionPerformed(evt);
			}
		});

		// Labels Text Alignments
		jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
		jLabel1.setText("Enter your number");

		jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
		jLabel2.setText("Result");

		jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
		jLabel3.setText("Efficiency");

		// ActionListener Event on Text Fields
		jTextField1.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jTextField1ActionPerformed(evt);
			}
		});

		jTextField2.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jTextField2ActionPerformed(evt);
			}
		});

		jTextField3.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jTextField3ActionPerformed(evt);
			}
		});

		// ActionListener Event on Buttons
		jButton1.setText("Compute");
		jButton1.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				jButton1ActionPerformed(evt);
			}
		});

		// don't change the layout //the components are aligned with specific field
		javax.swing.GroupLayout layout = new javax.swing.GroupLayout(jFrame1.getContentPane());
		jFrame1.getContentPane().setLayout(layout);
		layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout
				.createSequentialGroup().addContainerGap()
				.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
						.addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
								.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
										.addComponent(jLabel1, javax.swing.GroupLayout.DEFAULT_SIZE,
												javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
										.addComponent(jLabel2, javax.swing.GroupLayout.DEFAULT_SIZE,
												javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
										.addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 91,
												javax.swing.GroupLayout.PREFERRED_SIZE))
								.addGap(53, 53, 53)
								.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
										.addComponent(jButton1, javax.swing.GroupLayout.DEFAULT_SIZE, 214,
												Short.MAX_VALUE)
										.addComponent(jTextField1).addComponent(jTextField2).addComponent(jTextField3)))
						.addGroup(javax.swing.GroupLayout.Alignment.TRAILING,
								layout.createSequentialGroup()
										.addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 211,
												javax.swing.GroupLayout.PREFERRED_SIZE)
										.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
												.addComponent(jRadioButton2, javax.swing.GroupLayout.PREFERRED_SIZE, 95,
														javax.swing.GroupLayout.PREFERRED_SIZE)
												.addComponent(jRadioButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 95,
														javax.swing.GroupLayout.PREFERRED_SIZE))
										.addGap(64, 64, 64)))
				.addGap(20, 20, 20)));
		layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
				.addGroup(layout.createSequentialGroup().addGap(20, 20, 20).addComponent(jRadioButton1)
						.addGap(18, 18, 18).addComponent(jRadioButton2).addGap(30, 30, 30)
						.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
								.addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE,
										javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
								.addComponent(jLabel1))
						.addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED).addComponent(jButton1)
						.addGap(17, 17, 17)
						.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
								.addComponent(jLabel2).addComponent(jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE,
										javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
						.addGap(21, 21, 21)
						.addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
								.addComponent(jLabel3).addComponent(jTextField3, javax.swing.GroupLayout.PREFERRED_SIZE,
										javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
						.addContainerGap(22, Short.MAX_VALUE)));
		// layout ends

		// adding all the components in the jFrame1
		jFrame1.pack();
	}

	// methods for Action performed on TextFields
	private void jTextField2ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
	}

	// methods for Action performed on Button
	private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
		String text = jTextField1.getText(); // Retrieving user value
		String result = "";
		if (jRadioButton1.isSelected()) { // checking if the radio button is selected
			result = "" + Sequence.computeIterative(Integer.parseInt(text)); // calling the iterative function
		} else if (jRadioButton2.isSelected()) { // checking if radio button 2 is selected
			result = "" + Sequence.computeRecursive(Integer.parseInt(text)); // calling Recursive function
		} else { // when there is no text then result should be empyt
			result = "";
		}
		jTextField2.setText(result); // setting the result in the Result text field
		jTextField3.setText("" + Sequence.getEfficiency()); // getting the efficiency value and setting it in efficiency
															// text field
	}

	// methods for Action performed on Radio Buttons
	private void jRadioButton1ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
		jRadioButton1.setSelected(true);
	}

	private void jRadioButton2ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
	}

	private void jTextField1ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
	}

	private void jTextField3ActionPerformed(java.awt.event.ActionEvent evt) {
		// TODO add your handling code here:
	}

	// WindowsAction method when file is closed
	private void jFrame1WindowClosed(java.awt.event.WindowEvent evt) throws IOException {
		// TODO Auto-generated method stub
		int iterativeEff;
		int recursiveEff;
		/*
		 * Please create the .csv file where ever you want to you before running the
		 * program
		 */
		// opening the file
		// Please change the
		// C:\\Users\\Mehta\\Documents\\NetBeansProjects\\Pell_Number\\src\\Efficiency
		// Values.csv => with your directory (path of the file)
		FileWriter f_csv = new FileWriter(
				"C:\\Users\\Mehta\\Documents\\NetBeansProjects\\Pell_Number\\src\\Efficiency Values.csv");
		// looping for ten values
		f_csv.write("Number" + "," + "Iterative Method" + "," + "Recursive Method" + "\n");
		for (int n = 0; n <= 10; n++) {
			// calling the iterative method
			Sequence.computeIterative(n);
			// storing its efficiency
			iterativeEff = Sequence.getEfficiency();
			// calling the recursive methods
			Sequence.computeRecursive(n);
			// storing recursive efficiency
			recursiveEff = Sequence.getEfficiency();
			// writing the the values in the file as .csv (Do not forget to put commas)
			f_csv.write(n + "," + iterativeEff + "," + recursiveEff + "\n");
		}
		// closing the file
		f_csv.close();
	}

	public static void main(String args[]) {
		// running the GUI
		try {
			for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
				if ("Nimbus".equals(info.getName())) {
					javax.swing.UIManager.setLookAndFeel(info.getClassName());
					break;
				}
			}
			// checking error for any exception
		} catch (ClassNotFoundException ex) {
			java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (InstantiationException ex) {
			java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (IllegalAccessException ex) {
			java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (javax.swing.UnsupportedLookAndFeelException ex) {
			java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		}
		// </editor-fold>

		/* Create and display the form */
		// invoking the runnable method to display on the screen
		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				new GUI().jFrame1.setVisible(true);
			}
		});
	}
}
