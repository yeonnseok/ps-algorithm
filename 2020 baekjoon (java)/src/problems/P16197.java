package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P16197 {

	static int n, m;
	static char[][] a;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16197.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		int x1 = -1, x2 = -1, y1 = -1, y2 = -1;
		a = new char[n][m];
		for (int i = 0; i < n; i ++) {
			String row = br.readLine();
			for (int j = 0; j < m; j++) {
				a[i][j] = row.charAt(j);
				if (a[i][j] == 'o') {
					if (x1 == -1) {
						x1 = i;
						y1 = j;
					} else {
						x2 = i;
						y2 = j;
					}
					a[i][j] = '.';
				}
			}
		}
		
		System.out.println(solve(0, x1, y1, x2, y2));
		

	}
	
	public static int solve(int step, int x1, int y1, int x2, int y2) {
		boolean firstOut = false;
		boolean secondOut = false;
		if(x1 < 0 || x1 >= n || y1 < 0 || y1 >= m) firstOut = true;
		if(x2 < 0 || x2 >= n || y2 < 0 || y2 >= m) secondOut = true;
			
		// 불가능한 경우 => step > 10;
		if (step > 10 || (firstOut && secondOut)) {
			return -1;
		}
		
		// 종료
		if (firstOut || secondOut) return step;		
		else if (firstOut || secondOut) {
			return step;
		}
		int ans = -1;
		for (int k = 0; k < 4; k++) {
			int nx1 = x1 + dx[k];
			int ny1 = y1 + dy[k];
			int nx2 = x2 + dx[k];
			int ny2 = y2 + dy[k];
			
			if (0 <= nx1 && nx1 < n && 0 <= ny1 && ny1 < m && a[nx1][ny1] == '#') {
				nx1 = x1;
				ny1 = y1;
			}
			
			if (0 <= nx2 && nx2 < n && 0 <= ny2 && ny2 < m && a[nx2][ny2] == '#') {
				nx2 = x2;
				ny2 = y2;
			}
			
			int temp = solve(step + 1, nx1, ny1, nx2, ny2);
			if(temp == -1) continue;
			if (ans == -1 || ans > temp) {
				ans = temp;
			}
			
		}
		return ans;
	}

}
