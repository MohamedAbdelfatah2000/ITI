#include <iostream>
#include "LinkedList.h"
using namespace std;

/////////////////////////////////////////////////////// 1- ///////////////////////////////////////////////////
void linearSearch(int arr[], int size, int target) { //Finding all the occurrences
    int indices[size];
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            indices[count++] = i;
        }
    }

    if (count == 0) {
        cout << "Element not found in the array." << endl;
    } else {
        cout << "Element " << target << " found at indices: ";
        for (int i = 0; i < count; i++) {
            cout << indices[i] << "   ";
        }
        cout << endl;
    }
}


/////////////////////////////////////////////////////// 2- ///////////////////////////////////////////////////
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            left = mid + 1; // Search in the right half
        } else {
            right = mid - 1; // Search in the left half
        }
    }

    return -1;
}

/////////////////////////////////////////////////////// 3- ///////////////////////////////////////////////////

   void LinkedList::bubbleSort()  {
        if (!head){ //No linkedlist created
         return;
         }

        bool swapped;
        Node* current;

        do {
            swapped = false;
            current = head;

            while (current->Next) {

                 if (current->Data  >  current->Next->Data) {
                    int temp = current->Data;
                    current->Data = current->Next->Data;
                    current->Next->Data = temp;

                    swapped = true;
                }
                current = current->Next;
            }
        } while (swapped);
    }

///////////////////////////////////////////////////////// Main //////////////////////////////////////////////////////

int main() {

    cout<<"Testing the linearsearch                 "<<endl;
    cout<<"*************************************"<<endl;
    int arr[] = {1, 2, 4, 2, 8, 2};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 2;

    linearSearch(arr, size, target);

    cout<<"*************************************"<<endl;
    cout<<"Testing the binarysearch                 "<<endl;
    cout<<"*************************************"<<endl;
    int arr2[] = {1, 3, 5, 7, 9, 11, 13};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int target2;

    cout << "Array: ";
    for (int i = 0; i < size; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;

    cout << "Enter the target element to search: ";
    cin >> target2;

    int result = binarySearch(arr2, size2, target2);

    if (result != -1) {
        cout << "Element " << target2 << " found at index " << result << "." << endl;
    } else {
        cout << "Element " << target2 << " not found in the array." << endl;
    }




    cout<<"*************************************"<<endl;
    cout<<"Testing the bubblesort in linkedlist (data only)                 "<<endl;
    cout<<"*************************************"<<endl;

    LinkedList list;

    list.add(10);
    list.add(8);
    list.add(60);
    list.add(4);
    list.add(20);

    cout << "Original List: ";
    list.display();

    // Sort the list using bubble sort
    list.bubbleSort();

    cout << "Sorted List: ";
    list.display();

    return 0;
}

