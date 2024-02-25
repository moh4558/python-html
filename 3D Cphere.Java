import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class RedAndBlueDotSphere extends JFrame {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final int NUM_DOTS = 1500;
    private static final int RADIUS = 5;

    private JPanel canvas;

    public RedAndBlueDotSphere() {
        setTitle("Red and Blue Dot Sphere");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        canvas = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawDots(g);
            }
        };

        add(canvas);

        setVisible(true);
    }

    private void drawDots(Graphics g) {
        Random random = new Random();

        for (int i = 0; i < NUM_DOTS; i++) {
            int x = random.nextInt(WIDTH);
            int y = random.nextInt(HEIGHT);
            Color color = random.nextBoolean() ? Color.RED : Color.BLUE;

            g.setColor(color);
            g.fillOval(x, y, RADIUS, RADIUS);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new RedAndBlueDotSphere();
            }
        });
    }
}
