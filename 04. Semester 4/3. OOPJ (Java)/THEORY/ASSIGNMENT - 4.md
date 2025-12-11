

# OOPJ - ASSIGNMENT 4

## Name - Suryansh Mithu
## Roll - 24155060

## CSE - 25


# 1.

``` JAVA
class OperatorExample{  
  
public static void main(String args[]){  
  
int x=10;  
  
System.out.println(x++);  
  
System.out.println(++x);  
  
System.out.println(x--);  
  
System.out.println(--x);  
  
}}
```

## Output

![[Pasted image 20251211155626.png]]

---
# 2

``` JAVa
class OperatorExample  
  
{  
  
public static void main(String args[]){  
  
int a=10;  
  
int b=10;  
  
System.out.println(a++ + ++a);  
  
System.out.println(b++ + b++);  
  
}  
  
}
```


## Output

![[Pasted image 20251211155643.png]]

---
# 3.

``` JAVA
class OperatorExample{

public static void main(String args[]){

int a=10;

int b=-10;

boolean c=true;

boolean d=false;

System.out.println(~a);

System.out.println(~b);

System.out.println(!c);

System.out.println(!d);

}}
```


## Output 

![[Pasted image 20251211155703.png]]

---
# 4.

``` JAVA
class OperatorExample{

public static void main(String args[]){

System.out.println(10<<2);

System.out.println(10<<3);

System.out.println(20<<2);

System.out.println(15<<4);

}}
```

## Output

![[Pasted image 20251211155736.png]]

---
# 5.

``` JAVA
class OperatorExample

{

public static void main(String args[]){

System.out.println(10>>2);

System.out.println(20>>2);

System.out.println(20>>3);

}

}
```

## Output

![[Pasted image 20251211155755.png]]

---
# 6.

```JAVA
class OperatorExample{  
  
public static void main(String args[]){  
  
//For positive number, >> and >>> works same  
  
System.out.println(20>>2);  
  
System.out.println(20>>>2);  
  
//For negative number, >>> changes parity bit (MSB) to 0;  
  
System.out.println(-20>>2);  
  
System.out.println(-20>>>2);  
  
}}
```

## Output

![[Pasted image 20251211155813.png]]

---
# 7.

```JAVA
class OperatorExample{

public static void main(String args[]){

int a=10;

int b=5;

int c=20;

System.out.println(a<b&&a<c);//false && true = false

System.out.println(a<b&a<c);//false & true = false

}}
```

## Output

![[Pasted image 20251211155832.png]]

---
# 8.

```JAVA
class OperatorExample{

public static void main(String args[]){

int a=10;

int b=5;

int c=20;

System.out.println(a<b&&a++<c);//false && true = false

System.out.println(a);

System.out.println(a<b&a++<c);//false & true = false

System.out.println(a);

}}
```

## Output

![[Pasted image 20251211155849.png]]

---
# 9.

```JAVA
class OperatorExample{

public static void main(String args[]){

int a=10;

int b=5;

int c=20;

System.out.println(a>b||a<c);//true || true = true

System.out.println(a>b|a<c);//true | true = true

//|| vs |

System.out.println(a>b||a++<c);//true || true = true

System.out.println(a);

System.out.println(a>b|a++<c);//true | true = true

System.out.println(a);

}}
```

## Output 

![[Pasted image 20251211155911.png]]

---
# 10.

```JAVA
class OperatorExample{

public static void main(String args[]){

int a=2;

int b=5;

int min=(a<b)?a:b;

System.out.println(min);

}}
```

## Output

![[Pasted image 20251211155934.png]]

---
# 11.

```JAVA
class LabeledForExample {

public static void main(String[] args) {

aa:

for(int i=1;i<=3;i++){

bb:

for(int j=1;j<=3;j++){

if(i==2&&j==2){

break aa;

}

System.out.println(i+" "+j);}}}}
```

## Output

![[Pasted image 20251211160011.png]]

---
# 12.

```JAVA
class LabeledForExample2 {

public static void main(String[] args) {

aa:

for(int i=1;i<=3;i++){

bb:

for(int j=1;j<=3;j++){

if(i==2&&j==2){

break bb;

}

System.out.println(i+" "+j);
}
}}}
```

## Output :

![[Pasted image 20251211160029.png]]

---
# 13.

```JAVA
class BreakExample {

public static void main(String[] args) {

for(int i=1;i<=10;i++){

if(i==5){

break;

}

System.out.println(i);

}

}

}
```

## Output 

![[Pasted image 20251211160045.png]]

---
# 14.

```JAVA
class BreakExample2 {

public static void main(String[] args) {

for(int i=1;i<=3;i++){

for(int j=1;j<=3;j++){

if(i==2&&j==2){

break;

}

System.out.println(i+" "+j);

}

}

}

}
```

## Output

![[Pasted image 20251211160107.png]]

---
# 15.

```JAVA
class ContinueExample {

public static void main(String[] args) {

for(int i=1;i<=10;i++){

if(i==5){

continue;

}

System.out.println(i);

}

}

}
```

## Output

![[Pasted image 20251211160124.png]]

---
# 16.

```JAVA
class ContinueExample2 {

public static void main(String[] args) {

for(int i=1;i<=3;i++){

for(int j=1;j<=3;j++){

if(i==2&&j==2){

continue;

}

System.out.println(i+" "+j);

}

}

}

}
```

## Output

![[Pasted image 20251211160141.png]]