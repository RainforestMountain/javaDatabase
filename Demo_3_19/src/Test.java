import java.util.Arrays;

public class Test {

    public static void selectSort(int[] array) {
        int j = 1;
        int minIndex = 0;
        for (j = 1; j < array.length; j++) {
            minIndex = j - 1;
            for (int k = j; k < array.length; k++) {
                if (array[minIndex] > array[k]) {
                    minIndex = k;
                }
            }

            int tmp = array[j - 1];
            array[j - 1] = array[minIndex];
            array[minIndex] = tmp;

        }
    }

    public static void selectSort2(int[] array) {
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            int minIndex = left;
            int maxIndex = right;

            for (int k = left; k <= right; k++) {
                if (array[minIndex] > array[k]) {
                    minIndex = k;
                }

            }
            int tmp1 = array[left];
            array[left] = array[minIndex];
            array[minIndex] = tmp1;

            for (int k = left; k <= right; k++) {
                if (array[maxIndex] < array[k]) {
                    maxIndex = k;
                }
            }
            int tmp2 = array[right];
            array[right] = array[maxIndex];
            array[maxIndex] = tmp2;

            left++;
            right--;
        }
    }

    public static void main(String[] args) {

        int[] arr = {32, 4, 7, 9, 3, 25};
        selectSort2(arr);
        System.out.println(Arrays.toString(arr));
    }

}
