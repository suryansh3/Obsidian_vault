# Name : Suryansh Mithu

# Roll : 24155060

---

## 2.1

**Input file `inDec.txt`:**

```
30 75 2564
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

void bin(int n, FILE *fp)
{
    if(n>1)
        bin(n/2,fp);
    fprintf(fp,"%d",n%2);
}

int bits(int n)
{
    int c=0;
    if(n==0)
        return 1;
    while(n>0)
    {
        n=n/2;
        c++;
    }
    return c;
}

int main()
{
    FILE *fin,*fout;
    int n,i,pad;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inDec.txt","r");
    fout=fopen("outBin.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        pad=16-bits(n);
        fprintf(fout,"The binary equivalent of %d is ",n);
        for(i=0;i<pad;i++)
            fprintf(fout,"0");
        bin(n,fout);
        fprintf(fout,"\n");
    }

    fclose(fin);
    fclose(fout);

    printf("Conversion done, check outBin.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 21_bin.c -o 21_bin
$ ./21_bin
Name : Suryansh Mithu
Roll : 24155060

Conversion done, check outBin.txt
```

**Output file `outBin.txt`:**

```
The binary equivalent of 30 is 0000000000011110
The binary equivalent of 75 is 0000000001001011
The binary equivalent of 2564 is 0000101000000100
```

---

## 2.2

**Input file `inGcd.txt`:**

```
8 12
20 45
30 80
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

int gcd(int a,int b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}

int main()
{
    FILE *fin,*fout;
    int a,b,r;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inGcd.txt","r");
    fout=fopen("outGcd.dat","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d %d",&a,&b)!=EOF)
    {
        r=gcd(a,b);
        fprintf(fout,"The GCD of %d and %d is %d\n",a,b,r);
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outGcd.dat\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 22_gcd.c -o 22_gcd
$ ./22_gcd
Name : Suryansh Mithu
Roll : 24155060

Done, check outGcd.dat
```

**Output file `outGcd.dat`:**

```
The GCD of 8 and 12 is 4
The GCD of 20 and 45 is 5
The GCD of 30 and 80 is 10
```

---

## 2.3

**Input file `inFact.txt`:**

```
5 6 7
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

long fact(int n)
{
    if(n<=1)
        return 1;
    return n*fact(n-1);
}

int main()
{
    FILE *fin,*fout;
    int n;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inFact.txt","r");
    fout=fopen("outFact.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        fprintf(fout,"The factorial of %d is %ld\n",n,fact(n));
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outFact.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 23_fact.c -o 23_fact
$ ./23_fact
Name : Suryansh Mithu
Roll : 24155060

Done, check outFact.txt
```

**Output file `outFact.txt`:**

```
The factorial of 5 is 120
The factorial of 6 is 720
The factorial of 7 is 5040
```

---

## 2.4

**Input file `inFibo.txt`:**

```
5 7
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

int fibo(int n)
{
    if(n==0)
        return 0;
    if(n==1)
        return 1;
    return fibo(n-1)+fibo(n-2);
}

int main()
{
    FILE *fin,*fout;
    int n,i;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inFibo.txt","r");
    fout=fopen("outFibo.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        fprintf(fout,"The first %d Fibonacci terms are : ",n);
        for(i=0;i<n;i++)
        {
            fprintf(fout,"%d ",fibo(i));
        }
        fprintf(fout,"\n");
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outFibo.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 24_fibo.c -o 24_fibo
$ ./24_fibo
Name : Suryansh Mithu
Roll : 24155060

Done, check outFibo.txt
```

**Output file `outFibo.txt`:**

```
The first 5 Fibonacci terms are : 0 1 1 2 3 
The first 7 Fibonacci terms are : 0 1 1 2 3 5 8 
```

---

## 2.5

**Input file `inSum.txt`:**

```
5724 123 999
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

int sum(int n)
{
    if(n==0)
        return 0;
    return n%10+sum(n/10);
}

int main()
{
    FILE *fin,*fout;
    int n;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inSum.txt","r");
    fout=fopen("outSum.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        fprintf(fout,"The sum of digits of %d is %d\n",n,sum(n));
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outSum.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 25_sum.c -o 25_sum
$ ./25_sum
Name : Suryansh Mithu
Roll : 24155060

Done, check outSum.txt
```

**Output file `outSum.txt`:**

```
The sum of digits of 5724 is 18
The sum of digits of 123 is 6
The sum of digits of 999 is 27
```

---

## 2.6

**Input file `inRev.txt`:**

```
12345 6789
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

int rev(int n,int r)
{
    if(n==0)
        return r;
    return rev(n/10,r*10+n%10);
}

int main()
{
    FILE *fin,*fout;
    int n;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inRev.txt","r");
    fout=fopen("outRev.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        fprintf(fout,"The reverse of %d is %d\n",n,rev(n,0));
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outRev.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 26_rev.c -o 26_rev
$ ./26_rev
Name : Suryansh Mithu
Roll : 24155060

Done, check outRev.txt
```

**Output file `outRev.txt`:**

```
The reverse of 12345 is 54321
The reverse of 6789 is 9876
```

---

## 2.7

**Input file `inPalin.txt`:**

```
1221 1234 121
```

**Code:**

```c
/* Name : Suryansh Mithu */
/* Roll : 24155060 */

[[include]]<stdio.h>

int rev(int n,int r)
{
    if(n==0)
        return r;
    return rev(n/10,r*10+n%10);
}

int main()
{
    FILE *fin,*fout;
    int n,r;

    printf("Name : Suryansh Mithu\n");
    printf("Roll : 24155060\n\n");

    fin=fopen("inPalin.txt","r");
    fout=fopen("outPalin.txt","w");

    if(fin==NULL || fout==NULL)
    {
        printf("File error\n");
        return 0;
    }

    while(fscanf(fin,"%d",&n)!=EOF)
    {
        r=rev(n,0);
        if(n==r)
            fprintf(fout,"%d is Palindrome\n",n);
        else
            fprintf(fout,"%d is Not Palindrome\n",n);
    }

    fclose(fin);
    fclose(fout);

    printf("Done, check outPalin.txt\n");
    return 0;
}
```

**Output (terminal):**

```
$ gcc 27_palin.c -o 27_palin
$ ./27_palin
Name : Suryansh Mithu
Roll : 24155060

Done, check outPalin.txt
```

**Output file `outPalin.txt`:**

```
1221 is Palindrome
1234 is Not Palindrome
121 is Palindrome
```