const fs = require('fs');

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    main(data);
});

totalPaths = 0;
function main(data) {
    inputArr = data.split("\r\n");
    for (i = 0; i < inputArr.length; i++) {
        for (j = 0; j < inputArr[i].length; j++) {
            if (inputArr[i][j] == "0")
                traverse(j, i, inputArr);
        }
    }
    console.log(totalPaths);
}

function traverse(x, y, map) {
    checkPos(x, y, x + 1, y, map)
    checkPos(x, y, x - 1, y, map)
    checkPos(x, y, x, y + 1, map)
    checkPos(x, y, x, y - 1, map)
}

function checkPos(x1, y1, x2, y2, map) {
    if (x2 >= map[0].length || x2 < 0) {
        return;
    }
    if (y2 >= map.length || y2 < 0) {
        return;
    }
    if (map[y2][x2] == ".")
        return;
    if (Number(map[y2][x2]) - Number(map[y1][x1]) != 1) {
        return;
    }

    if (map[y2][x2] == "9")
        totalPaths++;
    else
        traverse(x2, y2, map);
}