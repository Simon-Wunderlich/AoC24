package org.example;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    static ArrayList<char[]> patterns = new ArrayList<>();
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
        patterns = new ArrayList<>();
        findPatterns(vals.length-1, new char[vals.length-1], 0);
        for(int i = 0; i < patterns.size(); i++) {
            long total = Long.parseLong(vals[0]);
            for (int j = 0; j < patterns.get(i).length; j++) {
                if (patterns.get(i)[j] == '*')
                    total *= Long.parseLong(vals[j+1]);
                else
                    total += Long.parseLong(vals[j+1]);
            }
            if (total == target)
                return target;
        }
        return 0;
    }
    static void findPatterns(int length, char[] line, int charNum) {
        char[] newLine = String.copyValueOf(line).toCharArray();
        if (charNum == length) {
            patterns.add(newLine);
            return;
        }

        newLine[charNum] = '+';
        findPatterns(length, newLine, charNum+1);

        newLine[charNum] = '*';
        findPatterns(length, newLine, charNum+1);

    }
}