import math

def learning(input_data, data_to_predict):
    k = math.sqrt(len(input_data))
    if k % 2 == 0:
        k += 1
    counterTrue = 0
    counterFalse = 0
    distance = []
    for i in input_data:
        clump = (i['clump_thickness'] - data_to_predict['clump_thickness'])**2
        cellSize = (i['uniformity_of_cell_size'] - data_to_predict['uniformity_of_cell_size'])**2
        cellShape = (i['uniformity_of_cell_shape'] - data_to_predict['uniformity_of_cell_shape'])**2
        marginal = (i['marginal_adhesion'] - data_to_predict['marginal_adhesion'])**2
        eCellsize = (i['single_epithelial_cell_size'] - data_to_predict['single_epithelial_cell_size'])**2
        bare = (i['bare_nuclei'] - data_to_predict['bare_nuclei'])**2
        bland = (i['bland_chromatin'] - data_to_predict['bland_chromatin'])**2
        normal = (i['normal_nucleoli'] - data_to_predict['normal_nucleoli'])**2
        mitoses = (i['mitoses'] - data_to_predict['mitoses'])**2
        sum = math.sqrt(clump + cellSize + cellShape + marginal + eCellsize + bare + bland + normal + mitoses)
        distance.append(sum)
    combine = zip(distance, input_data)
    combineList = list(combine)
    combineList.sort(key=lambda tup: tup[0])
    predict = combineList[0:int(k)]

    for i in predict:
        if i[1]['result'] == 2:
            counterTrue += 1
        elif i[1]['result'] == 4:
            counterFalse += 1

    if counterTrue > counterFalse:
        print('Result : benign')
    elif counterFalse > counterTrue:
        print('Result : malignant')


def take_input():
    print("amount of data with known result?")
    total_data = int(input())
    print("enter data with result (format(seperated with ',') : ID,Clump Thickness,Uniformity of Cell Size,Uniformity of Cell Shape,Marginal Adhesion,Single Epithelial Cell Size,Bare Nuclei,Bland Chromatin,Normal Nucleoli,Mitoses,Result)")
    input_data = []
    temp_data = {}
    for _ in range(total_data):
	    input_line = input().split(",")
	    temp_data['clump_thickness'] = int(input_line[1])
	    temp_data['uniformity_of_cell_size'] = int(input_line[2])
	    temp_data['uniformity_of_cell_shape'] = int(input_line[3])
	    temp_data['marginal_adhesion'] = int(input_line[4])
	    temp_data['single_epithelial_cell_size'] = int(input_line[5])
	    temp_data['bare_nuclei'] = int(input_line[6])
	    temp_data['bland_chromatin'] = int(input_line[7])
	    temp_data['normal_nucleoli'] = int(input_line[8])
	    temp_data['mitoses'] = int(input_line[9])
	    temp_data['result'] = int(input_line[10])
	    input_data.append(temp_data)

    print("enter data to predict result (format(seperated with ',') : ID,Clump Thickness,Uniformity of Cell Size,Uniformity of Cell Shape,Marginal Adhesion,Single Epithelial Cell Size,Bare Nuclei,Bland Chromatin,Normal Nucleoli,Mitoses)")
    data_to_predict = {}
    input_line = input().split(",")
    data_to_predict['clump_thickness'] = int(input_line[1])
    data_to_predict['uniformity_of_cell_size'] = int(input_line[2])
    data_to_predict['uniformity_of_cell_shape'] = int(input_line[3])
    data_to_predict['marginal_adhesion'] = int(input_line[4])
    data_to_predict['single_epithelial_cell_size'] = int(input_line[5])
    data_to_predict['bare_nuclei'] = int(input_line[6])
    data_to_predict['bland_chromatin'] = int(input_line[7])
    data_to_predict['normal_nucleoli'] = int(input_line[8])
    data_to_predict['mitoses'] = int(input_line[9])

    learning(input_data, data_to_predict)
 
take_input()