package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class P12886 {

	static int x;
	static int y;
	static int z;
	static int sum = x + y + z;
	static boolean[][] check = new boolean[1501][1501];
	public static void go(int x, int y) {
		if (check[x][y]) return;
		check[x][y] = true;
		int[] a = {x, y, sum-x-y};
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (a[i] < a[j]) {
					go(a[i] + a[i], a[j] - a[i]);
				}
			}
		}
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P12886.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());
		z = Integer.parseInt(st.nextToken());
		
		sum = x + y + z;
		if (sum % 3 != 0) {
			System.out.println(0);
			return;
		}
		
		go(x, y);
		if (check[sum/3][sum/3]) { // A => sum/3, B => sum/3 인지점을 방문했다면 성공.
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
		
	}

}
