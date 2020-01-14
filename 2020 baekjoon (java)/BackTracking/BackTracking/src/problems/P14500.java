package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14500 {

	static int n, m;
	static int[][] map;
	static boolean[][] check;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int ans = 0;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14500.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		check = new boolean[n][m];
		map = new int[n][m];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++){
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < m; j ++) {
				solve(i, j, 0, 0);
				if (j + 2 < m) {
					int temp = map[i][j] + map[i][j+1] + map[i][j+2];
					if (i + 1 < n) {
						int temp2 = temp + map[i+1][j+1];
						if (ans < temp2) ans = temp2;
					}
					if (i - 1 >= 0) {
						int temp2 = temp + map[i-1][j+1];
						if (ans < temp2) ans = temp2;
					}
				}
				if(i + 2 < n) {
					int temp = map[i][j] + map[i+1][j] + map[i+2][j];
					if (j + 1 < m) {
						int temp2 = temp + map[i+1][j+1];
						if (ans < temp2) ans = temp2;
					}
					if (j - 1 >= 0) {
						int temp2 = temp + map[i+1][j-1];
						if (ans < temp2) ans = temp2;
					}
				}
				
			}
		}
		System.out.println(ans);
		
	}
	
	public static void solve(int x, int y, int sum, int cnt) {
		if (cnt == 4) {
			if (ans < sum) ans = sum;
			return;
		}
		if (x < 0 || x >= n || y < 0 || y >= m) return;
		if (check[x][y]) return;
		check[x][y] = true;
		for (int k = 0; k < 4; k++) {
			solve(x + dx[k],  y + dy[k], sum + map[x][y], cnt + 1);
		}
		check[x][y] = false;
	}

}
