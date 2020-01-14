package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9663 {
	static int n, m;
	static boolean[][] a;
	static boolean[] check_col;
	static boolean[] check_dig;
	static boolean[] check_dig2;
	static int ans = 0;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P9663.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		
		a = new boolean[15][15];
		check_col = new boolean[15];
		check_dig = new boolean[40];
		check_dig2 = new boolean[40];
		
		System.out.println(calc(0));
	}
	
	public static int calc(int row) {
		if (row == n) {
			return 1;
		}
		
		int cnt = 0;
		for (int col = 0; col < n; col++) {
			
			if (check(row, col)) {
				check_col[col] = true;
				check_dig[row + col] = true;
				check_dig2[row - col + n] = true;
				a[row][col] = true; //퀸을 놓을 경우;
				cnt += calc(row + 1);
				check_col[col] = false;
				check_dig[row+col] = false;
				check_dig2[row-col+n] = false;
				a[row][col] = false;
			}
		}
		return cnt;
	}
	
	public static boolean check(int row, int col) {
		if (check_col[col]) {
			return false;
		}
		
		if (check_dig[row + col]) {
			return false;
		}
		
		if (check_dig2[row - col + n]) {
			return false;
		}
		return true;
	}

}
