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
import java.util.StringTokenizer;

public class P1300 {
	
	static long n, k;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1300.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		k = Integer.parseInt(br.readLine());
		
		long left = 1; // 처음 수
		long right = n*n; // 마지막 수
		long ans = 0;
		while (left <= right) {
			long mid = (left + right) / 2;
			long cnt = 0;
			for (long i = 1; i <= n; i++) {
				cnt += Math.min(n, mid/i);
			}
			if (cnt >= k) { // cnt 번째 가 더 큰 수이므로 범위를 줄인다. right = mid - 1; 
				ans = mid;
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		System.out.println(ans);
		
	}	
}
