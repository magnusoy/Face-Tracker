/**
     This is the camera controller for the Shelf-Bot.
*/

#include <PID_v1.h>
#include <Servo.h>

// Defining servos
Servo servoX;
Servo servoY;

// Constants representing the states in the state machine
const int S_INIT = 0;
const int S_SEARCHING = 1;
const int S_FOLLOWING = 2;
// A variable holding the current state
int currentState = S_INIT;

// Time for next timeout, in milliseconds
unsigned long nextTimeout = 0;

// Defining global variables for recieving data
boolean newData = false;
const byte numChars = 32;
char receivedChars[numChars]; // An array to store the received data

// Variables holding buttonvalues
const byte numCoordinates = 2;
int coordinates[numCoordinates] = {0, 0};

// PID Controller terms
double kp = 4.0; double ki = 0.0; double kd = 0.0;

// PID limitations
#define PID_OUTPUT_LOW 0
#define PID_OUTPUT_HIGH 180

// PID Controller X
double currentX = 0.0; double setX = 320.0; double outputX = 0.0;
PID pidX(&currentX, &setX, &outputX, kp, ki, kd, DIRECT);

// PID Controller Y
double currentY = 0.0; double setY = 240.0; double outputY = 0.0;
PID pidY(&currentY, &setY, &outputY, kp, ki, kd, DIRECT);

void setup() {
  // Start Serial for raspberry communication
  Serial.begin(9600);

  // Initialize servos
  servoX.attach(9);
  servoY.attach(6);

  // PID controller configurations
  pidX.SetMode(AUTOMATIC);
  pidY.SetMode(AUTOMATIC);

  pidX.SetSampleTime(50);
  pidY.SetSampleTime(50);

  pidX.SetOutputLimits(PID_OUTPUT_LOW, PID_OUTPUT_HIGH);
  pidY.SetOutputLimits(PID_OUTPUT_LOW, PID_OUTPUT_HIGH);
}

void loop() {
  readStringFromSerial();
  updateCoordinates();
  currentX = coordinates[0];
  currentY = coordinates[1];

  switch (currentState) {

    case S_INIT:
      if (currentX == 0) {
        int timeDelay = random(100, 600);
        startTimer(timeDelay);
        changeState(S_SEARCHING);
      }
      if ( currentX > 0) {
        changeState(S_FOLLOWING);
      }

      break;

    case S_SEARCHING:
      if ( timerHasExpired()) {
        moveServoRandomly(servoX, outputX);
        moveServoRandomly(servoY, outputY);
        changeState(S_INIT);
      }

      if (currentX > 0) {
        changeState(S_FOLLOWING);
      }

      break;

    case S_FOLLOWING:
      boolean computed = pidX.Compute();
      pidY.Compute();
      if (computed) {
        servoX.write(outputX);
        servoY.write(outputY);
      }

      if (currentX == 0) {
        changeState(S_SEARCHING);
      }

      break;
  }
}

/**
  Reads a string from Serial Monitor.
*/
void readStringFromSerial() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;

  while ((Serial.available() > 0) && (!newData)) {
    rc = Serial.read();

    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    } else {
      receivedChars[ndx] = '\0'; // Terminate the string
      ndx = 0;
      newData = true;
    }
  }
}

/**
  Fetches the value from a substring,
  wich is seperated with a given symbol.
  @param data your String to be seperated
  @param seperator your symbol to seperate by
  @param index where your value is located
  @return substring before seperator
*/
String getValueFromSerial(String data, char separator, int index) {
  int found = 0;
  int strIndex[] = { 0, -1 };
  int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
      found++;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  strIndex[0] = strIndex[1] + 1;
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

/**
  Reads from the recived char array and
  fills an array with the stored values.
*/
void updateCoordinates() {
  if (newData) {
    coordinates[0] = getValueFromSerial(receivedChars, ",", 0).toInt();
    coordinates[1] = getValueFromSerial(receivedChars, ",", 1).toInt();
  }
  newData = false;
}

/**
   Change the state of the statemachine to the new state
   given by the parameter newState

   @param newState The new state to set the statemachine to
*/
void changeState(int newState) {
  currentState = newState;
}

/**
  Move the servo to a random position.

  @servo The Servo object
  @offset The offset from where the movement start from
*/
void moveServoRandomly(Servo servo, double offset) {
  int result = offset + random(-50, 50);
  result = constrain(result, 0, 180);
  servo.write(result);
}

/**
   Starts the timer and set the timer to expire after the
   number of milliseconds given by the parameter duration.

   @param duration The number of milliseconds until the timer expires.
*/
void startTimer(unsigned long duration) {
  nextTimeout = millis() + duration;
}


/**
   Checks if the timer has expired. If the timer has expired,
   true is returned. If the timer has not yet expired,
   false is returned.

   @return true if timer has expired, false if not
*/
boolean timerHasExpired() {
  boolean hasExpired = false;
  if (millis() > nextTimeout) {
    hasExpired = true;
  }
  return hasExpired;
}
