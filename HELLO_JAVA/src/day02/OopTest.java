package day02;

public class OopTest {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.mylife);;
		ani.getAge();
		System.out.println(ani.mylife);
		
		Human hum = new Human();
		System.out.println(hum.mylife);
		System.out.println(hum.skill_lang);
		hum.getAge();
		hum.exp(50);
		System.out.println(hum.mylife);
		System.out.println(hum.skill_lang);
		
		
	}
}