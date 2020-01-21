package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class P14395 {

	final static long limit = 1000000000L;
	static long s, t;
	static Set<Long> check = new HashSet<>();
	static Queue<Long> q = new LinkedList<>();
	static Queue<String> qs = new LinkedList<>();

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P14395.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		s = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());
		
		q.offer(s);
		qs.offer("");
		check.add(s);
		
		
		while(!q.isEmpty()) {
			long x = q.poll();
			String str = qs.poll();
			if (x == t) {
				if(str.length() == 0) { //  s 와 t 가 연산 없이 같은 경우
					str = "0";
				}
				System.out.println(str);
				return;
			}
			
			if (0 <= x*x && x*x <= limit && check.contains(x*x) == false) {
				q.add(x*x);
				qs.add(str+"*"); // 연산자 저장
				check.add(x*x);
			}
			if (0 <= x+x && x+x <= limit && check.contains(x+x) == false) {
				q.add(x+x);
				qs.add(str+"+"); // 연산자 저장
				check.add(x+x);
			}
			if (0 <= x-x && x-x <= limit && check.contains(x-x) == false) {
				q.add(x-x);
				qs.add(str+"-"); // 연산자 저장
				check.add(x-x);
			}
			if (x != 0 && 0 <= x/x && x/x <= limit && check.contains(x/x) == false) {
				q.add(x/x);
				qs.add(str+"/"); // 연산자 저장
				check.add(x/x);
			}
		}
		System.out.println(-1);

	}

}
