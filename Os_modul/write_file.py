text = "yooooooo \nThis is some text\nHave a good one!\n"

# -------- this is only write and over write files method --------
with open('test2.txt', 'w') as file:
    file.write(text)

# ------ this method is append a new line with current files ----------
text2 = "this is new line with appending mode \nHave a good day! :)"
with open('test2.txt','a') as file:
    file.write(text2)