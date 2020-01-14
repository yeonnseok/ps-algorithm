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
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P11657 {

	static class Edge implements Comparable<Edge>{
		int from;
		int to;
		int cost;
		Edge (int from, int to, int cost){
			this.from = from;
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
	static final int INF = 100000000;
	static List<Edge> a = new ArrayList<>();
	static int[] dist;
	static PriorityQueue<Edge> pq = new PriorityQueue<>();

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P11657.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		

		for (int i = 0; i < m; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			a.add(new Edge(from, to, cost));
		}

		dist = new int[n + 1];
		Arrays.fill(dist, INF);
		
		boolean negative_cycle = false;
		dist[1] = 0; // 처음시작까지의 누적 경로 0
		for (int i = 1; i < n + 1; i++) {
			for (Edge e : a) {
				int x = e.from;
				int y = e.to;
				int z = e.cost;
				if (dist[x] != INF && dist[y] > dist[x] + z) {
					dist[y] = dist[x] + z;
					if(i == n) { // 선택된 간선의 최소 갯수는 n-1개 
						negative_cycle = true;
					}
				}
			}
		}
		if (negative_cycle) {
			System.out.println("-1");
		} else {
			for (int i = 2; i < n + 1; i++) {
				if (dist[i] == INF) dist[i] = -1;
				System.out.println(dist[i]);
			}
		}
		
	}
	
	
}
