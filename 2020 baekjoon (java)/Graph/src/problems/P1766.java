package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1766 {

	static int n, m;
	static int[] indegree;
	static PriorityQueue<Integer> q = new PriorityQueue<>();

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1766.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		indegree = new int[n + 1];
		List<Integer> graph[] = new ArrayList[n + 1];
		
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 1; i < m + 1; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			
			graph[from].add(to);
			indegree[to] ++;
		}
		
		for (int i = 1; i < n + 1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
			}
		}
		
		while (!q.isEmpty()) {
			int now = q.poll();
			bw.write(now + " ");
			for (int i : graph[now]) {
				indegree[i] --;
				if (indegree[i] == 0) {
					q.offer(i);
				}
			}
			
			
		}
	
			
		bw.flush();
		bw.close();
	}
}
