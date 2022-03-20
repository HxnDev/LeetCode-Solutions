import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) 
    {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) 
        {
            if (map.containsKey(nums[i])) 
            {
                result[0] = i;
                result[1] = map.get(nums[i]);
            }
            
            else 
            {
                map.put(target - nums[i], i);
            }
        }
        return result;
    }
}