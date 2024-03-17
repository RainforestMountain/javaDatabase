import java.util.ArrayList;
import java.util.List;

public class Test {
    public int[][] merge(int[][] intervals) {
        List<int[]> list = new ArrayList<>();
        
    }

    public int[] mergeTwo(int[] arr1, int[] arr2) {
        int x = arr1[0];
        int y = arr1[1];
        int a = arr2[0];
        int b = arr2[1];
        int[] ans = new int[2];
        if (y >= a && y < b) {
            ans[0] = x;
            ans[1] = b;
        } else {
            ans[0] = x;
            ans[1] = y;
        }
        return ans;
    }

    public boolean judeMerge(int[] arr1, int[] arr2) {
        if (arr1[1] > arr2[0]) {
            return false;
        }
        return true;
    }
}
