# words = "artificials"

words = "abcdefghijklmnopqrstuvwxyz"

vowel_count = 0

for ch in words:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch,"→ vowel")
        vowel_count+=1
    else:
        print(ch, "→ consonant")

print("Vowel Count = " , vowel_count)
