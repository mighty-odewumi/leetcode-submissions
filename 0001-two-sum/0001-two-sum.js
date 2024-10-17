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
  /* let additionArr = [];
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
  console.log("Addition Array", additionArr);
  console.log("Index Array", indexArr);

 

  // Using this also gives the same output as the for-of loop
  const result = additionArr.flatMap((val, index, arr) => {
    if (val === target) {
      const indexOfVal = arr.indexOf(val);
      console.log(indexArr[indexOfVal]);
      // const indicesGivingResult = indexArr[indexOfVal];
      return indexArr[indexOfVal];
    }
  });

  return result.filter(arr => arr !== undefined);
  // Not including the variable result and returning this outputs an undefined
  // because the twoSum function has nothing to return.
  */

  let valuesIndex = {};

  for (let i = 0; i < nums.length; i++) {
    const secondVal = target - nums[i];
    if (Object.hasOwn(valuesIndex, secondVal)) {
      console.log("Complement found", [valuesIndex[secondVal], i]);
      return [valuesIndex[secondVal], i];
    }
    else valuesIndex[nums[i]] = i;

  }
  console.log(valuesIndex);
};