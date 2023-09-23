import math

results = []

#open file
for i in range(1, 2):
    f = open("file" + str(i) + ".out")

    #find data
    for line_num, line in enumerate(f):
        if "FINAL R-B3LYP ENERGY" in line:
            final_rb3lyp_energy = float(line[30:44])
            average_CH_bond_length = 0
            results.append({"final_rb3lyp_energy": final_rb3lyp_energy, "average_CH_bond_length": average_CH_bond_length})

    f.close()

#output
heading = {"final_rb3lyp_energy": "Final R-B3LYP Energy", "average_CH_bond_length": "Average C-H Bond Length"}

print("|", heading["final_rb3lyp_energy"], "|", heading["average_CH_bond_length"], "|")

for result in results:
    final_rb3lyp_energy_padding = (len(heading["final_rb3lyp_energy"]) - len(str(result["final_rb3lyp_energy"]))) / 2
    average_CH_bond_length_padding = (len(heading["average_CH_bond_length"]) - len(str(result["average_CH_bond_length"]))) / 2

    print("|", " " * math.floor(final_rb3lyp_energy_padding) + str(result["final_rb3lyp_energy"]) + " " * math.ceil(final_rb3lyp_energy_padding), "|", " " * math.floor(average_CH_bond_length_padding) + str(result["average_CH_bond_length"]) + " " * math.ceil(average_CH_bond_length_padding), "|")