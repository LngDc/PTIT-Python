def check(string):
    return string == string[::-1]

def main():
    revs, max = [], 0
    
    for line in open('VANBAN.in', 'r'):
        words = line.strip().split()
        
        for word in words:
            if check(word):
                revs.append(word)      
                if len(word) > max:
                    max = len(word)
                    
    res = {}
    for rev in revs:
        if len(rev) == max:
            res[rev] = res[rev] + 1 if rev in res.keys() else 1
                
    for item in res.items():
        print(*item)
    


if __name__ == '__main__':
    main()