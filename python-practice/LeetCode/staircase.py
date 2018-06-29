class Solution:
    
    def memoize(func):
      cache = {}
      def memo_func(_, n):
        if n not in cache:
          cache[n] = func(_, n)
        return cache[n]
      return memo_func

    @memoize
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)
