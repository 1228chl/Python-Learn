import torch

# X -> (3,1,4)
# RNN
my_rnn = torch.nn.RNN(input_size=4,hidden_size=8,num_layers=1,batch_first=False)
for name,param in my_rnn.named_parameters():
    print(name)
    print(param)
print("*"*80)
# LSTM
my_rnn = torch.nn.LSTM(input_size=4,hidden_size=8,num_layers=1,batch_first=False)
for name,param in my_rnn.named_parameters():
    print(name)
    print(param)
print("*"*80)
# GRU
my_rnn = torch.nn.GRU(input_size=4,hidden_size=8,num_layers=1,batch_first=False)
for name,param in my_rnn.named_parameters():
    print(name)
    print(param)
print("*"*80)