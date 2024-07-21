package algorithm.inflearn.firstjava.array;

import java.util.Scanner;

public class N6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 제약 조건 : 상품은 최대 10개까지 등록할 수 있다.

        // 상품 이름을 저장할 String 배열
        String[] productNames = new String[10];
        // 상품 가격을 저장할 int 배열
        int[] productPrices = new int[10];
        // 현재 등록된 상품의 개수를 저장할 int 변수
        int productCount = 0;
        // 종료 조건
        boolean flag = true;

        while (flag) {
            System.out.println("1. 상품 등록 | 2. 상품 목록 | 3. 종료");

            System.out.print("메뉴를 선택하세요: ");
            int menu = scanner.nextInt();

            if (menu == 1) {
                if (productCount >= 10) {
                    System.out.println("더 이상 상품을 등록할 수 없습니다.");
                    flag = false;
                } else {
                    System.out.print("상품 이름을 입력하세요: ");
                    productNames[productCount] = scanner.next();

                    System.out.print("상품 가격을 입력하세요: ");
                    productPrices[productCount] = scanner.nextInt();

                    productCount += 1;
                }
            } else if (menu == 2) {
                if (productCount == 0) {
                    System.out.println("등록한 상품이 없습니다.");
                    flag = false;
                } else {
                    for (int i = 0; i < productCount; i++) {
                        System.out.println(productNames[i] + ": " + productPrices[i] + "원");
                    }
                }
            } else {
                System.out.println("프로그램을 종료합니다.");
                flag = false;
            }
        }
    }
}
