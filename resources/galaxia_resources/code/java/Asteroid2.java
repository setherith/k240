

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class Asteroid2 extends JPanel {

	private static final long serialVersionUID = 1L;

	private JFrame frame;

    private int x = 200; private int y = 200;
    private int grade = 30;
    private int size = 50;

    public void paintComponent(Graphics g) {
        DrawAsteroid(g, x, y, grade, size);
    }

    private void DrawAsteroid(Graphics g, int x, int y, int grade, int size) {
        Random rand = new Random();
        int angle = 360 / grade; int bearing = 0;
        int[] xs = new int[grade]; int[] ys = new int[grade];

        for (int i = 0; i < grade; i++) {
            xs[i] = (int) (x + Math.cos(Math.toRadians(bearing)) * size - (rand.nextDouble() * size * 0.25));
            ys[i] = (int) (y + Math.sin(Math.toRadians(bearing)) * size - (rand.nextDouble() * size * 0.25));
            bearing += angle;
        }

        g.setColor(Color.GRAY);
        g.fillPolygon(xs, ys, grade);
    }

    public static void main(String[] args) {
        new Asteroid2();
    }

    private void Blank(Graphics g) {
        g.clearRect(0, 0, getWidth(), getHeight());
    }

    public Asteroid2() {
        frame = new JFrame("Asteroid2");
        frame.add(this);
        frame.pack();
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                super.mouseClicked(e);
                Blank(getGraphics());
                DrawAsteroid(getGraphics(), x, y, grade, size);
            }
        });
    }


}
