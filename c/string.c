#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

static bool hasUniqueChars(const char* str)
{
    for (int i = 0; i < strlen(str); i++)
    {
        for (int j = 0; j < strlen(str); j++)
        {
            if (i == j)
            {
                continue;
            }
            else
            {
                if (str[i] == str[j])
                {
                    return false;
                }
            }
        }
    }

    return true;
}

static char* reverseString_Out(const char* str)
{
    char* ret = (char*) malloc(strlen(str) * sizeof(char));

    int i;
    for (i = 1; i < strlen(str) + 1; i++)
    {
        ret[i - 1] = str[strlen(str) - i];
    }

    ret[i] = '\0';

    return ret;
}

static void reverseString_In(char s[])
{
    int c, i, j;

    for (i = 0, j = strlen(s) - 1; i < j; i++, j--)
    {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

int main(void)
{
    assert(hasUniqueChars("banana") == false);
    assert(hasUniqueChars("ben") == true);

    char* result = reverseString_Out("ben");
    assert(strcmp(result, "neb") == 0);
    free(result);

    char test[] = "banana";
    reverseString_In(test);
    assert(strcmp(test, "ananab") == 0);

    printf("Passed!\r\n");

    return 0;
}
