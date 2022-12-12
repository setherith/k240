package enums;

public enum MapSize {
    Large(64),
    Medium(32),
    Small(16),
    Tiny(8);

    private int size;

    MapSize(int size) {
        this.size = size;
    }

    public int Size() {
        return this.size;
    }
}
