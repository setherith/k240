package enums;

public enum Tile {
    Space(0),
    Asteroid(1);

    private int tile;

    Tile(int tile) {
        this.tile = tile;
    }

    public int Value() {
        return this.tile;
    }
}
