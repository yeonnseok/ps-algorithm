package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P16198 {

	static int n;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16198.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		List<Integer> nums = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			nums.add(Integer.parseInt(st.nextToken()));
		}
		System.out.println(solve(nums));		
	}
	
	public static int solve(List<Integer> nums) {
		// 종료 조건
		int ll = nums.size();
		if (ll == 2) {
			return 0;
		}
		int ans = 0;
		for (int i = 1; i < ll - 1; i++) {
			int energy = nums.get(i-1) * nums.get(i+1);
			List<Integer> b = new ArrayList<>(nums);
			b.remove(i); //인덱스로 지우기
			energy += solve(b);
			if (ans < energy) {
				ans = energy;
			}
		}
		return ans;
	}
}
