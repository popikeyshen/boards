
const int chipSelectPin = 8;


#include <SPI.h>

void setup() {
  Serial.begin(9600);
  
  // start the SPI library:
  SPI.begin();
  
  pinMode(chipSelectPin, OUTPUT);
    
  delay(100);
}


void loop()
{
 digitalWrite(chipSelectPin, LOW);

unsigned char highByteA = SPI.transfer(0x00);  // Read High Byte
unsigned char lowByteA = SPI.transfer(0x00);  // Read Low Byte 
unsigned int RESval = (highByteA << 8 ) | (lowByteA);

 digitalWrite(chipSelectPin, HIGH);

Serial.println(RESval);

}
