package problems;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class P9935 {

	static class Pair{
		int first;
		int second;
		Pair(int first, int second){
			this.first = first;
			this.second = second;
		}
	}
	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P9935.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] a = br.readLine().toCharArray();
		char[] b = br.readLine().toCharArray();
		boolean[] erased = new boolean[a.length];

		
		
		if (b.length == 1) {
			for (int i = 0; i < a.length; i++) {
				if (a[i] == b[0]) {
					erased[i] = true;
				}
			}
		} else {
			Stack<Pair> s = new Stack<>();
			for (int i = 0; i < a.length; i++) {
				if (a[i] == b[0]) {
					s.add(new Pair(i, 0)); // 새로운 폭발문자열의 시작
				} else {
					if (!s.empty()) {
						Pair p = s.peek();
						if (a[i] == b[p.second + 1]) {
							s.add(new Pair(i, p.second + 1));
							if (p.second + 1 == b.length - 1) { // 끝에 도달하면
								for (int k = 0; k < b.length; k ++) { // 폭발물의 길이만큼 팝 시킴
									erased[s.pop().first]= true; 
								}
							}
						} else {
							while(!s.isEmpty()) {
								s.pop();
							}
						}
					}
				}
			}
		}
		
		boolean printed = false;
		for (int i = 0; i < erased.length; i++) {
			if (erased[i] == false) {
				System.out.print(a[i]);
				printed = true;
			}
		}
		
		if (printed == false) {
			System.out.println("FRULA");
		}

	}

}
