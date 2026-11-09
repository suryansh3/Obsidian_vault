---
course: "DAWR"
semester: 4
tags:
  - course/dawr
up: "[[DAWR]]"
---


---

## **1. Aim of Experiment**

To interface a PIR motion sensor and a Servo motor with an Arduino UNO to control the motor's position based on object detection. Specifically, to rotate the servo to **10 degrees** when an object is detected and to **150 degrees** when no object is detected, noting that the IR sensor operates on **active low** logic.

## **2. Components Required**

- Arduino UNO Board
    
- PIR Motion Sensor (Parallax style)
    
- Micro Servo Motor (SG90)
    
- USB Cable (A to B)
    
- Jumper Wires
    

## **3. Software Required**

- Arduino IDE (for coding and uploading)
    
- Tinkercad (for circuit simulation and verification)
    

## **4. Theory**

### **a) Arduino UNO**

The Arduino UNO is a microcontroller board based on the ATmega328P. It features 14 digital input/output pins (6 of which can be used as PWM outputs), providing the necessary platform to read sensor data and control motor positioning.

### **b) Sensor/Motor**

- **IR Sensor:** Used to detect motion by measuring changes in the infrared levels emitted by surrounding objects. In this experiment, it is configured as **Active Low**, meaning the signal pin drops to 0V (LOW) when an object is detected.
    
- **Servo Motor:** A rotary actuator that allows for precise control of angular position. It uses a Pulse Width Modulation (PWM) signal to determine the shaft's angle.
    

## **5. Designing and Testing**

The design follows a closed-loop feedback logic. The Arduino constantly polls the digital pin connected to the PIR sensor.

- **Logic Check:** If `digitalRead` returns `LOW`, the condition for "Object Detected" is met.
    
- **Testing:** During simulation, the motion bubble in Tinkercad is moved to trigger the sensor. The response of the servo is then verified against the expected degree markers (10° and 150°).
    

## **6. Interfacing Code**

C++

``` c++
[[include]] <Servo.h>

Servo myServo;        // Create servo object
int sensorPin = 2;    // IR Sensor connected to Digital Pin 2
int sensorState = 0;  // Variable to store sensor status

void setup() {
  myServo.attach(9);        // Servo data pin connected to Digital Pin 9
  pinMode(sensorPin, INPUT); // Set sensor pin as input
}

void loop() {
  sensorState = digitalRead(sensorPin); // Read the PIR sensor

  // Active Low Logic: LOW means object detected
  if (sensorState == LOW) {
    myServo.write(10);  // Rotate to 10 degrees
  } 
  else {
    myServo.write(150); // Rotate to 150 degrees
  }
  delay(15); // Small delay for servo movement stability
}
```

## **7. About Connection of Motor/Sensor**

Based on the provided circuit reference:

- **Servo Motor:**
    
    - **Brown/Black (GND):** Connected to Arduino GND.
        
    - **Red (VCC):** Connected to Arduino 5V.
        
    - **Orange/Green (Signal):** Connected to Digital Pin **9** (PWM).
        
- **IR Sensor:**
    
    - **GND Pin:** Connected to Arduino GND.
        
    - **VCC Pin:** Connected to Arduino 5V.
        
    - **OUT Pin:** Connected to Digital Pin **2**.
        

---

## **8. Conclusion**

The experiment was successfully conducted. By implementing the active low logic in the code, the Arduino correctly identified object detection from the PIR sensor. The servo motor accurately transitioned between 10 degrees (Detected) and 150 degrees (Not Detected), fulfilling the experimental requirements.

---

**Would you like me to explain how to modify this code if you wanted to add a "delay" so the motor stays at 10 degrees for a few seconds?**

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DAWR]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/DAWR/DAY_6|DAY_6]] · **Next:** -
> **Related:** [[IoT]] · [[DBMS]]
<!-- connections:end -->
