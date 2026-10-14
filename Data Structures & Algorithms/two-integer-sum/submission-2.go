func twoSum(nums []int, target int) []int {
    prev := make(map[int]int)

    for i, num := range nums{
        comp := target - num

        if j, ok := prev[comp]; ok{
            return[]int{j , i}
        } 

        prev[num] = i
    }
    return nil
}