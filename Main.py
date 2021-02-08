#Driver Code    
   
if __name__=="__main__":
    a=BinaryIndexedTree()
    a.Construct(4)
    a.Update(3,6)
    print(a.Get_Item(4))
    print(a.Prefix_Sum(2))
    print(a.Range_Sum(-2,1))
    print(a.Frequency())
