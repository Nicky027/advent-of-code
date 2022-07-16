#include "packet.h"
#include "utils.h"
#include <iostream>

#define VERSION_BITS_LENGTH 3
#define TYPE_ID_BITS_LENGTH 3
#define LENGTH_TYPE_ID_BIT 6
#define SUBPACKETS_LENGTH_BITS_LENGTH 15
#define NUMBER_OF_SUBPACKETS_BITS_LENGTH 11
#define LITERAL_CHUNK_SIZE 5

Packet::Packet(const std::vector<bool> &binaryVector) : m_inputData(binaryVector),
                                                        m_version(parseVersion(binaryVector)),
                                                        m_type(parseType(binaryVector))
{
    if (m_type == Literal)
    {
        m_data = parseLiteralData(binaryVector);
    }
    else
    {
        m_lengthType = (LengthType)binaryVector[LENGTH_TYPE_ID_BIT];
        switch (m_lengthType)
        {
        case SubpacketsLength:
        {
            m_subpacketsLength = parseSubpacketsLength(binaryVector);
            m_data = parseOperatorData(binaryVector, m_subpacketsLength, SubpacketsLength);
            m_subpackets = parseSubpackets(m_data, m_subpacketsLength, SubpacketsLength);
            break;
        }
        case NumberOfSubpackets:
            m_numberOfSubpackets = parseNumberOfSubpackets(binaryVector);
            m_data = parseOperatorData(binaryVector, m_numberOfSubpackets, NumberOfSubpackets);
            m_subpackets = parseSubpackets(m_data, m_numberOfSubpackets, NumberOfSubpackets);
            break;
        }
    }
}

bool Packet::IsLiteral() const
{
    return m_type == Literal;
}

unsigned int Packet::Version() const
{
    return m_version;
}

unsigned int Packet::VersionSum() const
{
    unsigned int subpacketsVersionSum{0};
    for (Packet s : m_subpackets)
    {
        subpacketsVersionSum += s.VersionSum();
    }
    return m_version + subpacketsVersionSum;
}

std::ostream &operator<<(std::ostream &os, const Packet &p)
{
    os << "Input Data: ";
    for (bool b : p.m_inputData)
        os << b;
    os << std::endl;

    os << "Version: " << p.m_version << std::endl;
    os << "Type ID: " << p.m_type << std::endl;
    os << "Length Type ID: " << p.m_lengthType << std::endl;
    os << "Subpackets Length: " << p.m_subpacketsLength << std::endl;
    os << "Number of Subpackets: " << p.m_numberOfSubpackets << std::endl;

    os << "Data: ";
    for (bool b : p.m_data)
        os << b;
    os << std::endl;

    os << "Version Sum: " << p.VersionSum() << std::endl;

    return os;
}

unsigned int parseVersion(const std::vector<bool> &binaryVector)
{
    std::vector<bool> versionBits(
        binaryVector.begin(),
        binaryVector.begin() + VERSION_BITS_LENGTH);
    return BinaryToDecimal(versionBits);
}

Type parseType(const std::vector<bool> &binaryVector)
{
    std::vector<bool> typeIdBits(
        binaryVector.begin() + VERSION_BITS_LENGTH,
        binaryVector.begin() + VERSION_BITS_LENGTH + TYPE_ID_BITS_LENGTH);
    return (Type)BinaryToDecimal(typeIdBits);
}

std::vector<bool> parseLiteralData(const std::vector<bool> &binaryVector)
{
    return std::vector<bool>(
        binaryVector.begin() + VERSION_BITS_LENGTH + TYPE_ID_BITS_LENGTH,
        binaryVector.end());
}

unsigned int parseSubpacketsLength(const std::vector<bool> &binaryVector)
{
    return BinaryToDecimal(
        std::vector<bool>(binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1,
                          binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + SUBPACKETS_LENGTH_BITS_LENGTH));
}

unsigned int parseNumberOfSubpackets(const std::vector<bool> &binaryVector)
{
    return BinaryToDecimal(
        std::vector<bool>(binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1,
                          binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + NUMBER_OF_SUBPACKETS_BITS_LENGTH));
}

std::vector<bool> parseOperatorData(const std::vector<bool> &binaryVector, unsigned int length, LengthType lengthType)
{
    std::vector<bool> data;
    switch (lengthType)
    {
    case SubpacketsLength:
        data = std::vector<bool>(
            binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + SUBPACKETS_LENGTH_BITS_LENGTH,
            binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + SUBPACKETS_LENGTH_BITS_LENGTH + length);
        break;
    case NumberOfSubpackets:
        data = std::vector<bool>(
            binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + NUMBER_OF_SUBPACKETS_BITS_LENGTH,
            binaryVector.end());
        break;
    }
    return data;
}

std::vector<Packet> parseSubpackets(const std::vector<bool> binaryVector, const unsigned int length, const LengthType lengthType)
{
    std::vector<Packet> subpackets;
    unsigned int subpacketsLength{0};
    unsigned int numberOfSubpackets{0};

    std::vector<bool> packetData{findPacketData(binaryVector)};
    std::vector<bool> remainingData(binaryVector.begin() + packetData.size(), binaryVector.end());

    subpackets.push_back(Packet(packetData));
    subpacketsLength += packetData.size();
    numberOfSubpackets += 1;

    std::vector<Packet> remainingSubpackets;
    switch (lengthType)
    {
    case SubpacketsLength:
        if (subpacketsLength < length)
        {
            remainingSubpackets = parseSubpackets(remainingData, length - subpacketsLength, lengthType);
        }
        break;
    case NumberOfSubpackets:
        if (numberOfSubpackets < length)
        {
            remainingSubpackets = parseSubpackets(remainingData, length - numberOfSubpackets, lengthType);
        }
        break;
    }
    for (Packet p : remainingSubpackets)
        subpackets.push_back(p);

    return subpackets;
}

std::vector<bool> findPacketData(const std::vector<bool> binaryVector)
{
    Type type{parseType(binaryVector)};

    std::vector<bool> packetData;

    for (auto i{binaryVector.begin()}; i < binaryVector.begin() + VERSION_BITS_LENGTH + TYPE_ID_BITS_LENGTH; i++)
    {
        packetData.push_back(*i);
    }

    if (type == Literal)
    {
        std::vector<bool> data{parseLiteralData(binaryVector)};

        bool packetEnded{false};
        size_t i{0};
        while (!packetEnded)
        {
            for (size_t j{i}; j < i + LITERAL_CHUNK_SIZE; j++)
                packetData.push_back(data[j]);

            if (data[i] == 0)
                packetEnded = true;

            i += LITERAL_CHUNK_SIZE;
        }
    }
    else
    {
        LengthType lengthType{(LengthType)binaryVector[LENGTH_TYPE_ID_BIT]};
        packetData.push_back(binaryVector[LENGTH_TYPE_ID_BIT]);
        switch (lengthType)
        {
        case SubpacketsLength:
        {
            unsigned int subpacketsLength{parseSubpacketsLength(binaryVector)};
            for (
                auto i{binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1};
                i < binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + SUBPACKETS_LENGTH_BITS_LENGTH + subpacketsLength;
                i++)
            {
                packetData.push_back(*i);
            }
            break;
        }
        case NumberOfSubpackets:
        {
            unsigned int subpacketsFound{0};
            unsigned int numberOfSubpackets{parseNumberOfSubpackets(binaryVector)};
            for (
                auto i{binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1};
                i < binaryVector.begin() + LENGTH_TYPE_ID_BIT + 1 + NUMBER_OF_SUBPACKETS_BITS_LENGTH;
                i++)
            {
                packetData.push_back(*i);
            }

            size_t index{LENGTH_TYPE_ID_BIT + 1 + NUMBER_OF_SUBPACKETS_BITS_LENGTH};
            while (subpacketsFound < numberOfSubpackets)
            {
                std::vector<bool> remainingData(binaryVector.begin() + index, binaryVector.end());
                std::vector<bool> remainingPacketData{findPacketData(remainingData)};
                for (bool b : remainingPacketData)
                {
                    packetData.push_back(b);
                }
                subpacketsFound += 1;
                index += remainingPacketData.size();
            }
            break;
        }
        }
    }

    return packetData;
}