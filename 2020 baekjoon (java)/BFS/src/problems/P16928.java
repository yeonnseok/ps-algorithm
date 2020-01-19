package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P16928 {

	static int n, m;
	static int[] next = new int[101];
	static int[] d = new int[101];
	static Queue<Integer> q = new LinkedList<>();
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P16928.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
	
		n = Integer.parseInt(st.nextToken());		
		m = Integer.parseInt(st.nextToken());
		Arrays.fill(d, -1);
		
		for (int x = 1; x <= 100; x++) {
			next[x] = x;
		}
		
		// 사다리 정보 (x < y)
		// 뱀정보 (x > y)
		for (int i = 0; i < n + m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			next[x] = y;
		}
		
		q.offer(1);
		d[1] = 0;
		
		while(!q.isEmpty()) {
			int x = q.poll();
			if (x == 100) {
				break;
			}
			for (int i = 1; i <= 6; i++) {
				int nx = x + i;
				if (nx > 100) continue;
				int y = next[nx];
				if (d[y] == -1){
					d[next[nx]] = d[x] + 1;
					q.offer(next[nx]);
				}
			}
		}
		
		System.out.println(d[100]);
	}

}
