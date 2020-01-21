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

public class P13397 {
	
	static int n, m;
	static int[] a;
	
	public static int go(int mid) {
		int n = a.length;
		int t1 = a[0];
		int t2 = a[0];
		int ans = 1;
		for (int i = 1; i < n; i++) {
			if (t1 > a[i]) {
				t1 = a[i];
			}
			if (t2 < a[i]) {
				t2 = a[i];
			}
			if (t2 - t1 > mid) { // 새로운 구간을 만듬.
				ans += 1;
				t1 = a[i];
				t2 = a[i];
			}
		}
		return ans;
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P13397.txt"));
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
			if (right < a[i]) {
				right = a[i];
			}
		}
		
		int ans = 0;
		while (left <= right) {
			int mid = (left + right) / 2;
			if (go(mid) <= m) { // 가능하면 정답을 더 작게 (최대의 최소값을 구하므로)
				ans = mid;
				right = mid - 1;
			} else { // 불가능하면 정답을 더 크게
				left = mid + 1;
			}
		}
		
		System.out.println(ans);
		
	}	
}
