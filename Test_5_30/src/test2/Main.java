package test2;

import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Read scanner = new Read();

    public static void main(String[] args) throws IOException {
        int n = scanner.nextInt();
        int q = scanner.nextInt();
        //下标的范围很大,但是个数不多,可用离散化数组
        List<Integer> ls = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();//先利用set去重
        Add[] adds = new Add[n];
        Enquire[] enquires = new Enquire[q];
        //离线操作,存增加和查询操作,对大点小标进行离散化,映射成连续的小点下标
        for (int i = 0; i < n; i++) {
            adds[i] = new Add();
            adds[i].a = scanner.nextInt();
            adds[i].x = scanner.nextInt();
            set.add(adds[i].a);
        }
        for (int i = 0; i < q; i++) {
            enquires[i] = new Enquire();
            enquires[i].l = scanner.nextInt();
            enquires[i].r = scanner.nextInt();
            set.add(enquires[i].l);
            set.add(enquires[i].r);
        }
        ls.addAll(set);
        ls.sort(((o1, o2) -> (o1 - o2)));
        //查找下标用二分
        int[] result = new int[ls.size() + 1];//离散化数组对应的结果数组,对这个数组进行增加和查询,下标范围压缩了
        for (Add add : adds) {
            int index = binary(ls, add.a);//大点通过离散化数组转换成连续的小点,index范围 [1, ls.size()]
            result[index] += add.x;
        }
        //结果数组前缀和,依然要大点转换成小点
        int[] prefix = new int[result.length + 1];
        for (int i = 1; i < result.length; i++) {
            prefix[i] = prefix[i - 1] + result[i];
        }
        for (Enquire enquire : enquires) {
            int l = binary(ls, enquire.l);
            int r = binary(ls, enquire.r);
            out.println(prefix[r] - prefix[l - 1]);
        }
        out.close();
    }

    public static int binary(List<Integer> ls, int x) {
        int left = 0;
        int right = ls.size() - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (ls.get(mid) == x) {
                return mid + 1;//推荐下标从一开始
            } else if (ls.get(mid) < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}

class Add {
    int a;
    int x;
}

class Enquire {
    int l;
    int r;
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

