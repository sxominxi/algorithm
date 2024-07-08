package algorithm.baekjoon.bronze;

import java.util.Scanner;

public class N2444 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        // 피라미드의 상단 부분 (가장 긴 행 포함)
        for (int n = 0; n < N; n++) {
            // (N-n-1) 개의 공백을 생성
            for (int space = 0; space < N - n - 1; space++) {
                System.out.print(" ");
            }
            // (n*2+1) 개의 별을 생성
            for (int star = 0; star < n * 2 + 1; star++) {
                System.out.print("*");
            }
            System.out.println(); // 줄바꿈
        }

        // 피라미드의 하단 부분
        for (int n = N - 2; n >= 0; n--) {
            // (N-n-1) 개의 공백을 생성
            for (int space = 0; space < N - n - 1; space++) {
                System.out.print(" ");
            }
            // (n*2+1) 개의 별을 생성
            for (int star = 0; star < n * 2 + 1; star++) {
                System.out.print("*");
            }
            System.out.println(); // 줄바꿈
        }
    }
}
