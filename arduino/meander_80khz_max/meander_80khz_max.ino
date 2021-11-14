/*
  up to 80 Khz meander generator

 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int pin = 8;

//unsigned long frequency = 1000+20;  //1000hz
unsigned long frequency = 2000;  //1000hz
//unsigned long frequency = 10000+1150;  //10 khz

unsigned long Second = 1000000/2; 
unsigned long processing_time = 0; //microseconds

unsigned long time = Second/frequency-processing_time ;

//int time = 1;  //80khz


// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(pin, OUTPUT);     
  
  Serial.begin(9600);
}



void f1()
{
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delayMicroseconds(time);
  //delay(1);               // wait for a second
  
  digitalWrite(pin, LOW);    // turn the LED off by making the voltage LOW
  delayMicroseconds(time);
  //delay(1);               // wait for a second
}

// the loop routine runs over and over again forever:
void loop() {
  Serial.println( time);
  
  while(1)
  {
  f1();
  }
}
