import numpy as np
from nltk import word_tokenize
from nltk import pos_tag

def load_data(df):
    X = np.array([]).reshape(0,vector_size)
    Y = np.array([])
    for sentenceID, labels in label_dict.items():
        if df[df.sentenceID == sentenceID].empty:
            print('empty')
            continue
        else: 
            sentence = df[df.sentenceID == sentenceID]['sentenceText'].values[0]
            print(sentence)
        #print(sentence, type(sentence))
            
        tok_sentence = word_tokenize(sentence)
        tok_sentence_pos = [ word + '_' + pos for word, pos in pos_tag(tok_sentence, tagset=None)]

        for word, label in zip(tok_sentence_pos, labels):
            word_vector = word_vectors[word]
            print(word_vector, label)
            X = np.vstack((X, word_vector))
            Y = np.append(Y, label)       
    return X, Y
