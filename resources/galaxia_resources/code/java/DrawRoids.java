import javax.swing.*;
import java.awt.*;

public class DrawRoids extends JPanel
{
    public static void main(String[] args) {
        new DrawRoids();
    }

    private JFrame frame;

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        doPaint(g);
    }

    public void doPaint(Graphics g) {
        g.setColor(Color.black);
        g.fillRect(0, 0, 400, 400);
        g.setColor(Color.white);
        DrawImprovedRoid(g, 200, 0);
        // DrawPolygon(g,20, 400);
        System.out.println("rendering...");
    }

    private void DrawImprovedRoid(Graphics g, int size, int points) {
        double x1 = Math.cos(Math.toRadians(45)) * size;
        double y1 = Math.sin(Math.toRadians(45)) * size;
        System.out.println(String.format("x: %f, y: %f", x1, y1));
        double x0 = 0; double y0 = 0;
        g.setColor(Color.red);
        g.drawLine((int) x0, (int) y0, (int) x1, (int) y1);
        g.setColor(Color.green);
        g.drawLine(0, 0, 0, size);
        g.drawLine(0, 0, size, 0);
    }

    public DrawRoids() {
        frame = new JFrame("Example drawn A'roid");
        frame.setSize(400, 400);
        frame.add(this);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

}