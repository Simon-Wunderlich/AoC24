#include <fstream>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <ranges>

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

bool dfs(std::string str, std::string target, std::vector<std::string> towels, std::vector<std::string> & memo) {
    if (str == target)
        return true;
    if (find(memo.begin(), memo.end(), str) != memo.end())
        return false;
    for (std::string s : towels) {
        if (target.substr(0,str.length() + s.length()) == str+s) {
            if (dfs(str+s, target, towels, memo))
                return true;
            memo.push_back(str+s);
        }
    }
    return false;
}


int main() {
    std::string inputLine;
    std::vector<std::string> inputList;
    std::string towelStr;
    std::ifstream inputFile("19/input.txt");
    std::getline(inputFile, towelStr);

    std::vector<std::string> towelList = split(towelStr, ", ");

    std::getline(inputFile, inputLine);
    int count = 0;

    std::vector<std::string> memo;
    while (std::getline(inputFile, inputLine)) {
        memo = {};
        count += dfs("", inputLine , towelList, memo) ? 1 : 0;
    }
    std::cout << count << std::endl;
}
