package drawing;

import javax.swing.*;
import java.awt.*;

public class IsoTop extends JPanel {

    private JFrame frame;

    public void paintComponent(Graphics g) {
        DrawGrid(g, 200, 200, -30);
    }

    private void DrawGrid(Graphics g, int a, int b, int ang) {
        g.setColor(Color.black);
        g.fillRect(0, 0, getWidth(), getHeight());
        g.setColor(Color.white);

        DrawIsoBox(g, new Point(200, 200), 100);
    }

    private void DrawIsoBox(Graphics g, Point origin, int size) {
        Point last = origin;
        int angle = -30;

        for (int i = 0; i < 4; i++) {
            Point p = ToPolar(last, size, angle);
            DrawLinePointToPoint(g, last, p);
            if (i % 2 == 0) {
                angle += 60;
            } else {
                angle += 120;
            }
            last = p;
        }
    }

    private void DrawLinePointToPoint(Graphics g, Point origin, Point destination) {
        g.drawLine(origin.x, origin.y, destination.x, destination.y);
    }

    private Point ToPolar(Point origin, int distance, int angle) {
        return new Point((int) (origin.x + Math.cos(Math.toRadians(angle)) * distance), (int) (origin.y + Math.sin(Math.toRadians(angle)) * distance));
    }

    public static void main(String[] args) {
        new IsoTop();
    }

    public IsoTop() {
        frame = new JFrame("Iso");
        frame.add(this);
        frame.pack();
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}