package test4;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read scanner = new Read();

    public static void main(String[] args) throws IOException {
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            String src = scanner.next();
            List<Character> charList = new ArrayList<>();
            List<Integer> numList = new ArrayList<>();
            boolean jude = true;
            boolean flag = false;//如果为false说明还没有字母,有了字母就是true
            for (int j = 0; j < src.length(); j++) {
                char ch = src.charAt(j);
                if (ch >= 'a' && ch <= 'z') {
                    if (!flag) {
                        flag = true;
                    }
                    charList.add(ch);
                } else if (ch >= '0' && ch <= '9') {
                    if (flag) {
                        jude = false;
                        break;
                    }
                    numList.add(ch - '0');
                } else {
                    jude = false;
                    break;
                }
            }
            if (!jude) {
                out.println("No");
            } else {
                for (int j = 1; j < charList.size(); j++) {
                    if (charList.get(j) < charList.get(j - 1)) {
                        jude = false;
                        break;
                    }
                }
                if (jude) {
                    for (int j = 1; j < numList.size(); j++) {
                        if (numList.get(j) < numList.get(j - 1)) {
                            jude = false;
                            break;
                        }
                    }
                }
                if (jude) {
                    out.println("Yes");
                } else {
                    out.println("No");
                }
            }
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

