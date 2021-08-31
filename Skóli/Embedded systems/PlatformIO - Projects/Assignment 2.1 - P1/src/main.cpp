#include "timer1_ms.h"
#include "digital_in.h"
#include "digital_out.h"
#include <avr/io.h>
#include <avr/interrupt.h>

// LED AND TIMER TIME
Digital_out LED(5);
// INPUT ARGUMENT IS MILLISECONDS
Timer1_ms TIME(1000);
int main()
{ // INIT LED AND TIMER
  LED.init();
  TIME.init();
  // PERMALOOP
  while (1)
  {
  }
  return 0;
}

// COMPARISON VECTOR INTERRUPT (LED STATE TOGGLE)
ISR(TIMER1_COMPA_vect)
{
  LED.toggle();
}