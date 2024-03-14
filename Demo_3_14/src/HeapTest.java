import java.util.Arrays;

public class HeapTest {
    public int[] array;
    public int size;

    public void initArray(int[] array) {
        this.array = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            this.array[i] = array[i];
        }
        this.size = array.length;
    }

    //大根堆
    public void creatMaxHeap(int[] array) {
        this.initArray(array);
        for (int parent = (size - 1 - 1) / 2; parent >= 0; parent--) {
            shiftDown(parent, size);
        }
    }

    public void shiftDown(int parent, int end) {
        int child = 2 * parent + 1;
        //child > end 时parent 在堆的最底层，child 已经越界说明向下调整完成
        while (child < end) {
            if (child + 1 < end && array[child] < array[child + 1]) {
                child = child + 1;
            }
            if (array[parent] < array[child]) {
                int tmp = array[parent];
                array[parent] = array[child];
                array[child] = tmp;
            } else {
                break;
            }
            parent = child;
            child = 2 * parent + 1;
        }
    }

    public int poll() {
        int tmp = array[0];
        array[0] = array[size - 1];
        array[size - 1] = tmp;

        size--;

        shiftDown(0, size);
        return tmp;
    }

    public boolean isFull() {
        return size == array.length;
    }

    public void insert(int value) {
        if (isFull()) {
            this.array = Arrays.copyOf(this.array, array.length * 2);
        }
        array[size] = value;
        size++;
        siftUp(size - 1);
    }

    public void siftUp(int child) {
        int parent = (child - 1) / 2;
        while (child > 0) {
            if (array[parent] >= array[child]) {
                break;
            }
            int tmp = array[parent];
            array[parent] = array[child];
            array[child] = tmp;
            //继续向上调整
            child = parent;
            parent = (child - 1) / 2;
        }
    }

    public static void heapSort(int[] array) {
        HeapTest heap = new HeapTest();
        heap.creatMaxHeap(array);

        int end = heap.size;
        while (end > 0) {
            int tmp = heap.array[0];
            heap.array[0] = heap.array[end - 1];
            heap.array[end - 1] = tmp;
            end--;
            heap.shiftDown(0, end);
        }
        System.arraycopy(heap.array, 0, array, 0, heap.array.length);
    }

    public static void main(String[] args) {
        HeapTest ht = new HeapTest();
        int[] arr = {27, 15, 19, 18, 28, 34, 65, 49, 25, 37};
        ht.creatMaxHeap(arr);
        System.out.println();
        //System.out.println(ht.poll());
        System.out.println();
        ht.insert(80);
        System.out.println();

        heapSort(arr);
        System.out.println(Arrays.toString(arr));
    }


}
