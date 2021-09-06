#include "encoder.h"
#include "digital_out.h"
#include <avr/io.h>
#include <avr/delay.h>

int main(){
  Encoder encoder;
  Digital_out outputPin(4);
  outputPin.init();
  int pos = 0;
  DDRB |= (1 << 5);
  while(true){
    PORTB |= (0 << 5);
    encoder.count(pos);
    /*
    if(pos != 0){
      outputPin.set_hi();
      _delay_us(20);
      pos = 0;
      outputPin.set_lo();
    }
    */
  }
  return 0;
}