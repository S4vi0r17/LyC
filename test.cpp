#include <iostream>
#include <string>
#include <cctype>

// Tipos de tokens posibles
enum class TokenType {
    INTEGER,
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
    END_OF_INPUT
};

class Token {
public:
    TokenType type;
    std::string value;
};
