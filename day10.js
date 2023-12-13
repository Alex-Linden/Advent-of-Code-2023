const fs = require("fs");
let contents = fs.readFileSync("day10.txt").toString().split(/\r?\n/);

let test1 = fs.readFileSync("day10T1.txt").toString().split(/\r?\n/);

let test2 = fs.readFileSync("day10T2.txt").toString().split(/\r?\n/);

const pipeMoves = {
  "|": [[1, 0], [-1, 0]],
  '-': [[0, 1], [0, -1]],
  'L': [[-1, 0], [0, 1]],
  'J': [[-1, 0], [0, -1]],
  '7': [[1, 0], [0, -1]],
  'F': [[1, 0], [0, 1]],
};

class PipeGame {
  constructor(map) {
    this.map = map;
    this.start = this.findStart();
  }

  findStart() {
    for (let row = 0; row < this.map.length; row++) {
      let col = this.map[row].indexOf("S");
      if (col !== -1) {
        return [row, col];
      }
    }
  }

  findStartNeighbors() {
    const [sX, sY] = this.start;
    const possibleN = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let validN = [];
    for (let n of possibleN) {
      // console.log(n)
      const [pX, pY] = [sX + n[0], sY + n[1]];
      let pipe = this.map[pX][pY];
      let moves = pipeMoves[pipe];
      if (pipe === "." || pipe === undefined) {
        continue;
      }
      // console.log(pipeMoves[pipe])
      for (let i = 0; i < moves.length; i++) {
        if (sX === pX + moves[i][0] && sY === pY + moves[i][1]) {
          if (i === 1) {
            validN.push([pX + moves[0][0], pY + moves[0][1]]);
          } else {
            validN.push([pX + moves[1][0], pY + moves[1][1]]);
          }
        }
      }
    }
    return validN;
  }
  //need to switch to tracking direction rather than previous pos
  nextStep(curPos, prevPos) {
    console.log(curPos, prevPos);
    let [cX, cY] = curPos;
    let [pX, pY] = prevPos;
    let pipe = this.map[cX][cY];
    console.log("nextStep pipe", pipe);
    for (let n of pipeMoves[pipe]) {
      if (pipe === "-") {
        if (pY !== cY + n[1]) {
          return [cX + n[0], cY + n[1]];
        }
      } else if (pipe === "|") {
        if (pX !== cX + n[0]) {
          return [cX + n[0], cY + n[1]];
        }
      } else if (pX !== cX + n[0] && pY !== cY + n[1]) {
        return [cX + n[0], cY + n[1]];
      }
    }
  }
  //TODO: create find total steps, will implement findStartN and nextStep plus counter
  findFarthest() {
    let [cur1, cur2] = this.findStartNeighbors();
    let prev1 = this.start;
    let prev2 = this.start;
    let i = 1;

    while (cur1 !== cur2 && cur1 !== this.start) {
      let next1 = this.nextStep(cur1, prev1);
      let next2 = this.nextStep(cur2, prev2);
      prev1 = cur1;
      cur1 = next1;
      prev2 = cur2;
      cur2 = next2;
      i++;
    }
    return i + 1;
  }

}

let t1 = new PipeGame(test1);
let t2 = new PipeGame(test2);
let puzzle = new PipeGame(contents);

console.log(t1.findFarthest());
// console.log(t2.findFarthest())
// console.log(puzzle.findFarthest())