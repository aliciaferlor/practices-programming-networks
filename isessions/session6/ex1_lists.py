from Seq0 import Seq
str_list = ["ACCGT", "am i valid?"]
seq_list = []

for st in str_list:
    if Seq.is_valid_sequence(st):
        seq_list.append(Seq(st))
    else:
        seq_list.append(Seq("ERROR"))

for i in range(0, len(seq_list)):
    print("sequence", str(i) + ":", seq_list[i])