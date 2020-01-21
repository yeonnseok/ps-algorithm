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
import java.util.StringTokenizer;

public class P2343 {
	
	static int n, m;
	static int[] a;
	
	// go: 크기가 size인 블루레이로 녹화했을 때 m개 이하의 블루레이가 나오는지? (정답 범위안에 들어가는지)
	// go -> true이면 size를 더 작게 만들어 도 된다는 말이다.
	public static boolean go(int size) {
		int cnt = 1;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			if (sum + a[i] > size) {
				cnt += 1;
				sum = a[i];
			} else {
				sum += a[i];
			}
		}
		return cnt <= m;
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P2343.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		a = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		
		int left = 0;
		int right = 0;
		for (int i =0 ; i < n; i++) {
			if (left < a[i]) {
				left = a[i];
			}
			right += a[i];
		}
		
		int ans = 0;
		while (left <= right) {
			int mid = (left + right) / 2;
			if (go(mid)) { // 가능하면 정답을 더 작게 (최대의 최소값을 구하므로)
				ans = mid;
				right = mid - 1;
			} else { // 불가능하면 정답을 더 크게
				left = mid + 1;
			}
		}
		
		System.out.println(ans);
		
	}	
}
