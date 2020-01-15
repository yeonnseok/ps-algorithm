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
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1854 {

	static final long INF = 1000000000L*50000L;
	static int n, m, k;
	static boolean[] check;
	static PriorityQueue<Integer>[] dist;
	static PriorityQueue<Edge> pq = new PriorityQueue<>();
	static List<Edge>[] graph;
	static class Edge implements Comparable<Edge>{
		int to;
		int cost;
		Edge(int to, int cost){
			this.to = to;
			this.cost = cost;
		}
		@Override
		public int compareTo(Edge o) {
			return this.cost > o.cost ? 1 : -1;
		}
	}
	static class Compare implements Comparator<Integer> {
        public int compare(Integer one, Integer two) {
            return two.compareTo(one);
        }
    }
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1854.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		check = new boolean[n+1];
		dist = new PriorityQueue[n+1];
		graph = (List<Edge>[]) new ArrayList[n+1];
		Compare cmp = new Compare();
		for (int i = 1; i <= n; i++) {
			dist[i] = new PriorityQueue<Integer>(1, cmp);
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			graph[from].add(new Edge(to, cost));
		}
		
		pq.add(new Edge(1, 0)); // cost, vertex (½ÃÀÛÁ¡)
		dist[1].offer(0);
		while(!pq.isEmpty()){
			Edge now = pq.remove();
			int cost = now.cost;
			int x = now.to;
			for (Edge e: graph[x]) {
				int y = e.to;
				if(dist[y].size() < k || dist[y].peek() > cost +  e.cost ){
					if (dist[y].size() == k) {
						dist[y].poll();
					}
					dist[y].offer(cost + e.cost);
					pq.add(new Edge(y, cost + e.cost));
				}
			}
		}
		
		for (int i = 1; i <= n; i++) {
			if (dist[i].size() != k) {
				bw.write(-1+"\n");
			} else {
				bw.write(dist[i].peek()+"\n");
			}
		}
		
		bw.flush();
		
		
		
	}

}
