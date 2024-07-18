package algorithm.inflearn.firstjava.scanner;

import java.util.Scanner;

public class N6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("1: 상품 입력, 2: 결제, 3: 프로그램 종료");
        boolean flag = true;

        int total = 0;

        while (flag) {
            int num = scanner.nextInt();

            if (num == 3) {
                flag = false;
            }
            
            scanner.nextLine(); // 이전에 입력된 개행문자 제거

            switch (num) {
                case 1:
                    System.out.print("상품명을 입력하세요 : ");
                    String name = scanner.nextLine();

                    System.out.print("상품의 가격을 입력하세요 : ");
                    int value = scanner.nextInt();

                    System.out.print("구매 수량을 입력하세요 : ");
                    int cnt = scanner.nextInt();

                    int sum = cnt * value;

                    total += sum;

                    System.out.println("상품명:" + name + " 가격:" + value + " 수량:" + cnt + " 합계:" + sum);
                    break;

                case 2:
                    System.out.println("총비용:" + total);
                    break;
            }
        }
        System.out.println("프로그램을 종료합니다.");
    }
}
