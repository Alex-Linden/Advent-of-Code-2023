const fs = require("fs");
let contents = fs.readFileSync("day10.txt").toString().split(/\r?\n/);

let test1 = fs.readFileSync("day10T1.txt").toString().split(/\r?\n/);

let test2 = fs.readFileSync("day10T2.txt").toString().split(/\r?\n/);

let p2test1 = fs.readFileSync("day10p2t1.txt").toString().split(/\r?\n/);

let p2test2 = fs.readFileSync("day10p2t2.txt").toString().split(/\r?\n/);

let p2test3 = fs.readFileSync("day10p2t3.txt").toString().split(/\r?\n/);

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
    this.loop = [];
    this.PolyArea = 0;
    this.corners = [];
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
            validN.push([pX, pY]);
          } else {
            validN.push([pX, pY]);
          }
        }
      }
    }
    // console.log(this.map[validN[0][0]][validN[0][1]], this.map[validN[1][0]][validN[1][1]])
    return validN;
  }
  //need to switch to tracking direction rather than previous pos
  nextStep(curPos, prevPos) {
    // console.log(curPos, prevPos);
    let [cX, cY] = curPos;
    let prevPosStr = `${prevPos[0]}-${prevPos[1]}`;
    let pipe = this.map[cX][cY];
    // console.log("nextStep pipe", pipe);
    for (let n of pipeMoves[pipe]) {
      // console.log(curPos, prevPosStr, pipe, `${cX + n[0]}-${cY + n[1]}`)
      if (prevPosStr !== `${cX + n[0]}-${cY + n[1]}`) {
        return [cX + n[0], cY + n[1]];
      }
    }
  }
  cordToString(cords) {
    return `${cords[0]}-${cords[1]}`;
  }
  //TODO: create find total steps, will implement findStartN and nextStep plus counter
  findFarthest() {
    let [cur1, cur2] = this.findStartNeighbors();
    let prev1 = this.start;
    // let prev2 = this.start;
    let i = 1;
    let seen = new Set();
    seen.add(this.cordToString(prev1));
    this.loop.push(prev1);

    while (this.cordToString(cur1) !== this.cordToString(this.start)) {
      if ("LJF7".indexOf(this.map[cur1[0]][cur1[1]] !== -1)) {
        this.corners.push(cur1);
      }
      if (seen.has(this.cordToString(cur1))) {
        // console.log("cords seen")
        break;
      }
      seen.add(this.cordToString(cur1));
      seen.add(this.cordToString(cur2));
      this.loop.push(cur1);
      // this.loop.push(cur2);
      // console.log(seen)
      let next1 = this.nextStep(cur1, prev1);
      // let next2 = this.nextStep(cur2, prev2);
      prev1 = cur1;
      cur1 = next1;
      // prev2 = cur2;
      // cur2 = next2;
      i++;
    }
    console.log(this.loop.length);
    return Math.ceil(i / 2);
  }

  shoelace() {
    let len = this.corners.length;
    let sum1 = 0;
    let sum2 = 0;
    let area = 0;
    let points = this.corners;
    points.push(this.start);
    for (let i = 0; i < len - 1; i++) {
      area += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1];
      sum1 = sum1 + points[i][0] * points[i + 1][1];
      sum2 = sum2 + points[i][1] * points[i + 1][0];
    }

    sum1 = sum1 + points[len - 1][0] * points[0][1];

    sum2 = sum2 + points[0][0] * points[len - 1][1];

    area = Math.abs(sum1 - sum2) / 2;
    this.PolyArea = area
    return area;
  }

  pick() {
    return (this.PolyArea - 0.5 * this.corners.length + 1);
  }
}

let t1 = new PipeGame(test1);
let t2 = new PipeGame(test2);
let puzzle = new PipeGame(contents);

let p2t1 = new PipeGame(p2test1);
let p2t2 = new PipeGame(p2test2);
let p2t3 = new PipeGame(p2test3);

console.log(t1.findFarthest());
console.log(t2.findFarthest());
console.log(puzzle.findFarthest());
console.log("-----------------------")
console.log("p2t1",p2t1.findFarthest());
console.log(p2t1.shoelace());
console.log(p2t1.pick());
console.log("-----------------------")
console.log("p2t2", p2t2.findFarthest());
console.log(p2t2.shoelace());
console.log(p2t2.pick());
console.log("-----------------------")
console.log("p2t3", p2t3.findFarthest());
console.log(p2t3.shoelace());
console.log(p2t3.pick());

console.log("-----------------------")
console.log("pt2", puzzle.shoelace());
console.log("pt2 picks", puzzle.pick());