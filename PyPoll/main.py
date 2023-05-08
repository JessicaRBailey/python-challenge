import os
import csv

PyPoll_csv = os.path.join("Resources", "election_data.csv")
output_txt = os.path.join("Analysis", "Poll_Analysis.txt")

total_votes = []
candidates = []
stockham_votes = []
degette_votes = []
doane_votes = []
winning_pcnt = 0 # to compare with candidates and find winner

with open(PyPoll_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    # The first row contains headers
    csv_header = next(csv_reader)
    
    # read the csv
    for vote in csv_reader:
        total_votes.append(vote[2])
        
        #A complete list of candidates who received votes
        if vote[2] not in candidates:
            candidates.append(vote[2])
        
        
        if vote[2] == "Charles Casper Stockham":
            stockham_votes.append(vote[0])
        elif vote[2] == "Diana DeGette":
            degette_votes.append(vote[0])
        elif vote[2] == "Raymon Anthony Doane":
            doane_votes.append(vote[0])
    
    #The total number of votes cast
    votes_cast = len(total_votes)
    #The total number of votes each candidate won
    #The percentage of votes each candidate won
    stockham_pcnt = round((len(stockham_votes) / votes_cast) *100,3)
    degette_pcnt = round((len(degette_votes) / votes_cast) *100,3)
    doane_pcnt = round((len(doane_votes) / votes_cast) *100,3)
    
    #The winner of the election based on popular vote
    if stockham_pcnt>winning_pcnt:
        Winner = "Charles Casper Stockham"
    if degette_pcnt>stockham_pcnt:
        Winner = "Diana DeGette"
    if  doane_pcnt>degette_pcnt:
        Winner = "Raymon Anthony Doane"
    

#print the analysis to the terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes : {votes_cast}") 
print("------------------------------")
print(f"Charles Casper Stockham: {stockham_pcnt}% ({len(stockham_votes)})") 
print(f"Diana DeGette: {degette_pcnt}% ({len(degette_votes)})") 
print(f"Raymon Anthony Doane: {doane_pcnt}% ({len(doane_votes)})")
print("------------------------------")
print(f"Winner: {Winner}")  
print("------------------------------")


# export a text file with the results
with open(output_txt, 'w') as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n------------------------------")
    txt_file.write(f"\nTotal Votes : {votes_cast}")
    txt_file.write("\n------------------------------")
    txt_file.write(f"\nCharles Casper Stockham: {stockham_pcnt}% ({len(stockham_votes)})")
    txt_file.write(f"\nDiana DeGette: {degette_pcnt}% ({len(degette_votes)})") 
    txt_file.write(f"\nRaymon Anthony Doane: {doane_pcnt}% ({len(doane_votes)})") 
    txt_file.write("\n------------------------------")
    txt_file.write(f"\nWinner: {Winner}")  
    txt_file.write("\n------------------------------")