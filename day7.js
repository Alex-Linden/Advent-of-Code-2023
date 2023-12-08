let test = [
  '32T3K 765',
  'T55J5 684',
  'KK677 28',
  'KTJJT 220',
  'QQQJA 483',
];


const fs = require("fs");
let contents = fs.readFileSync("day7.txt").toString().split(/\r?\n/);
// console.log(contents.slice(0, 5));

let hands = test;
hands = contents;

function rankHand(hand) {
  // let score = 0
  let count = {};
  let jCount = 0;
  let maxCount = 0;
  let maxCard = "";
  for (let card of hand) {
    if (card === "J") {
      jCount++;
    } else {
      let curCount = (count[card]) ? count[card] + 1 : 1;
      count[card] = curCount
      if(curCount > maxCount){
        maxCount = curCount
        maxCard = card
      }
    }
  }
  if(jCount > 0){
    count[maxCard] += jCount
  }
  let len = Object.keys(count).length;
  if (len === 5) {
    return 1;
  } else if (len === 4) {
    return 2;
  } else if (len === 3) {
    if (Object.values(count).sort()[2] == 2) {
      return 3;
    } else {
      return 4;
    }
  } else if (len === 2) {
    if (Object.values(count).sort()[1] == 3) {
      return 5;
    } else {
      return 6;
    }
  } else {
    return 7;
  }

  // console.log(count);
}

for (let i = 0; i < hands.length; i++) {

  let score = rankHand(hands[i].slice(0, 5));
  hands[i] = [score, hands[i]];
  // console.log(hands[i]);
}

// console.log(hands);

function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  // Divide the array into two halves
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  // Merge the two sorted halves
  return merge(left, right);

}

function merge(left, right) {
  const merged = [];
  let [l, r] = [0, 0];
  const cardRank = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'];

  while (l < left.length && r < right.length) {
    if (left[l][0] < right[r][0]) {
      merged.push(left[l]);
      l++;
    } else if (left[l][0] > right[r][0]) {
      merged.push(right[r]);
      r++;
    } else {
      for (let i = 0; i < 5; i++) {
        if (cardRank.indexOf(left[l][1][i]) < cardRank.indexOf(right[r][1][i])) {
          merged.push(left[l]);
          l++;
          break;
        } else if (cardRank.indexOf(left[l][1][i]) > cardRank.indexOf(right[r][1][i])) {
          merged.push(right[r]);
          r++;
          break;
        }
      }
    }
  }
  merged.push(...left.slice(l));
  merged.push(...right.slice(r));

  return merged;
}

hands = mergeSort(hands);

let totalWinnings = 0;

for (let i = 0; i < hands.length; i++) {
  let score = parseInt(hands[i][1].split(" ")[1]);
  totalWinnings += (score * (i + 1));
}

console.log(totalWinnings);
