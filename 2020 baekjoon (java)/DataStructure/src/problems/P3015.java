package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class P3015 {
	
	static class Pair{
		int first;
		int second;
		Pair(int first, int second){
			this.first = first;
			this.second = second;
		}
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P3015.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(br.readLine()); 
		}
		
		long ans = 0;
		Stack<Pair> s = new Stack<>();
		for (int i = 0; i < n; i++) {
			Pair p = new Pair(a[i], 1);
			while (!s.isEmpty()) {
				if(s.peek().first <= a[i]) {
					ans += (long)s.peek().second;
					if (s.peek().first == a[i]) {
						p.second += s.peek().second;
					}
					s.pop();
				} else {
					break;
				}
			}
			if (!s.isEmpty()) ans += 1L;
			s.push(p);
		}
		System.out.println(ans);
	}
}
