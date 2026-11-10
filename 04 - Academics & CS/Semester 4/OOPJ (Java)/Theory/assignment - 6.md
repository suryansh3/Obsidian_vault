---
course: "OOPJ (Java)"
semester: 4
tags:
  - course/oopj-java
up: "[[OOPJ (Java)]]"
---
```JAVA
public class ObjectcounterwithoutStatic {  
    private int count = 0;   
  
    public ObjectCounterWithoutStatic() {  
        count++;  
    }  
  
    public void displayCount() {  
        System.out.println("Count for this object: " + count);  
    }  
  
    public static void main(String[] args) {  
      
        ObjectCounterWithoutStatic obj1 = new ObjectCounterWithoutStatic();  
        obj1.displayCount(); 
  
        ObjectCounterWithoutStatic obj2 = new ObjectCounterWithoutStatic();  
        obj2.displayCount();   
        System.out.println("Issue: Cannot get total objects count without static variable");  
    }  
}
```

Output : 

![[Pasted image 20251217225123.png]]

### Explanation of above code is that :
Without static variable, each object has its own copy of `count`, so we cannot track the total number of objects created across all instances.


# 2. Object Count with Static

```JAVA
public class ObjectCounterWithStatic {  
    private static int objectCount = 0;  

    private int id;  
  
    public ObjectCounterWithStatic() {  
        objectCount++;   
        id = objectCount; 
    }  
 
    public static int getObjectCount() {  
        return objectCount;  
    }  
  
    public void displayInfo() {  
        System.out.println("Object ID: " + id + ", Total objects: " + objectCount);  
    }  
  
    public static void main(String[] args) {  
        ObjectCounterWithStatic obj1 = new ObjectCounterWithStatic();  
        obj1.displayInfo();  
  
        ObjectCounterWithStatic obj2 = new ObjectCounterWithStatic();  
        obj2.displayInfo();  
  
        ObjectCounterWithStatic obj3 = new ObjectCounterWithStatic();  
        obj3.displayInfo();
  
System.out.println("Total objects created: " + ObjectCounterWithStatic.getObjectCount());   
    }  
}
```

## Output :

![[Pasted image 20251217225528.png]]

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[OOPJ (Java)]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/ASSIGNMENT - 4|ASSIGNMENT - 4]] · **Next:** [[04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Assignment - 9(24052323)|Assignment - 9(24052323)]]
> **Related:** [[Data Structures]] · [[Operating Systems]] · [[DBMS]]
<!-- connections:end -->
