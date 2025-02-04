def H_index(citations):
    # Sort citations in descending order
    citations.sort(reverse=True) 

    # Iterate through the papers and check if that citations at that is less than ... and return the ....
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
        
        # Else the condition is satisfied and you should return the length of citations
    return len(citations)
    
print(H_index([3,0,6,1,5]))  # [6, 5, 3, 1, 0]
print(H_index([11, 15]))