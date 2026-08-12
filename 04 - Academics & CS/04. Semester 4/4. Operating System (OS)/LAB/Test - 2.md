# Name : Shivam Raj
# Roll : 24052323

## Sec : CSE - 25

``` JAVA
class Time
{
int a;
 int b;
  int c;

Time(int a,int b,int c)
{
this.a=a;
this.b=b;
this.c=c;

this.b=this.b+(this.c/60);
this.c=this.c%60;

this.a=this.a+(this.b/60);
this.b=this.b%60;
}

Time addSeconds(int s)
{
this.c=this.c+s;

this.b=this.b+(this.c/60);
this.c=this.c%60;

this.a=this.a+(this.b/60);
this.b=this.b%60;

return this;
}

public static void main(String[] args)
{
System.out.println("Name : Shivam Raj");
System.out.println("Roll : 24052323");
Time t=new Time(1,59,50);

t.addSeconds(15).addSeconds(70);

System.out.println(String.format("%02d:%02d:%02d",t.a,t.b,t.c));
}
}

```


## Output

![[Pasted image 20260106220259.png]]