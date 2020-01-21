package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;


public class P11652 {

	static int n;
	static long[] list;
	static long max;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P11652.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		
		list = new long[n];
		for(int i = 0; i < n; i++) {
			long num = Long.parseLong(br.readLine());
			list[i] = num;
		}
		
		Arrays.sort(list);
		long ans = list[0];
		int ans_cnt = 1;
		int cnt = 1;
		for (int i = 1; i < n; i++) {
			if (list[i] == list[i-1]) {
				cnt ++;
			} else {
				cnt = 1;
			}
			
			if (ans_cnt < cnt) {
				ans_cnt = cnt;
				ans = list[i];
			}
		}
		bw.write(ans+"");
		bw.flush();
		bw.close();
	}

}
