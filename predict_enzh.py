
#import torch
import re
#from transquest.algo.sentence_level.monotransquest.run_model import MonoTransQuestModel


#model = MonoTransQuestModel("xlmroberta", "TransQuest/monotransquest-da-en_zh-wiki", num_labels=1, use_cuda=torch.cuda.is_available())
from kiwi.lib import predict
runner = predict.load_system('./xlmr-en-zh.ckpt')

# Using readline()
file1 = open('./work/input.tsv', 'r')
file_out = open('./work/output.tsv', 'w')
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
        print("%s.%s:predicting EN <%s> vs ZH <%s>" %(lline[0], lline[1], lline[2], lline[3]))
        predictions = runner.predict(source, target)
        #predictions, raw_outputs = model.predict([[lline[2], lline[3]]])
        print("%s.%s:pred <%f> EN <%s> vs ZH <%s>" %(lline[0], lline[1], predictions.sentences_hter[0], lline[2], lline[3]))
        file_out.write(lline[0] + '\t' + lline[1] + '\t' + str(predictions.sentences_hter[0]) +'\t' + lline[2] + '\t' + lline[3] + '\r')

#    if count == 10:
#      break
file1.close()
file_out.close()
