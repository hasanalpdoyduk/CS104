with open("shapes.csv","r") as file:
    print(file.read())

with open("rectangles.csv","w") as file:
    file.write("50.04, 12.99, 650.0196\n")
    file.write("67.85, 32.39, 2197.6614999999997\n")
    file.write("66.02, 7.07, 466.7614\n")
    file.write("37.16, 8.49, 315.48839999999996")

with open("trapezoids.csv","w") as file:
    file.write("21.23, 74.55, 55.77, 2670.8253\n")
    file.write("64.4, 19.25, 83.9, 52005.41500000001\n")
    file.write("89.92, 34.11, 60, 92015.13600000001")

with open("circles.csv","w") as file:
    file.write("56.45, 10005.93185\n")
    file.write("25.06, 1971.9313039999997\n")
    file.write("54.276, 9248.031306000003\n")
    file.write("41.07, 5296.378986\n")
    file.write("99.4, 31024.330400000003\n")
    file.write("80.94, 20571.030504")
