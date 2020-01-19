package problems;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P9019 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            boolean[] check = new boolean[10001];
            int[] dist = new int[10001];
            char[] how = new char[10001];
            int[] from = new int[10001];
            check[n] = true;
            dist[n] = 0;
            from[n] = -1;
            Queue<Integer> q = new LinkedList<Integer>();
            q.add(n);
            while (!q.isEmpty()) {
                int now = q.remove();
                int next = (now*2) % 10000;
                if (check[next] == false) {
                    q.add(next);
                    check[next] = true;
                    dist[next] = dist[now]+1;
                    from[next] = now;
                    how[next] = 'D';
                }
                next = now-1;
                if (next == -1) next = 9999;
                if (check[next] == false) {
                    q.add(next);
                    check[next] = true;
                    dist[next] = dist[now]+1;
                    from[next] = now;
                    how[next] = 'S';
                }
                next = (now%1000)*10 + now/1000;
                if (check[next] == false) {
                    q.add(next);
                    check[next] = true;
                    dist[next] = dist[now]+1;
                    from[next] = now;
                    how[next] = 'L';
                }
                next = (now/10) + (now%10)*1000;
                if (check[next] == false) {
                    q.add(next);
                    check[next] = true;
                    dist[next] = dist[now]+1;
                    from[next] = now;
                    how[next] = 'R';
                }
            }
            StringBuilder ans = new StringBuilder();
            while (m != n) {
                ans.append(how[m]);
                m = from[m];
            }
            System.out.println(ans.reverse());
        }
    }
}
