package imported;

import static org.junit.Assert.assertTrue;

import org.junit.jupiter.api.Test;

import imported.Item;
import imported.Person;

class ItemTest {

	@Test
	void ItemToStringTest() {
		Item i = new Item();
		i.Name = "Person";
		i.Value = 4096.225;
		i.Weight = 5.6;
		
		System.out.println(i.toString());
		assertTrue(!i.toString().isEmpty());
	}
	
	@Test
	void PersonToStringTest() {
		Person p = Person.RandomPerson();
		System.out.println(p.toString());
		assertTrue(!p.toString().isEmpty());
	}

}
