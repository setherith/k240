package imported;

import java.util.UUID;

public class Ship {

	public UUID Id;
	public String Name;
	public Inventory Inventory;
	
	public Ship() {
		Id = UUID.randomUUID();
	}
}
