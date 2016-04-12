import csv

# === some parameter
input_name = 'sample_input' # example: input.csv giving the parameter 'input'
output_name = 'sample_output'
printflag = False
skip_weight_zero = True

# == store variable
csv_data = []
user_list = ['null']
user_relation = []

def isint(value):
  try:
    int(value)
    return True
  except:
    return False

# == read
csvfile = open(input_name+'.csv', 'rb')
for i,row in enumerate(csv.reader(csvfile, delimiter=',')):
	onerow = []
	valuerow = []
	# handle storing user list
	if i == 0:
		for j, user in enumerate(row):
			if j == 0:
				continue
			else:
				# print i, j, val
				user_list.append(user)
	# handle data
	else:
		for j, val in enumerate(row):
			if j == 0:
				# print 'username:', val
				continue
			else:
				if isint(val) :
					valuerow.append(int(val))
				elif val == 'X':
					valuerow.append(-1)
				else:
					valuerow.append(0)
				onerow.append(val)
				# print user_list[i], user_list[j], val
		csv_data.append(onerow)
		user_relation.append(valuerow)
if printflag:
	print user_relation


# == output data
## Source;Target;Type;Id;Label;Weight
with open(output_name+'_node.csv', 'w') as fp1:
	a = csv.writer(fp1, delimiter=',')
	a.writerow(['Id','Label','Modularity Class'])
	for i, val in enumerate(user_list):
		if i != 0:
			a.writerow([str(i),val,0])
with open(output_name+'_edge.csv', 'w') as fp2:
	a = csv.writer(fp2, delimiter=',')
	a.writerow(['Source','Target','Type','Id','Label','Weight'])
	if printflag:
		print 'Source'+'\t'+'Target'+'\t'+'Type'+'\t'+'Id'+'\t'+'Label'+'\t'+'Weight'
	id = 1
	for i, row in enumerate(user_relation):
		for j, val in enumerate(row):
			if i == j :
				continue
			else:
				if skip_weight_zero :
					if val == 0:
						continue
				tmpstr = user_list[i+1]+'->'+user_list[j+1]
				a.writerow([str(i+1),str(j+1),'Directed',str(id),str(tmpstr),str(val) ] )
				if printflag:
					print str(i+1)+'\t'+str(j+1)+'\t'+'Directed'+'\t'+str(id)+'\t'+user_list[i+1]+'->'+user_list[j+1]+'\t'+str(val) 
			id = id + 1;
