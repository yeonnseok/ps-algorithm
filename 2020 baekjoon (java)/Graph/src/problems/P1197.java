package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1197 {

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
	static int[] parent;
	static List<Edge> a = new ArrayList<>();
	static boolean[] check;
	static PriorityQueue<Edge> pq = new PriorityQueue<>();

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1922.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		parent = new int[n + 1];
		for (int i = 1; i < n + 1; i++) {
			parent[i] = i;
		}

		StringTokenizer st;
		for (int i = 0; i < m; i ++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			a.add(new Edge(from, to, cost));
		}
		Collections.sort(a);
		
		int ans = 0;
		for (Edge e : a) {
			int x = find(e.from);
			int y = find(e.to);
			if (x != y) { //  연결이 안되어 있다면!?
				union(x, y); // cost 더하고 집합도 합침.
				ans += e.cost;
			}
		}
		
		bw.write(ans+"");
		bw.flush();
		bw.close();
	}
	
	public static void union(int a, int b) {
		int x = find(a);
		int y = find(b);
		
		if (x < y) {
			parent[y] = x;
		} else if (x > y) {
			parent[x] = y;
		}
	}
	
	public static int find(int x) {
		if (parent[x] == x) {
			return x;
		}
		
		return parent[x] = find(parent[x]);
	}
}
