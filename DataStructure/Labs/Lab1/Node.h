#ifndef NODE_H
#define NODE_H


class Node
{
    public:
        Node * Prev,*Next;
        int Data;
        Node(int data){
            Data=data;
            Prev=Next=NULL;
        }

    protected:

    private:
};

#endif // NODE_H
