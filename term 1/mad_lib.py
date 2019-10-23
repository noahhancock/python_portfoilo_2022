user=input("what is your name ")
word1=input("enter a name ")
word2=input("enter something  ")
word3=input("enter a place ")
word4=input("enter a funny word ")

text=str.format("""
Mad Lib: Squigly's Surprise | Squigly's Playhouse

There was once a girl called {} who was 10 years old. One {} as she was walking through the {} with her twin brother, Joe, she stopped at a store called, "Magical Wishes". She was very curious about this store, and quickly grabbed her twin's hand and rushed through the crowds of people. Suddenly, out of nowhere, a strange man appeared.
"Pleased to meet you...Oh, you're twins!" He seemed delighted.

"Oh...err..." began one of the twins.

"Oh, my name is..." The man gestured "... My name is...THE FANTASTIC MR SPARKS!!!" he cried.

"Oh, erm...Mr Sparks...Can we see the supervisor?" asked the children, curiously.

"Ooooh, ceeerrrttaaiinnllyy!!!" he seemed too mysterious to describe-the way he said everything, how he dressed, the way he gestured!

The twins followed him and to their great surprise there sat Squigly, smiling, showing all his teeth.

"Oooh, Squigly!" gasped the twins. Squigly was a great friend of theirs, and he was great at making small gadgets into large inventions.

"Oi, hello twins!" he said with a slight touch of his {} accent. He was losing it somehow now that he had come to a foreign country. "What a pleasant surprise."

And they talked and talked and talked.""",word1,word2,word3,word4)
print("this is your mad-lib " + user)
print(text)
