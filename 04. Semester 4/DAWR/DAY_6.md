Here is the experiment report formatted exactly according to the structure provided in your image.

---

### 1. Aim of Experiment

To design and implement an autonomous sensor-actuator control system using an Arduino Microcontroller, which utilizes an Ultrasonic Sensor for distance measurement and a DC Servo Motor for automated actuation based on the sensor's input.

### 2. Components Required

- **Microcontroller:** Arduino UNO (or Arduino Mega)
    
- **Sensor:** HC-SR04 Ultrasonic Sensor
    
- **Actuator:** Micro Servo Motor (e.g., SG90)
    
- **Prototyping:** Breadboard
    
- **Connecting Wires:** Jumper wires (Male-to-Male, Male-to-Female)
    
- **Power Supply:** USB Cable (to connect Arduino to PC)
    

### 3. Software Required

- Arduino IDE (Integrated Development Environment)
    

### 4. Theory

**a) About Arduino Mega/UNO**

The Arduino UNO is an open-source microcontroller board based on the ATmega328P chip. It features 14 digital input/output pins (of which 6 can be used as PWM outputs for motor control), 6 analog inputs, a 16 MHz quartz crystal, a USB connection, and a power jack. It acts as the brain of this experiment, continuously reading inputs from the sensor, processing the logic, and sending precise control signals to the actuator.

**b) Sensor/Motor**

- **Ultrasonic Sensor (HC-SR04):** This sensor measures distance by emitting ultrasonic sound waves at 40,000 Hz and calculating the time it takes for the echo to bounce back from an object. Distance is calculated using the formula: $Distance = (Time \times Speed\ of\ Sound) / 2$.
    
- **DC Servo Motor:** A servo motor is a rotary actuator that allows for precise control of angular position. Unlike a standard DC motor that spins continuously, a standard servo usually turns between 0° and 180°. It operates by receiving Pulse Width Modulation (PWM) signals from the microcontroller, which dictates the exact angle the motor shaft should hold.
    

**c) Controller (if they use)**

In this system, the Arduino serves as the primary controller utilizing a basic proportional control logic. The controller is programmed to act autonomously: it monitors the distance variable in real-time and maps those physical distance values into corresponding angular degrees for the servo motor (e.g., opening a barrier if an object is within a specific threshold).

### 5. Designing and Testing

**Designing:** The system is designed as an automated proximity responder (like an automatic gate or a smart dustbin). The Arduino triggers the ultrasonic sensor every few milliseconds. If an object is detected within a designated threshold (e.g., less than 15 cm), the Arduino commands the servo motor to rotate to 90° (actuation state). If the object moves away, the servo returns to 0° (idle state).

**Testing:** 1. The sensor's accuracy is first tested by observing the output distance on the Arduino IDE's Serial Monitor.

2. The servo's sweeping capability is tested using basic PWM sweeps.

3. Finally, the integrated system is tested by placing an object in front of the sensor at varying distances to verify that the servo reacts strictly according to the programmed thresholds.

### 6. Interfacing Code

C++

```
#include <Servo.h>

// Define pins for Ultrasonic Sensor
const int trigPin = 9;
const int echoPin = 10;

// Define pin for Servo Motor
const int servoPin = 11;

// Define variables for distance calculation
long duration;
int distance;

// Create a servo object
Servo myServo;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
  
  myServo.attach(servoPin); // Attaches the servo on pin 11
  myServo.write(0);         // Initialize servo at 0 degrees
  
  Serial.begin(9600);       // Start serial communication for debugging
}

void loop() {
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Set the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance (Speed of sound is 0.034 cm/us)
  distance = duration * 0.034 / 2;
  
  // Print distance to Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Autonomous Control Logic
  if (distance > 0 && distance <= 15) {
    // If object is closer than 15 cm, actuate servo to 90 degrees
    myServo.write(90);
  } else {
    // Otherwise, keep servo at 0 degrees
    myServo.write(0);
  }
  
  delay(100); // Small delay to stabilize the readings
}
```

### 7. About Connection of Motor/Sensor

**Ultrasonic Sensor (HC-SR04) Wiring:**

- **VCC** connects to Arduino **5V**
    
- **GND** connects to Arduino **GND**
    
- **Trig** connects to Arduino Digital Pin **9**
    
- **Echo** connects to Arduino Digital Pin **10**
    

**Servo Motor Wiring:**

- **Red Wire (Power)** connects to Arduino **5V**
    
- **Brown/Black Wire (Ground)** connects to Arduino **GND**
    
- **Orange/Yellow Wire (Signal)** connects to Arduino Digital Pin **11** (Must be a PWM-capable pin, marked with a `~`).
    

### 8. Conclusion

The experiment was completed successfully. An autonomous sensor-actuator system was designed where the HC-SR04 ultrasonic sensor accurately mapped the physical environment, and the Arduino UNO effectively processed this data to control the SG90 servo motor in real-time. This experiment successfully demonstrates the foundational principles of closed-loop automation and micro-controller-based robotics without requiring manual human intervention.

---

Would you like me to explain how to modify the code so the servo motor follows the object's distance continuously rather than just switching between two positions?