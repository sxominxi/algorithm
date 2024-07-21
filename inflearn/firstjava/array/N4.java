package algorithm.inflearn.firstjava.array;

import java.util.Scanner;

public class N4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 개수 입력받기
        System.out.print("입력받을 숫자의 개수를 입력하세요: ");
        int len = scanner.nextInt();

        // 배열 선언
        int[] num = new int[len];

        // 배열에 정수 입력받기
        System.out.print("3개의 정수를 입력하세요: ");
        for (int i = 0; i < len; i++) {
            num[i] = scanner.nextInt();
        }

        // 가장 작은, 큰 정수 찾기
        int min, max;
        min = max = num[0];
        for (int i = 0; i < len; i++) {
            if (num[i] < min) {
                min = num[i];
            }

            if (num[i] > max) {
                max = num[i];
            }
        }

        // 출력
        System.out.println("가장 작은 정수: " + min);
        System.out.println("가장 큰 정수: " + max);
    }
}
