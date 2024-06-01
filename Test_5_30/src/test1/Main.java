package test1;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read scanner = new Read();
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        int n = scanner.nextInt();
        int[][] fee = new int[n][n];
        int[][] dp = new int[n][n];//dp[i][j]表示i站点到j站点最小租金
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                fee[i][j] = scanner.nextInt();
                dp[i][j] = fee[i][j];//dp数组和fee数组一致,初始i到j的路径是, 如果i到j有边,那么是边上的权值,否则是0 或者无穷大
            }
        }
        //由于不是多级图, 那么k 中间点的取值是除了起始点和终点都可能选,只要有边
        //状态转移,先枚举k,这样i到j的最短路径,不会漏算
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        System.out.println(dp[0][n - 1]);

    }

}

class Read {
    StringTokenizer st = new StringTokenizer("");
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String next() throws IOException {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(bf.readLine());
        }
        return st.nextToken();
    }

    String nextLine() throws IOException {
        return bf.readLine();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }
}
