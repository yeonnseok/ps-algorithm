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

public class P12738 {
	
	static int lower_bound(int[] a, int n, int key) {
		int left = 0;
		int right = n;
		while (left < right) {
			int mid = (left + right) / 2;
			if (a[mid] >= key) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		return right;
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P12738.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int len = 0;
		int[] a = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(st.nextToken());
			int p = lower_bound(a, len, num);
			a[p] = num;
			if (len == p) {
				len += 1;
			}
		}
	
		bw.write(""+len);
		bw.flush();
		 
		
		
	}	
}
