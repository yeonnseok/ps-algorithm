package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

import javafx.util.Pair;

public class P14888 {

	static class Pair{
		int first;
		int second;
		Pair(int first, int second) {
			this.first = first;
			this.second = second;
		}
	}
	static int n;
	static int[] nums;
	static int plus, minus, mul, div;
	static int ans;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14888.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		nums = new int[n];
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		plus = Integer.parseInt(st.nextToken());
		minus = Integer.parseInt(st.nextToken());
		mul = Integer.parseInt(st.nextToken());
		div = Integer.parseInt(st.nextToken());
		
		Pair answer = solve(1, nums[0], plus, minus, mul, div);
		System.out.println(answer.first);
		System.out.println(answer.second);
			
	}
	
	public static Pair solve(int index, int cur, int plus, int minus, int mul, int div) {
		if (index == n) {
			return new Pair(cur, cur);
		}
		
		List<Pair> res = new ArrayList<>();
		if (plus > 0) {
			res.add(solve(index + 1, cur + nums[index], plus - 1, minus, mul, div));
		}
		if (minus > 0 ) {
			res.add(solve(index + 1, cur - nums[index], plus, minus - 1, mul, div));
		}
		if (mul > 0) {
			res.add(solve(index + 1, cur * nums[index], plus, minus, mul - 1, div));
		}
		if (div > 0) {
			res.add(solve(index + 1, cur/nums[index], plus, minus, mul, div-1));
		}
		
		Pair ans = res.get(0);
		for (Pair p : res) {
			if (ans.first < p.first) {
				ans.first = p.first;
			}
			if (ans.second > p.second) {
				ans.second = p.second;
			}
		}
		return ans;
	}

}
