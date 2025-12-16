```JAVA
 import java.util.Scanner;   
class Student {   
    int rollNo;   
    String name;   
    int m1, m2, m3;   
    double percentage;   
    char grade;   
    void calculatePercentage() {   
        percentage = (m1 + m2 + m3) / 3.0;   
    }   
    void assignGrade() {   
        if (percentage >= 75)   
            grade = 'A';   
        else if (percentage >= 60)   
            grade = 'B';   
        else if (percentage >= 40)   
            grade = 'C';   
        else   
grade = 'F';   
    }   
    void display() {   
        System.out.println("Roll No: " + rollNo);   
        System.out.println("Name: " + name);   
        System.out.println("Percentage: " + percentage);   
        System.out.println("Grade: " + grade);   
    }   
}   
public class Day3_1 {  
    public static void main(String[] args) {   
        Scanner sc = new Scanner(System.in);   
        System.out.print("Enter number of students: ");   
        int n = sc.nextInt();   
        Student[] s = new Student[n];   
        for (int i = 0; i < n; i++) {   
            s[i] = new Student();   
            System.out.println("\nEnter details of student " + (i + 1));   
            System.out.print("Roll No: ");   
            s[i].rollNo = sc.nextInt();   
            System.out.print("Name: ");   
            s[i].name = sc.next();   
            System.out.print("Marks of 3 subjects: ");   
            s[i].m1 = sc.nextInt();   
            s[i].m2 = sc.nextInt();   
            s[i].m3 = sc.nextInt();   
   
            s[i].calculatePercentage();   
            s[i].assignGrade();   
        }   
        for (int i = 0; i < n - 1; i++) {   
            for (int j = 0; j < n - i - 1; j++) {   
                if (s[j].percentage < s[j + 1].percentage) {   
                    Student temp = s[j];   
                    s[j] = s[j + 1];   
                    s[j + 1] = temp;   
                }   
            }   
        }   
        System.out.println("\nTopper Details:");   
        s[0].display();   
        int countA = 0, countB = 0, countC = 0, countF = 0;   
        for (int i = 0; i < n; i++) {   
            if (s[i].grade == 'A')   
                countA++;   
            else if (s[i].grade == 'B')   
                countB++;   
            else if (s[i].grade == 'C')   
                countC++;   
            else   
countF++;   
        }   
        System.out.println("\nGrade Count:");   
        System.out.println("Grade A: " + countA);   
        System.out.println("Grade B: " + countB);   
        System.out.println("Grade C: " + countC);   
        System.out.println("Grade F: " + countF);   
       sc.close();   
    }   
}
```

![[Pasted image 20251216233324.png]]