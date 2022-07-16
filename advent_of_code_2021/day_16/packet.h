#pragma once

#include <vector>
#include <ostream>

enum Type
{
    Sum = 0,
    Product = 1,
    Minimum = 2,
    Maximum = 3,
    Literal = 4,
    GreaterThan = 5,
    LessThan = 6,
    EqualTo = 7
};

enum LengthType
{
    Undefined = -1,
    SubpacketsLength = 0,
    NumberOfSubpackets = 1
};

class Packet
{
private:
    std::vector<bool> m_inputData;
    std::vector<bool> m_data;
    unsigned int m_version;
    Type m_type;
    LengthType m_lengthType{Undefined};
    int m_subpacketsLength{-1};
    int m_numberOfSubpackets{-1};
    std::vector<Packet> m_subpackets;

public:
    Packet(const std::vector<bool> &binaryVector);
    unsigned int VersionSum() const;
    unsigned long long PacketValue() const;
    friend std::ostream &operator<<(std::ostream &os, const Packet &p);
};

unsigned int parseVersion(const std::vector<bool> &binaryVector);
Type parseType(const std::vector<bool> &binaryVector);
unsigned int parseSubpacketsLength(const std::vector<bool> &binaryVector);
unsigned int parseNumberOfSubpackets(const std::vector<bool> &binaryVector);
std::vector<bool> parseLiteralData(const std::vector<bool> &binaryVector);
std::vector<bool> parseOperatorData(const std::vector<bool> &binaryVector, unsigned int length, LengthType lengthType);
std::vector<Packet> parseSubpackets(std::vector<bool> binaryVector, unsigned int length, LengthType lengthType);
std::vector<bool> findPacketData(std::vector<bool> binaryVector);
