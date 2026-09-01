class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time , tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.following[userId].add(userId)
        for u_id in self.following[userId]:
            if self.tweets[u_id]:
                idx = len(self.tweets[u_id]) - 1
                tweets_time , tweetId = self.tweets[u_id][idx]
                minHeap.append([tweets_time , tweetId , u_id , idx - 1])
            heapq.heapify(minHeap)
        
        while minHeap and len(res)< 10:
          tweets_time , tweetsId , u_id , next_idx =  heapq.heappop(minHeap)
          res.append(tweetsId)

          if next_idx >= 0:
            next_time , next_id = self.tweets[u_id][next_idx]
            heapq.heappush(minHeap , [next_time , next_id , u_id , next_idx - 1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
