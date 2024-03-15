import java.util.Arrays;

public class Sort {
    public void insertSort(int[] array) {
        int i = 1;
        int j = 0;
        //升序
        for (i = 1; i < array.length; i++) {
            int temp = array[i];

            for (j = i - 1; j >= 0; j--) {
                if (temp < array[j]) {
                    array[j + 1] = array[j];
                } else {
                    break;
                }
            }
            //插入位置在j后面，因为此时array[j] < temp
            array[j + 1] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {10, 4, 18, 12, 5, 3, 7, 25};
        Sort sort = new Sort();
        sort.insertSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
