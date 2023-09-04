# ALGORITHM palindrome_words
# VAR
pal = input("Entrez un mot : ")  # L'utilisateur entre le mot
i = len(pal)
j = i - 1
k = 0

# BEGIN
while k < j:
    if pal[k] == pal[j]:
        k = k + 1
        j = j - 1
    else:
        print("Le mot n'est pas un palindrome")
        break
else:
    print("Le mot est un palindrome")
