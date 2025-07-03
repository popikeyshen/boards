#include <SPI.h>

const int PIN_CS  = 10;  // nSEL
const int PIN_SDN = 7;   // SDN

void setup() {
   delay(1000);
  Serial.begin(115200);
  delay(1000);
  

  pinMode(PIN_CS, OUTPUT);
  pinMode(PIN_SDN, OUTPUT);
  digitalWrite(PIN_CS, HIGH);
  digitalWrite(PIN_SDN, LOW); // Увімкнути чіп
  delay(50);

  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));

  // Читання регістра 0x26
  uint8_t rssi = readRegister(0x26);
  Serial.print("RSSI: 0x");
  Serial.println(rssi, HEX);
}

void loop() {
  // Читання регістра 0x26
  uint8_t rssi = readRegister(0x26);
  Serial.print("RSSI: 0x");
  Serial.println(rssi, HEX);

    delay(100);
}

// Читання одного регістра з Si4432
uint8_t readRegister(uint8_t reg) {
  digitalWrite(PIN_CS, LOW);
  SPI.transfer(reg & 0x7F);  // Читання (MSB = 0)
  uint8_t val = SPI.transfer(0x00);
  digitalWrite(PIN_CS, HIGH);
  return val;
}
