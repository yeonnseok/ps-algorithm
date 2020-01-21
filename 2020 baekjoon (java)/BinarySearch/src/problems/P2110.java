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

public class P2110 {

	static int n, c;
	static int[] a;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P2110.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(a);
		int ans = 1; 
		int left = 1;
		int right = a[n-1] - a[0];  // 가장 왼쪽과 오른쪽의 거리 차이 max

		while (left <= right) {
			int mid = (left + right) / 2;
			if (possible(a, c, mid)) { 
				ans = Math.max(ans,  mid);
				left = mid + 1; //  거리를 더  늘리고, 거리 최대값을 갱신한다.
			} else {
				right = mid - 1;
			}
		}
		
		System.out.println(ans);
		
	}	

	public static boolean possible(int[] a, int c, int mid) {
		int cnt = 1;
		int last = a[0];
		for (int house : a) {
			if (house - last >= mid) { // 여기가 핵심.
				cnt += 1;
				last = house;
			}
		}
		return cnt >= c; // 놓는 공유기 의 갯수가 c 보다 많으면 거리를 더 늘려도 된다.
	}
}
