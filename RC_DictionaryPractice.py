#Ruhika Chatterjee
#Python Period 5
#February 5, 2016
#Create a dictionary to translate between languages

#Trnslation: English to Bangla (English transcription)
#Assumption: The user will only enter words that are present in the dictionary

DICTIONARY = {'my':'amar', 'your':'tomar', 'how are you':'kamon aacho', 'hand':'haat', 'hurts':'baatha korche', 'life':'jibon', 'face':'mukh', 'tea':'chha', 'tree':'gachh', 'and':'ebom', 'also':'aar', 'because':'koran'}

def getSentence ():
    print ('Welcome to the Bangla Translator.')
    print ('You can now translate your sentences from english to bangla!')
    print ()
    sentence = input ('Enter the sentence you would like to translate: ')
    return sentence.lower().split()

def getTranslation (sentence):
    for i in range(len(sentence)):
        sentence[i] = DICTIONARY[sentence[i]]
    return sentence
    
def main():
    sentence = getSentence ()
    translation = getTranslation (sentence)
    print ('It is "' + ' '.join(translation) + '" in bangla.')
    
main()
