#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char hexToDecimal(char);

int main(void) {
    int decimal;
    char hex[7];
    int count;
    int result = 0;
    int end;

    scanf("%s", hex);
    count = strlen(hex);
    end = count - 1;

    for (int i = end; i >= 0; i--) { // 시작 글자(맨 뒤)의 인덱스부터 앞으로 탐색 [0, 1, 2, ..., end]
        decimal = hexToDecimal(hex[i]);
        result += (decimal * pow(16, end - i));
    }

    printf("%d", result);

    return 0;
}

char hexToDecimal(char ch) {
    int decimal;

    if ('0' <= ch && ch <= '9') {
        decimal = ch - '0';
        return decimal;
    } else {
        switch (ch) {
            case 'A': decimal = 10; break;
            case 'B': decimal = 11; break; 
            case 'C': decimal = 12; break;
            case 'D': decimal = 13; break;
            case 'E': decimal = 14; break;
            case 'F': decimal = 15; break;
        }
        return decimal;
    }
    
}

