public class Test {
    public static int findKthNumber(int k) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i <= k; i++) {
            str.append(i + "");
        }
        return Integer.parseInt(str.charAt(k) + "");
    }

    public static void main(String[] args) {
        System.out.println(findKthNumber(12));
    }
}
