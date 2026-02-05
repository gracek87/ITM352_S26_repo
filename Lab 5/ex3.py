responses =[ 5,7,3,8]
respondentIDs = (1012, 1035, 1021, 1053)

surveyDict = dict(zip(respondentIDs, responses))
print("Survey responses with respondent IDs:", surveyDict)

print(f"Respondent {respondentIDs[2]} gave a response of {surveyDict[respondentIDs[2]]}.")

