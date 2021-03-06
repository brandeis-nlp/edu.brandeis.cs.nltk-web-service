'''
    /**
     * @brief train a classifier based on features. 
     * @refer <a href="http://nltk.org/book/ch06.html" target="_blank">Supervised Classification</a>
     * @return classifierID
     * @throws ClassifyException
     */
    public String train(String featuresID) throws ClassifyException;
'''


import sys,os,time,nltk, cPickle as pickle
from nltk.corpus import *

from intfc_common_io import log,home,load_features, save_classifiers

def train_naive_bayes(path, fname):
    name='naive_bayes' + '_._' + fname
    featuresets = load_features(path,fname)
    log("load featuresets")
    train_set = featuresets[1:200]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    log("train classifier")
    save_classifiers(classifier, path, name)
    log("dump classifier")
    
def main():
    featuresID = sys.argv[1]
    train_naive_bayes(home(), featuresID)
    print featuresID

if __name__ == "__main__":
    main()

