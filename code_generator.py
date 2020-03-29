#include <stdbool.h> 
#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 

// Returns 'true' if the character is a DELIMITER. 
bool isDelimiter(char ch) { 
	if (ch == ' ' || 
		ch == ',' || ch == '(' || ch == ')' || 
		ch == '[' || ch == ']' || ch == '{' || ch == '}') 
		return (true); 
	return (false); 
} 

// Returns 'true' if the character is a PLUS. 
bool isPlus(char ch) { 
	if (ch == '+' ) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the character is a MINUS. 
bool isMinus(char ch) { 
	if (ch == '-' ) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the character is a MULT. 
bool isMult(char ch) { 
	if (ch == '*' ) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the character is a DIV. 
bool isDiv(char ch) { 
	if (ch == '/' ) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the character is ASSIGN. 
bool isAssing(char ch) { 
	if (ch == '=' ) 
		return (true); 
	return (false); 
}

// Returns 'true' if the character is FLOAT. 
bool isfloat(char ch) { 
	if (ch == 'f' ) 
		return (true); 
	return (false); 
}

// Returns 'true' if the character is INT. 
bool isInt(char ch) { 
	if (ch == 'i' ) 
		return (true); 
	return (false); 
}

// Returns 'true' if the character is PRINT. 
bool isPrint(char ch) { 
	if (ch == 'p' ) 
		return (true); 
	return (false); 
}

// Returns 'true' if the character is END. 
bool isEND(char ch) { 
	if (ch == ';' ) 
		return (true); 
	return (false); 
}

// Returns 'true' if the character is an OPERATOR. 
bool isOperator(char ch) { 
	if (ch == '>' || ch == '<' || ) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the string is a KEYWORD. 
bool isKeyword(char* str) { 
	if (!strcmp(str, "if") || !strcmp(str, "else") || 
		!strcmp(str, "while") || !strcmp(str, "do") || 
		!strcmp(str, "break") || 
		!strcmp(str, "continue") || !strcmp(str, "int") 
		|| !strcmp(str, "double") || !strcmp(str, "float") 
		|| !strcmp(str, "return") || !strcmp(str, "char") 
		|| !strcmp(str, "case") || !strcmp(str, "char") 
		|| !strcmp(str, "sizeof") || !strcmp(str, "long") 
		|| !strcmp(str, "short") || !strcmp(str, "typedef") 
		|| !strcmp(str, "switch") || !strcmp(str, "unsigned") 
		|| !strcmp(str, "void") || !strcmp(str, "static") 
		|| !strcmp(str, "struct") || !strcmp(str, "goto")) 
		return (true); 
	return (false); 
} 

// Returns 'true' if the string is an INTEGER. 
bool isInteger(char* str) { 
	int i, len = strlen(str); 

	if (len == 0) 
		return (false); 
	for (i = 0; i < len; i++) { 
		if (str[i] != '0' && str[i] != '1' && str[i] != '2'
			&& str[i] != '3' && str[i] != '4' && str[i] != '5'
			&& str[i] != '6' && str[i] != '7' && str[i] != '8'
			&& str[i] != '9' || (str[i] == '-' && i > 0)) 
			return (false); 
	} 
	return (true); 
} 

// Extracts the SUBSTRING. 
char* subString(char* str, int left, int right) { 
	int i; 
	char* subStr = (char*)malloc( 
				sizeof(char) * (right - left + 2)); 

	for (i = left; i <= right; i++) 
		subStr[i - left] = str[i]; 
	subStr[right - left + 1] = '\0'; 
	return (subStr); 
} 

// Parsing the input STRING. 
void parse(char* str) { 
	int left = 0, right = 0; 
	int len = strlen(str); 

	while (right <= len && left <= right) { 
		if (isDelimiter(str[right]) == false) 
			right++; 

		if (isDelimiter(str[right]) == true && left == right) { 
			if (isOperator(str[right]) == true) 
				printf("'%c' IS AN OPERATOR\n", str[right]); 

			right++; 
			left = right; 
		} else if (isDelimiter(str[right]) == true && left != right 
				|| (right == len && left != right)) { 
			char* subStr = subString(str, left, right - 1); 

			if (isKeyword(subStr) == true) 
				printf("keyword ", subStr); 

			else if (isInteger(subStr) == true) 
				printf("inum ", subStr); 
            
            else if (isAssing(subStr) == true) 
				printf("assing ", subStr);

            else if (isPlus(subStr) == true) 
				printf("plus ", subStr);

            else if (isMinus(subStr) == true) 
				printf("minus ", subStr);

            else if (isMult(subStr) == true) 
				printf("mult ", subStr);

            else if (isDiv(subStr) == true) 
				printf("div ", subStr);

            else if (isfloat(subStr) == true) 
				printf("floatdcl ", subStr);

            else if (isInt(subStr) == true) 
				printf("intdcl ", subStr);
            
            else if (isPrint(subStr) == true) 
				printf("print ", subStr);

            else if (isEND(subStr) == true) 
				printf(" \n", subStr);

            else(){
                printf("id", subStrs);
            }

		} 
	} 
	return; 
} 

// DRIVER FUNCTION 
int main() 
{ 
	// maximum legth of string is 100 here 
	char str[100] = "f b; i a; a = 5; p b;"; 

	parse(str); // calling the parse function 

	return (0); 
} 
