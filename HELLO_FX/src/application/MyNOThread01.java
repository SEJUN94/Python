package application;

public class MyNOThread01 {
	
	public static void showNum() {
		for(int i=0;i<100000;i++) {
			System.out.print(i);
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	public static void showAscii() {
		int iga = -1;
		int ihih = -1;
		for(int i=0;i<100000;i++) {
			if((char)i == '가') {
				iga = i;
			}
			if((char)i == '힣') {
				ihih = i;
			}
			System.out.print((char)i);
			if(i%100==0) {
				System.out.println();
			}
		}
		int dap = ihih - iga +1;
		System.out.println("dap:"+dap);
	}
		
	
	public static void main(String[] args) {
		int dap1 = '힣' - '가' + 1;
		System.out.println("dap1:"+dap1);
		showNum();
		showAscii();
	}
	
}
