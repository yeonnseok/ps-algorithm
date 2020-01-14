package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14225 {

	static int n;
	static int[] nums;
	static boolean[] check = new boolean[20 * 10000 + 1];
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14225.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		nums = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		solve(0, 0);
		for (int i = 1; i < check.length; i ++ ) {
			if (!check[i]) {
				System.out.println(i);
				return;
			}
		}
		
	}
	
	public static void solve(int index, int sum) {
		if (index == n) {
			check[sum] = true;
			return;
		}
		
		solve(index + 1, sum + nums[index]);
		solve(index + 1, sum);
	}

}
