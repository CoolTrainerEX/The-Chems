import math

results = [{"time": "Time", "ratio": "Peak A / Peak B"}]

for i in range(7, 29):
    with open("spa" + "0" * (5 - len(str(i))) + str(i) + ".txt") as f:
        time = float(f.readline())
        wavenumber = []
        absorbance = []
        

        for line in f:
            data = line.strip().split(" ")
            wavenumber.append(float(data[0]))
            absorbance.append(float(data[1]))

        #integrate
        dx = wavenumber[1] - wavenumber[0]
        area_a = 0
        area_b = 0
        #increments every time it goes up or down
        location = 0
        going_up = True

        for i in range(len(wavenumber)):
            y_i = absorbance [i - 1] if i != 0 else 0
            if absorbance[i] > y_i and going_up == False:
                going_up = True
                location += 1
            elif absorbance[i] < y_i and going_up == True:
                going_up = False
                location += 1

            area = dx * absorbance[i]
            if location > 2:
                area_a += area
            else:
                area_b += area
        
        results.append({"time": time, "ratio": area_a / area_b})

#output
max_time_len = 0
max_ratio_len = 0

for result in results:
    time_len = len(str(result["time"]))

    if time_len > max_time_len:
        max_time_len = time_len

    ratio_len = len(str(result["ratio"]))

    if ratio_len > max_ratio_len:
        max_ratio_len = ratio_len




for result in results:
    time_padding = (max_time_len - len(str(result["time"]))) / 2 + 1
    ratio_padding = (max_ratio_len - len(str(result["ratio"]))) / 2 + 1
    print("|" + " " * math.floor(time_padding) + str(result["time"]) + " " * math.ceil(time_padding) + "|" + " " * math.floor(ratio_padding) + str(result["ratio"]) + " " * math.ceil(ratio_padding) + "|")