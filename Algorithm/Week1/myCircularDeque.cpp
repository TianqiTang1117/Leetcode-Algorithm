class MyCircularDeque {
private:
    int* myCirDeque;
    int head;
    int tail;
    int maxLen;
    int curLen;
public:
    MyCircularDeque(int k) {
        myCirDeque=new int[k];
        head=1;
        tail=0;
        maxLen=k;
        curLen=0;
    }
    
    bool insertFront(int value) {
        if(isFull()){
            return false;
        }else{
            head--;
            head=(head+maxLen)%maxLen;
            myCirDeque[head]=value;
            
            curLen++;
            return true;
        }
    }
    
    bool insertLast(int value) {
        if(isFull()){
            return false;
        }else{
            tail++;
            tail=tail%maxLen;
            myCirDeque[tail]=value;    
            curLen++;
            return true;
        }
    }
    
    bool deleteFront() {
        if(isEmpty()){
            return false;
        }else{
            myCirDeque[head]=-1;
            head++;
            head=head%maxLen;
            curLen--;
            return true;
        }
    }
    
    bool deleteLast() {
        if(isEmpty()){
            return false;
        }else{
            myCirDeque[tail]=-1;
            tail--;
            tail=(tail+maxLen)%maxLen;
            curLen--;
            return true;
        }
    }
    
    int getFront() {
        if(isEmpty()){
            return -1;
        }
        return myCirDeque[head];
    }
    
    int getRear() {
        if(isEmpty()){
            return -1;
        }
        return myCirDeque[tail];
    }

    bool isEmpty() {
        return curLen==0;
    }
    
    bool isFull() {
        return curLen==maxLen;
    }

};