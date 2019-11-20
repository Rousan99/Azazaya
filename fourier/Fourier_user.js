//By K.A.Rousan
//https://editor.p5js.org/K.A.Rousan/full/pjZLu-5m6
//https://www.youtube.com/channel/UC5GoG8e7CNCwwgYlh4VyNqA
const Austin = 0;
const ONN = 1;
let x = [];
let fourierr;
let time = 0;
let path = [];
let art = [];
let state = -1;


function mousePressed() {
  state = Austin;
  art = [];
  x = [];
  y = [];
  time = 0;
  path = [];
}

function mouseReleased() {
  state = ONN;
  const step = 1;
  for (let i = 0; i < art.length; i += step) {
    const c = new Complex(art[i].x, art[i].y);
    x.push(c);
  }
  fourierr = cft(x);
  fourierr.sort((a, b) => b.amp - a.amp);
}

function setup() {
  wall=createCanvas(windowWidth, windowHeight);
}

function epicycles(x, y, rotation, fourier) {
  for (let i = 0; i < fourier.length; i++) {
    let prevx = x;
    let prevy = y;
    let freq = fourier[i].freq;
    let radius = fourier[i].amp;
    let phase = fourier[i].phase;
    x += radius * cos(freq * time + phase + rotation);
    y += radius * sin(freq * time + phase + rotation);
    stroke(255,50,50,100);
    strokeWeight(2.1)
    noFill();
    ellipse(prevx, prevy, radius * 2);
    stroke(100,200,255);
    strokeWeight(1.8)
    line(prevx, prevy, x, y);
  }
  return createVector(x, y);
}

function draw() {
  background(0);

  if (state == Austin) {
    let point = createVector(mouseX - width / 2, mouseY - height / 2);
    art.push(point);
    stroke(50,255,20);
    noFill();
    beginShape();
    for (let v of art) {
      vertex(v.x + width / 2, v.y + height / 2);
    }
    endShape();
  } else if (state == ONN) {
    let v = epicycles(width / 2, height / 2, 0, fourierr);
    path.unshift(v);

    beginShape();
    stroke(255,255,0)
    noFill();
    for (let i = 0; i < path.length; i=i+1) {
      vertex(path[i].x, path[i].y);
    }
    endShape();

    const dt = TWO_PI / fourierr.length;
    time += dt;

    if (time > TWO_PI) {
      time = 0;
      path = [];
    }
  }
}
class Complex {
  constructor(a, b) {
    this.re = a;
    this.im = b;
  }

  add(c) {
    this.re += c.re;
    this.im += c.im;
  }

  mult(c) {
    const re = this.re * c.re - this.im * c.im;
    const im = this.re * c.im + this.im * c.re;
    return new Complex(re, im);
  }
}

function cft(x) {
  const X = [];
  const N = x.length;
  for (let k = 0; k < N; k++) {
    let sum = new Complex(0, 0);
    for (let n = 0; n < N; n++) {
      const phi = (TWO_PI * k * n) / N;
      const c = new Complex(cos(phi), -sin(phi));
      sum.add(x[n].mult(c));
    }
    sum.re = sum.re / N;
    sum.im = sum.im / N;

    let freq = k;
    let amp = sqrt(sum.re * sum.re + sum.im * sum.im);
    let phase = atan2(sum.im, sum.re);
    X[k] = { re: sum.re, im: sum.im, freq, amp, phase };
  }
  return X;
}
