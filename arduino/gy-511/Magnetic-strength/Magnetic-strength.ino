#include <Wire.h>

// Адреса магнітометра LSM303
#define MAG_ADDRESS 0x1E 

// Регістр режиму магнітометра
#define CRA_REG_M 0x00  // Регістр конфігурації A
#define CRB_REG_M 0x01  // Регістр конфігурації B
#define MR_REG_M  0x02  // Режим роботи магнітометра
#define MAG_OUT_X_H 0x03 // Початок даних магнітометра

// Структура для зберігання векторних даних
struct Vector3 {
  int16_t x, y, z;
};

// Функція для зчитування вектора магнітного поля
Vector3 readMagneticVector() {
  Vector3 mag;

  // Починаємо читання даних з першого регістра (MAG_OUT_X_H)
  Wire.beginTransmission(MAG_ADDRESS);
  Wire.write(MAG_OUT_X_H);
  Wire.endTransmission();

  // Читаємо 6 байтів: X, Z, Y
  Wire.requestFrom(MAG_ADDRESS, 6);
  if (Wire.available() >= 6) {
    mag.x = (Wire.read() << 8) | Wire.read(); // X-вісь
    mag.z = (Wire.read() << 8) | Wire.read(); // Z-вісь
    mag.y = (Wire.read() << 8) | Wire.read(); // Y-вісь
  }

  // Корекція для 12-бітних знакових даних
  if (mag.x > 2047) mag.x -= 4096;
  if (mag.y > 2047) mag.y -= 4096;
  if (mag.z > 2047) mag.z -= 4096;

  return mag;
}

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Налаштування магнітометра
  Wire.beginTransmission(MAG_ADDRESS);
  
  // Встановлення найнижчої чутливості (±8.1 гаус, 230 µT/LSB)
  Wire.write(CRB_REG_M); 
  Wire.write(0xE0); // Встановлюємо конфігурацію ±8.1 гаус
  Wire.endTransmission();

  // Увімкнення безперервного режиму
  Wire.beginTransmission(MAG_ADDRESS);
  Wire.write(MR_REG_M);
  Wire.write(0x00); // Continuous conversion mode
  Wire.endTransmission();

  Serial.println("LSM303 налаштовано на найнижчу чутливість (±8.1 гаус).");
}

void loop() {
  Vector3 magneticField = readMagneticVector();

  // Виведення результатів
  Serial.print("X: ");
  Serial.print(magneticField.x);
  Serial.print(" Y: ");
  Serial.print(magneticField.y);
  Serial.print(" Z: ");
  Serial.print(magneticField.z);
  Serial.println(" (raw)");

  // Обчислення сили магнітного поля
  float sensitivity = 230.0; // µT/LSB для ±8.1 гаус
  float totalField = sqrt(
    pow(magneticField.x * sensitivity / 1000.0, 2) +
    pow(magneticField.y * sensitivity / 1000.0, 2) +
    pow(magneticField.z * sensitivity / 1000.0, 2)
  );

  Serial.print("Магнітне поле (мТл): ");
  Serial.println(totalField, 2);

  delay(500); // Затримка між вимірами
}