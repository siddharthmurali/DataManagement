import pymongo
import pdb
from pymongo import MongoClient
import sys
import json

#argv[1] == negative words
#argv[2] == positive words

def main(argv):


    		wordsNeg = list()
    		wordsPos = list()

    		f = open(sys.argv[1], 'r')
    		for word in f:
        		wordsNeg.append(word.translate(None,'\r\n'))
    		f.close()

    		g = open(sys.argv[2],'r')
    		for word in g:
        		wordsPos.append(word.translate(None,'\r\n'))
    		g.close()

    		client = MongoClient()

    		db = client['cs336']
    		unlabel_review = db['unlabel_review']
    		print unlabel_review.find_one()
    		reviewSplit = db['unlabel_review_after_splitting']

    		sentiment = dict()

    		for item in reviewSplit.find():
        		score = 0
        		for element in item['review']:
            			if element['word'] in wordsPos:
                			score += element['count']
            			elif element['word'] in wordsNeg:
                			score -= element['count']

        		if score >= 0:
            			sentiment[item['id']] = 'positive'
        		elif score < 0:
            			sentiment[item['id']] = 'negative'

		with open(sys.argv[3], 'wb') as handle:
			json.dump(sentiment, handle, indent = 2) 
		


if __name__ == "__main__":
    	main(sys.argv[1:])
