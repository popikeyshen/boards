#include <SPI.h>

#define NSS_PIN   10  // Chip Select (NSS)
#define RESET_PIN 9   // Reset pin

void resetSX1276() {
  digitalWrite(RESET_PIN, LOW);
  delay(10);
  digitalWrite(RESET_PIN, HIGH);
  delay(10);
}

uint8_t readRegister(uint8_t addr) {
  digitalWrite(NSS_PIN, LOW);
  SPI.transfer(addr & 0x7F); // Read bit = 0
  uint8_t value = SPI.transfer(0x00);
  digitalWrite(NSS_PIN, HIGH);
  return value;
}


void writeRegister(uint8_t addr, uint8_t value) {
  digitalWrite(NSS_PIN, LOW);
  SPI.transfer(addr | 0x80);
  SPI.transfer(value);
  digitalWrite(NSS_PIN, HIGH);
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("📖 SX1276 Register Reader");

  pinMode(NSS_PIN, OUTPUT);
  pinMode(RESET_PIN, OUTPUT);
  digitalWrite(NSS_PIN, HIGH);

  SPI.begin();
  resetSX1276();

  Serial.println("✅ SX1276 Ready. Reading registers...");


writeRegister(0x01, 0x10); // RegOpMode = Receiver mode
delay(10);
writeRegister(0x01, 0x85); // LoRa + Standby
delay(10);
writeRegister(0x01, 0x86); // LoRa + RX continuous
delay(10);

}

void loop() {
  // Читаємо всі регістри від 0x00 до 0x70
  /*
  for (uint8_t reg = 0x00; reg <= 0x70; reg++) {
    uint8_t value = readRegister(reg);
    Serial.print("Reg 0x");
    if (reg < 0x10) Serial.print("0");
    Serial.print(reg, HEX);
    Serial.print(" = 0x");
    if (value < 0x10) Serial.print("0");
    Serial.println(value, HEX);
    delay(50); // трішки паузи між читаннями
  }
  */
 

    uint8_t reg = 0x11;    // RSSI
    uint8_t value = readRegister(reg);
    Serial.print("Reg 0x");
    if (reg < 0x10) Serial.print("0");
    Serial.print(reg, HEX);
    Serial.print(" = 0x");
    if (value < 0x10) Serial.print("0");
    Serial.println(value, HEX);


  //Serial.println("🔄 Done. Waiting before next scan.");
  delay(50); 
}
