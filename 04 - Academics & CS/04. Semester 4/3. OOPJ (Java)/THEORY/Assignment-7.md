# Name : Suryansh Mithu

# Executions : 

```JAVA
class Student{  
int rollno;  
String name;  
float fee;  
Student(int rollno,String name,float fee){  
this.rollno=rollno;  
this.name=name;  
this.fee=fee;  
}  
void display(){System.out.println(rollno+" "+name+" "+fee);}  
}  
public class AddNumbers{  
public static void main(String args[]){  
Student s1=new Student(111,"ankit",5000f);  
Student s2=new Student(112,"sumit",6000f);  
s1.display();  
s2.display();  
}}
```

![[Pasted image 20251218222411.png]]

---

```JAVA
class Student{  
int rollno;  
String name;  
float fee;  
Student(int rollno,String name,float fee){  
rollno=rollno;  
name=name;  
fee=fee;  
}  
void display(){System.out.println(rollno+" "+name+" "+fee);}  
}  
public class TestThis1{  
public static void main(String args[]){  
Student s1=new Student(111,"ankit",5000f);  
Student s2=new Student(112,"sumit",6000f);  
s1.display();  
s2.display();  
}}
```

![[Pasted image 20251218222653.png]]

---

```JAVA
class A{  
void m(){System.out.println("hello m");}  
void n(){  
System.out.println("hello n");  
this.m();  
}  
}  
class TestThis{  
public static void main(String args[]){  
A a=new A();  
a.n();  
}}
```

![[Pasted image 20251218222833.png]]

---

```JAVA
class A{  
A(){System.out.println("hello a");}  
A(int x){  
this();  
System.out.println(x);  
}  
}  
public class TestThis1{  
public static void main(String args[]){  
A a=new A(10);  
}}
```

![[Pasted image 20251218222958.png]]

---

```JAVA
class A{  
A(){  
this(5);  
System.out.println("hello a");  
}  
A(int x){  
System.out.println(x);  
} }  
public class TestThis1{  
public static void main(String args[]){  
A a=new A();  
}}
```

![[Pasted image 20251218223111.png]]

---

```JAVA
class Student{
int rollno;
String name,course;
float fee;
Student(int rollno,String name,String course){

this.rollno=rollno;
this.name=name;
this.course=course;
}
Student(int rollno,String name,String course,float fee){
this(rollno,name,course);//reusing constructor
this.fee=fee;
}
void display(){System.out.println(rollno+" "+name+"
"+course+" "+fee);}
}
public class TestThis{
public static void main(String args[]){
Student s1=new Student(111,"ankit","java");
Student s2=new Student(112,"sumit","java",6000f);
s1.display();
s2.display();
}}
```

![[Pasted image 20251218223405.png]]

---

```JAVA
public class S2{  
  
void m(S2 obj){  
  
System.out.println("method is invoked");  
  
}  
  
void p(){  
  
m(this);  
  
}  
  
public static void main(String args[]){  
  
S2 s1 = new S2();  
  
s1.p();  
  
}  
  
}
```

![[Pasted image 20251218223651.png]]

---
```JAVA
class B{  
A obj;  
B(A obj){  
this.obj=obj;  
}  
void display(){  
System.out.println(obj.data);//using data member of A class  
}  
}  
public class A{  
int data=10;  
A(){  
B b=new B(this);  
b.display();  
}  
public static void main(String args[]){  
A a=new A();  
} }
```

![[Pasted image 20251218224127.png]]

---

```JAVA
class A{  
A getA(){  
return this;  
}  
void msg(){System.out.println("Hello java");}  
}  
class Test1{  
public static void main(String args[]){  
new A().getA().msg();  
}  
}
```

![[Pasted image 20251218224331.png]]


