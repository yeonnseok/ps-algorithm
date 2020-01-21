package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1981 {
	
	static int n;
	static int[][] a = new int[100][100];
	static boolean[][] c = new boolean[100][100];
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static class Point{
		int x;
		int y; 
		Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	public static boolean bfs(int mn, int mx) {
		if (mn > a[0][0] || mx < a[0][0]) {
			return false;
		}
		for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                c[i][j] = false;
            }
        }
		
		Queue<Point> q = new LinkedList<>();
		q.offer(new Point(0, 0));
		c[0][0] = true;
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (c[nx][ny] == false) {
					if (mn <= a[nx][ny] && a[nx][ny] <= mx) {
						q.offer(new Point(nx, ny));
						c[nx][ny] = true;
					}
				}
			}
		}
		return c[n-1][n-1];
	}
	
	public static boolean go(int diff) {
		for (int mn = 0; mn + diff<= 200; mn++) {
			if (bfs(mn, mn+diff)) {
				return true;
			}
		}
		return false;
	}
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1981.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		
		
		a = new int[n][n];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				a[i][j] = Integer.parseInt(st.nextToken());
			}
			
		}
		
		int left = 0;
		int right = 200;
		int ans = 0;
		while (left <= right) {
			int mid = (left + right) / 2;
			if (go(mid)) { // 가능하면 정답을 더 작게 (최대의 최소값을 구하므로)
				ans = mid;
				right = mid - 1;
			} else { // 불가능하면 정답을 더 크게
				left = mid + 1;
			}
		}
		
		System.out.println(ans);
		
	}	
}
