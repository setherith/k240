package buildings;

public class Mine extends Structure {
    private int ProductionRate = 1;
    private int BaseRate = 100;

    public Mine() {
        super(500);
    }

    public double Proc() {
        return super.Proc(this.BaseRate + (this.Level - 1) * this.Multiplier * this.ProductionRate);
    }

}
