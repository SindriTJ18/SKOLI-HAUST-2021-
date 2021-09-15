#include "encoder.h"
#include "digital_out.h"
#include <avr/io.h>
#include <avr/interrupt.h>

int ENCODER_COUNT = 0;
Digital_in dirPin(0, 'B');

Encoder::Encoder()
{
    Digital_in pin1(2, 'D');
    EICRA |= (1 << ISC01); //Sense interrupt on pin0 change rising edge (NOT SAME AS IN DATASHEET)
    EIMSK |= (1 << INT0);  //Enable interrupt on PCINT0
    sei();                 //Enable interrupts
}

int Encoder::count()
{
    return ENCODER_COUNT;
}

ISR(INT0_vect)
{
    if (dirPin.is_hi())
    {
        ENCODER_COUNT++;
    }
    else
    {
        ENCODER_COUNT--;
    }
}