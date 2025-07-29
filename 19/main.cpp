#include <fstream>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

std::vector<std::string> split(std::string input, std::string delimiter){

    std::vector<std::string> tokens;
    size_t pos = 0;
    std::string token;

    while((pos = input.find(delimiter)) != std::string::npos){
        token = input.substr(0, pos);
        tokens.push_back(token);
        input.erase(0, pos + delimiter.length());
    }

    tokens.push_back(input);

    return tokens;
}

void dfs(std::string str, std::string target, std::vector<std::string> towels, std::map<std::string,long> & memo, long & count) {
    if (memo.count(str) == 1) {
        count += memo[str];
        return;
    }
    if (str == target) {
        count++;
        return;
    }
    for (std::string s : towels) {
        if (target.substr(0,str.length() + s.length()) == str+s) {
            long temp = count;
            dfs(str+s, target, towels, memo, count);
            if (temp != count || count == 0) {
                memo[str+s] = count-temp;
            }
        }
    }
}


int main() {
    std::string inputLine;
    std::vector<std::string> inputList;
    std::string towelStr;
    std::ifstream inputFile("19/input.txt");
    std::getline(inputFile, towelStr);

    std::vector<std::string> towelList = split(towelStr, ", ");

    std::getline(inputFile, inputLine);
    long count = 0;

    std::map<std::string,long> memo;
    while (std::getline(inputFile, inputLine)) {
        memo = {};
        long _count = 0;
        dfs("", inputLine , towelList, memo, _count);
        count+=_count;
    }
    std::cout << count << std::endl;
}
