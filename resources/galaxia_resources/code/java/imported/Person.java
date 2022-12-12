package imported;

import java.util.Random;
import java.util.UUID;

import imported.Gender;

public class Person {
	
	private static final int MAX_AGE = 110;
	
	public UUID Id;
	public String Name;
	public int Age;
	public Gender Gender;
	
	public Person() {
		Id = UUID.randomUUID();
	}
	
	public static Person RandomPerson() {
		Random r = new Random();
		Person result = new Person();
		result.Age = r.nextInt(MAX_AGE) + 1;
		
		return result;
	}
	
	@Override
	public String toString() {
		return String.format("Person: %s | Age: $d", Name, Age);
	}
}
