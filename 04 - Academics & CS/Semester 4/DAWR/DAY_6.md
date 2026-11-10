---
course: "DAWR"
semester: 4
tags:
  - course/dawr
up: "[[DAWR]]"
---

---

### 1. Aim of Experiment

To design and implement an autonomous sensor-actuator control system using an Arduino Microcontroller, an Ultrasonic Sensor for distance measurement, a DC Servo Motor for actuation, and an LED as a visual indicator based on the sensor's input.

### 2. Components Required

- **Microcontroller:** Arduino UNO
    
- **Sensor:** HC-SR04 Ultrasonic Sensor
    
- **Actuator:** Micro Servo Motor (e.g., SG90)
    
- **Indicator:** Red LED
    
- **Resistor:** 1x Resistor (e.g., 220Ω or 330Ω to limit LED current)
    
- **Connecting Wires:** Jumper wires
    
- **Power Supply:** USB Cable (connected to PC)
    

### 3. Software Required

- Arduino IDE (Integrated Development Environment)
    

### 4. Theory

**a) About Arduino Mega/UNO**

The Arduino UNO is an open-source microcontroller board based on the ATmega328P chip. It acts as the central processing unit for this experiment, reading inputs from the ultrasonic sensor, processing the threshold logic, and sending simultaneous output signals to the servo motor and the LED.

**b) Sensor/Motor/Indicator**

- **Ultrasonic Sensor (HC-SR04):** Measures distance by emitting high-frequency sound waves and calculating the time it takes for the echo to return. The distance is calculated using the formula: $Distance = (Time \times Speed\ of\ Sound) / 2$.
    
- **DC Servo Motor:** A rotary actuator that provides precise control of angular position using Pulse Width Modulation (PWM) signals from the Arduino.
    
- **LED (Light Emitting Diode):** A semiconductor light source that emits light when current flows through it. It acts as a visual status indicator in this circuit.
    

**c) Controller**

The Arduino functions as the primary controller. It continuously polls the distance data from the sensor. When the distance falls below a pre-programmed threshold, the controller triggers a dual response: actuating the servo motor to a specific angle and illuminating the LED.

### 5. Designing and Testing

**Designing:** The system is designed as an automated proximity responder with visual feedback. The Arduino triggers the HC-SR04 sensor. If an object is detected within the target range (e.g., less than 15 cm), the Arduino commands the servo motor to rotate to 90° and simultaneously turns on the red LED connected to pin 12. If the object leaves the zone, the servo returns to 0° and the LED turns off.

**Testing:** 1. The sensor's distance readings are verified using the Arduino IDE's Serial Monitor.

2. The LED is tested with a simple blink sketch to ensure proper polarity and resistor connection.

3. The fully integrated system is tested by moving an object into the sensor's field of view to confirm that both the servo sweeps and the LED illuminates exactly when the threshold is crossed.

### 7. About Connection of Motor/Sensor

Based strictly on the provided wiring diagram, the connections are as follows:

**Ultrasonic Sensor (HC-SR04) Wiring:**

- **VCC:** Connected to Arduino **5V**
    
- **GND:** Connected to Arduino **GND**
    
- **Trig:** Connected to Arduino Digital Pin **6**
    
- **Echo:** Connected to Arduino Digital Pin **5**
    

**Servo Motor Wiring:**

- **Red Wire (Power):** Connected to Arduino **5V**
    
- **Black Wire (Ground):** Connected to Arduino **GND**
    
- **Yellow Wire (Signal):** Connected to Arduino Digital Pin **11**
    

**LED Wiring:**

- **Anode (Longer leg / Positive):** Connected to one end of the Resistor. The other end of the Resistor connects to Arduino Digital Pin **12**.
    
- **Cathode (Shorter leg / Negative):** Connected to Arduino **GND**.
    

### 8. Conclusion

The experiment was successfully adapted and completed according to the updated circuit design. By incorporating an LED alongside the servo motor, the system now provides both mechanical actuation and immediate visual feedback when an object breaches the proximity threshold. The Arduino UNO accurately processed the distance calculations from the HC-SR04 sensor on pins 5 and 6, demonstrating reliable multi-component automated control.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DAWR]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/DAWR/DAWR Day 1|DAWR Day 1]] · **Next:** [[04 - Academics & CS/Semester 4/DAWR/Experiment - 5|Experiment - 5]]
> **Related:** [[IoT]] · [[DBMS]]
<!-- connections:end -->
