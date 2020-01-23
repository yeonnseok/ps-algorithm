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
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P2109 {
	
	static int n;
	static List<Lecture> a = new ArrayList<>();
	static long ans;
	static PriorityQueue<Integer> pq = new PriorityQueue<>();
	static class Lecture implements Comparable<Lecture>{
		int pay;
		int day;
		int isLec;
		Lecture(int pay, int day){
			this.pay = pay;
			this.day = day;
			isLec = 1;
		}
		Lecture(int day){
			this.day = day;
			isLec = 0;
		}
		@Override
		public int compareTo(Lecture that) {
			if (this.day < that.day) {
				return 1;
			} else if (this.day == that.day) {
				if (this.isLec < that.day) {
					return 1;
				} else if (this.isLec == that.day) {
					return 0;
				} else {
					return -1;
				}
			} else {
				return -1;
			}
			
		}
		
		@Override
		public String toString() {
			if (isLec == 1) {
				return " " + this.pay + " " + this.day;
			} else {
				return " " + this.day + " ";	
			}
		}
	}

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P2109.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		
		// 1. 입력 값
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int pay = Integer.parseInt(st.nextToken());
			int day = Integer.parseInt(st.nextToken());
			a.add(new Lecture(pay, day));
		}
		Collections.sort(a);	// 정렬,	
		int k = 0;
		for (int i=10000; i>=1; i--) {
            while (k < n && a.get(k).day == i) {
                pq.offer(-a.get(k).pay);
                k += 1;
            }
            if (!pq.isEmpty()) {
                ans += -pq.poll();
            }
        }
		
		System.out.println(a);
		System.out.println(ans);
	}	
	
	
}
