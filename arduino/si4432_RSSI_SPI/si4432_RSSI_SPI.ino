#include <SPI.h>
#include "si4432.h"
//#include "Si4432Lite.h"

// 🖋️ Піни
const int PIN_CS1 = 2;   // nSEL для Si4432 #1
const int PIN_CS2 = 10;  // nSEL для Si4432 #2
const int PIN_SDN1 = 7;   //  SDN
const int PIN_SDN2 = 8;   //  SDN

// 📡 Два екземпляри Si4432
Si4432 radio1(PIN_CS1, PIN_SDN1, 3); 
Si4432 radio2(PIN_CS2, PIN_SDN2, 3); 

void setup() {
  Serial.begin(115200);
  delay(500);

  pinMode(PIN_CS1, OUTPUT);
  pinMode(PIN_CS2, OUTPUT);
  pinMode(PIN_SDN, OUTPUT);

  digitalWrite(PIN_SDN, LOW); // Увімкнути обидва чіпи
  delay(50);

  digitalWrite(PIN_CS1, HIGH); // Деактивувати обидва nSEL
  digitalWrite(PIN_CS2, HIGH);

  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));

  initRadio(radio1, PIN_CS1, "1");
  delay(50);
  initRadio(radio2, PIN_CS2, "2");
  delay(50);

  Serial.println("✅ Два Si4432 готові");
}

void loop() {
  uint8_t rssi1 = readRegister(PIN_CS1, 0x26);
  uint8_t rssi2 = readRegister(PIN_CS2, 0x26);

  Serial.print("📡 RSSI1: 0x");
  printHex(rssi1);
  Serial.print(" 📡 RSSI2: 0x");
  printHex(rssi2);
  Serial.println();

  delay(100);
}

// 🛠️ Ініціалізація Si4432
void initRadio(Si4432 &radio, int csPin, const char *label) {
  digitalWrite(csPin, LOW);
  if (!radio.init()) {
    Serial.print(label);
    Serial.println(" Si4432 not installed");
    while (1);
  }
  radio.setBaudRate(70);
  radio.setFrequency(433);
  radio.readAll();
  radio.startListening();
  digitalWrite(csPin, HIGH);
}

// 📖 Читання регістра
uint8_t readRegister(int csPin, uint8_t reg) {
  digitalWrite(csPin, LOW);
  SPI.transfer(reg & 0x7F);
  uint8_t val = SPI.transfer(0x00);
  digitalWrite(csPin, HIGH);
  return val;
}

// 🖨️ Красивий вивід HEX з ведучим нулем
void printHex(uint8_t value) {
  if (value < 0x10) Serial.print("0");
  Serial.print(value, HEX);
}
