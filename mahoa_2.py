P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1:
    input_string = input()
    if input_string == "0":
        break
    
    K, plain_text = input_string.split(" ")
    K = int(K)
    
    result_string = str()
    for letter in plain_text[::-1]:
        new_pos = (P.index(letter) + K) % 28
        result_string += P[new_pos]
        
    print(result_string)
    
    
        