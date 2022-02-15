package day15;

public class RefTest {
	public static void lentArr(int[] a) {
		a[0] = 3;
	}
	public static void lentA(int a) {
		a = 4;
	}
	public static void lentB(String b) {
		b = "12";
	}
	public static void main(String[] args) {
		int[] arr = {1};
		int a = 2;
		String b = "11"; 
		//String b = new String("11"); 
		
		System.out.println("arr[0] : "+arr[0]);
		System.out.println("a : "+a);
		
		lentArr(arr);
		lentA(a);
		lentB(b);
		
		System.out.println("arr[0] : "+arr[0]);
		System.out.println("a : "+a);
		System.out.println("b : "+b);
		
	}
}
