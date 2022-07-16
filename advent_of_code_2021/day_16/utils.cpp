#include <iostream>
#include <unordered_map>
#include <cmath>

#include "utils.h"

;
const std::unordered_map<char, std::vector<bool>> HexBitMap{
    {'0', {0, 0, 0, 0}},
    {'1', {0, 0, 0, 1}},
    {'2', {0, 0, 1, 0}},
    {'3', {0, 0, 1, 1}},
    {'4', {0, 1, 0, 0}},
    {'5', {0, 1, 0, 1}},
    {'6', {0, 1, 1, 0}},
    {'7', {0, 1, 1, 1}},
    {'8', {1, 0, 0, 0}},
    {'9', {1, 0, 0, 1}},
    {'A', {1, 0, 1, 0}},
    {'B', {1, 0, 1, 1}},
    {'C', {1, 1, 0, 0}},
    {'D', {1, 1, 0, 1}},
    {'E', {1, 1, 1, 0}},
    {'F', {1, 1, 1, 1}}};

std::vector<bool> StringToBinary(std::string binaryString)
{
    std::vector<bool> v;
    v.reserve(binaryString.size());

    for (char bit : binaryString)
    {
        v.push_back(bit == '1');
    }

    return v;
};

std::vector<bool> HexToBinary(std::string hexString)
{
    size_t length{hexString.size() * 4};
    std::vector<bool> v;
    v.reserve(length);

    for (char c : hexString)
    {
        std::vector<bool> bits = HexBitMap.at(c);
        for (bool b : bits)
            v.push_back(b);
    }

    return v;
}

unsigned long long BinaryToDecimal(const std::vector<bool> &binaryVector)
{
    unsigned long long x{0};

    size_t n{binaryVector.size()};

    for (size_t i{0}; i < binaryVector.size(); i++)
    {
        if (binaryVector[i])
            x += pow(2, n - 1 - i);
    }
    return x;
}

void PrintBinary(std::vector<bool> binaryVector)
{
    for (bool b : binaryVector)
        std::cout << b;
    std::cout << std::endl;
}