package test6;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read scanner = new Read();

    public static void main(String[] args) throws IOException {
        int t = scanner.nextInt();
        for (int k = 0; k < t; k++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int[] program = new int[n + m + 1];
            int[] test = new int[n + m + 1];
            for (int i = 0; i < n + m + 1; i++) {
                program[i] = scanner.nextInt();
            }
            for (int i = 0; i < n + m + 1; i++) {
                test[i] = scanner.nextInt();
            }
            int[] result = new int[n + m + 1];
            for (int i = 0; i < n + m + 1; i++) {
                int temp_p = n;
                int temp_t = m;
                int value = 0;
                for (int j = 0; j < n + m + 1; j++) {
                    if (j == i) {
                        continue;
                    }
                    if (program[j] >= test[j]) {
                        if (temp_p == 0) {
                            temp_t--;
                            value += test[j];
                        } else {
                            temp_p--;
                            value += program[j];
                        }
                    } else {
                        if (temp_t == 0) {
                            temp_p--;
                            value += program[j];
                        } else {
                            temp_t--;
                            value += test[j];
                        }
                    }
                }
                result[i] = value;
            }
            for (int val : result) {
                out.print(val + " ");
            }
            out.println();
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

