def fake_predict(input_temp):

	if input_temp > 10:
		prediction = "Hot (over ten)"

	else:
		prediction = "Cold (under ten)"
	
	return prediction