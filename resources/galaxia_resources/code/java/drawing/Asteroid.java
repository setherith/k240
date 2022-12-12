package drawing;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class Asteroid extends JPanel {

    private JFrame frame;

    public void paintComponent(Graphics g) {
        DrawAsteroid(g, 200, 200, 30,100);
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

        g.drawPolyline(xs, ys, grade);
        g.drawLine(xs[0], ys[0], xs[xs.length - 1], ys[ys.length - 1]);
    }

    public static void main(String[] args) {
        new Asteroid();
    }

    private void Blank(Graphics g) {
        g.clearRect(0, 0, getWidth(), getHeight());
    }

    public Asteroid() {
        frame = new JFrame("Test");
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
                DrawAsteroid(getGraphics(), 200, 200, 30,100);
            }
        });
    }
}