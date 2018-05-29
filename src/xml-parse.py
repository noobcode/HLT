import os
import pandas as pd
import fnmatch
from xml import etree
from xml.etree import ElementTree as ET
from paths import *
from analize_text import get_sentenceID

def parse(xml):
  ''' This function parses all needed information from given xml and returns two data frames
        -- one is with sentences (sentenceID, sentenceText) and the other with all the entities.
  '''
  sentenceIDs = list()
  sentenceTexts = list()
  entityIDs = list()
  entity_types = list()
  entity_names = list()
  entity_positions = list()
  
  root = xml.getroot()
  for sentence in root.iter('sentence'):
    if not sentence.attrib['id']:
      continue
    if not sentence.attrib['text']:
      continue
    if len(sentence.attrib['text']) < 2:
      continue

    sentenceIDs.append(sentence.attrib['id'])
    sentenceTexts.append(sentence.attrib['text'])

    for pair in sentence.iter('pair'):
     pass
     #build a dataframe with the pairs
     # save pretrained model in a file and load it in a new notebook

    for entity in sentence.iter('entity'):
      entityIDs.append(entity.attrib['id'])
      entity_names.append(entity.attrib['text'])
      entity_types.append(entity.attrib['type'])
      entity_positions.append(entity.attrib['charOffset'])
  s = {'sentenceID': sentenceIDs, 'sentenceText': sentenceTexts}
  sentences_df = pd.DataFrame(data=s)
    #print(sentences_df, '\n')
  e = {'entityID':entityIDs, 'type':entity_types, 'name':entity_names, 'position':entity_positions}
  entities_df = pd.DataFrame(data=e)
  #print(entities_df_train)
  return (sentences_df, entities_df)


if __name__ == "__main__":
  train = True
  test = 0
  for DATA_DIR in DATA_DIRS:
    print(DATA_DIR)
    frames_sentences = list()
    frames_entities = list()
    for DIR in DATA_DIR:
      print(DIR)
      xmls = [f for f in os.listdir(DIR) if fnmatch.fnmatch(f, '*.xml')]
      for xml in xmls:
        print(xml) # name of the xml file
        xml = ET.parse(os.path.join(DIR, xml))
        sentences_df, entities_df = parse(xml)
        frames_sentences.append(sentences_df)
        frames_entities.append(entities_df)
    if train:
      sentences_df_train = pd.concat(frames_sentences).drop_duplicates().reset_index(drop=True)
      entities_df_train = pd.concat(frames_entities).drop_duplicates().reset_index(drop=True)
    if test == 1:
      sentences_df_test1 = pd.concat(frames_sentences).drop_duplicates().reset_index(drop=True)
      entities_df_test1 = pd.concat(frames_entities).drop_duplicates().reset_index(drop=True)
    if test == 2:
      sentences_df_test2 = pd.concat(frames_sentences).drop_duplicates().reset_index(drop=True)
      entities_df_test2 = pd.concat(frames_entities).drop_duplicates().reset_index(drop=True)
    train = False
    test += 1

  print(sentences_df_train.head())
  print()
  print(entities_df_train.head())

  print (sentences_df_train.describe())
  print()
  print (entities_df_train.describe())  ## from here we can see that there are mostly drugs (9425 out of 14765 entities)
                                  ## the most common name is 'digoxin'
  sentences_df_train.info()
  sentences_df_test1.info()
  sentences_df_test2.info()
  print ()
  entities_df_train.info()
  entities_df_test1.info()
  entities_df_test2.info()

  # check if get_sentenceID works
  print(get_sentenceID("DDI-DrugBank.d157.s0.e0") == "DDI-DrugBank.d157.s0")

  # save DataFrames to .csv files
  sentences_df_train.to_csv(SENTENCE_PATH_train, index=False)
  entities_df_train.to_csv(ENTITY_PATH_train, index=False)
  
  sentences_df_test1.to_csv(SENTENCE_PATH_test1, index=False)
  entities_df_test1.to_csv(ENTITY_PATH_test1, index=False)

  sentences_df_test2.to_csv(SENTENCE_PATH_test2, index=False)
  entities_df_test2.to_csv(ENTITY_PATH_test2, index=False)

