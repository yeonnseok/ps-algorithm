package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class P2056 {
	
	
	static int n;
	static int[] indegree;
	static int[] work;
	static int[] d;
	static Queue<Integer> q = new LinkedList<>();
	static int total;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P2056.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		
		work = new int[n + 1];
		d = new int[n + 1];
		indegree = new int[n + 1];
		List<Integer> graph[] = new ArrayList[n + 1];
		
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		
		
		for (int i = 1; i < n + 1; i ++) {
			st = new StringTokenizer(br.readLine());
			int cost = Integer.parseInt(st.nextToken());
			int cnt = Integer.parseInt(st.nextToken());
			work[i] = cost;
			for (int j = 0; j < cnt ; j++) {
				int from = Integer.parseInt(st.nextToken());
				graph[from].add(i);
				indegree[i] ++;
			}
		}
		
		for (int i = 1; i < n + 1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
				d[i] = work[i];
				
			}
		}
		
		while (!q.isEmpty()) {
			int now = q.poll();
			for (int i : graph[now]) {
				indegree[i] --;
				if (d[i] < d[now] + work[i]) {
					d[i] = d[now] + work[i];
				}
				if (indegree[i] == 0) {
					q.offer(i);
				}
			}
		}
		
		for (int i = 1; i < n + 1; i++) {
			if (total < d[i]) {
				total = d[i];
			}
		}
		bw.write(total + "");
			
		bw.flush();
		bw.close();
	}
}
