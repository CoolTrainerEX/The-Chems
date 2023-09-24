import math

results = []

#open file
for i in range(1, 6):
    with open("file" + str(i) + ".out") as f:
        #find data
        average_CH_bond_length = 0.0
        count = 0
        for line in f:
            if "INTERNUCLEAR DISTANCES" in line:
                count += 1
                pair = True
            elif count == 5:
                for i in line[26:74].split(" *  "):
                    average_CH_bond_length += float(i)
                
                average_CH_bond_length /= 4
                count = 0
            elif count > 0:
                count += 1
            elif "FINAL R-B3LYP ENERGY" in line and pair == True:
                results.append({"final_rb3lyp_energy": float(line[30:44]), "average_CH_bond_length": average_CH_bond_length})
                average_CH_bond_length = 0.0
                pair = False

#output
heading = {"final_rb3lyp_energy": "Final R-B3LYP Energy", "average_CH_bond_length": "Average C-H Bond Length"}

print("|", heading["final_rb3lyp_energy"], "|", heading["average_CH_bond_length"], "|")

for result in results:
    final_rb3lyp_energy_padding = (len(heading["final_rb3lyp_energy"]) - len(str(result["final_rb3lyp_energy"]))) / 2
    average_CH_bond_length_padding = (len(heading["average_CH_bond_length"]) - len(str(result["average_CH_bond_length"]))) / 2

    print("|", " " * math.floor(final_rb3lyp_energy_padding) + str(result["final_rb3lyp_energy"]) + " " * math.ceil(final_rb3lyp_energy_padding), "|", " " * math.floor(average_CH_bond_length_padding) + str(result["average_CH_bond_length"]) + " " * math.ceil(average_CH_bond_length_padding), "|")