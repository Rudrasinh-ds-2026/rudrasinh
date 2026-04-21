def predict_college(percentile):
    print(f"\n--- GUJCET{percentile} %ile Report ---")

    if percentile >=91:
        print("Result: MSU CS mil sakta hai.try karo!")
    elif percentile >=85:
        print("Result: MSU IT Best Option")
        print("Backup: DDU CS ya Parul AI-DS")
    elif percentile >=75:
        print("Result: Parul CS / SVIT CS pakka")
    else:
        print("Result: Private college options dekho")

    print("Tip: College se zyada Skill matter karti hai.")
    print("Day 4: Function bhi aa gaya")


my_percentile=85
predict_college(my_percentile)

predict_college(92)
predict_college(78)
    
    
