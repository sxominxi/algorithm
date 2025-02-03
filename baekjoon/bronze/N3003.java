package algorithm.baekjoon.bronze;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.util.*;


public class N3003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력을 받음
        String line = br.readLine();

        // 문자열 배열로 변환
        String[] input = line.split(" ");

        // int 배열로 변환
        int[] numbers = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            numbers[i] = Integer.parseInt(input[i]);
        }

        // 필요한 피스 배열
        int[] need = new int[6];

        need[0] = 1 - numbers[0];
        need[1] = 1 - numbers[1];
        need[2] = 2 - numbers[2];
        need[3] = 2 - numbers[3];
        need[4] = 2 - numbers[4];
        need[5] = 8 - numbers[5];

        for (int i = 0; i < input.length; i++) {
            System.out.print(need[i] + " ");
        }
    }
}
