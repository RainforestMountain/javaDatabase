public class Heap {
    public int[] elem;
    public int size;

    public int poll() {
        int tmp = elem[0];
        elem[0] = elem[size - 1];
        elem[size - 1] = tmp;
        size--;
        shiftDown(0, size);
        return tmp;
    }
}
