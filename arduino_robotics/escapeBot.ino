#include <Servo.h>
Servo servoLeft;  //declares left servo
Servo servoRight;  //declares right servo
int red = 13; 

void setup() {
  pinMode(4, INPUT);  //right whisker to input 4
  pinMode(6, INPUT); //left whisker to input 6
  pinMode(red, OUTPUT);
  servoLeft.attach(10); //right
  servoRight.attach(11); //left
   servoLeft.writeMicroseconds(1500);         // Left wheel counterclockwise  
  servoRight.writeMicroseconds(1500); 
  digitalWrite(13,LOW);  
}

void loop() {
  // put your main code here, to run repeatedly:
  byte wLeft = digitalRead(6); // copy left result to wLeft
  byte wRight = digitalRead(4); //copy right result to wRight
  if ((wLeft == 0) && (wRight == 0)) 
  {  
    Serial.print("back");
    digitalWrite(13,HIGH);
    backward(1000);   //back up for one sec
    turnLeft(800);   //turn left 120 deg
  }
   else if (wLeft == 0) 
   {
    Serial.print("left");
    backward(1000);
    turnRight(400);  //turn right 60 deg
   }
    else if (wRight == 0) 
    {
      Serial.print("right");
      backward(1000);
      turnLeft(400);
    }
    else
    {
      Serial.print("forward");
      digitalWrite(13,LOW);
      forward(5);
    }
}

//1500 means not moving
//1300 = CLOCKWISE = LEFT
//1700 = COUNTER = RIGHT

void forward(int time)                       // Forward function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise  
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnLeft(int time)                      // Left turn function
{
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnRight(int time)                     // Right turn function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}

void backward(int time)                      // Backward function
{
  pinMode(red, OUTPUT);
  pinMode(red, HIGH);
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}
