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

public class P1956 {

	static int n, m;
	static int[][] dist;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1956.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		dist = new int[n][n];
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
		
			if (dist[x-1][y-1] == 0) {
				dist[x-1][y-1] = z;
			} else if (dist[x-1][y-1] > z){
				dist[x-1][y-1] = z; // 중복되는 도로가 있더라도 더 작은 도로 길이만 저장.
			}
		}
		
		
		for (int k = 0; k < n; k++) { // 중간 지점.
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (dist[i][k] != 0 && dist[k][j] != 0) { // k를 경유하는 경로가 있는지 확인
						// i -> j로 바로 가는 경로를 아직 안지났다면, k를 경유하는 경로를 업데이트
						// 0을 경유하는 모든 경로, 1을 경유하는 모든 경로, ....
						if (dist[i][j] == 0 || dist[i][j] > dist[i][k] + dist[k][j]) {
							dist[i][j] = dist[i][k] + dist[k][j];
						}
					}
				}
			}
		}
		
		int ans = -1;
		for (int i = 0; i < n; i++) {
			if (dist[i][i] != 0) {
				if (ans == -1 || ans > dist[i][i]) { // i 에서 i로 가는 경로가 있는지 확인
					ans = dist[i][i]; // 있다면 최단경로 를 출력
				}
			}
		}
		System.out.println(ans);
	}
}
