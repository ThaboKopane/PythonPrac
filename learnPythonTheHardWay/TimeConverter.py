
def twenty4toTwelve(x):
	return {
	"00":12,
	"01":1,
	"02":2,
	"03":3,
	"04":4,
	"05":5,
	"06":6,
	"07":7,
	"08":8,
	"09":9,
	"10":10,
	"11":11,
	"12":12,
	"13":1,
	"14":2,
	"15":3,
	"16":4,
	"17":5,
	"18":6,
	"19":7,
	"20":8,
	"21":9,
	"22":9,
	"23":11
		}.get(x,13)
def twelve2twenty4(x):
	return {
	"1":["01",13],
	"2":["02",14],
	"3":["03",15],
	"4":["04",16],
	"5":["05",17],
	"6":["06",18],
	"7":["07",19],
	"8":["08",20],
	"9":["09",21],
	"10":["10",22],
	"11":["11",23],
	"12":["00",12]
	}.get(x,25)
print("Enter a time ([h]h:mm [am|pm]):")
inputTime = input("> ")
inputLength = range(0,inputTime.find(":"))
outputTime1=""
outputTime=""

"""if inputTime[:2]:
	print(twenty4toTwelve(inputTime[:2]))
print(">",inputTime[:2])"""

if len(inputLength) > 1 and len(inputTime) <=5:
	if inputTime[:2] and inputTime[:2] <"12":
		outputTime1=twenty4toTwelve(inputTime[:2])
		outputTime=str(outputTime1)+inputTime[2:]+" am"
		print(">",outputTime)
	elif inputTime[:2] and inputTime[:2]>="12":
		outputTime1=twenty4toTwelve(inputTime[:2])
		outputTime=str(outputTime1)+inputTime[2:]+" pm"
		print(">",outputTime)
elif len(inputLength)>1 and len(inputTime)>5:
	if inputTime[6:]=="pm":
		outputTime1=twelve2twenty4(inputTime[:2])[1]
		outputTime=str(outputTime1)+inputTime[2:5]
		print(">",outputTime)
	elif inputTime[6:]=="am":
		outputTime1=twelve2twenty4(inputTime[:2])[0]
		outputTime=outputTime1+inputTime[2:5]
		print(">",outputTime)
elif len(inputLength)==1:
	if inputTime[5:]=="am":
		outputTime1=twelve2twenty4(inputTime[:1])[0]
		outputTime=outputTime1+inputTime[1:4]
		print(">",outputTime)
	elif inputTime[5:]=="pm":
		outputTime1=twelve2twenty4(inputTime[:1])[1]
		outputTime=str(outputTime1)+inputTime[1:4]
		print(">",outputTime)


