#include <Arduino.h>

char command;
String req_state;
// STARTS IN RED LIGHT
String current_state = "red";

void setup()
{
  Serial.begin(9600);
}
void timeout_yellow()
{
  for (int i = 0; i != 5; i++)
  {
    Serial.print("Yellow state timeout: ");
    Serial.println(5 - i);
    delay(1000);
  }
  current_state = "red";
  Serial.println("New state is: " + current_state);
}
void check_state()
{
  if (req_state == current_state)
  {
    Serial.println("The state is alredy " + current_state);
  }
  if (req_state != current_state)
  {
    Serial.println("Source state is: " + current_state + ", Requested state is: " + req_state);
    if (current_state == "green")
    {
      current_state = "yellow";
      Serial.println("New state is: " + current_state);
      timeout_yellow();
    }
    else
    {
      current_state = req_state;
      Serial.println("New state is: " + current_state);
    }
  }
}
void loop()
{
  if (Serial.available() > 0)
  {
    command = Serial.read();
    Serial.print("I received: ");
    Serial.print(command);
    switch (command)
    {
    case 'g':
      Serial.println(" (GO command)");
      req_state = "green";
      check_state();
      break;
    case 's':
      Serial.println(" (STOP command)");
      req_state = "red";
      check_state();
      break;
    }
  }
}
