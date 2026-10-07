from gtts import gTTS
from playsound import playsound

print("Today I Will Tell You A Story !")
print("To Know Why It Is Necessary To Think Before You Act!")
print("This Story Is About A Farmer, His Wife & Their Goose.")

farmer=input("What Is The Name Of the Farmer? ")
wife=input("What Is The Name Of the Farmer's Wife? ")
goose=input("What Is The Name Of the Goose? ")

story="""Once Upon A Time, """+farmer+""" Had A Goose Named """+goose+""" That Laid A Golden Egg Every Day.The Egg Provided Enough Money For """+farmer+""" & His Wife, """+wife+""" For Their Day-To-Day Needs.
"""+farmer+""" & """+wife+""" Were Happy For A Long Time. But One Day,"""+farmer+""" Got An Idea & Thought, "Why Should I Take Just 1 Egg A Day? Why Can't I Take All Of Them At Once & Make A Lot Of Money?"
Foolish """+wife+""" Also Agreed & Decided To Cut """+goose+"""'s Stomach For The Eggs.As Soon As They Killed """+goose+""" & Opened Its Stomach, They Found Nothing But Guts & Blood. """+farmer+""", Realising His Foolish Mistake Cried Over The Lost Resource!"""

saystory=gTTS(text=story,lang='en',slow=False)
saystory.save("GoldenEggsStory.mp3")
playsound("GoldenEggsStory.mp3")
