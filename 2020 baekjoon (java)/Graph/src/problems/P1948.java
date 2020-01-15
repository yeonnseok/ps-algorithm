package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1948 {
	
	static class Edge{
		int to;
		int cost;
		Edge(int to, int cost){
			this.cost = cost;
			this.to = to;
		}
	}
	static int n, m;
	static int[] indegree;
	static int[] indegree2;
	static int[] d;
	static Queue<Integer> q = new LinkedList<>();
	static int total;
	static boolean[] c;
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1948.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		d = new int[n + 1];
		indegree = new int[n + 1];
		indegree2 = new int[n + 1];
		c = new boolean[n + 1];
		List<Edge> graph[] = new ArrayList[n + 1];
		List<Edge> graph2[] = new ArrayList[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
			graph2[i] = new ArrayList<>();
		}
		
		StringTokenizer st;
		for (int i = 1; i < m + 1; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
		
			graph[from].add(new Edge(to, cost));
			graph2[to].add(new Edge(from, cost));
			indegree[to] ++;
			indegree2[from] ++;
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i < n + 1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
			}
		}
		while (!q.isEmpty()) {
			int now = q.poll();
			for (Edge e : graph[now]) {
				indegree[e.to] --;
				if (d[e.to] < d[now] + e.cost) {
					d[e.to] = d[now] + e.cost;
				}
				if (indegree[e.to] == 0) {
					q.offer(e.to);
				}
			}
		}
		
		// 최대 경로 비용
		bw.write(d[end] + "\n");
		
		// 경로에 포함된 간선인지 판단.
		c[end] = true;
		for (int i = 1; i <= n; i++) {
			if (indegree2[i] == 0) {
				q.offer(i);
			}
		}
		
		int ans = 0; 
		while(!q.isEmpty()) {
			int rev = q.poll();
			for (Edge ee : graph2[rev]) {
				if (!c[ee.to] && ee.cost == (d[rev] - d[ee.to])) {
					ans ++;
					c[ee.to] = true; 
				}
				indegree2[ee.to]--;
				if (indegree2[ee.to] == 0) {
					q.offer(ee.to);
				}
			}
		}
	
		bw.write(ans+"");
		
		bw.flush();
		bw.close();
	}
}
//dist[i] 에서 dist[j]를 뺏을 때 cost[i]와 같다면 포함된 간선이다.
