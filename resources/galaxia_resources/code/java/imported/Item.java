package imported;

public class Item {
	public String Name;
	public double Weight;
	public double Value;

	@Override
	public String toString() {
		return String.format("Item: %s | Weight: %1.2f | Value: %1.2f", Name, Weight, Value);
	}
}