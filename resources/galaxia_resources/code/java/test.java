import entities.Asteroid;
import enums.Fragmentation;
import enums.MapSize;

public class test {

    public static void main(String[] args) {
        Asteroid ast = new Asteroid(MapSize.Tiny, Fragmentation.Unstable);
        ast.InitRandomRoid();
        ast.Render();
        System.out.println(ast.Valid);
    }
}
