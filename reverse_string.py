stack = []

text = input("Enter Text: ")
print(f"Normal: {text}")


for ch in text:                        #  Time Complexity O(n)
    stack.append(ch)

reverse=""
while stack:                                   # Time Complexity O(n)
    reverse+=stack.pop()
print(f"Reverse : {reverse}")

                                                    #Space Complexity   O(n)
