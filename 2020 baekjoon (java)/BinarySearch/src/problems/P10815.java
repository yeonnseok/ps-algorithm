package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P10815 {

	static int n, m;
	static int[] cards;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P10815.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		cards = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i ++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(cards);
		
		
		m = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			if (hasCard(Integer.parseInt(st.nextToken()))) {
				bw.write(1 + " ");
			} else {
				bw.write(0 + " ");
			}
		}
		bw.flush();
		bw.close();
	}
	
	public static boolean hasCard(int target) {
		int start = 0;
		int end = cards.length - 1;
		
		int mid = 0;
		while (start <= end) {
			mid = (start + end) / 2;
			if (cards[mid] == target) {
				return true;
			} else if(cards[mid] > target) {
				end = mid - 1;
			} else {
				start = mid + 1;
			}
		}
		return false;
	}

}
