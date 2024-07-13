package algorithm.inflearn.firstjava.scanner;

import java.util.Scanner;

public class N2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("하나의 정수를 입력하세요:");
        int num = scanner.nextInt();

        switch (num % 2) {
            case 0:
                System.out.println("입력한 숫자 " + num + "는 짝수입니다.");
                break;
            case 1:
                System.out.println("입력한 숫자 " + num + "는 홀수입니다.");
                break;
        }
    }
}
