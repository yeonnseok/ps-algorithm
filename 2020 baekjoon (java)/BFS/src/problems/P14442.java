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

public class P14442 {

	static class Point{
		int x;
		int y;
		int k;
		Point(int x, int y, int k){
			this.x = x;
			this.y = y;
			this.k = k;
		}
	}
	static int n,m,l;
	static int[][] a;
	static int[][][] d;
	static Queue<Point> q = new LinkedList<>();
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14442.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		
		a = new int[n+1][m+1];
		d = new int[n+1][m+1][l+1];
		for (int i = 1; i <= n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 1; j <= m; j++) {
				a[i][j] = row[j-1] - '0';
			}
		}
		
		d[1][1][0] = 1; // 시작하는 칸도 포함해서 센다.
		q.offer(new Point(1, 1, 0));
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			int k = cur.k;
			for (int p = 0; p < 4; p++) {
				int nx = x + dx[p];
				int ny = y + dy[p];
				if (nx <= 0 || nx > n || ny <= 0 || ny > m) continue;
				
				//  벽을 부수고 지나갈 수 있는 경우
				if (k+1 <= l && d[nx][ny][k+1] == 0 && a[nx][ny] == 1) {
					q.offer(new Point(nx, ny, k+1));
					d[nx][ny][k+1] = d[x][y][k] + 1;
				} 
				//  벽이 아닌 경우
				if (d[nx][ny][k] == 0 && a[nx][ny] == 0) {
					q.offer(new Point(nx, ny, k));
					d[nx][ny][k] = d[x][y][k] + 1;
				}
				
			}
		}
		
		// -1이 있으면 제외하고 가자 작은 걸 출력.
		// 전부다 -1일때만 -1을 출력
		int ans = -1;
		for (int i = 0; i <= l; i ++) {
			if (d[n][m][i] == 0) continue;
			if (ans == -1 || ans > d[n][m][i]) {
				ans = d[n][m][i];
			}
		}
		System.out.println(ans);
	}

}
