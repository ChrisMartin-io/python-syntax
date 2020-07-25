function findMultiples(arr, count) {
  let freqObj = freqCounter(arr);
  let retArr = [];
  for (let key in freqObj) {
    if (freqObj[key] >= count) {
      retArr.push(+key);
    }
  }
  return retArr;
}



function freqCounter(arr) {
  let obj = {};
  for (let i = 0; i < arr.length; i++) {
    if (obj[arr[i]] === undefined) {
      obj[arr[i]] = 1;
    } else {
      obj[arr[i]] += 1;
    }
  } 
  return obj;
}
