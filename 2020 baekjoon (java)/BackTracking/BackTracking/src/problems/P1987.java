package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P1987 {
		
	static int n, m;
	static char[][] a;
	static boolean[] check;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int ans; 
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1987.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		a = new char[n][m];
		check = new boolean[26];
		for (int i = 0; i < n; i++) {
			String row = br.readLine();
			for (int j = 0; j < m; j++) {
				a[i][j] = row.charAt(j);
			}
		}
		check[a[0][0] - 'A'] = true;
		solve(0, 0, 1);
		System.out.println(ans);
		
	}
	
	public static void solve(int x, int y, int cnt) {
		
		if (ans < cnt) {
			ans = cnt;
		}
		
		// 1. Ã¼Å©ÀÎ
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m ) continue;
			if (!check[a[nx][ny] - 'A']) {
				check[a[nx][ny] - 'A'] = true;
				solve(nx, ny, cnt + 1);
				check[a[nx][ny] - 'A'] = false;
			}
		}		
		
	}

}
