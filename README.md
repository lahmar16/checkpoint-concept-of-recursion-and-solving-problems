# checkpoint-concept-of-recursion-and-solving-problems
ALGORITHM palindrome-words
VAR
pal : ARRAY_OF type[length];
i=length[pal]
j=i-1
k=0
BEGIN
WHILE (k<j) DO
IF (pal[k]=pal[j]) THEN
k=k+1
j=j-1
write"word is palindrome"

END_IF
END_WHILE

ELSE
write"word is not palindrome"

END
