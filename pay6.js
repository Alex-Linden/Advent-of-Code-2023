let input = `
Time:        40     92     97     90
Distance:   215   1064   1505   1100
`;

let test = `Time:      7  15   30
Distance:  9  40  200`;
let time = [40, 92, 97, 90];
// let time = [7, 15, 30];
let distance = [215, 1064, 1505, 1100];
// let distance = [9, 40, 200];
let possible = [];

for (let i = 0; i < time.length; i++) {
  let curTime = time[i];
  let curD = distance[i];
  let [l, r] = [1, curTime];
  while (l < r) {
    let distTraveled = (curTime - l) * l;
    // console.log(distTraveled);
    if (distTraveled > curD) {
      break;
    }
    l++;
  }
  while (l < r) {
    let distTraveled = (curTime - r) * r;
    if (distTraveled > curD) {
      break;
    }
    r--;
  }
  console.log(l, r);
  possible.push(r - l + 1);
}

console.log(possible);

let out = 1
for(let p of possible){
  out *= p
}
console.log(out)

// part 2
let time2 = 40929790
// let time2 = 71530

let distance2 = 215106415051100
// let distance2 = 940200

// let l = 1
// let r = time2
// let ogMid = Math.floor((l+r)/2)
// let bottomLimit = 1

let [l, r] = [1, time2];
while (l < r) {
  let distTraveled = (time2 - l) * l;
  // console.log(distTraveled);
  if (distTraveled > distance2) {
    break;
  }
  l++;
}
while (l < r) {
  let distTraveled = (time2 - r) * r;
  if (distTraveled > distance2) {
    break;
  }
  r--;
}

console.log(r-l+1)

