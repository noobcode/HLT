"""
Module implements a class which is used for custom feature extraction. 
The class needs to be inherited for pipeline compatibility.
Allows for extraction of feature names.
"""

from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin

class FeatureTransformer(BaseEstimator, TransformerMixin): 
  """Class used for feature extraction."""

  def fit(self, X, y=None, **fit_params):
    """As a stateless transformer, this does nothing."""
    return self
  
  def get_feature_names(self):
    """Gets a list of feature names.
      Uses the class name by default. 
      Must be overriden if the transformation 
      produces more than 1 feature.
    """
    return [self.__class__.__name__]


