
#import torch
import re
#from transquest.algo.sentence_level.monotransquest.run_model import MonoTransQuestModel


import kiwi

model = kiwi.load_model('runs/estimator/best_model.torch')
#model = kiwi.load_model('runs/estimator/epoch_19/model.torch')

#source = ['ladies and gentleman.']
#target = ['大家好今天我想跟大家分享一下。男女性的性别歧视以及他们在购物方面的不同之处。']

#predictions = model.predict(examples)
#print(predictions)

# Using readline()
file1 = open('./input.tsv', 'r')
file_out = open('./output.tsv', 'w')
count = 0

while True:
    count += 1
    # Get next line from file
    line = file1.readline().strip()
    # if line is empty
    # end of file is reached
    if not line:
        break
    #print("Line{}: {}".format(count, line))
    lline = re.split(r'\t+', line)
    if len(lline) > 3 and len(lline[2].strip()) > 0 and len(lline[3].strip()) > 0:
        source = [lline[2]]
        target = [lline[3]]
        examples = {'source': source,'target': target}
        print("%s.%s:predicting SRC <%s> vs TGT <%s>" %(lline[0], lline[1], lline[2], lline[3]))
        predictions = model.predict(examples)
        shter = predictions['tags'][0][0]
        #predictions, raw_outputs = model.predict([[lline[2], lline[3]]])
        print("%s.%s:pred <%f> SRC <%s> vs TGT <%s>" %(lline[0], lline[1], shter, lline[2], lline[3]))
        file_out.write(lline[0] + '\t' + lline[1] + '\t' + str(shter) +'\t' + lline[2] + '\t' + lline[3] + '\r')

#    if count == 10:
#      break
file1.close()
file_out.close()
