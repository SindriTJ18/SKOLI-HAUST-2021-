#include "encoder.h"
#include "digital_out.h"
#include <avr/io.h>

#include <avr/interrupt.h>
bool ENCODERFLAG = false;
Digital_in dirPin(0, 'B');



Encoder::Encoder(){
    Digital_in pin1(2, 'D');
    EICRA |= (1 << ISC01);   //Sense interrupt on pin0 change rising edge
    EIMSK |= (1 << INT0);                   //Enable interrupt on PCINT0
    sei();                                  //Enable interrupts
}

void Encoder::count(int &counter){
    if(ENCODERFLAG){
        if (dirPin.is_hi()){
            counter++;
        }
        else {
            counter--;
        }
    }
    ENCODERFLAG = false;
}

ISR(INT0_vect){
    PORTB |= (1 << 4);
    ENCODERFLAG = true;
    PORTB &= ~(1 << 4);
}