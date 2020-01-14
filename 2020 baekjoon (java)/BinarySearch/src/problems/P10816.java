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

public class P10816 {

	static int n, m;
	static int[] cards;

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P10816.txt"));
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
			int input = Integer.parseInt(st.nextToken());
			int len = upperBound(input) - lowerBound(input);
			
			bw.write(len + " ");
			
		}
		bw.flush();
		bw.close();
	}
	
	public static int lowerBound(int target) {
		int start = 0;
		int end = cards.length - 1;
		
		int mid = 0;
		while (start <= end) {
			mid = (start + end) / 2;
			if (cards[mid] < target) {
				start = mid + 1;
			} else if(cards[mid] >= target) {
				end = mid - 1;
			}
		}
		return start;
	}
	
	public static int upperBound(int target) {
		int start = 0;
		int end = cards.length - 1;
		
		int mid = 0;
		while (start <= end) {
			mid = (start + end) / 2;
			if (cards[mid] <= target) {
				start = mid + 1;
			} else if(cards[mid] > target) {
				end = mid - 1;
			}
		}
		return start;
	}

}
