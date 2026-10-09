/*
  ESP32 Sensor Fusion - Vibration + Current Acquisition
  Motor Fault Diagnosis Project

  Reads 2x MPU6050 (vibration, drive-end & non-drive-end)
  and 2x ACS712 (current, per phase), streams CSV over Serial.

  Wiring:
    MPU6050 #1 (DE):  AD0 -> GND (addr 0x68), SDA/SCL -> ESP32 I2C
    MPU6050 #2 (NDE): AD0 -> 3.3V (addr 0x69), SDA/SCL -> ESP32 I2C
    ACS712 #1: OUT -> voltage divider -> GPIO34
    ACS712 #2: OUT -> voltage divider -> GPIO35
*/

#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpuDE(0x68);   // drive-end
MPU6050 mpuNDE(0x69);  // non-drive-end

const int CURRENT_PIN_1 = 34;
const int CURRENT_PIN_2 = 35;

const unsigned long SAMPLE_INTERVAL_US = 500; // 2kHz sample rate
unsigned long lastSampleTime = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  mpuDE.initialize();
  mpuNDE.initialize();

  if (!mpuDE.testConnection()) Serial.println("MPU6050 DE connection failed");
  if (!mpuNDE.testConnection()) Serial.println("MPU6050 NDE connection failed");

  // CSV header
  Serial.println("timestamp_us,ax_de,ay_de,az_de,ax_nde,ay_nde,az_nde,current1_raw,current2_raw");
}

void loop() {
  unsigned long now = micros();
  if (now - lastSampleTime >= SAMPLE_INTERVAL_US) {
    lastSampleTime = now;

    int16_t ax_de, ay_de, az_de, gx, gy, gz;
    int16_t ax_nde, ay_nde, az_nde;

    mpuDE.getMotion6(&ax_de, &ay_de, &az_de, &gx, &gy, &gz);
    mpuNDE.getMotion6(&ax_nde, &ay_nde, &az_nde, &gx, &gy, &gz);

    int current1 = analogRead(CURRENT_PIN_1);
    int current2 = analogRead(CURRENT_PIN_2);

    Serial.print(now); Serial.print(",");
    Serial.print(ax_de); Serial.print(",");
    Serial.print(ay_de); Serial.print(",");
    Serial.print(az_de); Serial.print(",");
    Serial.print(ax_nde); Serial.print(",");
    Serial.print(ay_nde); Serial.print(",");
    Serial.print(az_nde); Serial.print(",");
    Serial.print(current1); Serial.print(",");
    Serial.println(current2);
  }
}