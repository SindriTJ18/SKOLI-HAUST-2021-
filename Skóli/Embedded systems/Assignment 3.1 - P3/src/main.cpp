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
  ~Green()
  {
    Serial.println("I AM AMAZING");
  }

  void Go() override;

  void Stop() override
  {
    Serial.println("Green handles request2.");
  }
};

class Yellow : public State
{
public:
  void Go() override
  {
    Serial.println("Yellow handles request2.");
  }

  void Stop() override
  {
    Serial.println("Yellow handles request2.");
  }
};

class Red : public State
{
public:
  void Go() override
  {
    Serial.println("Red handles request1.");
    Serial.println("Red wants to change the state of the context.");
    this->context_->TransitionTo(new Green);
  }
  void Stop() override
  {
    Serial.println("Red handles request2.");
  }
};

void Green::Go()
{
  {
    Serial.println("Green handles request1.");
    Serial.println("Green wants to change the state of the context.");

    this->context_->TransitionTo(new Red);
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