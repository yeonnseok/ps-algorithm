package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P6087 {

	static class Point{
		int x;
		int y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	static int n, m;
	static int[][] a;
	static int[][] dist;	
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {-1, 0, 1, 0}; // 위 왼쪽 순으로 이동;;
	static int[] dy = {0, -1, 0, 1};
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P6087.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 1. 입력 및 초기화
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		a = new int[n][m];
		dist = new int[n][m];
	
		
		int sx = -1, sy = -1;
		int ex = -1, ey = -1;
		for(int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				a[i][j] = row[j];
				dist[i][j] = -1;
				if (a[i][j] == 'C') {
					if (sx == -1) {
						sx = i;
						sy = j;
					} else{
						ex = i;
						ey = j;
					}
				}
			}
		}
		
		q.offer(new Point(sx, sy));
		dist[sx][sy] = 0;
		
		while (!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				while (nx >= 0 && nx < n && ny >= 0 && ny < m) {
					if (a[nx][ny] == '*') break;
					if (dist[nx][ny] == -1) {
						q.offer(new Point(nx, ny));
						dist[nx][ny] = dist[x][y] + 1;
					}
					nx += dx[k];
					ny += dy[k];
				}
			}
		}
		System.out.println(dist[ex][ey]-1);
	}

}
