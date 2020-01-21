package problems;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class P10814 {

	static int n;
	static class Person implements Comparable<Person>{
		int age;
		String name;
		int join;
		Person(int age, String name, int join){
			this.age = age;
			this.name = name;
			this.join = join;
		}
		@Override
		public int compareTo(Person p) {
			if (this.age > p.age) {
				return 1;
			} else if (this.age == p.age) {
				if (this.join >= p.join) {
					return 1;
				} else {
					return -1;
				}
			} else {
				return -1;
			}
		}
		
	}
	

	public static void main(String[] args) throws FileNotFoundException, IOException {
		System.setIn(new FileInputStream("src/input/P10814.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		
		List<Person> list = new ArrayList<>();
		
		for(int i = 1; i <= n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			list.add(new Person(age, name, i));
		}
		
		Collections.sort(list);
		for (Person p : list) {
			bw.write(p.age + " " + p.name + "\n");
		}
		
		bw.flush();
		bw.close();
	}

}
