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

public class P1285 {
	
	static int n;
	static String[] a;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1285.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		
		// 1. ÀÔ·Â °ª
		a = new String[n];
		for (int i = 0; i < n; i++) {
			a[i] = br.readLine();
		}
		int ans = n*n;
        for (int state=0; state<(1<<n); state++) {
            int sum = 0;
            for (int j=0; j<n; j++) {
                int cnt = 0;
                for (int i=0; i<n; i++) {
                    char cur = a[i].charAt(j);
                    if ((state & (1 << i)) != 0) {
                        cur = flip(cur);
                    }
                    if (cur == 'T') {
                        cnt += 1;
                    }
                }
                sum += Math.min(cnt, n-cnt);
            }
            if (ans > sum) ans = sum;
        }
        System.out.println(ans);
		
	}	
	
	static char flip(char x) {
		if (x == 'H') return 'T';
		else return 'H';
	}
}
