#include "digital_out.h"
#include <stdint.h>
#include <avr/io.h>
#include <util/delay.h>

int main()
{
  // CREATE OBJECTS FOR LED AND BUTTON WITH PIN NUMBER
  Digital_out LED(5);
  // INITIALIZE REGISTER FOR LED
  LED.init();
  // PERMALOOP
  while (1)
  {
    LED.toggle();
    _delay_ms(100);
  }
  return 0;
}