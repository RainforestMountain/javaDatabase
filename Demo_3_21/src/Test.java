import java.util.Arrays;

public class Test {

    public static void shellSort(int[] array) {
        int gap = array.length;

        while (gap > 1) {
            gap = gap / 3 + 1;
            insertSort(array, gap);

        }
    }

    public static void insertSort(int[] array, int gap) {
        for (int i = gap; i < array.length; i++) {
            int temp = array[i];
            int j = i - gap;
            for (; j >= 0; j = j - gap) {
                if (temp < array[j]) {
                    array[j + gap] = array[j];
                } else {
                    break;
                }
            }
            array[j + gap] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 9, 4, 2, 7, 6, 8};
        shellSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
