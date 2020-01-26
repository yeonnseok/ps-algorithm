package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class P6549 {
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P6549.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int n = Integer.parseInt(st.nextToken()); 
			if (n == 0) {
				return;
			}
			long[] a = new long[n];
			for (int i = 0; i < n; i ++) {
				a[i] = Integer.parseInt(st.nextToken());
			}
			
			Stack<Integer> s = new Stack<>();
			long ans = 0;
			for (int i = 0; i < n; i++) {
				int left = i;
				while(!s.isEmpty() && a[s.peek()] > a[i]) { // 오른쪽 다음 막대가 더 작으면
					long height = a[s.pop()]; // 스택 마지막 요소
					long width = i;
					if (!s.empty()) {
						width = (i - s.peek() - 1);
					}
					if (ans < (long)width * height) {
						ans = (long)width * height;
					}
				}
				s.push(i);
			}
			
			while(!s.empty()) {
				long height = a[s.pop()];
				long width = n;
				
				if (!s.isEmpty()) {
					width = n - s.peek() - 1;
				}
				
				if (ans < (long)width*height) {
					ans = (long)width*height;
				}
			}
			
			System.out.println(ans);
		}
		
	}
}
