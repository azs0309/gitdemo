flightdict = {
    '102': ['HNL', 'HKG', '4:00', 'Monday', '8:00', 'Monday', 99.95, 4],
    '132': ['HNL', 'HNL', '4:00', 'Monday', '8:00', 'Monday', 59.0, 2],
    '276': ['HKG', 'CDG', '15:00', 'Monday', '3:00', 'Tuesday', 233.99, 2],
    '303': ['HKG', 'ARN', '9:00', 'Monday', '16:00', 'Monday', 233.99, 2],
    '498': ['NRT', 'ITO', '14:00', 'Monday', '0:00', 'Tuesday', 159.99, 2],
    '390': ['CUR', 'CUR', '4:00', 'Thursday', '8:00', 'Thursday', 599.95, 3],
    '465': ['NRT', 'YYZ', '4:00', 'Thursday', '8:00', 'Thursday', 59.0, 3],
    '1305': ['ITO', 'ARN', '4:00', 'Thursday', '8:00', 'Thursday', 125.0, 2],
    '375': ['HKG', 'HNL', '6:00', 'Friday', '11:00', 'Friday', 299.99, 4],
    '444': ['NRT', 'LHR', '15:00', 'Friday', '3:00', 'Saturday', 125.0, 3],
    '1572': ['HNL', 'HNL', '4:00', 'Sunday', '8:00', 'Sunday', 125.0, 2] 
}

round_trip=[]
night_flight=[]

##2
for number,details in flightdict.items():
	if details[0] == details[1]:
		round_trip.append(number)
	if details[3] != details[5]:
		night_flight.append(number)

print("The list of flight numbers for the round-trip flights is ",round_trip)
print("The list of flight numbers for the overnight flights is ",night_flight)
