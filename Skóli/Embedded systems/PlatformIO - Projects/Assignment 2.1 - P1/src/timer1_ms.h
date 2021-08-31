#ifndef TIMER1_MS_H

#define TIMER1_MS_H

class Timer1_ms
{
public:
    Timer1_ms(int ms);
    void init();

private:
    int compare;
};

#endif