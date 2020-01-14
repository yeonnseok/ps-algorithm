package problems;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class P2580 {
	static final int n = 9;
	static int[][] a;
	static boolean[][] check_col;
	static boolean[][] check_row;
	static boolean[][] check_square;
	
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("src/input/P2580.txt"));
		Scanner sc = new Scanner(System.in);
		
		
		a = new int[n][n];
		check_col = new boolean[n][n+1];
		check_row = new boolean[n][n+1];
		check_square = new boolean[n][n+1];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				a[i][j] = sc.nextInt();
				check_row[i][a[i][j]] = true;
				check_col[j][a[i][j]] = true;
				check_square[square(i, j)][a[i][j]] = true;
			}
		}

		solve(0);
	}
	
	public static void solve(int z) {
		if (z == 81) { // 종료
			printAnswer();
			System.exit(0);
		}
		
		System.out.println("count");
		int x = z / n;
		int y = z % n;
		if (a[x][y] != 0) {
			solve(z + 1);
		} else { // 0일 경우에는
			for (int number = 1; number < 10; number ++ ) {
				if (!check_col[y][number] && !check_row[x][number] && !check_square[square(x, y)][number]) {
					check_col[y][number] = check_row[x][number]  = check_square[square(x, y)][number] = true;
					a[x][y] = number;
					solve(z+1);
					a[x][y] = 0;
					check_col[y][number] = check_row[x][number]  = check_square[square(x, y)][number] = false;
				}
			}                        
		}
		
	}
	
	public static int square(int x, int y) {
		return  (x / 3) * 3 + (y / 3);
	}
	
	public static void printAnswer() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(a[i][j] + " ");
			}
			System.out.println();
		}
	}
}
