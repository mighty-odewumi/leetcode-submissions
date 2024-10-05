/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Brute force method
// Given an array nums, go through each of the elements and add the prev to the next.
// Save each result in an array.
// Put the indices of the two elements that gave each result inside another array.
// Iterate over the addition array and check if any of the results is equal to the target.
// Get the index of the result in the addition array and use it to get the indices stored in the second array.

var twoSum = function (nums, target) {
  let additionArr = [];
  let indexArr = [];

  nums.flatMap((num, index, arr) => {
    const additionResult = arr[index] + arr[index + 1];
    if (isNaN(additionResult)) {
      return [];
    } else {
      additionArr.push(additionResult);
      indexArr.push([index, index + 1]);
    }
  });

  /* for (result of additionArr) {
    if (result === target) {
      const indexOfResult = additionArr.indexOf(result);
      const indicesGivingResult = indexArr[indexOfResult];
      return indicesGivingResult;
    }
  } */

  // Using this also gives the same output as the for-of loop
  const result = additionArr.flatMap((val, index, arr) => {
    if (val === target) {
      const indexOfVal = arr.indexOf(val);
      return indexArr[indexOfVal];
    }
  });

  return result.filter(arr => arr !== undefined);
  // Not including the variable result and returning this outputs an undefined
  // because the twoSum function has nothing to return.
};
// @lc code=end

