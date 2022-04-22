import csv
import sys
import pyrankvote

from pyrankvote import Candidate, Ballot

candidates = []
ballots = []

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        names = next(csvreader)
        for name in names:
            candidates.append(Candidate(name))

        for row in csvreader:
            row = row[:len(candidates)]
            ranked_choices = []
            for i in range(1, len(candidates) + 1):
                try:
                    idx = row.index(str(i))
                    ranked_choices.append(candidates[idx])
                except:
                    break
            ballots.append(Ballot(ranked_candidates=ranked_choices))

def main():
    if len(sys.argv) < 3:
        return

    filename = sys.argv[1]
    num_winners = int(sys.argv[2])

    read_csv(filename)

    election_result = pyrankvote.single_transferable_vote(candidates, ballots, num_winners)

    print(election_result)

if __name__ == "__main__":
    main()
