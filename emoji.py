message = input(">")
words=message.split(' ')
emojis = {
       "happy": "😁",
       "sad": "😢",
        "love": "❤💕",
        "boy" :  "🤷‍",
        "girl" : "🤷‍"
}
output = ""
for w in words:
    output+=emojis.get(w,w)+ " "
print(output)
