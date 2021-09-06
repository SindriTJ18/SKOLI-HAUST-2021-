#include "digital_in.h"
#include <avr/io.h>

Digital_in::Digital_in(int pinNumber, char port)
{
    pinMask = 1 << pinNumber;
    portChar = port;

}

// Enables selected pin on PORTB as input and pulls it up.
void Digital_in::init()
{
    switch(portChar){
        case 'B':
            DDRB |= pinMask;
            PORTB |= pinMask;
            break;
        case 'C':
            DDRC |= pinMask;
            PORTC |= pinMask;
            break;
        case 'D':
            DDRD |= pinMask;
            PORTD |= pinMask;
            break;
    }
}

bool Digital_in::is_hi()
{
    if(PINB && pinMask)
    {
        return true;
    }
    return false;
}

bool Digital_in::is_lo()
{
    if(PINB && pinMask)
    {
        return false;
    }
    return true;
}