package ui;

import java.awt.Graphics;
import java.awt.Image;

import javax.swing.JPanel;

public class MenuItem {

	public JPanel panel;

	public Image Draw() {
		panel = new JPanel();
		panel.setSize(400, 20);
		Graphics g = panel.getGraphics();
		
		g.clearRect(0, 0, 400, 20);
		return panel.createImage(400, 20);
	}
	
}
