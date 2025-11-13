```c 
#include <stdio.h>
#include <string.h>

#define MAX 100

int checkForward(char expr[]) {
char stack[MAX];
 int top = -1;

for (int i = 0; expr[i] != '\0'; i++) {
char ch = expr[i];

 if (ch == '(' || ch == '{' || ch == '[') {
stack[++top] = ch;
  } else if (ch == ')' || ch == '}' || ch == ']') {
 if (top == -1) return 0;  
char open = stack[top--]; // pop
if ((ch == ')' && open != '(') ||
(ch == '}' && open != '{') ||
(ch == ']' && open != '[')) {
return 0;}}}

    return (top == -1);
}

int checkReverse(char expr[]) {
char stack[MAX];
int top = -1;
int len = strlen(expr);

for (int i = len - 1; i >= 0; i--) {
char ch = expr[i];
if (ch == ')' || ch == '}' || ch == ']') {
stack[++top] = ch;
   } 
else if (ch == '(' || ch == '{' || ch == '[') {
if (top == -1) return 0;

char close = stack[top--];
if ((ch == '(' && close != ')') ||
(ch == '{' && close != '}') ||
(ch == '[' && close != ']')) {
return 0;}}}
return (top == -1);
}

int main() {
    char expr[MAX];

    printf("Enter an expression: ");
    scanf("%s", expr);

    if (checkForward(expr) && checkReverse(expr)) {
        printf("Expression has balanced parentheses in correct order (forward & reverse).\n");
    } else {
        printf("Expression is NOT balanced correctly.\n");
    }

    return 0;
}