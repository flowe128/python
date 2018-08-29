#!/usr/bin/python

# Get sentence from user

original = raw_input("Please enter your sentence: ").strip().lower()

# Split sentance into words
words = original.split()
print(words)

# Loop through the words and convert to pig latin

new_words = []

for word in words:
   #print(word)
   if word[0] in "aeiou":
      new_word = word + "yay"
      new_words.append(new_word)
   else:
      vowel_pos = 0
      for letter in word:
         if letter not in "aeiou":
            vowel_pos = vowel_pos + 1
         else:
           break 
      cons = word[:vowel_pos]
      the_rest = word[vowel_pos:]
      new_word = the_rest + cons + "ay"
      new_words.append(new_word)

print(new_words)
      

# if the word starts with a vowel, just add "yay"



# Otherwise, move the first consonant cluster to end and add "ay"


# Stick words back together

output = " ".join(new_words)

# Output the final string
print(output)


