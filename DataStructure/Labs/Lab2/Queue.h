#ifndef QUEUE_H
#define QUEUE_H

using namespace std;

class Queue {
private:
    int *arr;
    int front;
    int rear;
    int size;
    int count;

public:
    Queue(int s) {
        size = s;
        arr = new int[size];
        front = -1;
        rear = -1;
        count = 0;
    }

    bool isEmpty() {
        return count == 0;
    }

    bool isFull() {
        return count == size;
    }

    void enQueue(int data) {
        if (isFull()) {
            cout << "Queue is full. Cannot enqueue " << data << endl;
            return;
        }

        if (front == -1){
                front = 0;
        }

        rear = (rear + 1) % size;
        arr[rear] = data;
        count++;
        cout << "Enqueued: " << data << endl;
    }

    void deQueue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue.\n";
            return;
        }

        cout << "Dequeued: " << arr[front] << endl;
        front = (front + 1) % size;
        count--;

        if (count == 0) {
            front = -1;
            rear = -1;
        }
    }

    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty.\n";
            return -1;
        }
        return arr[front];
    }

    int getRear() {
        if (isEmpty()) {
            cout << "Queue is empty.\n";
            return -1;
        }
        return arr[rear];
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty.\n";
            return;
        }

        cout << "Queue contents: ";
        int  i = front;
        for (int counter = 0 ; counter< count ; counter++) {
            cout << arr[i] << " \t";
            i = (i + 1) % size;
        }
        cout << endl;
    }
    ~Queue() {
        delete[] arr;
    }
};

#endif // QUEUE_H
