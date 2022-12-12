package scratch;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Engine implements Runnable {

	private JFrame app;
	private JPanel canvas;

	private double FPS = 30;
	private double UPS = 1;
	private boolean running;
	
	private double coal;

	public static void main(String args[]) {
		new Engine().start();
	}

	public void start() {
		running = true;
		run();
	}

	@Override
	public void run() {
		long initialTime = System.nanoTime();
		final double timeF = 1000000000 / FPS;
		final double timeU = 1000000000 / UPS;
		double deltaF = 0, deltaU = 0;
		int frames = 0, ticks = 0;
		long timer = System.currentTimeMillis();

		while (running) {

			long currentTime = System.nanoTime();
			deltaF += (currentTime - initialTime) / timeF;
			deltaU += (currentTime - initialTime) / timeU;
			initialTime = currentTime;

			if (deltaU >= 1) {
				getInput();
				update();
				ticks++;
				deltaU--;
			}

			if (deltaF >= 1) {
				render();
				frames++;
				deltaF--;
			}

			if (System.currentTimeMillis() - timer > 1000) {
				System.out.println(String.format("UPS: %s, FPS: %s", ticks, frames));
				frames = 0;
				ticks = 0;
				timer += 1000;
			}
		}
	}

	public Engine() {
		new Thread(this);

		app = new JFrame("Scratch Test");
		app.setSize(400, 400);
		app.setLocationRelativeTo(null);
		app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		app.setVisible(true);

		canvas = new JPanel();
		app.add(canvas);
	}

	private void render() {
		Graphics g = canvas.getGraphics();
		Random r = new Random();
		g.clearRect(0, 0, 400, 400);
		g.setColor(new Color(r.nextInt()));
		g.fillRect(r.nextInt(380), r.nextInt(380), 10, 10);
		Graphics2D g2 = (Graphics2D) g;
		g.setColor(Color.black);
		g2.drawString("C: " + coal, 10, 10);
	}

	private void getInput() {

	}

	private void update() {
		System.out.println("Coal: " + coal);
		coal+= 0.5;
	}

}
