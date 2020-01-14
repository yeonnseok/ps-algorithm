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

public class P1922 {

	static class Edge implements Comparable<Edge>{
		int to;
		int cost;
		Edge (int to, int cost){
			this.to = to;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Edge edge) {
			return this.cost > edge.cost ? 1 : -1;
		}
		
	}
	static int n, m;
	static int ans;
	static List<Edge> graph[];
	static boolean[] check;
	static PriorityQueue<Edge> pq = new PriorityQueue<>();

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1922.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		check = new boolean[n + 1];
		graph = new ArrayList[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		StringTokenizer st;
		for (int i = 0; i < m; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			graph[from].add(new Edge(to, cost));
			graph[to].add(new Edge(from, cost)); // 양방향 간선

		}
		
		check[1] = true;
		for (Edge edge : graph[1]) {
			pq.offer(edge);
		}
	
		while (!pq.isEmpty()) {
			Edge edge = pq.poll();
			if (check[edge.to] == true) {
				continue;
			}P1197.java
			check[edge.to] = true; 
			ans += edge.cost;
			for (Edge e : graph[edge.to]) {//  선별된 edge.to
				pq.offer(e);
			}
		}
	
		bw.write(ans+"");
		bw.flush();
		bw.close();
	}
}
