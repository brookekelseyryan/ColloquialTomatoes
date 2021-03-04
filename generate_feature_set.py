import csv
from nrclex import NRCLex


file_pos = open("pos_review.csv", "r")
file_neg = open("neg_review.csv", "r")

pos_feature_matrix_raw_emotion = []
pos_feature_matrix_affect_frequencies = []
neg_feature_matrix_raw_emotion = []
neg_feature_matrix_affect_frequencies = []

### Two ideas for features
#### 1 use raw_emotion_scores
#### 2 use affect_frequencies
#### first value for all matrices is just length of review
#### Currenly not doing any stemming, should be very easy to add to code


#### raw_emotion feature order:
#### length, anger, anticipation, disguist, fear, joy, negataive, positive, sadness, surprise, trust

#### affect_frequencies feature order:
#### length, anger, anticip, anticipation, disgust, fear, joy, negative, positive, sadness, surprise, trust



csv_reader = csv.reader(file_pos, delimiter=",")


#increase ctr based on size of data you want to train on
ctr = 1
for row in csv_reader:
    if ctr > 500:
        break
    review = row[0]
    #when stemming, call stemming function on review
    text_object = NRCLex(review)
    review_len = len(review.split(" "))
    
    feature_list = []
    feature_list.append(review_len)

    raw_emotion = text_object.raw_emotion_scores
    raw_emotion = [(k,v) for k,v in raw_emotion.items()]
    raw_emotion.sort()
    #print(raw_emotion)
    raw_emotion = [v for (k,v) in raw_emotion]
    #print(raw_emotion)
    feature_list.extend(raw_emotion)
    pos_feature_matrix_raw_emotion.append(feature_list)

    feature_list_2 = [review_len]
    affect_frequencies = text_object.affect_frequencies
    affect_frequencies = [(k,v) for k,v in affect_frequencies.items()]
    affect_frequencies.sort()
    
    #print(affect_frequencies)
    affect_frequencies = [v for (k,v) in affect_frequencies]

    #print(affect_frequencies)
    feature_list_2.extend(affect_frequencies)
    pos_feature_matrix_affect_frequencies.append(feature_list_2)
    
    ctr += 1

#print(pos_feature_matrix_affect_frequencies[0:10])
#print(pos_feature_matrix_raw_emotion[0:10])


csv_reader_2 = csv.reader(file_neg, delimiter=",")


ctr = 1
for row in csv_reader_2:
    if ctr > 500:
        break
    review = row[0]
    #when stemming, call stemming function on review
    text_object = NRCLex(review)
    review_len = len(review.split(" "))
    
    feature_list = []
    feature_list.append(review_len)

    raw_emotion = text_object.raw_emotion_scores
    raw_emotion = [(k,v) for k,v in raw_emotion.items()]
    raw_emotion.sort()
    #print(raw_emotion)
    raw_emotion = [v for (k,v) in raw_emotion]
    #print(raw_emotion)
    feature_list.extend(raw_emotion)
    neg_feature_matrix_raw_emotion.append(feature_list)

    feature_list_2 = [review_len]
    affect_frequencies = text_object.affect_frequencies
    affect_frequencies = [(k,v) for k,v in affect_frequencies.items()]
    affect_frequencies.sort()
    
    #print(affect_frequencies)
    affect_frequencies = [v for (k,v) in affect_frequencies]

    #print(affect_frequencies)
    feature_list_2.extend(affect_frequencies)
    neg_feature_matrix_affect_frequencies.append(feature_list_2)
    
    ctr += 1

#print(neg_feature_matrix_affect_frequencies[0:10])
#print(neg_feature_matrix_raw_emotion[0:10])

file_pos.close()
file_neg.close()

