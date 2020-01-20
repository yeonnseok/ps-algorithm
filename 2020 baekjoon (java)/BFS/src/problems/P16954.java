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

public class P16954 {

	static class Point{
		int x;
		int y;
		int t;
		Point(int x, int y, int t){
			this.x = x;
			this.y = y;
			this.t = t;
		}
	}
	static final int N = 8;
	static char[][] a;
	static boolean[][][] dist;
	static Queue<Point> q = new LinkedList<>();
	static int[] dx = {1, -1, 0, 0, 1, 1, -1, -1, 0}; // 제자리 있는 것도 추가해준다.
	static int[] dy = {0, 0, 1, -1, 1, -1, 1, -1, 0};
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16954.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 1. 입력 및 초기화
		a = new char[N][N];
		dist = new boolean[N][N][9];
		for(int i = 0; i < N; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < N; j++) {
				a[i][j] = row[j];
			}
		}

		// 2. 시작 및 종료 칸
		int e_x = 0;
		int e_y = N-1;
		q.offer(new Point(7, 0, 0));  // t는 8초까지만 준비해놓으면 된다.
		dist[7][0][0] = true;
		
		// 3. bfs
		boolean ans = false;	
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			int t = cur.t;
			if (x == e_x && y == e_y) ans = true;
			for (int k = 0; k < 9; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				int nt = Math.min(t+1, 8);
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if (nx - t >= 0 && a[nx-t][ny] == '#') continue;
				if (nx - t -1 >= 0 && a[nx-t-1][ny] == '#') continue;
				if (!dist[nx][ny][nt]) {
					dist[nx][ny][nt] = true;
					q.offer(new Point(nx, ny, nt));
				}
			}
		}
		
		System.out.println(ans ? 1 : 0);
	}

}
