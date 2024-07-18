package algorithm.inflearn.firstjava.scanner;

import java.util.Scanner;

public class N5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번째 숫자를 입력하세요 : ");
        int firstNum = scanner.nextInt();

        System.out.print("두 번째 숫자를 입력하세요 : ");
        int secondNum = scanner.nextInt();

        int smallNum;
        int largeNum;
        if (firstNum >= secondNum) {
            smallNum = secondNum;
            largeNum = firstNum;
        } else {
            smallNum = firstNum;
            largeNum = secondNum;
        }

        System.out.print("두 숫자 사이의 모든 정수 : ");
        for (int i = smallNum; i <= largeNum; i++) {
            System.out.print(i);

            if (i < largeNum) {
                System.out.print(",");
            }
        }
    }
}
