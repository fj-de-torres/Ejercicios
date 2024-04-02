import os

start = 127_743
end = 129_751
current_path = os.path.dirname(__file__)
with open(os.path.join(current_path,"emoji.csv"),'wt') as emoji:
    emoji.write("EMOJI,Decimal ASCII code\n")
    for index in range(start,end):
        if chr(index).isprintable():
            emoji.write(f"{chr(index)},{index}\n")
        else:
            pass
