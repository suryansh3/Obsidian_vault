
## **1. Default Constructor Program**
```java
class a{int x;String y;a(){x=0;y="";}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("x: "+x);System.out.println("y: "+y);}}
public class Main{public static void main(String[] args){a o=new a();o.d();}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
x: 0
y: 
Process finished with exit code 0
```

---
## **2. Parameterized Constructor for Student**
```java
class stu{int r;String n;int m;stu(int r,String n,int m){this.r=r;this.n=n;this.m=m;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Student: "+n+" Roll: "+r+" Marks: "+m);}}
public class Main{public static void main(String[] args){stu s=new stu(101,"Raj",85);s.s();}}
```

# Output
 
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Student: Raj Roll: 101 Marks: 85
Process finished with exit code 0
```

---
## **3. Employee Class Constructor**
```java
class emp{int i;int s;emp(int i,int s){this.i=i;this.s=s;}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("ID: "+i+" Salary: "+s);}}
public class Main{public static void main(String[] args){emp e=new emp(1001,50000);e.d();}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
ID: 1001 Salary: 50000
Process finished with exit code 0
```

---
## **4. Constructor Overloading Box Class**
```java
class box{int l,b,h;box(int s){l=b=h=s;}
box(int l,int b,int h){this.l=l;this.b=b;this.h=h;}
void v(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Vol: "+(l*b*h));}}
public class Main{public static void main(String[] args){box b1=new box(5);box b2=new box(2,3,4);b1.v();b2.v();}}
```

#  Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Vol: 125
Name : Suryansh Mithu
Roll : 24155060
Vol: 24
Process finished with exit code 0
```

---
## **5. Book Class with Price Calculation**
```java
class book{int q;int p;int t;book(int q,int p){this.q=q;this.p=p;t=q*p;}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Total: "+t);}}
public class Main{public static void main(String[] args){book b=new book(3,250);b.d();}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Total: 750
Process finished with exit code 0
```

---
## **6. Constructor Counting Objects**
```java
class cnt{static int c;cnt(){c++;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Count: "+c);}}
public class Main{public static void main(String[] args){new cnt();new cnt();new cnt();}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Count: 1
Name : Suryansh Mithu
Roll : 24155060
Count: 2
Name : Suryansh Mithu
Roll : 24155060
Count: 3
Process finished with exit code 0
```
---

## **7. Constructor Chaining**
```java
class chain{int a,b;chain(){this(0);}
chain(int a){this(a,0);}
chain(int a,int b){this.a=a;this.b=b;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("a="+a+" b="+b);}}
public class Main{public static void main(String[] args){new chain();new chain(5);new chain(3,4);}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
a=0 b=0
Name : Suryansh Mithu
Roll : 24155060
a=5 b=0
Name : Suryansh Mithu
Roll : 24155060
a=3 b=4
Process finished with exit code 0
```

---
## **8. Constructor vs Method Execution Order**
```java
class ord{ord(){System.out.println("Constructor");}
void m(){System.out.println("Method");}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");}}
public class Main{public static void main(String[] args){ord o=new ord();o.d();o.m();}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Constructor
Name : Suryansh Mithu
Roll : 24155060
Method
Process finished with exit code 0
```

---
## **9. Time Class with Normalization**
```java
class time{int h,m,s;time(int h,int m,int s){this.h=h;this.m=m;this.s=s;if(s>=60){m+=s/60;this.s=s%60;}
if(m>=60){h+=m/60;this.m=m%60;}System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println(h+":"+this.m+":"+this.s);}}
public class Main{public static void main(String[] args){time t=new time(2,70,90);}}
```

# Output

```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
3:11:30
Process finished with exit code 0
```

---
## **10. Initialize Array Using Constructor**
```java
class arr{int[] a;arr(int s){a=new int[s];for(int i=0;i<s;i++)a[i]=i+1;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");for(int i=0;i<s;i++)System.out.print(a[i]+" ");}}
public class Main{public static void main(String[] args){new arr(5);}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
1 2 3 4 5 
Process finished with exit code 0
```

---
## **11. this to Distinguish Variables**
```java
class diff{int a;diff(int a){this.a=a;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Value: "+this.a);}}
public class Main{public static void main(String[] args){diff d=new diff(10);}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Value: 10
Process finished with exit code 0
```

---
## **12. this() to Call Another Constructor**
```java
class call{int x,y;call(){this(1,2);}
call(int x,int y){this.x=x;this.y=y;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("x="+x+" y="+y);}}
public class Main{public static void main(String[] args){new call();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
x=1 y=2
Process finished with exit code 0
```

---
## **13. Method Returns this Reference**
```java
class ret{ret get(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");return this;}
void show(){System.out.println("Showing");}}
public class Main{public static void main(String[] args){ret r=new ret();r.get().show();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Showing
Process finished with exit code 0
```
---
## **14. Pass Current Object as Argument**
```java
class arg{void m1(arg o){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Method1");}
void m2(){m1(this);System.out.println("Method2");}}
public class Main{public static void main(String[] args){arg a=new arg();a.m2();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Method1
Method2
Process finished with exit code 0
```
---
## **15. Method Chaining Using this**
```java
class chainm{chainm m1(){System.out.print("One ");return this;}
chainm m2(){System.out.print("Two ");return this;}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");}}
public class Main{public static void main(String[] args){chainm c=new chainm();c.d();c.m1().m2();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
One Two 
Process finished with exit code 0
```
---
## **16. this Improves Readability**
```java
class read{int a,b;read(int a,int b){this.a=a;this.b=b;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("a="+this.a+" b="+this.b);}}
public class Main{public static void main(String[] args){read r=new read(10,20);r.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
a=10 b=20
Process finished with exit code 0
```
---
## **17. this to Avoid Shadowing**
```java
class shadow{int x;shadow(int x){this.x=x;System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Value: "+this.x);}}
public class Main{public static void main(String[] args){shadow s=new shadow(5);}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Value: 5
Process finished with exit code 0
```
---
## **18. Incorrect Without this**
```java
class inc{int v;inc(int v){v=v;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Wrong: "+v);}}
class cor{int v;cor(int v){this.v=v;}
void s(){System.out.println("Correct: "+v);}}
public class Main{public static void main(String[] args){inc i=new inc(5);i.s();cor c=new cor(5);c.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Wrong: 0
Correct: 5
Process finished with exit code 0
```
---
## **19. Single Inheritance**
```java
class p{void show(){System.out.println("Person");}}
class s extends p{void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");show();System.out.println("Student");}}
public class Main{public static void main(String[] args){s o=new s();o.d();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Person
Student
Process finished with exit code 0
```
---
## **20. Multilevel Inheritance**
```java
class v{void m(){System.out.print("Vehicle ");}}
class c extends v{void m1(){System.out.print("Car ");}}
class e extends c{void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");m();m1();System.out.print("Electric");}}
public class Main{public static void main(String[] args){e obj=new e();obj.d();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Vehicle Car Electric
Process finished with exit code 0
```
---
## **21. Constructor Calling Sequence**
```java
class a1{a1(){System.out.println("Base");}}
class b1 extends a1{b1(){System.out.println("Derived");}}
class c1 extends b1{c1(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Child");}}
public class Main{public static void main(String[] args){c1 o=new c1();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Base
Derived
Name : Suryansh Mithu
Roll : 24155060
Child
Process finished with exit code 0
```
---
## **22. Aggregation Address-Employee**
```java
class ad{String c;ad(String c){this.c=c;}}
class em{String n;ad a;em(String n,ad a){this.n=n;this.a=a;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println(n+" "+a.c);}}
public class Main{public static void main(String[] args){ad addr=new ad("City");em e=new em("John",addr);e.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
John City
Process finished with exit code 0
```
---
## **23. Engine Aggregated in Car**
```java
class eng{String t;eng(String t){this.t=t;}}
class car{String m;eng e;car(String m,eng e){this.m=m;this.e=e;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println(m+" "+e.t);}}
public class Main{public static void main(String[] args){eng e=new eng("V8");car c=new car("Toyota",e);c.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Toyota V8
Process finished with exit code 0
```
---
## **24. Department Has Multiple Teachers**
```java
class t{String n;t(String n){this.n=n;}}
class d{t[] ts;d(t[] ts){this.ts=ts;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");for(t t:ts)System.out.print(t.n+" ");}}
public class Main{public static void main(String[] args){t[] arr={new t("T1"),new t("T2")};d dept=new d(arr);dept.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
T1 T2 
Process finished with exit code 0
```
---
## **25. Array of Objects Aggregation**
```java
class item{String n;item(String n){this.n=n;}}
class store{item[] items;store(item[] items){this.items=items;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");for(item i:items)System.out.print(i.n+" ");}}
public class Main{public static void main(String[] args){item[] it={new item("A"),new item("B")};store st=new store(it);st.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
A B 
Process finished with exit code 0
```
---
## **26. Inheritance vs Aggregation**
```java
class b{void show(){System.out.print("Base ");}}
class d1 extends b{void d(){show();System.out.println("Inheritance");}}
class d2{b obj;d2(b obj){this.obj=obj;}
void d(){obj.show();System.out.println("Aggregation");}}
public class Main{public static void main(String[] args){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");d1 i=new d1();i.d();d2 a=new d2(new b());a.d();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Base Inheritance
Base Aggregation
Process finished with exit code 0
```
---
## **27. College Contains Students**
```java
class stu{String n;stu(String n){this.n=n;}}
class col{stu[] ss;col(stu[] ss){this.ss=ss;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");for(stu s:ss)System.out.print(s.n+" ");}}
public class Main{public static void main(String[] args){stu[] arr={new stu("A"),new stu("B")};col c=new col(arr);c.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
A B 
Process finished with exit code 0
```
---
## **28. HAS-A Relationship**
```java
class wheel{int s;wheel(int s){this.s=s;}}
class vehicle{wheel w;vehicle(wheel w){this.w=w;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Wheel: "+w.s);}}
public class Main{public static void main(String[] args){wheel wh=new wheel(4);vehicle v=new vehicle(wh);v.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Wheel: 4
Process finished with exit code 0
```
---
## **29. Constructor-Based Aggregation**
```java
class part{String n;part(String n){this.n=n;}}
class whole{part p;whole(part p){this.p=p;}
void s(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");System.out.println("Part: "+p.n);}}
public class Main{public static void main(String[] args){part pa=new part("X");whole w=new whole(pa);w.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Part: X
Process finished with exit code 0
```
---
## **30. Parent Destroyed, Child Lives**
```java
class child{String n;child(String n){this.n=n;}
void s(){System.out.println("Child: "+n);}}
class parent{child c;parent(child c){this.c=c;}
void kill(){System.out.println("Parent destroyed");}
void d(){System.out.println("Name : Suryansh Mithu");
System.out.println("Roll : 24155060");}}
public class Main{public static void main(String[] args){child ch=new child("Alive");parent p=new parent(ch);p.d();p.kill();ch.s();}}
```
# Output
```
C:\Users\surya\.jdks\openjdk-25.0.1\bin\java.exe
Name : Suryansh Mithu
Roll : 24155060
Parent destroyed
Child: Alive
Process finished with exit code 0
```