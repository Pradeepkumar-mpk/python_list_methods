weekdays = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
list = weekdays+month
list.sort()
list.reverse()
print(list)
sub = list[0:3]
print(sub)
del list[0:3]
list = list + sub
print(list)