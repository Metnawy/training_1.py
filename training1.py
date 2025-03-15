class stack_ADT_array:
    '''
    here we define stack sequential class/data type which works according the paradigm of LIFO (last-in first-out)
    we use the array data structure to represents the stack 
    
    '''
    def __init__(self) -> None:
        self._list=[]
        self.top=self.peek()
        
        
    @property
    def list(self):
            return self._list

    @list.setter
    def list(self,data):
        if type(data)== list:
           self._list=data
        else:
            raise TypeError

              
    @property
    def top(self):
        return self.peek()
    @top.setter
    def top(self,data):
        pass 

    def push(self,data):
        self.list.append(data)
        
    
    def pop(self):
        if not  self.is_empty():
             
             return self.list.pop(-1)
        else:
            return "the stack is empty "
    
    def peek(self):
        if not self.is_empty():
          return self.list[-1]
        else:
            return "the stack is empty"

    # info 
    
    def is_empty(self):
        return len(self.list)==0
        
    def __len__(self):
        return len(self.list)
    def __repr__(self) -> str:
        return f"{self.list}"
        
class stack_ADT_singly_linked_list:
    '''
    objective: define stack class with paradigm LIFO using singly linked list as internal data structure 

    '''
    class _node:
        # _node class to define the nodes the basic unit of linked list internal data structure 
        def __init__(self,data=None,next=None) -> None:
            self.data=data
            self._next=next

        def __repr__(self) -> str:
            return f"{self.data}"

    def __init__(self) -> None:
        # using sentienal technique to build the linked list 
        self.tail=self._node()
        self.head=self._node(None,self.tail)
        self.size=0
        


    def push(self,data):
        
        new_node=self._node(data,self.head._next)
        self.head._next=new_node
        self.size+=1
    def peek(self):
        if self.size==0:
            return"the list is empty no top most value"
        else :
            return self.head._next.data
         
    def pop(self):
        if self.size==0:
            return "the list is empty no last value to pop out "
        else:
            value=self.head._next.data 
            self.head._next=self.head._next._next
            self.size-=1
            return value
    # info methods is_empty, length, string representation
    def is_empty(self):
        return self.size==0
    
    def __len__(self):
        return self.size
    
    def __repr__(self) -> str:
         if self.size==0:
             return "head-->tail"
         else:
             string="head-->"
             curser=self.head._next
             for i in range(self.size):
                string=string+str(f"{curser.data}")+"-->"
                curser=curser._next
             string=string+"tail"
             return string 
         
  
class stack_ADT_doublly_linked_list:
    '''
    objective: define stack class with paradigm LIFO using doublly linked list as internal data structure 

    '''
    class _node:
        def __init__(self,data=None,next=None,prev=None):
            self.data=data
            self._next=next
            self._prev=prev
        def __repr__(self) -> str:
            return f"{self.data}"
        
    def __init__(self) -> None:
        self.head=self._node()
        self.tail=self._node(None,None,self.head)
        self.head._next=self.tail
        self.size=0
    # operations methods 
    def push(self,data):
        new_data=self._node(data,self.tail,self.tail._prev)
        self.tail._prev._next=new_data
        self.tail._prev=new_data
        self.size+=1

    def peek(self):
        if self.size==0:
            return "it's empty list"
        else:
            return self.tail._prev
        
    def pop(self):
        if self.size==0:
            return "it's empty list "
        else:
            node=self.tail._prev
            pre_last=self.tail._prev
            pre_last._next=self.tail
            self.tail._prev=pre_last
            self.size-=1
            return node
    # info about the class instance   
    def is_empty(self):
        return self.size==0
    
    def __len__(self):
        return self.size
    
    def __repr__(self) -> str:
        if self.size==0:
            return "head-->tail"
        
        else:
            curser=self.head._next
            string="head-->"

            for _ in range(self.size):
                string=string+f"({curser.data})"+" -->"
                curser=curser._next
            string=string+"tail"
            return string




class queue_doublly_linked_list:
    '''
    objective: create a list with the paradigm FIFO ( first in - first out)
    '''
    class _node:
        def __init__(self,data=None,next=None,prev=None):
            self.data=data
            self._next=next
            self._prev=prev
        
        def __repr__(self) -> str:
            return f"{self.data}"
    
    def __init__(self):
        self.head=self._node()
        self.tail=self._node(None,None,self.head)
        self.head._next=self.tail
        self.size=0
    #operations
    def queue(self,data):
        # add a new node to the queue according to FIFO 
        new_node=self._node(data,self.tail,self.tail._prev)
        pre_tail=self.tail._prev

        pre_tail._next=new_node
        self.tail._prev=new_node
        self.size+=1

    def dequeue(self):
        first=self.head._next
        after_first=self.head._next._next

        self.head._next=after_first
        after_first._prev=self.head
        value=first.data
        first._next=first._prev=first.data=None
        self.size-=1
        return value 

    def first(self):
        return self.head._next.data

    #info
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0 
    def __repr__(self) -> str:
        if self.size==0:
            return "head-->tail"
        else:
            string="head-->"
            curser=self.head._next
            for _ in range(self.size):
                string=string+f"({curser.data})"+"-->"
                curser=curser._next
            string=string+"tail"
            return string
     

    def concatenate(self,second):
        if isinstance(second,queue_doublly_linked_list):
            # we will denote first list as q1 and second list as q2 
            last_q1=self.tail._prev
            first_q2=second.head._next
            last_q2=second.tail._prev

            #swapping steps
            last_q1._next=first_q2
            first_q2._prev=last_q1

            last_q2._next=self.tail
            self.tail._prev=last_q2
            second.head._next=second.tail
            second.tail._prev=second.head

            self.size+=second.size
            second.size=0
        else:   
          raise TypeError
x=queue_doublly_linked_list()



y=queue_doublly_linked_list()



class singlly_recursive:
    class _node:
        def __init__(self,data,rest=None) -> None:
            self.data=data
            self.rest=rest

    def __init__(self,data=None) -> None:
        self.head=self._node(data)
        self.size=1 if data!=None else 0 
        
    def add(self,data):
        if self.size==0:
            self.head=self._node(data)
            self.size+=1
        else:
            new_node=self._node(data,self.head)
            self.head=new_node
            self.size+=1

    def delete_first(self):
        if self.size==0:
            return None
        else:
            data=self.head.data
            self.head=self.head.rest
            self.size-=1
            return data
    def delete_last(self): 
        if self.size==0:
            return None
        else:
            first=self.head
            second=self.head
            flag=1
            for i in range(self.size):
                if flag:
                    if second.rest==None:
                        value=second.data
                        first.rest=None
                        self.size-=1
                        flag=0
                        return value
                    else:
                        second=second.rest
                        flag=0
                else:
                    if second.rest==None:
                        value=second.data
                        first.rest=None
                        self.size-=1
                        
                        return value
                    else:
                        first=first.rest
                        second=second.rest

                        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
   

    def __repr__(self) -> str:
        if self.size==0:
            return "none"
        else:
            l=[]
            curser=self.head
            for i in range(self.size):
                l.append(str(curser.data))
                curser=curser.rest
            x= "-->".join(str(n) for n in l)
            return x
class singlly_reccursive_methods:
    class _node:
        def __init__(self,data):
            self.data=data
            self.rest=None
        def __repr__(self) -> str:
            return f"{self.data}"
        
    def __init__(self,data=None):
        self.head=self._node(data)
        self.size=1 
    
    def add_last(self,data):
        def helper(node,data):
            if node.rest==None:
               node.rest=self._node(data)
               self.size+=1
            else:
                helper(node.rest,data)

        if self.size==0:
             self.head=self._node(data)
             self.size+=1
        elif self.size==1 and self.head.data==None:
            self.head.data=data
        else:
            helper(self.head,data)

    def add_first(self,data):
        if self.size==1 :
            if self.head.data==None:
                self.head.data=data
                return 
        new_data=self._node(data)
        new_data.rest=self.head
        self.head=new_data
        self.size+=1
    

    def delete_first(self):
        if self.size==0:
            return None
        else:
            data=self.head.data
            self.head=self.head.rest
            self.size-=1
            return data 
        
    def delete_last(self):
        def helper(node):
            if node.rest.rest==None:
                data=node.rest.data
                node.rest=None
                return data
            else:
               return helper(node.rest)


        if self.size==0:
            return "None"
        else:
            if self.head.rest==None:
                data=self.head.data
                self.head.data=None
                return data 
            else:
                self.size-=1
                return helper(self.head)
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
    
    def __repr__(self) -> str:
        
        if self.size==0:
            return "none"
        #if self.size==1 and self.head.data==None:
           # return "none"
        
        else:
            curser=self.head
            new=[]

            for i in range(self.size):
                new.append(curser.data)
                curser=curser.rest
            
            print(new)
            return "--".join(str(n) for n in new)

class singally_recursive:

    def __init__(self,data=None,tail=None):
        self.head=data
        self.tail=tail

    #operation
    def add_first(self,data) :
        if self.head==None:
            self.head=data
            self.tail=singally_recursive()
        else:
            past_head=self.head
            past_tail=self.tail
            self.head=data
            self.tail=singally_recursive(past_head)
            self.tail.tail=past_tail
    
    def add_last(self,data):
        
        if self.head==None:
            self.head=data
            self.tail=singally_recursive()
        else:
            self.tail.add_last(data)
    def delete_first(self):
        if self.head==None:
            return "it's already empty"
        else:
            if self.tail.head==None:
                value=self.head
                self.head=None
                return value
            else:
                value=self.head
                self.head=self.tail.head
                self.tail=self.tail.tail
                return value
    def delete_last(self):
        def helper(self):
            if self.tail.head==None:
                value=self.head
                self.head=None
                return value
            else:
                return helper(self.tail)
        if self.head==None:
            return "it is already empty"
        else:
            return helper(self)
    
    #info
    def is_empty(self):
        return self.head==None 
    
    def __len__(self):
        number=0
        def counting(self):
            if self.head==None:
                return 0
            else:
               return 1+counting(self.tail)
        return counting(self)

    def __repr__(self) -> str:
        if self.head==None:
            return "head-->tail"
        string=""
        curser=self
        while curser.head:
            string=string+f"{curser.head} "
            curser=curser.tail
        return string

# Test cases
list1 = singlly_reccursive_methods(10)
print(list1)  # Output: [10]
print(list1.size)
print("\n")
list1.add_last(20)
print(list1)  # Output: [20, 10]
print(list1.size)
print("\n")
print(list1.delete_first())
print(list1)  # Output: [10]
print("\n")
list1.delete_last()
print(list1)  # Output: []
print("\n")
# Create a larger list
list2 = singlly_reccursive_methods(1000)
print(list2.delete_last())
print(list2)
for i in range(2, 11):

    list2.add_first(i)
    list2.add_last(i*3)
    
    



print(list2)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Test deleting multiple elements
while not list2.is_empty():
    print(list2.delete_first())


print("pppppppppp")

x=singally_recursive()
print(x,len(x))
x.add_first(5)
print(x,len(x))
x.add_last(10)
x.add_first(500)
print(x,len(x))
print(x.delete_last())
print(x,len(x))