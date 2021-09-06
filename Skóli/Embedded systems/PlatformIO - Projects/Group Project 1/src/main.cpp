#include <Arduino.h>
#include "digital_in.h"
#include "digital_out.h"

Digital_in C1(1);
Digital_in C2(3);
Digital_out LED(5);
Digital_out indicator(4);
int pos = 0;
int main()
{
  C1.init();
  C2.init();
  indicator.init();
  LED.init();

  bool stateInit = C1.is_hi();
  while (1)
  {
    if (stateInit == false && C1.is_hi()){
      indicator.set_hi();
      _delay_us(10);
      if(C2.is_hi()){
        pos++;
      }
      else{
        pos--;
      }
      indicator.set_lo();
    }
    stateInit = C1.is_hi();
    if (abs(pos)>700){
      LED.toggle();
      pos = 0;
    }
  }
}
