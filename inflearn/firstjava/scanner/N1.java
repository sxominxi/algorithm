package algorithm.inflearn.firstjava.scanner;

import java.util.Scanner;

public class N1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("당신의 이름을 입력하세요:");
        String name = scanner.nextLine();

        System.out.print("당신의 나이을 입력하세요:");
        String age = scanner.nextLine();

        System.out.print("당신의 이름은 " + name + "이고, 나이는 " + age + "살입니다.");
    }
}
