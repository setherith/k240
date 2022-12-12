package ui;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class MenuScreen extends JPanel {

	private static final long serialVersionUID = 1L;
	private final double VERSION = 0.1;
	private final int WIDTH = 800;
	private final int HEIGHT = 600;

	private JFrame app;

	private int[][] stars;

	public static void main(String[] args) {
		new MenuScreen();
	}

	public MenuScreen() {

		Random r = new Random();
		stars = new int[1000][3];

		for (int i = 0; i < 1000; i++) {
			stars[i][0] = r.nextInt(WIDTH);
			stars[i][1] = r.nextInt(HEIGHT);
			stars[i][2] = r.nextInt(255);
		}

		app = new JFrame(String.format("Galaxia v%1.1f", VERSION));
		setPreferredSize(new Dimension(WIDTH, HEIGHT));
		app.add(this);
		app.pack();
		app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		app.setLocationRelativeTo(null);
		app.setVisible(true);
	}

	public void paintComponent(Graphics g) {
		g.setColor(Color.black);
		g.fillRect(0, 0, WIDTH, HEIGHT);

		for (int i = 0; i < 1000; i++) {
			g.setColor(new Color(stars[i][2], stars[i][2], stars[i][2]));
			g.drawLine(stars[i][0], stars[i][1], stars[i][0], stars[i][1]);

			stars[i][0] += 1;
		}
		
		Image mn = new MenuItem().Draw();
		g.drawImage(mn, 10, 10, 400, 20, this);
	}
}