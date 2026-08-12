``` java
import java.util.Scanner;  
  
class Account {  
    int accountNo;  
    String name;  
    float balance;  
  
    void openAccount() {  
        Scanner sc = new Scanner(System.in);  
        System.out.print("Enter account number: ");  
        accountNo = sc.nextInt();  
        sc.nextLine();  
        System.out.print("Enter name: ");  
        name = sc.nextLine();  
        System.out.print("Enter initial balance: ");  
        balance = sc.nextFloat();  
    }  
  
    void deposit(float amount) {  
        balance += amount;  
        System.out.println("Deposited: " + amount);  
    }  
  
    void withdraw(float amount) {  
        if(amount <= balance) {  
            balance -= amount;  
            System.out.println("Withdrawn: " + amount);  
        } else {  
            System.out.println("Insufficient balance");  
        }  
    }  
  
    void displayBalance() {  
        System.out.println("Balance: " + balance);  
    }  
  
    public static void main(String[] args) {  
        System.out.println("Name : Suryansh Mithu");  
        System.out.println("Roll : 24155060");  
        Account acc = new Account();  
        acc.openAccount();  
  
        Scanner sc = new Scanner(System.in);  
        System.out.print("Enter deposit amount: ");  
        float dep = sc.nextFloat();  
        acc.deposit(dep);  
  
        System.out.print("Enter withdrawal amount: ");  
        float wd = sc.nextFloat();  
        acc.withdraw(wd);  
  
        acc.displayBalance();  
    }  
}```


![[Pasted image 20251215235442.png]]


