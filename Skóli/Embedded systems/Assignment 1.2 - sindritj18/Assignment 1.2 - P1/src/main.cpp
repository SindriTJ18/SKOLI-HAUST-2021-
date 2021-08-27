#include <stdint.h>
#include <avr/io.h>
#include <util/delay.h>

// LEFT SHIFT PIN 5
const int LED_PIN = (1 << 5);
int main()
{
  DDRB |= LED_PIN; // PIN DIRECTION - OUTPUT
  while (1)
  {
    _delay_ms(100);
    PORTB ^= LED_PIN; // XOR = TOGGLE PIN STATE
  }
  return 0;
}
