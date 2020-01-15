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
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1162 {

	static class Node implements Comparable<Node>{
		long cost;
		int vertex;
		int step;
		Node(long cost, int vertex, int step){
			this.cost = cost;
			this.vertex = vertex;
			this.step = step;
		}
		@Override
		public int compareTo(Node o) {
			return this.cost > o.cost ? 1 : -1;
		}
		
	}
	static final long INF = 1000000000L*50000L;
	static int n, m, k;
	static long[][] dist;
	static boolean[][] check;
	static PriorityQueue<Node> pq = new PriorityQueue<>(); 
	static List<Edge>[] graph;
	static class Edge{
		int to;
		int cost;
		Edge(int to, int cost){
			this.to = to;
			this.cost = cost;
		}
	}
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1162.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		dist = new long[n+1][k+1]; // 도시 번호와  step(최대 k까지)
		check = new boolean[n+1][k+1];
		for (int i = 0; i < n + 1; i++) {
			for (int j = 0; j < k + 1; j++) {
				dist[i][j] = INF;
			}
		}

		graph = (List<Edge>[]) new ArrayList[n+1];
		for (int i = 1; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			//양방향 도로
			graph[from].add(new Edge(to, cost));
			graph[to].add(new Edge(from, cost));
		}
		
		dist[1][0] = 0; // 시작점.
		pq.add(new Node(0, 1, 0)); // cost, vertex, step
		
		while(!pq.isEmpty()){
			Node now = pq.remove();
			int v = now.vertex;
			int step = now.step;
			if(check[v][step]) continue;
			check[v][step] = true;
			for (Edge e: graph[v]) {
				int to = e.to;
				if (step + 1 <= k && dist[to][step+1] > dist[v][step]) {
					dist[to][step+1] = dist[v][step];
					pq.add(new Node(dist[to][step+1], to, step+1));
				}
				
				if (dist[to][step] > dist[v][step] + e.cost) {
					dist[to][step] = dist[v][step] + e.cost;
					pq.add(new Node(dist[to][step], to, step));
				}
			}
		}
		
		
		long ans = INF;
		for (int i = 1; i <= k; i++) {
			if (check[n][i] && ans > dist[n][i]) {
				ans = dist[n][i];
			}
		}
		bw.write(ans+"");
		bw.flush();
		
		
		
	}

}
