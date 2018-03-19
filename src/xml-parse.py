import os
import pandas as pd
import fnmatch
from xml import etree
from xml.etree import ElementTree as ET
from paths import *

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
    sentenceIDs.append(sentence.attrib['id'])
    sentenceTexts.append(sentence.attrib['text'])
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
  #print(entities_df)
  return (sentences_df, entities_df)

# TODO move this where it will be useful
def get_sentenceID(entityID):
  ''' Gets entityID and returns sentenceID of a sentence that the drug was mentioned in. '''
  return '.'.join(entityID.split('.')[:-1])


if __name__ == "__main__":
  frames_sentences = list()
  frames_entities = list()
  for DATA_DIR in DATA_DIRS:
    xmls = [f for f in os.listdir(DATA_DIR) if fnmatch.fnmatch(f, '*.xml')]
    for xml in xmls:
#      print(xml) # name of the xml file
      xml = ET.parse(os.path.join(DATA_DIR, xml))
      sentences_df, entities_df = parse(xml)
      frames_sentences.append(sentences_df)
      frames_entities.append(entities_df)
  sentences_df = pd.concat(frames_sentences).drop_duplicates().reset_index(drop=True)
  entities_df = pd.concat(frames_entities).drop_duplicates().reset_index(drop=True)

  print(sentences_df.head())
  print()
  print(entities_df.head())

  print (sentences_df.describe())
  print()
  print (entities_df.describe())  ## from here we can see that there are mostly drugs (9425 out of 14765 entities)
                                  ## the most common name is 'digoxin'
  sentences_df.info()
  print ()
  entities_df.info()

  # check if get_sentenceID works
  print(get_sentenceID("DDI-DrugBank.d157.s0.e0") == "DDI-DrugBank.d157.s0")

  # save DataFrames to .csv files
  sentences_df.to_csv(SENTENCE_PATH, index=False)
  entities_df.to_csv(ENTITY_PATH, index=False)


