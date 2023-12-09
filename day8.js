const fs = require("fs");
let contents = fs.readFileSync("day8.txt").toString().split(/\r?\n/);

let test = [
  "RL",
  "",
  'AAA = (BBB, CCC)',
  'BBB = (DDD, EEE)',
  'CCC = (ZZZ, GGG)',
  'DDD = (DDD, DDD)',
  'EEE = (EEE, EEE)',
  'GGG = (GGG, GGG)',
  'ZZZ = (ZZZ, ZZZ)',
];

let test2 = [
  'LLR',
  '',
  'AAA = (BBB, BBB)',
  'BBB = (AAA, ZZZ)',
  'ZZZ = (ZZZ, ZZZ)',
];

let test3 = [
  'LR',
  '',
  '11A = (11B, XXX)',
  '11B = (XXX, 11Z)',
  '11Z = (11B, XXX)',
  '22A = (22B, XXX)',
  '22B = (22C, 22C)',
  '22C = (22Z, 22Z)',
  '22Z = (22B, 22B)',
  'XXX = (XXX, XXX)',
];
let moves = contents;
// moves = test
// moves = test2;
// moves = test3;

let map = {};
let curSpotsPt2 = []

for (let i = 2; i < moves.length; i++) {
  let location = moves[i].slice(0, 3);
  let l = moves[i].slice(7, 10);
  let r = moves[i].slice(12, 15);
  map[location] = { l, r };
  if(location[2] === "A"){
    curSpotsPt2.push(location)
  }
  // console.log(map[location]);
}
let i = 0;
let curSpot = "AAA";
let moveOrder = moves[0].toLowerCase();
while (true) {
  let x = i % moveOrder.length;
  let nextM = moveOrder[x];
  let nextS = map[curSpot][nextM];

  if (nextS === "ZZZ") {
    console.log("part1=", i + 1);
    break;
  }
  curSpot = nextS;
  i++;
}



// part 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

console.log(curSpotsPt2)

function findNext(dir, loc){
  return map[loc][dir]
}
function findStep(start){
  let pos = start
  let i = 0
  while(pos[2] !== "Z"){
    let d = moveOrder[i % moveOrder.length]
    pos = findNext(d, pos)
    i++
  }
  return i
}
function hcf(num1, num2){
  let highest = 1
  for(let i = 1; i <= num1 && i<= num2; i++){
    if (num1 % i === 0 && num2 % i === 0){
      highest = i
    }
  }
  return highest
}
let lcm = 1
for(let start of curSpotsPt2){
  let steps = findStep(start)
  let h = hcf(lcm, steps)
  lcm = (lcm * steps) / h
}

console.log("part2 = ", lcm)
// i = 0
// while(true){
//   let x = i % moveOrder.length;
//   let nextM = moveOrder[x];
//   let nextSpots = curSpotsPt2.map((a) => findNext(nextM, a))
//   if(nextSpots.every(a => a[2] === "Z")){
//     console.log(i + 1)
//     break
//   }

//   curSpotsPt2 = nextSpots
//   i++
//   // if(i % 1000  0){
//   //   console.log(i)
//   // }
// }


