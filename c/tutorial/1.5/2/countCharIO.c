#include <stdio.h>

/* count characters in input */

int main(void)
{
  double nc;

  for (nc = 0; getchar() != EOF; ++nc)
    ;
  printf("%.0f\n", nc);
  
  return 0;
}
