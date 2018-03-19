from paths import *
import pandas as pd

sentences_df = pd.read_csv(SENTENCE_PATH)
entities_df = pd.read_csv(ENTITY_PATH)
print (sentences_df.head())
print (entities_df.head())