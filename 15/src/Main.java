import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int y = 0;
    static int x = 0;
    static boolean obstacleEncountered = false;

    public static void main(String[] args) throws IOException {
        File input = new File("15/src/input.txt");
        Scanner scnr = new Scanner(input);

        ArrayList<String[]> map = new ArrayList<>();

        int count = 0;

        while(scnr.hasNext()) {
            String line = scnr.nextLine();
            line = line.replaceAll("\\.", "..");
            line = line.replaceAll("@", "@.");
            line = line.replaceAll("O", "[]");
            line = line.replaceAll("#", "##");
            if (line.contains("@")) {
                y = count;
                x = line.indexOf("@");
            }
            map.add(line.split(""));
            count++;
            if (line.isEmpty())
                break;
        }
        StringBuilder instructions = new StringBuilder();
        while(scnr.hasNextLine()) {
            instructions.append(scnr.nextLine());
        }
        for(String step : instructions.toString().split("")) {
            for(String[] line : map) {
                System.out.println(String.join("", line));
            }
            System.out.println();
            map = nextStep(map, step);
        }
        for(String[] line : map) {
            System.out.println(String.join("", line));
        }
        System.out.println();
        int gpsSum = 0;
        for(int y = 0; y < map.size(); y++) {
            for(int x = 0; x < map.get(y).length; x++) {
                if (map.get(y)[x].equals("["))
                    gpsSum+= 100*y + x;
            }
        }
        System.out.println("GPS Sum: " + gpsSum);
    }

    public static ArrayList<String[]> nextStep(ArrayList<String[]> map, String step) {
        int[] dir = parseDir(step);

        int _x = x;
        int _y = y;
        System.out.println("Step: " + step);

        ArrayList<String[]> prevMap = new ArrayList<>();
        for(String[] line : map) {
            prevMap.add(line.clone());
        }
        propagate(map, dir, _x, _y);
        if (obstacleEncountered) {
            System.out.println("Obstacle Encountered!");
            x = _x;
            y =  _y;
            obstacleEncountered = false;
            return prevMap;
        }
        return map;
    }

    public static void propagate(ArrayList<String[]> map, int[] dir, int bx, int by) {
        if (obstacleEncountered)
            return;
        int _x = bx + dir[0];
        int _y = by + dir[1];
        if  (map.get(_y)[_x].equals("]")) {
            propagate(map, dir, _x, _y);
            if (dir[0] == 0)
                propagate(map, dir, _x-1, _y);
        }
        if  (map.get(_y)[_x].equals("[")) {
            propagate(map, dir, _x, _y);
            if (dir[0] == 0)
                propagate(map, dir, _x+1, _y);
        }
        if (map.get(_y)[_x].equals(".")) {
            if (map.get(by)[bx].equals("@")) {
                x += dir[0];
                y += dir[1];
            }
            String temp = map.get(_y)[_x];
            map.get(_y)[_x] = map.get(by)[bx];
            map.get(by)[bx] = temp;
        } else if ((map.get(_y)[_x].equals("#"))) {
            obstacleEncountered = true;
        }
    }

    public static int[] parseDir(String step) {
        return switch (step) {
            case ">" -> new int[]{1, 0};
            case "<" -> new int[]{-1, 0};
            case "^" -> new int[]{0, -1};
            case "v" -> new int[]{0, 1};
            default -> new int[]{0, 0};
        };
    }
}