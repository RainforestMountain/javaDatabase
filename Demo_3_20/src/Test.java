import java.util.Arrays;

public class Test {
    public static void quickSort(int[] array, int left, int right) {
        //序列只有一个元素不用排序
        if (left >= right) {
            return;
        }

        //通过基准元素进行左右划分
        int div = partition(array, left, right);

        //对左边序列进行排序
        quickSort(array, left, div);

        //对右边序列进行排序
        quickSort(array, div + 1, right);
    }


    public static int partition(int[] array, int left, int right) {
        int i = left;
        int j = right - 1;
        int base = array[i];

        while (i < j) {
            while (i < j && array[j] >= base) {
                j--;
            }
            while (i < j && array[i] <= base) {
                i++;
            }

            swap(array, i, j);
        }
        swap(array, left, i);
        return i;
    }

    private static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    public static void main(String[] args) {
        int[] arr = {15, 4, 8, 9, 20, 6, 1, 18};
        quickSort(arr, 0, arr.length);
        System.out.println(Arrays.toString(arr));
    }
}
