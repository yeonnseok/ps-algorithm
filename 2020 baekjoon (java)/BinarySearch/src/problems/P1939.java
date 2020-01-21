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
import java.util.StringTokenizer;

public class P1939 {
	
	static class Edge{
		int to;
		int cost;
		Edge(int to, int cost){
			this.to = to;
			this.cost = cost;
		}
	}
	static int n, m, start, end;
	static ArrayList<Edge>[] a = new ArrayList[10001];
	static boolean[] c = new boolean[10001];
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1939.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<Edge>();
        }
        while (m-- > 0) {
        	st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            a[from].add(new Edge(to, cost));
            a[to].add(new Edge(from, cost));
        }
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		int left = 1;
        int right = 1000000000;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right-left)/2;
            Arrays.fill(c,false);
            if (go(start, mid)) {
                ans = mid;
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        System.out.println(ans);
		
	}	

	static boolean go(int node, int limit) {
        if (c[node]) return false;
        c[node] = true;
        if (node == end) return true;
        for (Edge e : a[node]) {
            int next = e.to;
            int cost = e.cost;
            if (cost >= limit) {
                if (go(next, limit)) return true;
            }
        }
        return false;
    }
	
	
}
