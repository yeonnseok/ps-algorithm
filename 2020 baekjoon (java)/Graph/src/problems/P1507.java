package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1507 {

	static int n;
	static int[][] dist;
	static boolean[][] unused;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1507.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		unused = new boolean[n+1][n+1];
		dist = new int[n+1][n+1];
		StringTokenizer st;
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				dist[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		for (int k = 1; k <= n; k++) { // 중간 지점.
			for (int i = 0; i <= n; i++) {
				if (i == k) continue;
				for (int j = 0; j <= n; j++) {
					if (i == j) continue;
					if (k == j) continue;
					if (dist[i][j] > dist[i][k] + dist[k][j]) {
						System.out.println(-1);
						System.exit(0);
					}
					if (dist[i][j] == dist[i][k] + dist[k][j]) {
						unused[i][j] = true; // i=>j가는 길은 필요가 없다.
					}
				}
			}
		}
		
		
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++){
				if (!unused[i][j]) {
					ans += dist[i][j];
				}
			}
		}
		
		ans /= 2;
        System.out.println(ans);
		
	}

}
