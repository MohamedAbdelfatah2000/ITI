#include <iostream>
#include "Stack.h"
#include "Queue.h"

using namespace std;

int main() {
    cout << "************************************  "<< endl;
    cout << "*********      STACK      **********  "<< endl;
    cout << "************************************  "<< endl;

    Stack stack;

    // Push elements onto the stack
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);

    // Display the stack
    stack.display();

    // Peek the top element
    cout << "Top element: " << stack.peek() << endl;

    // Pop elements from the stack
    stack.pop();
    stack.pop();

    // Display the stack after popping
    stack.display();

    // Peek the top element again
    cout << "Top element: " << stack.peek() << endl;

    // Pop all elements
    stack.pop();
    stack.pop();

    // Try popping from an empty stack
    stack.pop();


    cout << "************************************  "<< endl;
    cout << "*********      QUEUE      **********  "<< endl;
    cout << "************************************  "<< endl;


     Queue q(5); // Create a queue with a capacity of 5

    q.enQueue(10);
    q.enQueue(20);
    q.enQueue(30);
    q.enQueue(40);
    q.enQueue(50);
    q.enQueue(60);

    q.display();

    q.deQueue();
    q.deQueue();

    q.display();

    q.enQueue(70);
    q.enQueue(80);

    q.display();

    cout << "Front element: " << q.getFront() << endl;
    cout << "Rear element: " << q.getRear() << endl;

    return 0;
}
