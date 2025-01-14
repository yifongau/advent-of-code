#include <stdio.h>

main()
{
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;
  
  printf("%4s\t%6s\t\t", "FAHR", "CELSIUS");
  printf("%6s\t%4s\n", "CELSIUS", "FAHR");

  while (fahr <= upper) {
    celsius = (5.0/9.0) * (fahr-32.0);
    printf("%4.0f\t%7.1f\t\t", fahr, celsius);
    printf("%7.1f\t%4.0f\n", celsius, fahr);
    fahr = fahr + step;
  }


}


