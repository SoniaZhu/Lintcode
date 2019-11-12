class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0
        # write your code here
        res = 0
        leftMax = 0
        rightMax = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            leftMax = max(heights[l], leftMax)
            rightMax = max(heights[r], rightMax)
            if leftMax < rightMax:
                res += leftMax - heights[l]
                l += 1
            else:
                res += rightMax - heights[r]
                r -= 1
        return res

## merge intervals. employee free time
class Solution {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
      vector<Interval> all;
      for (const auto intervals : schedule)
        all.insert(all.end(), intervals.begin(), intervals.end());
      std::sort(all.begin(), all.end(),
                [](const Interval& a, const Interval& b){
                  return a.start < b.start;
                });
      vector<Interval> ans;
      int end = all.front().end;
      for (const Interval& busy : all) {
        if (busy.start > end)
          ans.emplace_back(end, busy.start);
        end = max(end, busy.end);
      }
      return ans;
    }
};
