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

public class P2138 {
	
	static int n;
	static int[] a, b;
	static class Pair{
		boolean first;
		int second;
		Pair(boolean first, int second){
			this.first = first;
			this.second = second;
		}
	}
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P2138.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		
		// 1. ÀÔ·Â °ª
		a = new int[n];
		b = new int[n];
		char[] row = br.readLine().toCharArray();
		for (int i = 0; i < n; i++) {
			a[i] = row[i] - '0';	
		}
		row = br.readLine().toCharArray();
		for (int i = 0; i < n; i++) {
			b[i] = row[i] - '0';	
		} 
		
		int[] a_c = new int[a.length];
		System.arraycopy(a, 0, a_c, 0, a.length);
		Pair p1 = go(a_c);
		change(a, 0);
		Pair p2 = go(a);
		if(p2.first) {
			p2.second+=1;
		}
		if (p1.first && p2.first) {
			System.out.printf("%d\n",Math.min(p1.second, p2.second));
        } else if (p1.first) {
            System.out.printf("%d\n",p1.second);
        } else if (p2.first) {
            System.out.printf("%d\n",p2.second);
        } else {
            System.out.printf("-1\n");
        }
		
	}	
	static Pair go(int[] a) {
		int n = a.length;
		int ans = 0;
		for (int i = 0; i < n-1; i++) {
			if (a[i] != b[i]) {
				change(a, i+1);
				ans += 1;
			}
		}
		boolean ok = true;
		for (int i = 0; i < n; i++) {
			if (a[i] != b[i]) {
				ok = false;
			}
		}
		
		if(ok) {
			return new Pair(true, ans);
		}else {
			return new Pair(false, ans);
		}
	}
	static void change(int[] a, int x) {
		for (int i=x-1; i<=x+1; i++) {
			if (0<=i && i < n) {
				a[i] = 1-a[i];
			}
		}
	}
}
