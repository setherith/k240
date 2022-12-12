package buildings;

import enums.PlantState;

public class Structure {
    public int Health;
    public int MaxHealth;
    public int Level = 1;
    public double Multiplier = 1.1;
    public PlantState State = PlantState.Building;

    public Structure(int hp) {
        this.MaxHealth = hp;
        this.Health = hp;
    }

    public double Proc(double value) {
        if (this.Health == 0 || this.State == PlantState.Destroyed)
            return 0;

        if (this.Health < (0.25 * this.MaxHealth)) {
            this.State = PlantState.Damaged;
            return value * 0.5;
        }

        if (this.State == PlantState.Operational) {
            return value;
        }

        return 0;
    }
}
