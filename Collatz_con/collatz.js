let start = 1;
let reset = start;
let angle =0.1;
let inc = 300;
let len=7;
let sw=2;

function setup() {
  createCanvas(innerWidth, innerHeight);
  background(0);
  colorMode(HSB, 3, 1.2, 1, 1);
  
  let minDimension = min(width, height)
  

  strokeWeight(sw);
  

}

function draw() {
  let sequence = [];
  let n = start;
  do {
    sequence.push(n);
    n = collatz(n);
  } while (n != 1);
  sequence.push(1);
  sequence.reverse();

  resetMatrix();
  translate(width / 1.5, height/1.3);
  for (let j = 0; j < sequence.length; j++) {
    let value = sequence[j];
    if (value % 2 == 0) {
      rotate(j/(j-6)*angle);

    } else {
      rotate(-j/(j-6)*angle);

    }
    
    stroke(j / sequence.length, 1,2,0.2);
    line(0, 0, 0, -len);
    translate(0, -len);
  }
  start += inc;


  if (start > 500000) {
    reset++
    start = reset
  }
}

function collatz(n) {
  // even
  if (n % 2 == 0) {
    return n / 2;
    // odd
  } else {
    return (n * 3 + 1) / 2;
  }
}
