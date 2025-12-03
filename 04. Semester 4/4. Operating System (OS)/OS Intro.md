# **📚 OS Fundamentals Overview**

### **Brief Overview**

This note covers **Operating System** and was created from the [CS162 Lecture 2: Four Fundamental OS Concepts](https://www.youtube.com/watch?v=4FpG1DcvHzc) YouTube video. It covers **process roles**, **memory protection**, device drivers, and basic scheduling.

### **Key Points**

- OS as referee, illusionist, and glue
    
- Protection via base‑bound, segmentation, and paging
    
- Threads, processes, and virtual memory fundamentals
    
- Scheduling and context‑switch overhead
    

---

## **🧩 Operating System Roles**

> **Operating System (OS)** – software that manages hardware resources and provides common services to applications.

|   |   |
|---|---|
|Role|Description|
|**Referee**|Enforces protection rules: isolates processes, prevents unauthorized access to memory, files, sockets, and the kernel.|
|**Illusionist**|Presents a clean, virtual view of resources (e.g., virtual machines, virtual memory) that is simpler than the raw hardware.|
|**Glue**|Supplies common services such as windowing systems and file systems that make program development easier.|

---

## **📂 Processes & Protection**

> **Process** – an instance of a program together with its own virtual resources (threads, address space, files, sockets).

- Each process **believes** it has exclusive access to the machine.
    
- The OS prevents a process (e.g., _process 2_) from:
    
    1. Observing or modifying another process’s state.
        
    2. Altering the kernel in unauthorized ways.
        
    3. Accessing storage without permission.
        
- Violations typically result in a **segmentation fault** or termination with a core dump.
    

---

## **🖥️ Hardware Complexity & OS Abstraction**

- Modern CPUs (e.g., Intel SkyLake) include:
    
    - High‑bandwidth DRAM channels, integrated graphics, and a **Direct Media Interface** (formerly the south bridge).
        
    - Connections to PCI‑Express devices, USB, Ethernet, audio, RAID, etc.
        
    - A slower interface for BIOS/firmware.
        
- The OS abstracts this layered hardware into **virtual resources** that programs can use uniformly.
    

|   |   |
|---|---|
|Physical Component|Virtual Abstraction|
|Processor core|**Thread** (virtual CPU)|
|DRAM blocks|**Address space**|
|Disk/SSD blocks|**File system**|
|Network interface|**Socket API**|
|BIOS services|**Standard firmware interface**|

---

## **⚙️ Device Drivers & Reliability**

> **Device driver** – software that mediates between the OS and a hardware device, often supplied by the hardware vendor.

- Drivers are a major source of system crashes (≈ 50‑60 % of faults in measured data).
    
- Issues arise because drivers must handle **very complex hardware** while exposing a clean API.
    
- Poorly vetted third‑party drivers can create security holes (e.g., Spectre, Meltdown).
    
- Strategies to improve reliability:
    
    - Vendor vetting processes (Microsoft, Apple, Linux).
        
    - Isolation techniques (microkernels, containers such as Docker).
        

---

## **🌐 Virtualization Concepts**

### **🧵 Threads**

> **Thread** – a single line of execution containing a program counter, registers, execution flags, stack pointer, and other state.

- A thread is the **virtualized counterpart** of a processor core.
    
- Only one thread per core is **resident** (its state lives in registers).
    
- Non‑resident threads are stored in memory as a **Thread Control Block (TCB)**.
    

### **📁 Address Spaces**

> **Address space** – the set of memory addresses a process can reference, optionally translated by hardware paging.

- Provides a cleaner view than raw physical memory.
    

### **🗂️ Processes (recap)**

- Consist of one or more threads plus a **protection domain** (memory, files, sockets).
    
- The OS enforces isolation between processes.
    

### **🔐 Dual‑Mode Operation**

> **Dual mode** – processors operate in at least two modes: **kernel (supervisor) mode** and **user mode**.

- Kernel mode grants full hardware access; user mode is restricted.
    
- Context switches between modes enable the OS to maintain the illusion of safe, isolated execution.
    

---

## **⏱️ Context Switching**

### **📋 Thread Control Block (TCB)**

- Stores all register values, program counter, stack pointer, and flags for a suspended thread.
    
- Located in kernel memory.
    

### **🔄 Resident vs. Suspended**

|   |   |   |
|---|---|---|
|State|Where the thread lives|What the CPU does|
|**Resident**|Registers of the core|Executes instructions, program counter points to next instruction|
|**Suspended**|Memory (TCB)|CPU runs another thread; original thread’s state is saved|

### **⚡ Switching Overhead**

- Typical switch time: **a few microseconds**.
    
- Excessive switching leads to **thrashing** (most time spent switching).
    

### **📂 Cache & TLB Handling**

- Generally **one cache per core**; threads share it.
    
- Fast switches may avoid flushing if page tables are updated; otherwise the cache/TLB may be flushed.
    

---

## **📊 Execution Flags & Registers**

- **Execution flags** are one‑bit registers (e.g., Zero flag, Sign flag) set by arithmetic operations.
    
- Used for conditional branching (e.g., “branch if equal”).
    
- Different architectures expose different flag sets (e.g., x86 **EFLAGS**).
    

|   |   |
|---|---|
|Architecture|Typical Register Count|
|RISC‑V (e.g., RISC‑5)|~32 integer registers + floating‑point|
|x86 (modern)|Fewer general‑purpose registers, plus segment registers, flag registers, etc.|

---

## **📅 Scheduling & Responsiveness (preview)**

- **Preemptive scheduling** (e.g., timer interrupt) ensures no single thread monopolizes the CPU, improving responsiveness.
    
- **Voluntary yield** (e.g., waiting for I/O) also triggers a context switch.
    
- Trade‑off: running a thread to completion maximizes efficiency but harms responsiveness for other tasks.
    

## **📚 Project & Course Administration**

> **Project Zero** – First Pintos assignment; introduces kernel‑level thread implementation.

- Examine **thread.h** and **thread.c** to see how Pintos creates and manages threads.
    
- **Homework 0** (due Thursday) covers:
    
    1. **GDB** debugging basics.
        
    2. Compilation workflow.
        
    3. Git usage.
        
    4. Setting up the virtual machine environment.
        
- **Slip days**: ↑ to **four** for both homework and projects.
    
    - _Strategy_: conserve early; use later for larger deadlines.
        
- **Optional C / C++ review** (Zoom, recorded).
    
    - Primary language for Pintos is **C**; C++ not required but useful background.
        
- **Drop deadline**: Friday (four days away).
    
    - Late drops are difficult; decide early to free wait‑list spots.
        
- **Collaboration policy**:
    
    |   |   |
    |---|---|
    |Allowed|Prohibited|
    |Discuss algorithms, testing ideas, debugging strategies at a high level|Share code, test cases, or detailed debug traces with other groups|
    |Search for generic data‑structure implementations (e.g., hash tables)|Copy or read another group's code, prior‑year solutions, or online submissions|
    

---

## **🧵 Threads in the Kernel**

> **Thread** – Execution context (registers, PC, stack pointer) managed by the OS kernel.

- For now, assume **threads reside in kernel memory** (user‑level threads will be covered later).
    
- Pintos implements threads directly in the kernel; the **Thread Control Block (TCB)** lives in kernel space.
    

### **🔧 Kernel‑Level Thread Lifecycle**

1. **Create** – Allocate TCB, initialize registers, add to ready queue.
    
2. **Schedule** – Kernel selects a TCB, loads its registers, marks it _resident_.
    
3. **Block / Exit** – Save registers back to the TCB, move to blocked or free list.
    

---

## **🗂️ Address Spaces**

> **Address space** – Set of logical memory addresses a process (or thread group) can reference, together with the state governing those addresses.

- 32‑bit example: addresses **0x00000000 → 0xFFFFFFFF** (≈ 4 GiB).
    
- Not every address maps to physical DRAM; the OS decides which portions are backed.
    

### **📦 Typical Segments**

|   |   |   |
|---|---|---|
|Segment|Typical Contents|Access Characteristics|
|**Code**|Executable instructions|Read‑only, executable|
|**Static / Data**|Global variables, string literals|Read‑write (globals), read‑only (constants)|
|**Stack**|Local variables, return addresses|Grows downward, grows on demand via page faults|
|**Heap**|Dynamically allocated objects (malloc)|Grows upward, expands via page faults|

- **Stack & heap growth**: start with a few pages; on a fault the OS allocates additional physical pages.
    

---

## **🛡️ Hardware‑Based Protection: Base & Bound**

> **Base‑bound protection** – Uses two registers (base, bound) to delimit the memory region a thread may access.

- **Base register** = lowest permissible address (inclusive).
    
- **Bound register** = first address _outside_ the allowed region (exclusive).
    

### **✅ Enforcement Mechanism**

1. For every memory reference, hardware checks:
    
2. If the check fails, the processor raises an exception (e.g., kills the offending thread).
    

- This model requires **no extra translation latency**; only a comparison.
    
- Early systems (e.g., Cray machines) used this scheme with **relocatable loaders**.
    

### **📐 Relation to Segmentation**

- x86 _segment registers_ (CS, DS, SS, etc.) embody the same idea: each holds a base and a limit.
    
- The **instruction pointer** is an offset inside the current code segment; the physical address is base + offset.
    

---

## **🔄 Relocation & Loading**

> **Relocation** – Adjusting program addresses at load time so that code runs at its assigned base address.

- Programs are compiled assuming a **logical origin (address 0)**.
    
- The loader copies the binary into memory at some **runtime base** (e.g., 0x1000) and updates the base register.
    
- No page‑table translation is needed for this primitive scheme; the hardware adds the base on the fly.
    
- Limitation: expanding the region later may require **copying** the whole code/data to a larger area, leading to fragmentation.
    

---

## **🧩 Towards Virtual Memory**

> **Virtual memory** – Abstracts physical memory as a collection of fixed‑size _pages_ mapped via a _page table_.

- Overcomes base‑bound drawbacks:
    
    - **Fragmentation** is minimized because pages can be placed anywhere in physical RAM.
        
    - **Protection** is per‑page; the OS can set read/write/execute bits per entry.
        

### **📖 High‑Level Sketch**

1. **Page size** (e.g., 4 KiB) divides the address space into equal frames.
    
2. **Page table** pointer stored in a special hardware register (e.g., CR3 on x86).
    
3. On each memory reference:
    
    - Hardware translates **virtual page number → physical frame** using the page table.
        
    - Checks per‑page permission bits; on violation, raises a **page‑fault exception**.
        

- The **precise exception** problem (saving exact CPU state) makes OS implementation harder; imprecise exceptions are avoided in production kernels.
    

---

## **⚙️ Process vs. Thread Memory Sharing**

- In Pintos’s current **thread model**, all threads share a **single address space**:
    
    - They can read/write each other’s stacks, heap, and static data.
        
    - This design is **intentional** for early labs but is **insecure** for real‑world workloads.
        
- **Isolation strategy**: run separate **processes** with distinct address spaces; the OS enforces protection via base‑bound or page tables.
    
- Consequence of shared address space: a buggy or malicious thread can overwrite the OS kernel or another thread’s data, leading to crashes or security breaches.
    

---

## **📊 Summary of Protection Mechanisms**

|   |   |   |   |
|---|---|---|---|
|Mechanism|Granularity|Hardware Support|Main Advantage|
|**Base‑Bound**|Whole region per thread|Simple compare registers|Minimal overhead|
|**Segmentation**|Variable‑size segments|Segment registers (x86)|Flexible layout|
|**Paging (Virtual Memory)**|Fixed‑size pages|Page‑table walk, TLB|Fine‑grained protection, low fragmentation|
|**User/Kernal Modes**|Execution privilege|CPU mode bits|Isolates OS from user code|

---

## **🌐 Virtual Address Translation & Page Tables**

> **Virtual address** – the address used by a program; it is translated by the hardware to a physical address in DRAM.

- **Instruction fetch**, **load/store** operations all start with virtual addresses.
    
- The **page table** maps each virtual page to a physical frame (or indicates that the page is not resident).
    
- Translation enables any page of the address space to be placed in any physical frame, eliminating the fragmentation problems of base‑bound protection.
    

|   |   |
|---|---|
|Aspect|Detail|
|**Granularity**|Fixed‑size pages (e.g., 4 KiB).|
|**Direction**|Virtual → Physical (normal execution) and Physical → Virtual (e.g., for debugging).|
|**Hardware support**|Page‑table base register (CR3 on x86), TLB cache for fast look‑ups.|
|**Protection**|Per‑page read/write/execute bits; a process cannot address pages belonging to another process because its page table points elsewhere.|

---

## **📦 Processes: Definition & Protection**

> **Process** – an execution environment with a _restricted address space_ that owns one or more threads, file descriptors, and filesystem context.

- A process is the **unit of protection**: its address space is isolated from other processes by the page‑table mechanism.
    
- Creation is performed via **fork** (duplicate current address space) and **exec** (replace it with a new program).
    

### **🧩 Process Structure**

|   |   |
|---|---|
|Component|Role|
|**Address space**|Holds code, data, heap, and stack segments; protected by page tables.|
|**Threads**|Execution contexts (register set, PC, stack) that run inside the same address space.|
|**File descriptors & FS context**|Provide controlled access to files, pipes, sockets, etc.|

> **Restricted rights** – a process may only perform operations the OS explicitly permits (via system calls).

### **🔐 Protection via Translation**

- If two processes have **different page tables**, their virtual addresses map to **different physical pages**.
    
- The CPU cannot generate a physical address that belongs to another process, so **cross‑process memory reads/writes are impossible** without OS mediation.
    

---

## **🧵 Threads Inside Processes**

### **⚙️ Single‑Threaded vs Multi‑Threaded Process**

|   |   |   |
|---|---|---|
|Feature|Single‑Threaded Process|Multi‑Threaded Process|
|**Number of stacks**|One stack|One stack per thread|
|**Thread Control Block (TCB)**|One TCB|One TCB per thread (register set, PC, flags)|
|**Concurrency**|None (only time‑slicing)|True concurrency on multiple cores|
|**Communication**|Implicit via shared memory (the only memory)|Threads share the same address space, so they can communicate via shared variables but must avoid race conditions.|

- **Thread switching** saves the current thread’s registers into its TCB and loads the next thread’s registers, giving the illusion of multiple processors.
    

### **📊 Trade‑off: Performance vs Isolation**

- **Many threads in one process** → low communication overhead (shared memory) → high parallelism but **less isolation** (a buggy thread can corrupt another’s stack/heap).
    
- **Separate processes** → strong isolation (each has its own address space) → inter‑process communication (IPC) is more expensive (pipes, sockets, shared memory segments).
    

---

## **🔄 Dual‑Mode Execution & System Calls**

> **Dual mode** – processors operate in **kernel (supervisor) mode** with full privileges or **user mode** with restricted rights.

### **📣 Controlled Transitions**

|   |   |   |
|---|---|---|
|Transition type|Origin → Destination|Typical cause|
|**System call**|User → Kernel|Program requests OS service (e.g., read, open).|
|**Interrupt**|Asynchronous hardware event (timer, I/O) → Kernel|Timer tick, device ready signal.|
|**Trap / Exception**|User → Kernel|Faults such as page fault, divide‑by‑zero.|
|**Return from kernel**|Kernel → User|After handling the above, control is handed back to the process.|

- In **user mode** the base/bound registers (or page‑table controls) are active, preventing the process from accessing memory outside its assigned region.
    
- In **kernel mode** those restrictions are lifted, allowing the OS to modify page tables, enable/disable interrupts, and manage hardware.
    

### **🛠️ Kernel Responsibilities When Loading a Process**

1. **Allocate** a page table for the new process.
    
2. **Set** base (lowest allowed address) and bound (first disallowed address) registers or appropriate page‑table entries.
    
3. **Load** the user program counter (user PC) with the entry point of the executable.
    
4. **Execute** a _return‑to‑user_ instruction, which switches the CPU to user mode and begins execution of the process code.
    

---

## **📋 Process Control Block & Scheduling**

> **Process Control Block (PCB)** – kernel data structure that records the complete state of a process.

- The PCB contains:
    
    - Process identifier (PID)
        
    - Pointer to the **page table** (address‑space definition)
        
    - List of **Thread Control Blocks** for all threads in the process
        
    - Open file descriptors and filesystem context
        
    - Scheduling information (priority, state, CPU time used)
        

### **🗓️ Scheduler Role**

- The **scheduler** runs in kernel mode, periodically (e.g., every 10–100 µs) on a timer interrupt.
    
- It examines the set of **ready PCBs**, selects the next process (according to a policy such as round‑robin or priority), and performs the context switch:
    
    1. **Save** current thread’s registers into its TCB (which lives in the PCB).
        
    2. **Load** the selected thread’s registers from its TCB.
        
    3. **Update** the CPU’s page‑table base register to the new process’s page table.
        
    4. **Return** to user mode, resuming execution of the chosen thread.
        
- The scheduler thus provides the **policy layer** that decides _which_ protected address space runs at any moment, completing the mechanism introduced earlier (protection via translation + dual‑mode execution).