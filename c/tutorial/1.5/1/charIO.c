#include <stdio.h>

/* copy input to output */

int main(void)
{
  int c;
  
  while ((c = getchar()) != EOF) {
    putchar(c);
  }
  
  return 0;
}
