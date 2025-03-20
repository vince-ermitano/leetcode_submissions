class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # a senator should always ban another senator of the other party to his right
        # keep a queue for the order of the senators' votes
        # maintain a counter for each party to track how many are currently banned
        # keep a counter for each party to track how many currently exist
        # so that we know when a party has won

        party_counts = Counter(senate)
        num_banned_r = 0
        num_banned_d = 0
        q = deque(senate)

        print(party_counts)

        while party_counts['R'] > 0 and party_counts['D'] > 0:
            curr = q.popleft()

            if curr == 'R':
                if num_banned_r > 0:
                    num_banned_r -= 1
                else:
                    num_banned_d += 1
                    party_counts['D'] -= 1
                    q.append(curr)
            else:
                if num_banned_d > 0:
                    num_banned_d -= 1
                else:
                    num_banned_r += 1
                    party_counts['R'] -= 1
                    q.append(curr)

        return 'Radiant' if party_counts['R'] > 0 else 'Dire'