class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        row,column = len(matrix)-1,0
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        def binarySearchColumn(start,end,matrix,target):
            if matrix[start][0] == target:
                return start
            elif matrix[end][0] <= target:
                return end
            while start < end:
                mid = (start + end) / 2
                if matrix[mid][0] <= target:
                    if matrix[mid+1][0] > target:
                        return mid
                    else:
                        start = mid
                elif matrix[mid][0] > target:
                    if matrix[mid-1][0] <= target:
                        return mid - 1
                    else:
                        end = mid
            if start >= end:
                return -1

        def binarySearchRow(start,end,arr,target):
            if arr[start] == target:
                return True
            while start < end:
                if end - start == 1:
                    if arr[start] == target or arr[end] == target:
                        return True
                    else:
                        return False
                mid = (start + end) / 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    start = mid
                else:
                    end = mid
            return False

        column_number = binarySearchColumn(0,len(matrix)-1,matrix,target)
        rst = binarySearchRow(0,len(matrix[column_number])-1,matrix[column_number],target)
        return rst

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]


    print s.searchMatrix(matrix,24)