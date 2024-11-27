#ifndef STACK_H
#define STACK_H

#include "Node.h"

using namespace std;

class Stack {
private:
    Node *top;

public:
    Stack() {
        top = NULL;
    }

    void push(int data) {
        Node *newNode = new Node(data);
        newNode->Next = top;
        top = newNode;
    }

    void pop() {
        if (top == NULL) {
            cout << "Stack is empty. Cannot pop.\n";
            return;
        }

        Node *temp = top;
        top = top->Next;
        cout << "Popped: " << temp->Data << endl;
        delete temp;
    }

    int peek() {
        if (top == NULL) {
            cout << "Stack is empty.\n";
            return -1;
        }
        return top->Data;
    }

    void display() {
        if (top == NULL) {
            cout << "Stack is empty.\n";
            return;
        }

        Node *current = top;
        cout << "Stack contents: ";
        while (current != NULL) {
            cout << current->Data << "\t";
            current = current->Next;
        }
        cout << endl;
    }

    ~Stack() {
        while (top != NULL) {
            pop();
        }
    }
};



#endif // STACK_H
