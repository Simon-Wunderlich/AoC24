import java.io.File;
import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        Scanner scnr = new Scanner(input);

        int safeReports = 0;

        while(scnr.hasNext()) {
            String[] lineScnr = scnr.nextLine().split(" ");
            safeReports += analyseReport(lineScnr, false);
        }
        System.out.println(safeReports);
    }
    public static int analyseReport(String[] line, boolean dampening) {
        int prevInt = Integer.parseInt(line[0]);
        int currentInt = 0;
        double direction = 0;

        for(int i = 1; i < line.length; i++) {
            currentInt = Integer.parseInt(line[i]);

            if (direction == 0)
                direction = Math.signum(currentInt - prevInt);

            if (Math.abs(currentInt - prevInt) > 3 || currentInt - prevInt == 0 || Math.signum(currentInt - prevInt) != direction) {
                if (dampening)
                    return 0;
                for(int x = 0; x < line.length; x++) {
                    String[] lineCopy = new String[line.length-1];
                    System.arraycopy(line, 0, lineCopy, 0, x);
                    System.arraycopy(line, x + 1, lineCopy, x, line.length - 1 - x);
                    if (analyseReport(lineCopy, true) == 1)
                        return 1;
                }
                return 0;
            }
            direction = Math.signum(currentInt - prevInt);
            prevInt = currentInt;
        }
        return 1;
    }
}