#ifndef TREE_H
#define TREE_H

#include "Node.h"
using namespace std;

class Tree {
    Node * root;

public:
    Tree() {
        root = NULL;
    }

    void add(int data) {
        Node * newNode = new Node(data);
        Node * parent = NULL;

        if (root == NULL) {
            root = newNode;
        } else {
            Node * current = root;
            while (current != NULL) {
                parent = current;
                if (data > current->data) {
                    current = current->Right;
                } else {
                    current = current->Left;
                }
            }
            if (data > parent->data) {
                parent->Right = newNode;
            } else {
                parent->Left = newNode;
            }
        }
    }

    Node * getNodeByData(int data) {
        Node * current = root;
        while (current != NULL) {
            if (data == current->data) {
                return current;
            }
            if (data > current->data) {
                current = current->Right;
            } else {
                current = current->Left;
            }
        }
        return NULL;
    }

    int getMaxDepth() {
        return calculateDepth(root);
    }

private:
    int calculateDepth(Node * node) {
        if (node == NULL) {
            return 0; // Base case: empty tree has depth 0
        }

        // Recursively calculate depth of left and right subtrees
        int leftDepth = calculateDepth(node->Left);
        int rightDepth = calculateDepth(node->Right);

        // Depth of the current node is 1 + max depth of subtrees
        return 1 + max(leftDepth, rightDepth);
    }
};

#endif // TREE_H

