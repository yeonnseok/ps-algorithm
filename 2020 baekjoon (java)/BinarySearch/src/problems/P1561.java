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

public class P1561 {
	
	static int n, m;
	static int[] a;
	static boolean[][] c = new boolean[100][100];

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1561.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		a = new int[m];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			a[i] = Integer.parseInt(st.nextToken());		
		}
		
		if (n <= m) {
			System.out.println(n);
			return;
		}
		
		long left = 0;
		long right = 200;
		while (left <= right) {
			long mid = (left + right) / 2;
			long begin, end;
			begin = end = 0;
			end = m;
			for (int i=0; i<m; i++) {
				end += mid/a[i];
			}
			begin = end;
			for (int i =0 ; i < m; i++) {
				if (mid % a[i] == 0) {
					begin -= 1;
				}
			}
			begin += 1;
			if (n < begin) {
				right = mid-1;
			} else if(n > end) {
				left = mid + 1;
			} else {
				for (int i = 0; i < n; i++) {
					if (mid % a[i] == 0) {
						if (n == begin) {
							System.out.println(i + 1);
							return;
						}
						begin += 1;
					}
				}
			}
		}
		
	}	
}