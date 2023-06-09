def main():
    N = int(input())
    scores = list(map(float, input().split()))
    
    score_max = max(scores)
    score_min = min(scores)
    
    scores_fixed = [score for score in scores if score != score_max and score != score_min]
    avg = sum(scores_fixed) / len(scores_fixed)
    
    print(round(avg, 2))
    
    
    

if __name__ == '__main__':
    main()  