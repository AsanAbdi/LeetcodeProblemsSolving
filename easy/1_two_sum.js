var twoSum = function(nums, target) {
    var map = {};
    for(var i = 0 ; i < nums.length ; i++){
        var n = nums[i];

        if(map[target-n] >= 0){
            return [map[target-n],i]
        } 
        else {
            map[n] = i;  
        }
    }
};