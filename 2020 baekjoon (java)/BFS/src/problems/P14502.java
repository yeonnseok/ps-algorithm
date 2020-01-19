package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P14502 {
	
	static class Point{
		int x;
		int y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	static int n, m;
	static int ans;
	static int[][] a;
	static int[][] b;
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14502.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		a = new int[n][m];
		b = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				a[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 벽세우기
		for (int x1 = 0; x1 < n; x1 ++) {
			for (int y1 = 0; y1 < m; y1 ++) {
				if (a[x1][y1] != 0) continue;
				for (int x2 = 0; x2 < n; x2 ++) {
					for (int y2 = 0; y2 < m; y2++) {
						if (a[x2][y2] != 0) continue;
						for (int x3 = 0; x3 < n; x3 ++) {
							for (int y3 = 0; y3 < m; y3++) {
								if (a[x3][y3] != 0) continue;
								if (x1 == x2 && y1 == y2) continue;
								if (x2 == x3 && y2 == y3) continue;
								if (x3 == x1 && y3 == y1) continue;
								a[x1][y1] = a[x2][y2] = a[x3][y3] = 1;
								ans = Math.max(ans, calcSafeZone());
								a[x1][y1] = a[x2][y2] = a[x3][y3] = 0;
							}
						}
					}
				}
			}
		}
		
		System.out.println(ans);
		
	}
	
	public static int calcSafeZone() {
		// 0 빈칸, 1 벽, 2 바이러스위치
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				b[i][j] = a[i][j];
				if (a[i][j] == 2) { // 바이러스 시작점
					q.offer(new Point(i, j));
				}
			}
		}
		
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (b[nx][ny] == 0) { // 바이러스가 안퍼졌다면,
					q.add(new Point(nx, ny));
					b[nx][ny] = 2;
				}
			}
			
		}
		
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (b[i][j] == 0) {
					cnt ++;
				}
			}
		}
		return cnt;
	}

}
