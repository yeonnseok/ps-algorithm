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

public class P16236 {

	static class Point{
		int x;
		int y;
		int dist;
		Point(int x, int y, int dist){
			this.x = x;
			this.y = y;
			this.dist = dist;
		}
	}
	static int n;
	static int[][] a;
	static int[][] dist;	
	static Queue<Point> q;
	static int[] dx = {-1, 0, 1, 0}; // 위 왼쪽 순으로 이동;;
	static int[] dy = {0, -1, 0, 1};
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16236.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 1. 입력 및 초기화
		n = Integer.parseInt(br.readLine());
		a = new int[n][n];
		
		int s_x = 0, s_y = 0;
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				a[i][j] = Integer.parseInt(st.nextToken());
				if (a[i][j] == 9) {
					s_x = i;
					s_y = j;
					a[i][j] = 0;
				}
			}
		}
		 
		int ans = 0;
		int size = 2;
		int exp = 0;
		while (true) {
			Point p = bfs(s_x, s_y, size);
			if (p == null) break; // 잡아먹을 물고기가 없으면 null을 리턴
			ans += p.dist;
			exp += 1; // 물고기 한마리 잡아먹기
			
			if (exp == size) {
				size += 1;
				exp = 0;
			}
			s_x = p.x;
			s_y = p.y;
			
		}
		System.out.println(ans);
		
	}
	
	public static Point bfs(int s_x, int s_y, int size) {
		dist = new int[n][n];
		ArrayList<Point> ans = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				dist[i][j] = -1;
			}
		}
		q = new LinkedList<>();
		q.offer(new Point(s_x, s_y, 0));
		dist[s_x][s_y] = 0;
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (dist[nx][ny] == -1) {
					boolean ok = false;
					boolean eat = false;
					
					if (a[nx][ny] == 0) { // 빈공간이면 이동 가능
						ok = true;
					} else if (a[nx][ny] == size) {
						ok = true;
					} else if (a[nx][ny] < size) {
						ok = true;
						eat = true;
					}
					
					if (ok) {
						q.offer(new Point(nx, ny, 0));
						dist[nx][ny] = dist[x][y] + 1;
						if (eat) {
							ans.add(new Point(nx, ny, dist[nx][ny]));
						}
					}
					
				}
			}
		}
		if (ans.isEmpty()) {
			return null;
		}
		
		Point best = ans.get(0); // 가장 거리가 가까운걸 찾는다.
		for (Point p : ans) {
			if (best.dist > p.dist) {
				best = p;
			} else if (best.dist == p.dist && best.x > p.x) {
				best = p;
			} else if (best.dist == p.dist && best.x == p.x && best.y > p.y){
				best = p;
			}
		}
		a[best.x][best.y] = 0; 
		return best; // 가장 가까운 물고기 위치;
	}

}
