from paths import *
import pandas as pd


# TODO move this where it will be useful
def get_sentenceID(entityID):
  ''' Gets entityID and returns sentenceID of a sentence that the drug was mentioned in. '''
  return '.'.join(entityID.split('.')[:-1])


sentences_df = pd.read_csv(SENTENCE_PATH)
entities_df = pd.read_csv(ENTITY_PATH)
print(sentences_df.head())
print(entities_df.head())

label_dict = dict()

#for index, row in sentences_df.iterrows():
 # print(row['sentenceText'])

#iterate over all entities
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
  words = sentence.lower().split()
  entity_words = sentence[int(position[0]):int(position[1]) + 1].lower().split()
  #print(words)
  #print(entity_words)
  

  if sentenceID not in label_dict:
    labels = ['O' for w in words] #label everything with O
  else:
    labels = label_dict[sentenceID] #load previous labels

  for l in range(len(labels)):
    if labels[l] == 'O': #dont touch the labels that are already defined
      if words[l] in entity_words:
        #print(entity_words[0], words[l])
        if words[l] == entity_words[0]:
          labels[l] = 'B'
        else:
          labels[l] = 'I'
  label_dict[sentenceID] = labels
  #print(labels)
  
print(sentences_df.loc[sentences_df.sentenceID =='DDI-DrugBank.d178.s13']['sentenceText'].values)
print(label_dict['DDI-DrugBank.d178.s13'])
