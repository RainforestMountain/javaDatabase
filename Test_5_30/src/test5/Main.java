package test5;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read scanner = new Read();

    public static void main(String[] args) throws IOException {
        int t = scanner.nextInt();
        for (int k = 0; k < t; k++) {
            int n = scanner.nextInt();
            int[] a = new int[n + 1];
            int[] b = new int[n + 1];
            for (int j = 0; j < n; j++) {
                a[j] = scanner.nextInt();
            }
            for (int j = 0; j <= n; j++) {
                b[j] = scanner.nextInt();
            }
            int[] diff = new int[n + 1];
            for (int j = 0; j < n; j++) {
                diff[j] = b[j] - a[j];
            }
            int dx = Integer.MAX_VALUE;
            int index = 0;
            for (int j = 0; j < n; j++) {
                int abs = Math.abs(a[j] - b[n]);
                if (abs < dx) {
                    dx = abs;
                    index = j;
                }
            }
            a[n] = a[index];
            diff[n] = b[n] - a[n];
            int count = 1;
            int positive = 0;
            int negative = 0;
            for (int j = 0; j < diff.length; j++) {
                if (diff[j] > 0) {
                    positive = Math.max(positive, diff[j]);
                } else if (diff[j] < 0) {
                    negative = Math.min(negative, diff[j]);
                }
            }
            out.println(count + positive - negative);
        }
        out.close();
    }
}

class Read {
    StringTokenizer st = new StringTokenizer("");
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String next() throws IOException {
        while (!st.hasMoreTokens()) {//没有分割就继续分割
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

