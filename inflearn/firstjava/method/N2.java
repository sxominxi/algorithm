package algorithm.inflearn.firstjava.method;

public class N2 {
    public static void main(String[] args) {
        printMessage("Hello, world!", 3);
        printMessage("Hello, world!", 5);
        printMessage("Hello, world!", 7);
    }

    public static void printMessage(String message, int a) {
        for (int i =0; i < a; i++) {
            System.out.println(message);
        }
    }
}
