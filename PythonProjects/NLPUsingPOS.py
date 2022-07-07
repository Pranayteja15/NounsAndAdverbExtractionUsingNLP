
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

def NounAndAdverbExtractor(text):
    
    print('NOUNS AND ADVERBS EXTRACTED FROM THE GIVEN TEXT:')
    
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP' or tag =="RB" :
                print(word)

text =  "Sara ran very quickly to school"
NounAndAdverbExtractor(text)