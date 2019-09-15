import GoogleNatLangAPI as GNL
import time

g = raw_input("Enter your name : ")
print('Working'),
for i in range(10):
    print('.'),
    time.sleep(0.25)
print('')
print(g)
#test = GNL.GetSentiment('Hello world, this is a test')
#print(test)
