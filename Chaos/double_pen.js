//https://editor.p5js.org/K.A.Rousan/full/_2xYgdHTN
//try it

var r1 = 125;
var sliderr1;
var r2 = 125;
var sliderr2;
var m1 = 10;
var sliderm1;
var m2 = 10;
var sliderm2;
let a1 = 0;



let a2 = 0;
let a1_v = 0;
let a2_v = 0;
var g = 1;
var sliderg;


let px2 = -1;
let py2 = -1;
let cx, cy;

let buffer;

function setup() {
  let canvas = createCanvas(800, 600);
  canvas.position(300,50);
  sliderm1 = createSlider(1,20,10,1);
  sliderm2 = createSlider(1,20,10,1);
  sliderr1 = createSlider(2,200,125,1);
  sliderr2 = createSlider(1,250,125,1);
  sliderg  = createSlider(0,10,1,1);


  sliderm1.input(draw);
  sliderm1.input(draw);
  sliderr1.input(draw);
  sliderr2.input(draw);
  sliderg.input(draw);


  pixelDensity(1);
  a1 = PI/2;
  a2 = PI / 2;
  cx = width / 2;
  cy = 200;
  buffer = createGraphics(width, height);
  buffer.background(0);
  buffer.translate(cx, cy);
}

function draw() {
	m1 = sliderm1.value()
	m2 = sliderm1.value()
	r1 = sliderr1.value()
	r2 = sliderr2.value()
  background(220,180,200);
  imageMode(CORNER);
  image(buffer, 0, 0, width, height);

  let num1 = -g * (2 * m1 + m2) * sin(a1);
  let num2 = -m2 * g * sin(a1 - 2 * a2);
  let num3 = -2 * sin(a1 - a2) * m2;
  let num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2);
  let den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
  let a1_a = (num1 + num2 + num3 * num4) / den;

  num1 = 2 * sin(a1 - a2);
  num2 = (a1_v * a1_v * r1 * (m1 + m2));
  num3 = g * (m1 + m2) * cos(a1);
  num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2);
  den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
  let a2_a = (num1 * (num2 + num3 + num4)) / den;

  translate(cx, cy);
  stroke(0);
  strokeWeight(2);

  let x1 = r1 * sin(a1);
  let y1 = r1 * cos(a1);

  let x2 = x1 + r2 * sin(a2);
  let y2 = y1 + r2 * cos(a2);
  fill(255,0,255);
  ellipse(0,0,10,10);
  fill(0);
  stroke(0,255,255);
  line(0, 0, x1, y1);
  stroke(0);
  fill(255,0,0);
  ellipse(x1, y1, m1, m1);
  stroke(255,255,0);
  line(x1, y1, x2, y2);
  fill(0,255,0);
  stroke(0);
  ellipse(x2, y2, m2, m2);

  a1_v += a1_a;
  a2_v += a2_a;
  a1 += a1_v;
  a2 += a2_v;

  buffer.stroke(255,0,0);
  if (frameCount > 1) {
    buffer.line(px2, py2, x2, y2);
  }

  px2 = x2;
  py2 = y2;
}
