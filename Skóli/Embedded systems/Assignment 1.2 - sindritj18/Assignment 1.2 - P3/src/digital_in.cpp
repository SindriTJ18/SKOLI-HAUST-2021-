#include "digital_in.h"
#include <stdint.h>
#include <avr/io.h>
#include <util/delay.h>

Digital_in::Digital_in(int pin)
{
    pinMask = 1 << pin;
}

void Digital_in::init()
{
    DDRB &= ~pinMask;
    PORTB |= pinMask;
}

bool Digital_in::is_hi()
{
    bool isHi = PINB & pinMask;
    return isHi;
}

bool Digital_in::is_lo()
{
    bool isLo = PINB & ~pinMask;
    return isLo;
}
