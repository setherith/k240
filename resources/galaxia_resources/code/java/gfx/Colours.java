package gfx;

import java.util.Random;

public class Colours {

	private static Random r = new Random();

	public static int[] Black = new int[] { 0, 0, 0 };
	public static int[] White = new int[] { 255, 255, 255 };
	public static int[] Random = new int[] { 
			155 + r.nextInt(100), 
			155 + r.nextInt(100), 
			155 + r.nextInt(100) };
}
