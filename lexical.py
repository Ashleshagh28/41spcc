# Simple Lexical Analyzer
keywords = ["int", "float", "if", "else", "while", "return"]
operators = ["=", "+", "-", "*", "/", ">"]
symbols = ["(", ")", "{", "}"]
punctuations = [":", ",", ";"]

code = """int a = 10;
float b = 5;
if (a > b)
{
a = a + b;
}
return 0;
"""

# Separate operators, symbols, and punctuations
for item in operators + symbols + punctuations:
    code = code.replace(item, f" {item} ")

tokens = code.split()

print("Lexeme\t\tToken")

token_count = 0

for token in tokens:
    token_count += 1

    if token in keywords:
        print(token, "\t\tKEYWORD")
    elif token in operators:
        print(token, "\t\tOPERATOR")
    elif token in symbols:
        print(token, "\t\tSYMBOL")
    elif token in punctuations:
        print(token, "\t\tPUNCTUATION")
    elif token.isdigit():
        print(token, "\t\tCONSTANT")
    else:
        print(token, "\t\tIDENTIFIER")
print("\nTotal number of tokens =", token_count)

