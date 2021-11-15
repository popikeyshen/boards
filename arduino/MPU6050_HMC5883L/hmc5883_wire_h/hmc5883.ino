#include <Wire.h>

#define address 0x1E //I2C 7bit address of HMC5883

void setup(){

  Serial.begin(9600);
  Wire.begin();
  
  //Put the HMC5883 IC into the correct operating mode
  Wire.beginTransmission(address);
  Wire.write(0x02);
  Wire.write(0x00);
  Wire.endTransmission();
  
  /// 0x3C 0x01 0xA0   to set gain 5
  Wire.beginTransmission(address);
  Wire.write(0x3C);
  Wire.write(0x01);
  Wire.write(0xA0);
  Wire.endTransmission();
}

void loop(){

int x,y,z;

//begin reading data
Wire.beginTransmission(address);
Wire.write(0x03); //select register 3, X MSB register
Wire.endTransmission();

//Read data from each axis, 2 registers per axis
Wire.requestFrom(address, 6);
if(6<=Wire.available()){
    x = Wire.read()<<8; //X msb
    x |= Wire.read(); //X lsb
    z = Wire.read()<<8; //Z msb
    z |= Wire.read(); //Z lsb
    y = Wire.read()<<8; //Y msb
    y |= Wire.read(); //Y lsb
}

//Print out values of each axis
Serial.print(' ');
Serial.print(x);
Serial.print(' ');
Serial.print(y);
Serial.print(' ');
Serial.println(z);

delay(250);
}
