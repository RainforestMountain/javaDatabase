import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Week w = Week.sunday;
        System.out.println(w);
        System.out.println(w.ordinal());
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a week:");
        w = Week.values()[sc.nextInt()];
        switch (w) {
            case monday -> System.out.println("this is monday");
            case tuesday -> System.out.println("this is tuesday");
            case wendsday -> System.out.println("this is wendsday");
            case thursday -> System.out.println("this is thursday");
            case  friday -> System.out.println("this is friday");
            case  saturday -> System.out.println("this is saturday");
            case  sunday -> System.out.println("this is sunday");
        }
    }
}
