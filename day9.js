const fs = require("fs");
let contents = fs.readFileSync("day9.txt").toString().split(/\r?\n/);

let test = [
  "0 3 6 9 12 15",
  '1 3 6 10 15 21',
  '10 13 16 21 30 45',
];

// first thought is just brute force
// write recursive func that takes an arr
// creates new func of arr[n+1] - arr[n]
// if all elements in new function are the same then
// return last element
// else last element plus recursive answer from new element

function findNextandPrev(arr){
  if(arr.every((a) => a === 0)){
    return [0, 0]
  }
  let diffArr = []
  for(let i = 0; i <arr.length - 1; i++){
    let diff = arr[i+1] - arr[i]
    diffArr.push(diff)
  }
    let [prev, next] = findNextandPrev(diffArr)
    return [arr[0] - prev, arr.pop() + next]
}

let nextVals = []
let prevVals = []
let readings = contents
// readings = test
for(let i = 0; i < readings.length; i++){
  let reading = readings[i].split(" ").map(a => parseInt(a))
  let [prev, next] = findNextandPrev(reading)
  prevVals.push(prev)
  nextVals.push(next)
}

console.log(nextVals)
function add(accumulator, a) {
  return accumulator + a;
}
console.log(nextVals.reduce(add, 0))

//part 2

console.log("part2=", prevVals.reduce(add, 0))

