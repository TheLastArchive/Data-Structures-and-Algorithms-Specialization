# Uses python3
def edit_distance(s, t):
    #write your code here
    s = list(s.lower())
    t = list(t.lower())
    D = []
    #Construct 2D array
    first_row = []
    first_row.extend(range(0, len(t) + 1))
    D.append(first_row)
    for i in range(1, len(s) + 1):
        D.append([0] * (len(t) + 1))
        D[i][0] = i
        
    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            distance = []
            #Insertion
            distance.append(D[i][j-1] + 1)
            #Deletion 
            distance.append(D[i-1][j] + 1)
            if (s[i-1] == t[j-1]):
                #Match
                distance.append(D[i-1][j-1])
            else:
                #Mismatch
                distance.append(D[i-1][j-1] + 1)
            
            D[i][j] = min(distance)
    
    return D[-1][-1]

if __name__ == "__main__":
    # print(edit_distance("editing", "distance"))
    print(edit_distance(input(), input()))
