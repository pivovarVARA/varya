def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

 ciphertext = ""
 m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 z = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 while shift >= 26:
  shift -= 26
 for i in range(len(plaintext)):
  l = 0
  for j in range(26):
   if plaintext[i] == m[j]:
    l = 1
  for j in range(26):
   if plaintext[i] == z[j]:
    l = 1
  if l == 0:
   ciphertext += plaintext[i]
  else:
   if plaintext[i].islower():
    index = m.index(plaintext[i])
    if index + shift < 26:
     index += shift
     ciphertext += m[index]
    else:
     index = index + shift - 26
     ciphertext += m[index]      
   else:
    index = z.index(plaintext[i])
    if index + shift < 26:
     index += shift
     ciphertext += z[index]
    else:
     index = index + shift - 26
     ciphertext += z[index]

        
 return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
 
 plaintext = ""
 m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 z = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 while shift >= 26:
  shift -= 26
 for i in range(len(ciphertext)):
  l = 0
  for j in range(26):
   if ciphertext[i] == m[j]:
    l = 1
  for j in range(26):
   if ciphertext[i] == z[j]:
    l = 1
  if l == 0:
   plaintext += ciphertext[i]
  else:
   if ciphertext[i].islower():
    index = m.index(ciphertext[i])
    if index - shift >= 0:
     index -= shift
     plaintext += m[index]
    else:
     index = index - shift + 26
     plaintext += m[index]      
   else:
    index = z.index(ciphertext[i])
    if index - shift >= 0:
     index -= shift
     plaintext += z[index]
    else:
     index = index - shift + 26
     plaintext += z[index]

 return plaintext
