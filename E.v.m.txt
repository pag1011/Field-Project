#Project = Electronic Voting Machine (E.V.M.)

print("Please enter your voter id")

voters = input("Please enter your email id = ")

print("Please enter the otp sent to your gmail id. Do not share with anyone.")

print("Your voter id is verified. Now you can caste your vote by pressing the given symbols of respective candidates of your own choice.")


voter_id  = ["abc123@gmail.com", "def456@gmail.com", "ghi789@gmail.com", "jkl101@gmail.com", "mno112@gmail.com"]

series = [1, 2, 3, 4, 5]

print("Voters Name\tseries")

for i in range(len(voter_id)):
    print(voter_id[i] + "\t\t" + str(series[i]))

candidates = ["Prachi", "Sarthak", "Somya", "Tarun", "Suhani"]

symbol = [1, 2, 3, 4, 5]

print("Candidates\tSymbol")

for i in range(len(candidates)):
    print(candidates[i] + "\t\t" + str(symbol[i]))

def winner(candidates):
    votes = Counter(candidates)
    dict = {}
 
    for value in votes.values():
        dict[value] = []
 
    for (key,value) in votes.items():
        dict[value].append(key)
 
    maxVote = sorted(dict.keys(),reverse=True)[0]
 
    if len(dict[maxVote])>1:
        print (sorted(dict[maxVote])[0])
    else:
        print (dict[maxVote][0])








