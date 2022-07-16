#pragma once

#include <vector>
#include <string>

std::vector<bool> StringToBinary(std::string binaryString);
std::vector<bool> HexToBinary(std::string hexString);
unsigned int BinaryToDecimal(const std::vector<bool> &binaryVector);
void PrintBinary(std::vector<bool> binaryVector);