#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include "Node.h"
using namespace std;

class LinkedList
{
    private:
        Node * head;
        Node * tail;

        Node * getNodeUsingData(int data)
        {
            Node *current=head;
            while(current != NULL)
            {
                if(current->Data==data)
                {
                    return current;
                }
                //Jump
                current=current->Next;
            }
        return NULL;
      }


    public:

        LinkedList() {
            head=tail=NULL;
        }

        void add(int data){
            //Create Node
            Node * node = new Node(data); //Create Object Node

                if(head == NULL){    //First Node
                    head=tail=node;
                }
                else{                        //Not First Node
                    tail->Next =node;
                    node->Prev=tail;
                    tail=node;
                }
        }

        void display(){
            Node * current =head;
            if(current == NULL){
                cout<<"Linked List is Empty \n";
                return ;
            }
            while(current != NULL){
                cout<<current->Data<<" ----> ";
                current=current->Next;
            }
            cout<<endl;
        }


    void removeNode(int data){
        //Search Linked List
        Node * node = getNodeUsingData(data);
        if(node == NULL){
            cout<<"Element Not Found , Can't Remove \n";
            return;
        }
        else{
            //Remove First
            if(node == head)
                {
                    if(node == tail){
                        tail=head=NULL;
                        }
                    else{
                        head=node->Next;
                        head->Prev=NULL;
                        }
                }
            else if (node == tail){ //Remove Last
                tail=node->Prev;
                tail->Next=NULL;
            }
            else{                       //Remove Mid
                Node * A=node->Prev;
                Node * B=node->Next;
                A->Next=B;
                B->Prev=A;
            }

            delete(node);

        }

    }

    int search_using_data(int data){
        Node * node = getNodeUsingData(data);
        if(node == NULL){
            return 0;
        }
        else{
            return 1;
        }
    }

    //===================================================
    //===================================================
    //===================================================

    int GetCount() {
    int count = 0;
    Node *current = head;
    while (current != NULL) {
        count++;
        current = current->Next;
    }
    return count;
      }


      int GetDataByIndex(int index) {
            if (index < 0) {
                cout << "Invalid index.\n";
                return -1;
            }

            Node *current = head;
            int currentIndex = 0;

            while (current != NULL) {
                if (currentIndex == index) {
                    return current->Data;
                }
                current = current->Next;
                currentIndex++;
            }

        cout << "Index out of range.\n";
        return -1;
    }



      void InsertAfter(int data, int afterData) {
            Node *current = getNodeUsingData(afterData);
            if (current == NULL) {
                cout << "Node with data " << afterData << " not found.\n";
                return;
                }

                Node *newNode = new Node(data);

                newNode->Next = current->Next;
                newNode->Prev = current;

                if (current->Next != NULL) {
                    current->Next->Prev = newNode;
                } else {
                    tail = newNode;  // Update tail if inserting at the end
                }

                current->Next = newNode;
            }


        void InsertBefore(int data, int beforeData) {
            Node *current = getNodeUsingData(beforeData);
            if (current == NULL) {
                cout << "Node with data " << beforeData << " not found.\n";
                return;
            }

            Node *newNode = new Node(data);

            newNode->Next = current;
            newNode->Prev = current->Prev;

            if (current->Prev != NULL) {
                current->Prev->Next = newNode;
            } else {
                head = newNode; // Update head if inserting at the beginning
            }

            current->Prev = newNode;
        }


};

#endif // LINKEDLIST_H
