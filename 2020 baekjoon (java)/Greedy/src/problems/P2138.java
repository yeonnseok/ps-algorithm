package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P1082 {
	
	static int n, m;
	static int[][] a, b;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1082.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		// 1. 입력 값
		a = new int[n][m];
		b = new int[n][m];
		for (int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				a[i][j] = row[j] - '0';
			}
		}
		for (int i = 0; i < n; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < m; j++) {
				b[i][j] = row[j] - '0';
			}
		}
		 
		// 2.(N-2)*(M-2) 칸에 대해서  a[i][j] == b[i][j]비교연산 수행
		int ans = 0;
		for (int i = 0; i < n-2; i++) {
			for (int j = 0; j < m-2; j++) {
				if (a[i][j] != b[i][j]) {
					ans += 1;
					flip(i+1, j+1);
				}
			}
		}
		
		// 3. 전체가 같은지 확인
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] != b[i][j]) {
					System.out.println(-1);
					return;
				}
			}
		}
		
		bw.write(ans+"");
		bw.flush();
		
	}	
	
	public static void flip(int x, int y) {
		for (int i=x-1; i<=x+1; i++) {
			for (int j=y-1; j<=y+1; j++) {
				a[i][j] = 1-a[i][j];
			}
		}
	}
}
