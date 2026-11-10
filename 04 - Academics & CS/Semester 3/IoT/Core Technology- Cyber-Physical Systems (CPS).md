---
course: "IoT"
semester: 3
tags:
  - course/iot
up: "[[IoT]]"
---

---

### **1. Embedded Systems vs. Cyber-Physical Systems (CPS)**

*   **Embedded System:**
    *   A **computational system** (microprocessor) embedded within a physical device.
    *   **Focus:** Primarily on the **computational component** to perform a specific, dedicated function.
    *   **Examples:** Washing machine controller, microwave oven timer, a simple wireless switch.
    *   Often designed as **stand-alone devices**.

*   **Cyber-Physical System (CPS):**
    *   **Integrations of computation, networking, and physical processes.**
    *   **Focus:** On the **interconnection and feedback** between the cyber (computation, communication) and physical worlds.
    *   **Key Differentiator:** **Data exchange** over a network. A CPS is essentially an embedded system that can send and receive data.
    *   **When connected to the internet,** it becomes a part of the **Internet of Things (IoT)**.
    *   **Examples:** A smart factory, a self-driving car, a human operator (brain computes, body acts, voice communicates).

**Summary:** All CPS contain embedded systems, but not all embedded systems are CPS. CPS emphasizes **networked, interactive systems** with feedback loops.

---

### **2. Components of a CPS**

A CPS is built from four key components that work together:

1.  **Sensing & Actuation Components:**
    *   **Sensors:** Measure parameters of the physical world (e.g., temperature, pressure, location).
    *   **Actuators:** Influence or control the physical world (e.g., turn a motor on/off, adjust a valve).
    *   **Function:** Enable the CPS to **interact with the physical world**.

2.  **Information Processing & Communication Components:**
    *   **Microcontrollers/Processors:** Run algorithms to process sensor data and make decisions.
    *   **Communication Interfaces:** (e.g., WLAN, Ethernet, CAN bus) to **exchange data** with other systems or the cloud.
    *   **Function:** To **compute** and **communicate**.

3.  **Control Components:**
    *   **Controllers:** Ensure the system behaves as intended.
    *   **Function:** **Regulate** the flow of information and control the system’s actuation, managing uncertainties.

4.  **Interfaces with Humans (HMI - Human-Machine Interface):**
    *   **GUIs, Dashboards, Apps:** Allow people to monitor the system and input commands.
    *   **Function:** Enable **human interaction** with the cyber-physical system.

---

### **3. Implementing CPS: Extending an Embedded System**

There are three main approaches to turn a traditional embedded system into a CPS:

1.  **Direct System Extension:**
    *   **How:** Add a **communication interface** (e.g., Wi-Fi module) directly to the existing control unit and modify its software.
    *   **Pro:** Integrated solution.
    *   **Con:** Requires low-level access and modification of the original system.

2.  **System Expansion by a Microcontroller Board:**
    *   **How:** Connect a separate **microcontroller board** (e.g., Arduino, Raspberry Pi) to the existing system. This board acts as a **gateway** to handle all communication with the cloud.
    *   **Pro:** Less invasive to the original system; easier to adapt to different systems.
    *   **Con:** Requires a uniform interface to connect the board.

3.  **Extension by Smart Actuators and Sensors:**
    *   **How:** Replace traditional sensors/actuators with **"smart"** ones that have built-in processing and communication capabilities.
    *   **Pro:** Highly decentralized and intelligent edge processing.
    *   **Con:** Can be **expensive** and generate a **very high volume of data**.

---

### **4. CPS Reference Architecture Models**

These are blueprints for building and understanding complex CPS ecosystems, especially for Industry 4.0.

| Model | Developed By | Primary Focus | Key Concept |
| :--- | :--- | :--- | :--- |
| **5C Architecture** | Academia | **Data Acquisition & Processing** | A 5-level guide for implementing CPS from the sensor up to a adaptive system. |
| **RAMI 4.0** | Platform Industrie 4.0 (Germany) | **Manufacturing Integration** | A **3D map** that provides a common language for integrating everything in a factory. |
| **IIRA** | Industrial Internet Consortium (IIC) | **Interoperability across Industries** | An open architecture focused on ensuring different IIoT systems can work together. |

#### **5C Architecture Levels:**
1.  **Smart Connection:** Getting data from sensors.
2.  **Data-to-Information Conversion:** Turning raw data into useful information.
3.  **Cyber:** Creating virtual models (digital twins) of the physical assets.
4.  **Cognition:** Monitoring and prediction (e.g., for predictive maintenance).
5.  **Configuration:** Feedback to the physical world; making the system self-adaptive.

#### **RAMI 4.0 (Reference Architectural Model Industrie 4.0):**
*   A **3-dimensional model** with axes:
    1.  **Hierarchy Levels:** From product to enterprise network.
    2.  **Product Lifecycle:** From design to maintenance.
    3.  **Architecture Layers:** From physical assets to business functions.
*   **Core Concept:** The **Administration Shell (AS)**, a standardized digital twin that contains all the information of a physical asset and enables its connection to I4.0.

#### **IIRA (Industrial Internet Reference Architecture):**
*   Organized into **4 Viewpoints**:
    1.  **Business:** Why are we building this? (Business value)
    2.  **Usage:** What are the system's responsibilities?
    3.  **Functional:** What components are needed?
    4.  **Implementation:** How do we build it with technology?

**Correlation:** While each model has a different focus (5C on data, RAMI on manufacturing, IIRA on interoperability), they share common CPS concepts. **Standardization** (e.g., of protocols and data formats) is key to making them work together.

---

### **5. Case Study: Industrial Coffee Machine**

*   **Project:** Transforming a traditional coffee machine into a CPS.
*   **Method:** **System expansion by a microcontroller board** (a Cerebot board).
*   **Implementation:** The board was connected to the machine's internal network (CANopen fieldbus), acting as a **gateway to the cloud**.
*   **CPS Benefits Achieved:**
    *   **Remote Diagnostics:** Maintenance crews can identify problems (e.g., a defect, empty ingredients) from anywhere.
    *   **Remote Customization:** Users can adjust coffee strength and temperature via a smartphone app.
    *   **Data Analytics:** Usage data is sent to the cloud for analysis.
    *   **Networking:** The machine could be connected to a social network to find the nearest machine that offers a desired product.

### **Exam Summary Focus:**

1.  **Define CPS** and clearly **contrast it with an Embedded System**. (Use the key terms: **computation, networking, physical processes, feedback loops**).
2.  Know the **four components** of a CPS (Sensing, Processing, Control, HMI).
3.  Understand the **three methods** for implementing a CPS (Direct, Microcontroller Board, Smart Sensors).
4.  Be familiar with the **purpose of the three reference models** (5C, RAMI 4.0, IIRA). You don't need to memorize every layer, but know what each is used for.
5.  The **coffee machine case study** is a perfect example to use in answers to illustrate how a CPS works and what benefits it brings.

Good luck with your exam

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[IoT]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 3/IoT/Cloud computing and FOG computing|Cloud computing and FOG computing]] · **Next:** [[04 - Academics & CS/Semester 3/IoT/Industry 4.0 Environment & Design Principles|Industry 4.0 Environment & Design Principles]]
> **Related:** [[AI & ML Roadmap]] · [[DAWR]] · [[CN]]
<!-- connections:end -->
