data = []

input1 = open("lower/class-1/class-1_lower.txt","r")
input1 = input1.read()
input1 = input1.split("\n")

for line in input1:
    data.append("__label__class1 "+line+"\n")

input2 = open("lower/class-2/class-2_lower.txt","r")
input2 = input2.read()
input2 = input2.split("\n")

for line in input2:
    data.append("__label__class2 "+line+"\n")

input3 = open("lower/class-3/class-3_lower.txt","r")
input3 = input3.read()
input3 = input3.split("\n")

for line in input3:
    data.append("__label__class3 "+line+"\n")

input4 = open("lower/class-4/class-4_lower.txt","r")
input4 = input4.read()
input4 = input4.split("\n")

for line in input4:
    data.append("__label__class4 "+line+"\n")

#############
input5 = open("lower/class-5/class-5_lower.txt","r")
input5 = input5.read()
input5 = input5.split("\n")

for line in input5:
    data.append("__label__class5 "+line+"\n")

input6 = open("lower/class-6/class-6_lower.txt","r")
input6 = input6.read()
input6 = input6.split("\n")

for line in input6:
    data.append("__label__class6 "+line+"\n")

input7 = open("lower/class-7/class-7_lower.txt","r")
input7 = input7.read()
input7 = input7.split("\n")

for line in input7:
    data.append("__label__class7 "+line+"\n")

#############

input8 = open("lower/class-8/class-8_lower.txt","r")
input8= input8.read()
input8 = input8.split("\n")

for line in input8:
    data.append("__label__class8 "+line+"\n")

input9 = open("lower/class-9/class-9_lower.txt","r")
input9 = input9.read()
input9 = input9.split("\n")

for line in input9:
    data.append("__label__class9 "+line+"\n")

input10 = open("lower/class-10/class-10_lower.txt","r")
input10 = input10.read()
input10 = input10.split("\n")

for line in input10:
    data.append("__label__class10 "+line+"\n")

input11 = open("lower/class-11/class-11_lower.txt","r")
input11 = input11.read()
input11 = input11.split("\n")

for line in input11:
    data.append("__label__class11 "+line+"\n")

#############
input12 = open("lower/class-12/class-12_lower.txt","r")
input12 = input12.read()
input12 = input12.split("\n")

for line in input12:
    data.append("__label__class12 "+line+"\n")

input13 = open("lower/class-13/class-13_lower.txt","r")
input13 = input13.read()
input13 = input13.split("\n")

for line in input13:
    data.append("__label__class13 "+line+"\n")

input14 = open("lower/class-14/class-14_lower.txt","r")
input14 = input14.read()
input14 = input14.split("\n")

for line in input14:
    data.append("__label__class14 "+line+"\n")

#############

input15 = open("lower/class-15/class-15_lower.txt","r")
input15 = input15.read()
input15 = input15.split("\n")

for line in input1:
    data.append("__label__class15 "+line+"\n")

input16 = open("lower/class-16/class-16_lower.txt","r")
input16 = input16.read()
input16 = input16.split("\n")

for line in input16:
    data.append("__label__class16 "+line+"\n")

input17 = open("lower/class-17/class-17_lower.txt","r")
input17 = input17.read()
input17 = input17.split("\n")

for line in input17:
    data.append("__label__class17 "+line+"\n")

input18 = open("lower/class-18/class-18_lower.txt","r")
input18 = input18.read()
input18 = input18.split("\n")

for line in input18:
    data.append("__label__class18 "+line+"\n")

#############
input19 = open("lower/class-19/class-19_lower.txt","r")
input19 = input19.read()
input19 = input19.split("\n")

for line in input19:
    data.append("__label__class19 "+line+"\n")

input20 = open("lower/class-20/class-20_lower.txt","r")
input20 = input20.read()
input20 = input20.split("\n")

for line in input20:
    data.append("__label__class20 "+line+"\n")

input21 = open("lower/class-21/class-21_lower.txt","r")
input21 = input21.read()
input21 = input21.split("\n")

for line in input21:
    data.append("__label__class21 "+line+"\n")

#############

input22 = open("lower/class-22/class-22_lower.txt","r")
input22= input22.read()
input22 = input22.split("\n")

for line in input22:
    data.append("__label__class22 "+line+"\n")

input23 = open("lower/class-23/class-23_lower.txt","r")
input23 = input23.read()
input23 = input23.split("\n")

for line in input23:
    data.append("__label__class23 "+line+"\n")

i=0

for i in range(len(data)):
    i=i+1
print(i)

compositefile = open("composite2train.txt","w")
compositefile.write("".join(data))
compositefile.close()
