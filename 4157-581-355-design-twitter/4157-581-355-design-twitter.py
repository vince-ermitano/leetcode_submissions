class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> list of [time, tweetId]
        self.followerMap = defaultdict(set) # userId -> set of userIds

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []
        self.follow(userId, userId)

        for followeeId in self.followerMap[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                minHeap.append([time, tweetId, followeeId, idx-1])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx-1])

        return res


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)