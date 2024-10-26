#Merge Sort 
def mergeSort(a,low,high): 
    # Base case: Only proceed if low index is less than high index
    if low<high: 
        mid=(low+high)//2 
        # Recursively sort the left half
        mergeSort(a,low,mid) 
        # Recursively sort the right half
        mergeSort(a,mid+1,high) 
      # Merge the two sorted halves
        merge(a,low,high,mid) 
def merge(a,low,high,mid): 
    left=a[low:mid+1] 
    right=a[mid+1:high+1] 
    i=0 
    j=0 
    k=low 
   
    while i<len(left) and j<len(right): 
        if left[i]<right[j]: 
            a[k]=left[i] 
            i+=1 
        else: 
            a[k]=right[j] 
            j+=1 
        k+=1 
    while i<len(left): 
        a[k]=left[i] 
        i+=1 
        k+=1 
    while j<len(right): 
        a[k]=right[j] 
        j+=1 
        k+=1 
a=list(map(int,input('Enter the list of elements:').split())) 
print('Before Merge sorting:',a) 
mergeSort(a,0,len(a)-1) 
print('After Merge Sorting:',a) 
