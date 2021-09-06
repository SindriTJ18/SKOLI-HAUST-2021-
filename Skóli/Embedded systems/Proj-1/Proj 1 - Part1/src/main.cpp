#include "encoder.h"
#include "arduino.h"
#include "digital_out.h"
#include <avr/io.h>
#include <avr/delay.h>
#include <string.h>
                                                                                                                                                                                                              
void setup(){
  Serial.begin(57600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Native USB only
  }
}
int main(){
  Encoder encoder;
  // OUTPUT PIN TO SHOW PULSE SENSING
  Digital_out outputPin(4);
  // INIT OUTPUT PIN AND POSITION INTEGER
  outputPin.init();
  int pos;
  //DDRB |= (1 << 5);
  uint16_t counter = 0;
  while(true){
    counter++;
    //PORTB |= (0 << 5);
    // READS FROM ENCODER AND INCREMENTS FOR WHICH DIRECTION
    pos = encoder.count();
    // OUPTUT PIN, SIGNALS THAT ENCODER POS IS TRACKING CLOCKWISE
    float deg = pos/700.0 * 360;
    String filler = "  Deg:  ";
    if(counter == 10000){
      Serial.print(pos);
      Serial.print(filler);
      Serial.println(deg);
      _delay_us(100);
      counter = 0;
    }
  }
  return 0;
}