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

public class P1931 {
	
	static class Meeting implements Comparable<Meeting>{
		int start; 
		int end;
		Meeting (int start, int end){
			this.start = start;
			this.end = end;
		}
		
		@Override
		public int compareTo(Meeting mm) {
			if (this.end > mm.end) {
				return 1;
			} else if (this.end == mm.end){
				if (this.start > mm.start) {
					return 1;
				}
			} else {
				return -1;
			}
			return -1;
		}
		
	}
	
	static int n;
	static Meeting[] a;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1931.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());

		a = new Meeting[n];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			a[i] = new Meeting(start, end);
		}
		
		Arrays.sort(a);
		int now = -1;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (now <= a[i].start) {
				now = a[i].end;
				ans += 1;
			}
		}
		System.out.println(ans);
		
	}	
}
