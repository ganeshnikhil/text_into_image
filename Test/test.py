import textwrap 

def text_balance(text , width):
   wrapper = textwrap.TextWrapper(width=width) 
   return wrapper.wrap(text=text)


text = ''' hello  how are you my friend what the fuck are you doing nothing and fucking the fuck out of you '''
new_text = "\n".join(text_balance(text , 20))
print(new_text)