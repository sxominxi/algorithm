package algorithm.baekjoon.bronze;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class N10988 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();

        List<Character> charList = new ArrayList<>();
        for (char c : word.toCharArray()) {
            charList.add(c);
        }

        int ans = 1;
        int len = charList.size();

        for (int i = 0; i < len / 2; i++) {
            if (charList.get(i) != charList.get(len - i - 1)) {
                ans = 0;
                break;
            }
        }

        System.out.println(ans);
    }
}
