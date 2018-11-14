#include <stdio.h>
#define ЯКЩО if
#define ІНАКШЕ else
#define ТО {
#define КІНЕЦЬ }


int main()
{
    int i;
    printf("Input i: ");
    scanf("%i", &i);

    ЯКЩО(i == 1) ТО
        printf("Hello World\n");
    КІНЕЦЬ

    ІНАКШЕ ЯКЩО(i == 0) ТО
        printf("Goodbye\n");
    КІНЕЦЬ

    ІНАКШЕ ТО
        printf("blablabla\n");
    КІНЕЦЬ


    return 0;
}