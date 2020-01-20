package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class P16946 {
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
	static boolean[][] check;
	static int[][] group;
	static Queue<Point> q;
	static ArrayList<Integer> group_size = new ArrayList<>();
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16946.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		a = new int[n][m];
		check = new boolean[n][m];
		group = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j< m; j++) {
				a[i][j] = row[j] - '0';
				group[i][j] = -1;
			}
		}
		
		// 1. group을 생성한다.
		for (int i = 0; i < n; i++) {
			for (int j = 0; j< m; j++) {
				if (a[i][j] == 0 && !check[i][j]) {
					bfs(i, j);
				}
			}
		}
		
		// 2. 이동할 수 있는 칸을 순회하면서, 각각의 벽을 빈칸으로 바꾸고 이동할 수 있는 group의 갯수를 set에 저장한다.
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] == 0) { // 원래 빈칸인 곳은 0을 출력한다.
					System.out.print(0);
				} else {
					Set<Integer> set = new HashSet<>();
					for (int k = 0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
						if (a[nx][ny] == 0) {
							set.add(group[nx][ny]);
						}
					}
					
					int ans = 1;
					for (Integer g : set) {
						ans += group_size.get(g);
					}
					System.out.print(ans%10);
				}
			}
			System.out.println();
		}
		
	}
	
	
	public static void bfs(int sx, int sy) {
		int g = group_size.size();
		q = new LinkedList<>();
		q.offer(new Point(sx, sy));
		check[sx][sy] = true;
		group[sx][sy] = g;
		int cnt = 1;
		
		while(!q.isEmpty()) {
			Point cur = q.poll();
			int x = cur.x;
			int y = cur.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (!check[nx][ny] && a[nx][ny] == 0) {
					group[nx][ny] = g;
					q.offer(new Point(nx, ny));
					check[nx][ny] = true;
					cnt += 1; // 그룹이 몇 개의 칸으로 이루어져있는지 갯수를 센다.
				}
			}
		}
		group_size.add(cnt);
	}


}
