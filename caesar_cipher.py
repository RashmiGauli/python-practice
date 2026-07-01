user_input = input("write anything you want:\n").lower()

shift = int(input("by how much letter you want to shift?:"))

options = int(input("enter 1 for encrypt and 2 for decrypt: "))


result = ''
for i in user_input:
    if i == " ":
        answer = " "
    else:
        match options:
            case 1:
                answer = chr((ord(i)-ord('a') + shift)%26 + ord('a'))
                
            case 2:
                answer = chr((ord(i)-ord('a')-shift)%26 + ord('a'))
    result += answer
print(result)