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

public class P11437 {

	static int n;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P11437.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		List<Integer>[] a = new ArrayList[n+1];
		for (int i = 1; i < n+1; i++) {
			a[i] = new ArrayList<>();
		}
		
		StringTokenizer st;
		for (int i = 1; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());			
			int y = Integer.parseInt(st.nextToken());
			a[x].add(y);
			a[y].add(x); //  인접리스트
		}
		int[] depth = new int[n+1];
		boolean[] check = new boolean[n+1];
		int[] parent = new int[n+1];
		int start = 1; //1번정점을 시작 점으로 트리를 구성한다.
		Queue<Integer> q = new LinkedList<Integer>();
		check[start] = true;
		depth[start] = 0;
		parent[start] = 0;
		q.add(start);
		while(!q.isEmpty()) {
			int x = q.remove();
			for (int y: a[x]) {
				if (check[y] == false) {
					depth[y] = depth[x] + 1;
					check[y] = true;
					parent[y] = x;
					q.add(y);
				}
			}
		}
		
		int m = Integer.parseInt(br.readLine());
		while(m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());			
			int y = Integer.parseInt(st.nextToken());
			if (depth[x] < depth[y]) {
				int temp = x;
                x = y;
                y = temp;
			}
			while (depth[x] != depth[y]) {
                x = parent[x];
            }
            while (x != y) {
                x = parent[x];
                y = parent[y];
            }
            bw.write(x + "\n");
        }
        bw.flush();
		
	}

}
