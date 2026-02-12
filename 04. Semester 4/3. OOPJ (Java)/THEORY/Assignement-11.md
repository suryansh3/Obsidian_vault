# 1.
```java
public class StringExample{ 

    public static void main(String args[]){ 

    String s1="java";//creating string by java string literal 

    char ch[]={'s','t','r','i','n','g','s'}; 

    String s2=new String(ch);//converting char array to string 

    String s3=new String("example");//creating java string by new keyword 

    System.out.println(s1); 

    System.out.println(s2); 

    System.out.println(s3); 

    }}
```

```
PS C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_1' 
java
strings
example
```

---
# 2.

```java
public class day9_2 {

    public static void main(String args[]) {

        String s = "Sachin";

        s.concat(" Tendulkar");// concat() method appends the string at the end

        System.out.println(s);// will print Sachin because strings are immutable objects

    }

}
```

```
PS C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  c:; cd 'c:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB'; & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_1' 
Sachin
```

---
# 3.
``` java
class day9_3{ 

     public static void main(String args[]){ 

       String s1="Sachin"; 

       String s2="Sachin"; 

       String s3=new String("Sachin"); 

       String s4="Saurav"; 

       System.out.println(s1.equals(s2));//true 

       System.out.println(s1.equals(s3));//true 

       System.out.println(s1.equals(s4));//false 

     } 

    }
```

```
S C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  c:; cd 'c:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB'; & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_3' 
true
true
false
```

---
# 4.

```java
public class day9_4 {

    public static void main(String args[]) {

        String s1 = "Sachin";

        String s2 = "SACHIN";

  

        System.out.println(s1.equals(s2));// false

        System.out.println(s1.equalsIgnoreCase(s2));// true

    }

}
```

```
PS C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  c:; cd 'c:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB'; & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_4' 
false
true
```

---
# 5.
```java
public class day9_5 {

  public static void main(String args[]) {

    String s1 = "Sachin";

    String s2 = "Sachin";

    String s3 = new String("Sachin");

    System.out.println(s1 == s2);// true (because both refer to same instance)

    System.out.println(s1 == s3);// false(because s3 refers to instance created in nonpool)

  }

}
```

```
PS C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  c:; cd 'c:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB'; & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_5' 
false
true
```

---
# 6.

```java
public class day9_6 {
  public static void main(String args[]) {
    String s1 = "Sachin";
    String s2 = "Sachin";
    String s3 = new String("Sachin");
    System.out.println(s1 == s2);// true (because both refer to same instance)
    System.out.println(s1 == s3);// false(because s3 refers to instance created in nonpool)
  }
}
```

```
PS C:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB>  c:; cd 'c:\Users\surya\OneDrive\Documents\Java_OOPJ\OOPJ_LAB'; & 'C:\Program Files\Java\jre1.8.0_481\bin\java.exe' '-cp' 'C:\Users\surya\AppData\Roaming\Antigravity\User\workspaceStorage\9eec13107ef84a4b935f5c5438ac2750\redhat.java\jdt_ws\OOPJ_LAB_696e422c\bin' 'day9_6' 
false
true
```
