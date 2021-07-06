# DailyChallengeSolutions
Solutions for daily challenges

1.Write a script that sorts an input string alphanumerically and removes duplicates.
  
  Answer:
word = sorted(list(set(input().split())))
print(" ".join(word))
