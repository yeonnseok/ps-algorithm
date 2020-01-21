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

public class P1654 {

	static int n, k;
	static int[] lines;
	static int max;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1654.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		lines = new int[n];
		for (int i = 0; i < n; i++) {
			lines[i] = Integer.parseInt(br.readLine());
			if (max < lines[i]) {
				max = lines[i];
			}
		}
		
		// 이분탐색
		long left = 1;
		long right = max;
		long ans = 0;
		while (left <= right) {
			long mid = (left + right) / 2;
			long cnt = calc(mid);
			if (k <= cnt) { // n을 크게 만드는 것
				ans = mid;
				left = mid + 1;
			} else { // n을 작게 만드는 것
				right = mid - 1;
			}
		}
		
		System.out.println(ans);
		
	}
	
	// n까지 수를 이어 붙였을 때 길이
	public static long calc(long mid) {
		long ans = 0;
		for (int i = 0; i < n; i++) {
			ans += lines[i] / mid;
		}
		return ans;
	}
}
