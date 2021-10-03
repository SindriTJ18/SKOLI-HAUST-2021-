# SKOLI-HAUST-2021-
#include "Arduino.h"

void setup()
{
  Serial.begin(9600);
}

class Context;

class State
{
protected:
  Context *context_;

public:
  virtual ~State()
  {
  }

  void set_context(Context *context)
  {
    this->context_ = context;
  }

  virtual void Go() = 0;
  virtual void Stop() = 0;
  virtual void Entry() = 0;
};

class Context
{
private:
  State *state_;

public:
  Context(State *state) : state_(nullptr)
  {
    this->TransitionTo(state);
  }
  ~Context()
  {
    delete state_;
  }
  void TransitionTo(State *state)
  {
    Serial.println("Context: Transition to ");
    if (this->state_ != nullptr)
      delete this->state_;
    this->state_ = state;
    this->state_->set_context(this);
    this->state_->Entry();
  }
  void Request1()
  {
    this->state_->Go();
  }
  void Request2()
  {
    this->state_->Stop();
  }
};

class Green : public State
{
public:
  void Go() override;

  void Stop() override
  {
    Serial.println("Green handles stop request.");
  }
  void Entry() override
  {
    Serial.println("Green handles Entry request.");
  }
};
class Red : public State
{
public:
  void Go() override
  {
    Serial.println("Red handles go request.");
    Serial.println("Red wants to change the state of the context to green");
    this->context_->TransitionTo(new Green);
  }
  void Stop() override
  {
    Serial.println("Red handles stop request.");
  }
  void Entry() override
  {
    Serial.println("Red handles Entry request.");
  }
};

class Yellow : public State
{
public:
  void Go() override
  {
    Serial.println("Yellow handles go request");
  }

  void Stop() override
  {
    Serial.println("Yellow handles stop request");
  }
  void Entry() override
  {
    for (int i=0; i<5; i++){
      Serial.print("Timeout yellow: ");
      Serial.println(5 - i);
      delay(1000);
    }
    this->context_->TransitionTo(new Red);
  }
};


void Green::Go()
{
  {
    Serial.println("Green handles go request.");
    Serial.println("Green wants to change the state of the context.");

    this->context_->TransitionTo(new Yellow);
  }
}


void ClientCode()
{
  Context *context = new Context(new Green);
  context->Request1();
  context->Request2();
  delete context;
}

void loop()
{
  ClientCode();
  Serial.println("-----------------------------------------------------------");
  delay(5000);
}
