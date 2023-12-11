const fs = require("fs");
let contents = fs.readFileSync("day10.txt").toString().split(/\r?\n/);

let test1 = fs.readFileSync("day10T1.txt").toString().split(/\r?\n/);

let test2 = fs.readFileSync("day10T2.txt").toString().split(/\r?\n/);

const pipeMoves = {
  "|": [[1, 0], [-1, 0]],
  '-': [[0, 1], [0, -1]],
  'L': [[1, 0], [0, 1]],
  'J': [[1, 0], [0, -1]],
  '7': [[-1, 0], [0, -1]],
  'F': [[-1, 0], [0, 1]],
};

class PipeGame {
  constructor(map) {
    this.map = map;
    this.start = findStart();
  }

  findStart() {
    for (let row = 0; row < this.map.length; row++) {
      let col = this.map[row].indexOf("S");
      if (col !== -1) {
        this.start = [row, col];
      }
    }
  }

  findStartNeighbors(start) {
    const [sX, sY] = start;
    const possibleN = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let validN = [];
    for (let n of possibleN) {
      const [pX, pY] = [sX + n[0], sY + n[1]];
      let pipe = this.map[pX][pY];
      for (let m of pipeMoves[pipe]) {
        if (sX === pX + m[0] && sY === pY + m[1]) {
          validN.push([pX + m[0], pY + m[1]]);
        }
      }
    }
    return validN;
  }

  nextStep(curPos, prevPos) {
    let [cX, cY] = curPos;
    let [pX, pY] = prevPos;
    let pipe = this.map[cX][cY];
    for (let n of pipeMoves[pipe]) {
      if (pX !== cX + n[0] && pY !== cY + n[1]) {
        return [cX + n[0], cY + n[1]];
      }
    }
  }


}

let t1 = new PipeGame(test1);
let t2 = new PipeGame(test2);
let puzzle = new PipeGame(contents);