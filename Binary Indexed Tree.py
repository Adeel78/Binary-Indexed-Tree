
class BinaryIndexedTree():
    
    def __init__(self):
        self.flag=False
        self.count=0        
 
 
    
#This func will construct a BIT of given size    

    def Construct(self,size):
 
        self.size = size
        self.tree = [0]*(self.size + 1)
        
        for i in range(1,self.size+1):
        	self.count+=1
        	print("Enter "+str(i)+"th Node: ")
        	b=int(input())
        	self.Update(i,b)


#This function will return the No.of child nodes present at a given node
#as well as help us to find the no.of Parents node of a given node
        	        	
    def LSB(self,i):
    	return i & (-i)



#This function will Update the given node by adding the given val
#As well as update  all its parent nodes by adding given val in it
    	    	    	
    def Update(self, node_ind, val):
        
        if node_ind<1 or node_ind>self.count:
            return "Out of index"
        
        
        while node_ind <= self.size:
            self.tree[node_ind] += val
            node_ind += self.LSB(node_ind)


                                                    
#This function will return size of BIT
                        
    def Size(self):
    	
    	return ("Size of BIT is "+str(self.count))
    


#This function will return value of given node
                
    def Get_Item(self, idx):
        if idx<1 or idx>self.count:
        	return "Out of index"
        if idx==1:
        	return self.Prefix_Sum(idx)
        return self.Prefix_Sum(idx)-self.Prefix_Sum(idx-1)
        


#This function will return all the values as a list
                
    def Frequency(self):
                
        freq=[0]*(self.size)
        for i in range(1,self.size+1):
                if i==1:
                        freq[i-1]=self.Prefix_Sum(i)
                else:
                        freq[i-1]=self.Prefix_Sum(i)-self.Prefix_Sum(i-1)
        return freq
                		
                
                
 #This function will return Sum of all the values of nodes present between given range               
                                
    def Range_Sum(self, node_ind1,node_ind):
                     
       
        if node_ind >self.count or node_ind1 >self.count or node_ind1<1 or node_ind<1:
            return("Out of index")
        
        self.flag=True
        if node_ind1>node_ind:
            

                         
        
            a=self.Prefix_Sum(node_ind1)
            self.flag=True
            b=self.Prefix_Sum(node_ind-1)
            return a-b
        
        else:
        
            a=self.Prefix_Sum(node_ind)
            self.flag=True
            b=self.Prefix_Sum(node_ind1-1)
            return a-b              	        	

        
        
        
 #This function will return Sum of all the values of nodes present between given 1st node to two given node
                 
        
          
    def Prefix_Sum(self,node_ind):
       	
       if node_ind >self.count or (node_ind<1 and self.flag==False) :

        	
            return("Out of index")        	
      
     
       self.flag=False                                                              
       curr_sum = 0
       while node_ind:
            curr_sum += self.tree[node_ind]
            node_ind -= self.LSB(node_ind)
       
            
                    
       return curr_sum

              

