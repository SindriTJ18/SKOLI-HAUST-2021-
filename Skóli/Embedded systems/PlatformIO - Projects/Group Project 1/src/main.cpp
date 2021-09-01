#include <Arduino.h>
#include "digital_in.h"
#include "digital_out.h"

Digital_in C1(1);
Digital_in C2(2);
Digital_out LED(5);
int cnt = 0;
int main()
{
  C1.init();
  C2.init();
  LED.init();
  while (1)
  {
    if (C1.is_hi() == true)
    {
      cnt++;
    }
    if (cnt > 1400)
    {
      LED.set_hi();
    }
  }
}
