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

public class P3055 {

	static class Point{
		int x;
		int y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	static int n, m;
	static char[][] a;
	static int[][] dist;
	static int[][] water;
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {1, -1, 0, 0}; // 제자리 있는 것도 추가해준다.
	static int[] dy = {0, 0, 1, -1};
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P3055.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		// 1. 입력 및 초기화
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		a = new char[n][m];
		dist = new int[n][m];
		water = new int[n][m];
		
		int s_x = 0, s_y = 0;
		int e_x = 0, e_y = 0;
		for(int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				a[i][j] = row[j];
				water[i][j] = -1;
				dist[i][j] = -1;
				
				if (a[i][j] == 'S') {
					s_x = i;
					s_y = j;
					a[i][j] = '.';
				}
				
				if (a[i][j] == 'D') {
					e_x = i;
					e_y = j;
				}
				

				if (a[i][j] == '*') {
					q.offer(new Point(i, j));
					water[i][j] = 0;
				}
			}
		}

		// 2. water 채우기
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (water[nx][ny] != -1) continue;
				if (a[nx][ny] == 'X') continue;
				if (a[nx][ny] == 'D') continue;
				q.offer(new Point(nx, ny));
				water[nx][ny] = water[x][y] + 1;
			}
		}

		// 3. bfs
		boolean ans = false;
		dist[s_x][s_y] = 0;
		q.offer(new Point(s_x, s_y));
		
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			if (x == e_x && y == e_y) ans = true;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (a[nx][ny] != 'X' && dist[nx][ny] == -1) {
					if (water[nx][ny] == -1 || dist[x][y] + 1 < water[nx][ny]) {
						dist[nx][ny] = dist[x][y] + 1;
						q.offer(new Point(nx, ny));
					}
				}
				
			}
		}
		System.out.println(ans == true ? dist[e_x][e_y] : "KAKTUS");
	}

}
