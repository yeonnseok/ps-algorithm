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

public class P16948 {

	static class Point{
		int x;
		int y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	static int n, m;
	static int[][] d;
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {-2, -2, 0, 0, 2, 2};
	static int[] dy = {-1, 1, -2, 2, -1, 1};
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16948.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());	
		d = new int[n][n];

		StringTokenizer st = new StringTokenizer(br.readLine());
		int x1 = Integer.parseInt(st.nextToken());
		int y1 = Integer.parseInt(st.nextToken());
		int x2 = Integer.parseInt(st.nextToken());
		int y2 = Integer.parseInt(st.nextToken());

		for (int i = 0; i < n; i++) {
			Arrays.fill(d[i], -1);
		}
		d[x1][y1] = 0;
		q.offer(new Point(x1, y1));
		
		while(!q.isEmpty()) {
			Point cur = q.remove();
			int x = cur.x;
			int y = cur.y;
			if (x == x2 && y == y2) {
				break;
			}
			
			for (int k = 0; k < 6; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (d[nx][ny] == -1) {
					d[nx][ny] = d[x][y] + 1;
					q.offer(new Point(nx, ny));
				}
			}
		}
		System.out.println(d[x2][y2]);
	}

}
