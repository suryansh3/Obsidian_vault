---
course: "IoT"
semester: 3
tags:
  - course/iot
up: "[[IoT]]"
---
Of course. Here is a detailed breakdown of the Cloud and Fog Computing lecture into structured bullet points and keywords for your exam preparation.

### **Core Technologies: Cloud Computing & Fog Computing**

---

### **1. Distributed Computing Fundamentals**

*   **Computing:** The process of using computer technology to complete a task. It involves designing and developing software/hardware systems.
*   **Distributed System:** A system where components located on networked computers communicate and coordinate their actions by passing messages.
*   **Characteristics (SEAM):**
    *   **S**ingle-system image: Appears as one computer to the user.
    *   **E**xpandable: Easy to add new resources.
    *   **A**vailability: High reliability; failures in one part are covered by others.
    *   **M**iddleware supported: Software that connects the distributed components.

**Advantages of Distributed over Centralized Systems (SIRI):**
*   **S**peed: Can achieve higher speeds through parallel processing.
*   **I**nherent Distribution: Some applications are naturally distributed (e.g., banking, airline reservations).
*   **R**eliability: A single failure doesn't bring down the entire system.
*   **I**ncremental Growth: Easier to scale by adding more machines.

**Disadvantages:**
*   Complex software development, network issues (saturation, loss), security challenges, and hard-to-detect faults.

**Related Concepts:**
*   **Cluster Computing:** A group of **tightly coupled** computers working together as a single system via a **fast Local Area Network (LAN)**. Used for **high performance** and **availability**.
*   **Grid Computing:** The integration of computer resources from multiple domains to reach a common goal. It's like a **virtualized supercomputer** built from distributed, **loosely coupled** systems over a **WAN**. Focuses on sharing isolated IT resources.

---

### **2. Cloud Computing**

*   **Definition:** A model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications) that can be rapidly provisioned with minimal management effort.
*   **Basic Concept:** Using the internet to deliver computing services, a step beyond utility computing.

#### **Cloud Service Models (The SPI Model):**

1.  **Infrastructure as a Service (IaaS):**
    *   **Provides:** Fundamental computing resources - virtual machines, storage, networks.
    *   **Analogy:** Renting a plot of land. You build what you want, but you're responsible for the OS, runtime, data, and applications.
    *   **Example:** Amazon Web Services (EC2), Microsoft Azure VMs.

2.  **Platform as a Service (PaaS):**
    *   **Provides:** A runtime environment, development and deployment tools for applications.
    *   **Analogy:** Renting a fully equipped workshop. You build your product, but the owner maintains the building and tools.
    *   **Example:** Google App Engine, Microsoft Azure App Services.

3.  **Software as a Service (SaaS):**
    *   **Provides:** Complete, ready-to-use software applications over the internet.
    *   **Analogy:** Renting a fully built and furnished house. You just live in it.
    *   **Example:** Gmail, Salesforce, Microsoft Office 365.

#### **Cloud Deployment Models:**

*   **Public Cloud:** Services are open to the general public. **Less secure** but cost-effective. (e.g., AWS, Google Cloud).
*   **Private Cloud:** Services are used exclusively by a single organization. **More secure** and offers greater control.
*   **Community Cloud:** Shared by several organizations with common concerns (e.g., security, compliance).
*   **Hybrid Cloud:** A **mix of public and private** clouds. Critical operations use the private cloud, while non-critical ones use the public cloud.

#### **Key Characteristics of Cloud (NIST Definition):**

*   **On-Demand Self-Service:** Users can provision resources automatically without human interaction.
*   **Broad Network Access:** Services are available over the network and accessed through standard mechanisms (e.g., phones, laptops).
*   **Resource Pooling:** Provider’s resources are pooled to serve multiple consumers (multi-tenant model).
*   **Rapid Elasticity:** Resources can be rapidly and elastically provisioned to scale out and released to scale in. Appears unlimited to the user.
*   **Measured Service:** Cloud systems automatically control and optimize resource use by leveraging a metering capability (pay-per-use).

#### **Benefits of Cloud Computing:**

*   **Cost Savings:** No large upfront capital investment; pay only for what you use (operational expenditure vs. capital expenditure).
*   **Scalability & Elasticity:** Instantly scale resources up or down based on demand.
*   **Reliability & Availability:** Built-in failover and redundancy.
*   **Focus on Business:** Companies can focus on their core business instead of IT infrastructure.

---

### **3. Fog Computing (Edge Computing)**

*   **Why Fog? Cloud Limitations:** Cloud computing is insufficient for applications requiring **very low latency**, **geographical distribution**, and **mobility**.
*   **Definition:** A decentralized computing infrastructure in which data, compute, storage, and applications are located somewhere between the data source (the "thing") and the cloud.
*   **Purpose:** The Fog layer provides **local, low-latency processing** and only sends relevant data to the cloud for heavier analysis.

#### **Characteristics of Fog Computing:**

*   **Low Latency:** Essential for real-time applications (e.g., video streaming, online gaming, augmented reality).
*   **Location Awareness:** Services are aware of their geographical context (e.g., traffic lights, navigation).
*   **Widespread Geographical Distribution:** Nodes are distributed across a wide area, closer to the edge.
*   **Mobility Support:** Seamlessly supports mobile devices (phones, vehicles, fitness trackers).
*   **Predominance of Wireless Access & Real-time Applications:** Optimized for streaming and immediate response.
*   **Heterogeneity:** Comprises a wide variety of devices.

#### **Architectural Drivers for Fog:**

*   **Low Latency / Real-Time Response:** Needed for immediate actionable information.
*   **Dynamic Number of Nodes:** The system must handle devices constantly joining and leaving.
*   **Highly Mobile Nodes:** The Fog must adapt to devices moving in and out of its coverage.
*   **Diverse Failure Modes:** Must handle many different types of device failures seamlessly.
*   **Security:** Requires robust access control mechanisms.

#### **The Role of the Data Center:**

*   The central hub in the cloud that provides powerful, centralized services.
*   **Services include:** Data storage & management, big data/ML/AI processing, high-volume e-commerce, and running productivity applications.

### **Exam Summary Focus:**

1.  **Define Cloud Computing** and its **5 key characteristics**.
2.  Clearly explain the **three service models (IaaS, PaaS, SaaS)** with an analogy for each.
3.  Know the **four deployment models** (Public, Private, Community, Hybrid).
4.  Understand **why Fog Computing is needed** (to solve Cloud's latency and mobility issues).
5.  List the **key characteristics of Fog Computing** (Low Latency, Location Awareness, etc.).
6.  Be able to **contrast Cloud and Fog/Edge** computing.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[IoT]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 3/IoT/BIG Data|BIG Data]] · **Next:** [[04 - Academics & CS/Semester 3/IoT/Core Technology- Cyber-Physical Systems (CPS)|Core Technology- Cyber-Physical Systems (CPS)]]
> **Related:** [[AI & ML Roadmap]] · [[DAWR]] · [[CN]]
<!-- connections:end -->
