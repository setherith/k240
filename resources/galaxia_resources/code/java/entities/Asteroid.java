package entities;

import enums.Fragmentation;
import enums.MapSize;
import enums.Tile;

import java.util.Random;

public class Asteroid {

    private MapSize size;
    private Fragmentation fragmentation;
    private int[] map;

    public boolean Valid;

    public Asteroid() {
        size = MapSize.Medium;
        fragmentation = Fragmentation.SemiStable;
    }

    public Asteroid(MapSize size, Fragmentation frag) {
        this.size = size;
        this.fragmentation = frag;
    }

    public void InitRandomRoid() {
        // setup
        map = new int[size.Size() * size.Size()];

        // make the asteroid fill the map
        for (int i = 0; i < map.length; i++) {
            map[i] = Tile.Asteroid.Value();
        }

        int roughness;
        switch (fragmentation) {
            case Unstable:
                roughness = size.Size();
                break;
            case SemiStable:
                roughness = size.Size() / 2;
                break;
            case Stable:
                roughness = size.Size() / 4;
                break;
            default:
                roughness = 1;
        }

        // generate
        Random rand = new Random();

        this.Valid = true;

        // break map into chunks of 'size'
        for (int i = 0; i < map.length; i += size.Size()) {

            // select two random values and mark them as void space from each end of chunk
            int left = rand.nextInt(roughness);

            for (int l = 0; l < left; l++) {
                map[i + l] = Tile.Space.Value();
            }

            int right = rand.nextInt(roughness);
            for (int r = 0; r < right; r++) {
                map[i + size.Size() - 1 - r] = Tile.Space.Value();
            }

            if (left + right >= size.Size()) {
                this.Valid = false;
            }
        }

    }

    public void Render() {
        // render
        for (int i = 1; i <= map.length; i++) {

            switch (map[i - 1]) {
                case 1:
                    System.out.print("[ ]");
                    break;
                case 0:
                    System.out.print("   ");
                    break;
            }

            if (i % size.Size() == 0) System.out.print("\n");
        }
    }

}
