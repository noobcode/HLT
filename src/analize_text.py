from paths import *
import pandas as pd


# TODO move this where it will be useful
def get_sentenceID(entityID):
  ''' Gets entityID and returns sentenceID of a sentence that the drug was mentioned in. '''
  return '.'.join(entityID.split('.')[:-1])


sentences_df = pd.read_csv(SENTENCE_PATH)
entities_df = pd.read_csv(ENTITY_PATH)
#print (sentences_df.head())
#print (entities_df.head())

label_dict = dict()

#for index, row in sentences_df.iterrows():
 # print(row['sentenceText'])

for index, row in entities_df.iterrows():
  sentenceID = get_sentenceID(row['entityID'])
#  print(sentenceID)
#  sentence = sentences_df[sentences_df['sentenceID'] == sentenceID]['sentenceText']
  sentence = str(sentences_df.loc[sentences_df.sentenceID==sentenceID]['sentenceText'].values[0])
  print(sentence)
  if ';' in row['position']:
    continue
  position = row['position'].split('-')
  words = sentence.split()
  entity_words = sentence[int(position[0]):int(position[1]) + 1]
 # print(words)
  print(entity_words)
  
  labels = ['O' for w in words]
  if sentenceID not in label_dict:
 #   print(sentenceID)
    label_dict['sentenceID'] = labels
  else:
    labels = label_dict['sentenceID']

  first_word = True
  for l in range(len(labels)):
    if labels[l] == 'O':
      if words[l].lower() in entity_words.lower().split():
        print(entity_words.split()[0], words[l])
        if words[l].lower() == entity_words.split()[0].lower():
          labels[l] = 'B'
          first_word = False
        else:
          labels[l] = 'I'
  label_dict[sentenceID] = labels
  print(labels)
  
