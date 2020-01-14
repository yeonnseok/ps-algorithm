package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1182 {

	static int n, s;
	static int[] nums;
	static int ans;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1182.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		nums = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		solve(0, 0);
		if (s == 0) {
			ans -= 1; 
		}
		System.out.println(ans);
		
	}

	public static void solve(int index, int sum) {
		if (index == n && sum == s) {
			ans ++;
			return;
		}
		
		if (index == n && sum != s) {
			return;
		}
		
		solve(index + 1, sum + nums[index]);
		solve(index + 1, sum);
	}
}
