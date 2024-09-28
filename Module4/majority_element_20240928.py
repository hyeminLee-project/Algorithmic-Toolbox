def majority_element(elements):
    # Phase 1: Find the candidate for majority element
    candidate = None
    count = 0
    
    for element in elements:
        if count == 0:
            candidate = element
        count += (1 if element == candidate else -1)
    
    # Phase 2: Verify the candidate
    count = 0
    for element in elements:
        if element == candidate:
            count += 1
    
    # Check if the candidate occurs more than n/2 times
    if count > len(elements) // 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
