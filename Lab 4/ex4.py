# Try to append to a tuple. It wont work!

surveyRespondents = (1012, 1035, 1021, 1053)
print("Original tuple of survey respondents:", surveyRespondents)

# surveyRespondents += (1067,) 
# #This will raise an Attribute Error

surveyRespondents = surveyRespondents + (1054,)
print("After adding 1054:", surveyRespondents)

