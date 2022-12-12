package scratch;

import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import org.lwjgl.opengl.GL;

public class Main {

	public Main() {
		
		if (!glfwInit()) {
			System.err.println("GLFW failed to start!");
			System.exit(-1);
		}
		
		long win = glfwCreateWindow(640, 480, "Window", 0, 0);
		
		glfwShowWindow(win);
		
		glfwMakeContextCurrent(win);
		
		GL.createCapabilities();
		
		glEnable(GL_TEXTURE_2D);
		Texture tex = new Texture("./resources/gfx/test.png");
		
		while (!glfwWindowShouldClose(win)) {
			glfwPollEvents();
			
			if (glfwGetKey(win, GLFW_KEY_ESCAPE) == GL_TRUE) {
				glfwSetWindowShouldClose(win, true);
			}
			
			glClear(GL_COLOR_BUFFER_BIT);
			
			tex.bind();
			
			glBegin(GL_QUADS);
				glTexCoord2f(0, 0);
				glVertex2f(-0.5f, 0.5f);
				
				glTexCoord2f(1, 0);
				glVertex2f(0.5f, 0.5f);
				
				glTexCoord2f(1, 1);
				glVertex2f(0.5f, -0.5f);
				
				glTexCoord2f(0, 1);
				glVertex2f(-0.5f, -0.5f);
			glEnd();
			
			glfwSwapBuffers(win);
		}
		
		glfwTerminate();
	}
	
	public static void main(String args[]) {
		new Main();
	}

}
