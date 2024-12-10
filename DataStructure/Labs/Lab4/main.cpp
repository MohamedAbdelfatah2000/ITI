#include <iostream>
#include "Tree.h"
using namespace std;

int main() {
    Tree tr;
    tr.add(20);
    tr.add(50);
    tr.add(10);
    tr.add(30);
    cout << "Maximum Depth: " << tr.getMaxDepth() << endl;
    return 0;
}
