#include "digital_out.h"
#include "digital_in.h"
#include <stdint.h>
#include <avr/io.h>
#include <util/delay.h>

int main()
{
  // CREATE OBJECTS FOR LED AND BUTTON WITH PIN NUMBER
  Digital_out LED(5);
  Digital_in BUTTON(1);
  // INITIALIZE REGISTER FOR LED
  LED.init();
  BUTTON.init();
  // PERMALOOP
  while (1)
  {
    // BUTTON ON - LED OFF
    while (BUTTON.is_hi() == true)
    {
      LED.set_lo();
    }
    // BUTTON OFF - LED TOGGLE
    LED.toggle();
    _delay_ms(100);
  }
  return 0;
}