#ifndef NODE_H
#define NODE_H


class Node
{
    public:

        int data;
        Node * Left,*Right;
        Node(int data) {
            this->data=data;
            Left=Right=NULL;

        }
        ~Node() {}

    protected:

    private:
};

#endif // NODE_H
