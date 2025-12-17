```JAVA
```java
import java.util.Scanner;

class Student {
    int studentId;
    String studentName;
    int subject1Score;
    int subject2Score;
    int subject3Score;
    double studentPercentage;
    char studentGrade;

    void computePercentage() {
        studentPercentage = (subject1Score + subject2Score + subject3Score) / 3.0;
    }

    void determineGrade() {
        if (studentPercentage >= 75)
            studentGrade = 'A';
        else if (studentPercentage >= 60)
            studentGrade = 'B';
        else if (studentPercentage >= 40)
            studentGrade = 'C';
        else
            studentGrade = 'F';
    }

    void showStudentInfo() {
        System.out.println("Roll Number: " + studentId);
        System.out.println("Name: " + studentName);
        System.out.println("Percentage: " + studentPercentage);
        System.out.println("Grade: " + studentGrade);
    }
}

public class StudentResultSystem {
    public static void main(String[] args) {
        Scanner inputReader = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int studentCount = inputReader.nextInt();
        Student[] studentRecords = new Student[studentCount];

        for (int index = 0; index < studentCount; index++) {
            studentRecords[index] = new Student();
            System.out.println("\nEnter details of student " + (index + 1));
            System.out.print("Roll Number: ");
            studentRecords[index].studentId = inputReader.nextInt();
            System.out.print("Name: ");
            studentRecords[index].studentName = inputReader.next();
            System.out.print("Marks of 3 subjects: ");
            studentRecords[index].subject1Score = inputReader.nextInt();
            studentRecords[index].subject2Score = inputReader.nextInt();
            studentRecords[index].subject3Score = inputReader.nextInt();

            studentRecords[index].computePercentage();
            studentRecords[index].determineGrade();
        }

        for (int firstIndex = 0; firstIndex < studentCount - 1; firstIndex++) {
            for (int secondIndex = 0; secondIndex < studentCount - firstIndex - 1; secondIndex++) {
                if (studentRecords[secondIndex].studentPercentage < studentRecords[secondIndex + 1].studentPercentage) {
                    Student temporaryHolder = studentRecords[secondIndex];
                    studentRecords[secondIndex] = studentRecords[secondIndex + 1];
                    studentRecords[secondIndex + 1] = temporaryHolder;
                }
            }
        }

        System.out.println("\nTopper Details:");
        studentRecords[0].showStudentInfo();

        int gradeACount = 0;
        int gradeBCount = 0;
        int gradeCCount = 0;
        int gradeFCount = 0;

        for (int index = 0; index < studentCount; index++) {
            if (studentRecords[index].studentGrade == 'A')
                gradeACount++;
            else if (studentRecords[index].studentGrade == 'B')
                gradeBCount++;
            else if (studentRecords[index].studentGrade == 'C')
                gradeCCount++;
            else
                gradeFCount++;
        }

        System.out.println("\nGrade Count:");
        System.out.println("Grade A: " + gradeACount);
        System.out.println("Grade B: " + gradeBCount);
        System.out.println("Grade C: " + gradeCCount);
        System.out.println("Grade F: " + gradeFCount);

        inputReader.close();
    }
}
```


![[Pasted image 20251216233324.png]]