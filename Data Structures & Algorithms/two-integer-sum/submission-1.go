func twoSum(nums []int, target int) []int {
    // Initialize a hash map to store value -> index
    prevMap := make(map[int]int)

    for i, num := range nums {
        diff := target - num

        // Check if the difference already exists in our map
        if j, ok := prevMap[diff]; ok {
            return []int{j, i}
        }

        // Add the current number and its index to the map
        prevMap[num] = i
    }

    // Return nil if no solution is found (though LeetCode guarantees one)
    return nil
}