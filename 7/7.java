package org.example;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    static boolean isValid = false;
    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        Scanner scnr = new Scanner(input);
        long total = 0;
        while(scnr.hasNextLine()) {
            String line = scnr.nextLine();
            line = line.replace(":", "");
            String[] vals =  line.split(" ");
            total += validate(Long.parseLong(vals[0]), Arrays.copyOfRange(vals, 1, vals.length));
        }
        System.out.println(total);
    }
    static long validate(long target, String[] vals) {
        isValid = false;
        findPatterns(vals.length, Long.parseLong(vals[0]), target, 1, vals);
        if (isValid)
            return target;
        return 0;
    }
    static void findPatterns(int length, long total, long target, int charNum, String[] vals) {
        if (charNum == length) {
            if (total == target)
                isValid = true;
            return;
        }
        if (isValid)
            return;

        long newTotal = total + Long.parseLong(vals[charNum]);
        findPatterns(length, newTotal, target, charNum+1, vals);

        newTotal = total * Long.parseLong(vals[charNum]);
        findPatterns(length, newTotal, target, charNum+1, vals);

        newTotal = Long.parseLong(String.format("%d%s",total,vals[charNum]));
        findPatterns(length, newTotal, target, charNum+1, vals);

    }
}