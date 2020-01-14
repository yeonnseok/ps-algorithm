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
import java.util.StringTokenizer;

public class P6603 {

	static int N;
	static int[] nums;
	static List<Integer> lotto = new ArrayList<>();
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P6603.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			if(N == 0) {
				return;
			}
			nums = new int[N];
			for (int i = 0; i < N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			solve(0, 0);
		}
		
	}
	
	public static void solve(int index, int cnt) {
		// 정답을 찾은 경우
		if (cnt == 6) {
			for (int num : lotto) {
				System.out.printf("%d ", num);
			}
			System.out.println();
			return;
		}
		
		// 답이 안나오는 경우
		if (index >= N) {
			return;
		}
		
		// 다음 함수 호출
		lotto.add(nums[index]);
		solve(index + 1, cnt + 1);
		lotto.remove(lotto.size() - 1);
		solve(index + 1, cnt);
	}
}
