import pandas as pd
import os
from functions import prepare_data_iden_soft_otg_hard

inp_data_train = "./Dynamic_data/Train.csv"
inp_data_test = "./Dynamic_data/Train.csv"
inp_data_dev = "./Dynamic_data/Dev.csv"

label_file_train = "./Dynamic_data/Train_label.csv"
label_file_test = "./Dynamic_data/Test_label.csv"
label_file_dev = "./Dynamic_data/Dev_label.csv"

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

