import pyjokes
import os

joke = pyjokes.get_joke()
folder = 'C:/Users/Gavin'

print(joke)
print(os.listdir(folder))

