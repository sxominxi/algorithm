package algorithm.inflearn.firstjava.array;

import java.util.Scanner;

public class N5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] arr = new int[4][3];

        for (int i = 0; i < 4; i++) {
            System.out.println((i + 1) + "번 학생의 성적을 입력하세요:");
            System.out.print("국어 점수: ");
            arr[i][0] = scanner.nextInt();
            System.out.print("영어 점수: ");
            arr[i][1] = scanner.nextInt();
            System.out.print("수학 점수: ");
            arr[i][2] = scanner.nextInt();
        }

        for (int i = 0; i < 4; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++) {
                sum += arr[i][j];
            }

            double avg = (double) sum / 3;
            System.out.println((i + 1) + "번 학생의 총점: " + sum + ", 평균: " + avg);
        }
    }
}
