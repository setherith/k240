package core;

public class GameContainer implements Runnable {

    private Thread thread;
    private Window window;
    private Renderer renderer;

    private boolean running = false;
    private final double UPDATE_CAP = 1.0 / 60.0;

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public float getScale() {
        return scale;
    }

    public String getTitle() {
        return title;
    }

    private int width = 320, height = 240;
    private float scale = 3f;
    private String title = "Galaxia v0.1";

    public GameContainer() {
        window = new Window(this);
        renderer = new Renderer(this);
        thread = new Thread(this);
        thread.run();
    }

    public void start() {

    }

    public Window getWindow() {
        return window;
    }

    public void stop() {

    }

    public void run() {
        running = true;

        boolean render;
        double firstTime;
        double lastTime = System.nanoTime() / 1000000000.0;
        double passedTime;
        double unprocessedTime = 0;

        double frameTime = 0;
        int frames = 0;
        int fps = 0;

        while(running) {
            render = false;

            firstTime = System.nanoTime() / 1000000000.0;
            passedTime = firstTime - lastTime;
            lastTime = firstTime;

            unprocessedTime += passedTime;
            frameTime += passedTime;

            while(unprocessedTime >= UPDATE_CAP) {
                unprocessedTime -= UPDATE_CAP;
                render = true;

                // TODO: Update game
                if (frameTime >= 1.0) {
                    frameTime = 0;
                    fps = frames;
                    frames = 0;
                    System.out.println("FPS: " + fps);
                }
            }

            if(render) {
                renderer.clear();
                // TODO: Render game

                window.update();
                frames++;
            } else {
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        dispose();
    }

    private void dispose() {

    }

    public static void main(String args[]) {
        GameContainer gc = new GameContainer();
        gc.start();
    }

}
