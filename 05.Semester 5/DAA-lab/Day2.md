
---

## 2.1


```c
#include <stdio.h>
void bin(int n,char s[],int i){
if(i>=0){bin(n/2,s,i-1);s[i]=(n%2)?'1':'0';}
}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *in,*out;
int n,i,x;
char b[17];
in=fopen("inDec.txt","r");
out=fopen("outBin.txt","w");
fscanf(in,"%d",&n);
for(i=0;i<n;i++){
fscanf(in,"%d",&x);
b[16]='\0';
bin(x,b,15);
fprintf(out,"The binary equivalent of %d is %s\n",x,b);
printf("%d -> %s\n",x,b);
}
fclose(in);fclose(out);
return 0;
}
```

```
3
30 75 2564
```

```
$ gcc dec2bin.c -o dec2bin
$ ./dec2bin
Name : Suryansh Mithu
Roll : 24155060
30 -> 0000000000011110
75 -> 0000000001001011
2564 -> 0000101000000100
```

```
The binary equivalent of 30 is 0000000000011110
The binary equivalent of 75 is 0000000001001011
The binary equivalent of 2564 is 0000101000000100
```

---

## 2.2 

```c
#include <stdio.h>
int gcd(int a,int b){return b?gcd(b,a%b):a;}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *in,*out;
int a,b;
in=fopen("inGcd.txt","r");
out=fopen("outGcd.dat","w");
while(fscanf(in,"%d %d",&a,&b)==2){
int g=gcd(a,b);
fprintf(out,"The GCD of %d and %d is %d\n",a,b,g);
}
fclose(in);fclose(out);
in=fopen("outGcd.dat","r");
char c;
while((c=fgetc(in))!=EOF) putchar(c);
fclose(in);
return 0;
}
```

```
8 12
20 45
30 80
```

```
$ gcc gcd.c -o gcd
$ ./gcd
Name : Suryansh Mithu
Roll : 24155060
The GCD of 8 and 12 is 4
The GCD of 20 and 45 is 5
The GCD of 30 and 80 is 10
```

---

## 2.3


```c
#include <stdio.h>
long long fact(int n){return n<=1?1:n*fact(n-1);}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n;
f=fopen("inFact.txt","r");
fscanf(f,"%d",&n);
fclose(f);
printf("%d! = %lld\n",n,fact(n));
return 0;
}
```


```
7
```


```
$ gcc fact.c -o fact
$ ./fact
Name : Suryansh Mithu
Roll : 24155060
7! = 5040
```

---

## 2.4

```c
#include <stdio.h>
int fib(int n){return n<=1?n:fib(n-1)+fib(n-2);}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i;
f=fopen("inFibo.txt","r");
fscanf(f,"%d",&n);
fclose(f);
printf("First %d Fibonacci numbers: ",n);
for(i=0;i<n;i++) printf("%d ",fib(i));
printf("\n");
return 0;
}
```

```
6
```

```
$ gcc fibo.c -o fibo
$ ./fibo
Name : Suryansh Mithu
Roll : 24155060
First 6 Fibonacci numbers: 0 1 1 2 3 5 
```

---

## 2.5

```c
#include <stdio.h>
int sum(int n){return n?n%10+sum(n/10):0;}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n;
f=fopen("inSum.txt","r");
fscanf(f,"%d",&n);
fclose(f);
printf("Sum of digits of %d = %d\n",n,sum(n));
return 0;
}
```

```
5724
```

```
$ gcc sumdig.c -o sumdig
$ ./sumdig
Name : Suryansh Mithu
Roll : 24155060
Sum of digits of 5724 = 18
```

---

## 2.6

```c
#include <stdio.h>
int rev(int n,int r)
{return n?rev(n/10,r*10+n%10):r;}

int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n;
f=fopen("inRev.txt","r");
fscanf(f,"%d",&n);
fclose(f);
printf("Reverse of %d = %d\n",n,rev(n,0));
return 0;
}
```

```
12345
```

```
$ gcc revnum.c -o revnum
$ ./revnum
Name : Suryansh Mithu
Roll : 24155060
Reverse of 12345 = 54321
```

---

## 2.7

```c
#include <stdio.h>
#include <string.h>
int pal(char s[],int l,int r){
if(l>=r) return 1;
if(s[l]!=s[r]) return 0;
return pal(s,l+1,r-1);
}
int main(){
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i;
char s[50];
f=fopen("inPal.txt","r");
fscanf(f,"%d",&n);
for(i=0;i<n;i++){
fscanf(f,"%s",s);
if(pal(s,0,strlen(s)-1))
printf("%s -> Palindrome\n",s);
else
printf("%s -> Not Palindrome\n",s);
}
fclose(f);
return 0;
}
```

```
3
1221
1234
555
```

```
$ gcc pal.c -o pal
$ ./pal
Name : Suryansh Mithu
Roll : 24155060
1221 -> Palindrome
1234 -> Not Palindrome
555 -> Palindrome
```

---
