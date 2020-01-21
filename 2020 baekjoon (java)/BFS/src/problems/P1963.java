package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1963 {

	static int t;
	static boolean[] check;
	static boolean[] che;
	static int[] dist;
	static Queue<Integer> q = new LinkedList<>();
	
	public static int change(int now, int index, int digit) {
		if (index == 0 && digit == 0) return -1;
		String str = Integer.toString(now);
		StringBuilder sb = new StringBuilder(str);
		sb.setCharAt(index, (char)(digit + '0'));
		return Integer.parseInt(sb.toString());
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P1963.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 1. 소수를 만들어 놓는다.
		che = new boolean[10001];
		for (int i = 2; i <= 10000; i++) {
			if (che[i]) continue;
			for (int j = i+i; j <= 10000; j += i) {
				che[j] = true;
			}
		}
		for (int i = 0; i <= 10000; i++) {
			che[i] = !che[i];
		}
		

		t = Integer.parseInt(br.readLine());
		while (t-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int target = Integer.parseInt(st.nextToken());
			
			dist = new int[10001];
			check = new boolean[10001];
			
			// 2. start지점 큐에 넣는다.
			q.offer(start);
			dist[start] = 0;
			check[start] = true;
			while (!q.isEmpty()) {
				int now = q.poll();
				for (int i = 0; i < 4; i++) {
					for (int j = 0; j <= 9; j++) {
						int next = change(now, i, j);  // 3. start부터 앞에서부터 한자리씩 0~9까지 바꿔가며, bfs를 진행한다.
						if (next == -1) continue;
						if (che[next] && check[next] == false) {
							q.offer(next);
							check[next] = true;
							dist[next] = dist[now] + 1;
						}
					}
				}
			}
			System.out.println(dist[target]);
		}

	}

}
