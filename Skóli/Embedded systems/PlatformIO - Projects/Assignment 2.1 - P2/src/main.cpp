#include "timer1_ms.h"
#include "digital_in.h"
#include "digital_out.h"
#include <avr/io.h>
#include <avr/interrupt.h>

// INITIALIZE CONSTRUCTORS (LED-PIN & MILLISECS)
Digital_out LED(5);
Timer1_ms TIME(20);
int main()
{
  // INIT LED AND TIMER
  LED.init();
  TIME.init();
  // SET DUTY CYCLE (%)
  TIME.duty(20);
  // PERMALOOP
  while (1)
  {
  }
  return 0;
}

// INTERRUPTS FOR DUTY CYCLE
ISR(TIMER1_COMPA_vect)
{
  LED.set_lo();
}
ISR(TIMER1_COMPB_vect)
{
  LED.set_hi();
}