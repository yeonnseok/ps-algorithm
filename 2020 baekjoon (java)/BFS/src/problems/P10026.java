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
import java.util.List;
import java.util.Queue;

import problems.P16236.Point;

public class P10026 {
	
	static class Point{
		int x;
		int y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	static int n;
	static int[][] a;
	static boolean[][] check;
	static boolean[][] check_gr;
	static int[][] group;
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P10026.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		a = new int[n][n];
		check = new boolean[n][n];
		check_gr = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < n; j++) {
				a[i][j] = row[j];
			}
		}
		
		int g = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (check[i][j]) continue;
				g = bfs(i, j, g);
			}
		}
		
		int g_r = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (check_gr[i][j]) continue;
				g_r = bfs_gr(i, j, g_r);
			}
		}
		
		g--;
		g_r--;
		bw.write(g + " " + g_r);
		bw.flush();
		bw.close();
	}
	
	public static int bfs(int i, int j, int g) {
		group = new int[n][n];
		
		q.offer(new Point(i, j));
		check[i][j] = true;
		group[i][j] = g;
		while (!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (check[nx][ny] == false && a[nx][ny] == a[x][y]) {
					group[nx][ny] = g;
					q.offer(new Point(nx, ny));
					check[nx][ny] = true;
				}
			}
		}
		return g + 1;
	}
	
	public static int bfs_gr(int i, int j, int g) {
		group = new int[n][n];
		
		q.offer(new Point(i, j));
		check_gr[i][j] = true;
		group[i][j] = g;
		while (!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (check_gr[nx][ny] == false && (a[nx][ny] == a[x][y] || (a[nx][ny] == 'G' && a[x][y] == 'R') || (a[nx][ny] == 'R' && a[x][y] == 'G'))) {
					group[nx][ny] = g;
					q.offer(new Point(nx, ny));
					check_gr[nx][ny] = true;
				}
			}
		}
		return g + 1;
	}
	
}
