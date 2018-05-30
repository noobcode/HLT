from paths import *
import numpy as np
import pandas as pd

# nltk
import nltk
from nltk import word_tokenize


# TODO move this where it will be useful
def get_sentenceID(entityID):
  ''' Gets entityID and returns sentenceID of a sentence that the drug was mentioned in. '''
  return '.'.join(entityID.split('.')[:-1])

if __name__ == '__main__':
  # read dataframes of sentences and entities
  sentences_df_train = pd.read_csv(SENTENCE_PATH_train)
  entities_df_train = pd.read_csv(ENTITY_PATH_train)

  sentences_df_test1 = pd.read_csv(SENTENCE_PATH_test1)
  entities_df_test1 = pd.read_csv(ENTITY_PATH_test1)

  sentences_df_test2 = pd.read_csv(SENTENCE_PATH_test2)
  entities_df_test2 = pd.read_csv(ENTITY_PATH_test2)
  # Concatenating training and test data for the word2vec training!
  sentences_df = pd.concat([sentences_df_train,
                            sentences_df_test1,
                            sentences_df_test2]).drop_duplicates().reset_index(drop=True)

  entities_df = pd.concat([entities_df_train,
                           entities_df_test1,
                           entities_df_test2]).drop_duplicates().reset_index(drop=True)
  label_dict = dict()

  #for index, row in sentences_df.iterrows():
   # print(row['sentenceText'])

  #iterate over all entities

  sentenceIDs = [row['sentenceID'] for index, row in sentences_df.iterrows()]
  sentences = [row['sentenceText'] for index, row in sentences_df.iterrows()] 
  for ID, sen in zip(sentenceIDs, sentences):
    print(ID, sen)
    words = word_tokenize(sen.lower())
    label_dict[ID] = ['O' for word in words]
  

  for index, row in entities_df.iterrows():
    #get the sentence ID to reach the sentence
    sentenceID = get_sentenceID(row['entityID'])
    #print(sentenceID)
    sentence = str(sentences_df.loc[sentences_df.sentenceID==sentenceID]['sentenceText'].values[0])
    #print(sentence)

    #skip all entities that have discontinued names
    if ';' in row['position']:
      continue
    position = row['position'].split('-')
    words = word_tokenize(sentence.lower())
    entity_words = sentence[int(position[0]):int(position[1]) + 1].lower().split()


    if sentenceID not in label_dict:
      labels = ['O' for w in words] #label everything with O
    else:
      labels = label_dict[sentenceID] #load previous labels

    for l in range(len(labels)):
      if labels[l] == 'O': #dont touch the labels that are already defined
        if words[l] in entity_words:
          if words[l] == entity_words[0]:
            labels[l] = 'B'
          else:
            labels[l] = 'I'
    label_dict[sentenceID] = labels

  print(sentences_df.loc[sentences_df.sentenceID =='DDI-DrugBank.d178.s13']['sentenceText'].values)
  print(label_dict['DDI-DrugBank.d178.s13'])

  # save labels to csv
  label_dict_path = os.path.join(ROOT_DIR, 'Train', 'bio_labels')
  np.save(label_dict_path, label_dict)
  read_dictionary = np.load(label_dict_path + '.npy').item()

  print(label_dict['DDI-DrugBank.d178.s13'])
  print(read_dictionary['DDI-DrugBank.d178.s13'])
