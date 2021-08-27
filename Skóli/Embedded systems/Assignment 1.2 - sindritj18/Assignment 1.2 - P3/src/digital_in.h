#define DIGITAL_IN
#include <stdint.h>

class Digital_in
{
public:
    Digital_in(int pin);
    void init();
    bool is_hi();
    bool is_lo();

private:
    uint8_t pinMask;
};