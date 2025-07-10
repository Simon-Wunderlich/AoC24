import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        Scanner scnr = new Scanner(input);

        int safeReports = 0;

        while(scnr.hasNext()) {
            Scanner lineScnr = new Scanner(scnr.nextLine());
            safeReports += analyseReport(lineScnr);
        }
        System.out.println(safeReports);
    }
    public static int analyseReport(Scanner lineScnr) {
        int prevInt = lineScnr.nextInt();
        int currentInt = 0;
        double direction = 0;

        while(lineScnr.hasNext()) {
            currentInt = lineScnr.nextInt();

            if (direction == 0)
                direction = Math.signum(currentInt - prevInt);

            if (Math.abs(currentInt - prevInt) > 3 || currentInt - prevInt == 0 || Math.signum(currentInt - prevInt) != direction) {
                System.out.printf("%d %d\n", prevInt, currentInt);
                return 0;
            }
            direction = Math.signum(currentInt - prevInt);
            prevInt = currentInt;
        }
        return 1;
    }
}