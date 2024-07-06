package algorithm.baekjoon.bronze;

import java.util.Scanner;

public class N3003 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] piece = new int[6]; // 배열 크기 선언

        for (int i = 0; i < piece.length; i++) {
            piece[i] = scanner.nextInt(); // 사용자 입력을 배열에 할당

            if (i == 0 || i == 1) {
                System.out.print(1 - piece[i] + " ");
            }
            if (i == 2 || i == 3 || i == 4) {
                System.out.print(2- piece[i]+ " ");
            }
            if (i == 5) {
                System.out.print(8 - piece[i]);
            }
        }
    }
}
