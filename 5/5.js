const fs = require('fs');

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    main(data);
});

function convertoMap(arr) {
    map = new Object();
    for (i = 0; i < arr.length; i++) {

        pair = arr[i].split("|");
        if (!(pair[0] in map))
            map[pair[0]] = [];
        values = map[pair[0]]
        map[pair[0]].push(pair[1]);
    }
    return map;
}

function verifySequence(seq, map) {
    for (i = 0; i < seq.length; i++) {
        pastVals = seq.slice(0, i)
        if (!(seq[i] in map))
            continue;
        if ((pastVals.filter(value => map[seq[i]].includes(value))).length != 0)
            return false;
    }
    return true;
}

function sort(seq, map) {
    for (i = 0; i < seq.length; i++) {
        for (j = i; j < seq.length; j++) {
            if (!(seq[j] in map))
                continue;
            if (map[seq[j]].includes(seq[i])) {
                [seq[i], seq[j]] = [seq[j], seq[i]];
            }
        }
    }
    return seq;
}

function findMiddle(arr) {
    return Number(arr[Math.floor(arr.length/2)])
}

function main(inputStr) {
    inputArr = inputStr.split("\r\n\r\n");
    rules = inputArr[0].split("\r\n");
    ruleMap = convertoMap(rules);
    updates = inputArr[1].split("\r\n");
    total = 0;
    for (x of updates) {
        if (!verifySequence(x.split(","), ruleMap)) {
            sorted = sort(x.split(","), ruleMap);
            total += findMiddle(sorted);
        }
    }
    console.log(total);
}


