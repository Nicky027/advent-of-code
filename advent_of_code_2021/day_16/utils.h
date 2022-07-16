#pragma once

#include <vector>
#include <string>

std::vector<bool> StringToBinary(std::string binaryString);
std::vector<bool> HexToBinary(std::string hexString);
void PrintBinary(std::vector<bool> binaryVector);
unsigned long long BinaryToDecimal(const std::vector<bool> &binaryVector);