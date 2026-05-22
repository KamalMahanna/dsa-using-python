def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransome_dict={}
    magzine_dict = {}
    
    for i in ransomNote:
        ransome_dict[i] = ransome_dict.get(i,0)+1
    
    for i in magazine:
        if i in ransome_dict:
            magzine_dict[i]=magzine_dict.get(i,0)+1
    print(ransome_dict, magzine_dict)
    for i in ransome_dict:
        if magzine_dict[i]<ransome_dict[i]:
            return False
    return True

print(canConstruct("a","b"))