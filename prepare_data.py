import pandas as pd
import os
from functions import prepare_data_iden_soft_otg_hard

inp_data_train = "./dynamic_data_v0.2.3/train.csv"
inp_data_test = "./dynamic_data_v0.2.3/test.csv"
inp_data_dev = "./dynamic_data_v0.2.3/dev.csv"

label_file_train = "./dynamic_data_v0.2.3/train_label.csv"
label_file_test = "./dynamic_data_v0.2.3/test_label.csv"
label_file_dev = "./dynamic_data_v0.2.3/dev_label.csv"

out_file_train = "./Tagged_data/train_tagged.txt"
out_file_test = "./Tagged_data/test_tagged.txt"
out_file_dev = "./Tagged_data/dev_tagged.txt"

file_hb = "./eng_lexicon.tsv"
file_tar = './identity_combined.txt'

if not os.path.isdir('Tagged_data'):
    os.mkdir('Tagged_data')

print('Preparing training data...')
prepare_data_iden_soft_otg_hard(inp_data_train, label_file_train, file_hb, file_tar, out_file_train)
print('Preparing test data...')
prepare_data_iden_soft_otg_hard(inp_data_test, label_file_test, file_hb, file_tar, out_file_test)
print('Preparing dev data...')
prepare_data_iden_soft_otg_hard(inp_data_dev, label_file_dev, file_hb, file_tar, out_file_dev)

train_labels = pd.read_csv(label_file_train, sep = '\t', header=None, lineterminator='\n')
dev_labels = pd.read_csv(label_file_dev, sep = '\t', header=None, lineterminator='\n')
test_labels = pd.read_csv(label_file_test, sep = '\t', header=None, lineterminator='\n')

train_labels[0] = sorted(list(train_labels[0]))
dev_labels[0] = sorted(list(dev_labels[0]))
test_labels[0] = sorted(list(test_labels[0]))

train_labels.to_csv('Tagged_data/train_label_ordered.csv', sep = '\t', header=None, index = False)
dev_labels.to_csv('Tagged_data/dev_label_ordered.csv', sep = '\t', header=None, index = False)
test_labels.to_csv('Tagged_data/test_label_ordered.csv', sep = '\t', header=None, index = False)

