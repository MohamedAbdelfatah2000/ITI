#include <iostream>
#include "LinkedList.h"

using namespace std;

int main() {
    // Create a new linked list
    LinkedList list;

    // Add nodes to the list
    list.add(10);
    list.add(20);
    list.add(30);
    list.add(40);

    // Display the list
    cout << "Linked List after adding elements: ";
    list.display();

    // Get the count of nodes
    cout << "Count of nodes in the list: " << list.GetCount() << endl;

    // Get data by index
    int index = 2;
    cout << "Data at index " << index << ": " << list.GetDataByIndex(index) << endl;

    // Insert a node after a given node's data
    list.InsertAfter(25, 20);
    cout << "Linked List after inserting 25 after 20: ";
    list.display();

    // Insert a node before a given node's data
    list.InsertBefore(5, 10);
    cout << "Linked List after inserting 5 before 10: ";
    list.display();

    // Remove a node by its data
    list.removeNode(30);
    cout << "Linked List after removing 30: ";
    list.display();

    // Search for a data element in the list
    int searchData = 20;
    if (list.search_using_data(searchData)) {
        cout << "Element " << searchData << " found in the list." << endl;
    } else {
        cout << "Element " << searchData << " not found in the list." << endl;
    }

    // Display the final state of the list
    cout << "Final state of the linked list: ";
    list.display();

    return 0;
}
