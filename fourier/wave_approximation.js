//By K.A.Rousan
//https://editor.p5js.org/K.A.Rousan/full/DTJdc2lOK
//https://www.youtube.com/channel/UC5GoG8e7CNCwwgYlh4VyNqA
let time = 0;
let path = [];
let on = 1;

let epyslider;
let inslider;
let onslider;


function setup() {
  createCanvas(windowWidth, windowHeight/1.2);
  epyslider = createSlider(2, 300, 2);
  inslider = createSlider(1, 7, 2,1);
  onslider = createSlider(0,1,1);
}

function draw() {
  background(0);
  translate(0.9*windowWidth/3, 1.1*windowHeight/3);

  let x = 0;
  let y = 0;
  fill(255,0,0);
  circle(x,y,6);

  if( onslider.value()== 1){
  for (let i = 1; i < epyslider.value(); i=i+inslider.value()) {
    let prevx = x;
    let prevy = y;
    let radius = 90 * (4 / (i * PI));
    x += radius * cos(i * time);
    y += radius * sin(i * time);
    noFill();
    stroke(100+i*i*7,50,255-i*10);
    circle(prevx, prevy, radius * 2);
    stroke(255-i,i*i*i,0);
    line(prevx, prevy, x, y);
    stroke(0,255,255);
    circle(x,y,4);
  }
  }
  else{
  for (let i = 1; i < epyslider.value(); i=i+2) {
    let prevx = x;
    let prevy = y;
    let radius = 300 * (4 *(pow(-1,(i-1)/2))/ (i*i * PI*PI));
    x += radius * cos(i * time);
    y += radius * sin(i * time);
    noFill();
    stroke(100+i*i*7,50,255-i*10);
    circle(prevx, prevy, radius * 2);
    stroke(255-i,i*i*i,0);
    line(prevx, prevy, x, y);
    stroke(0,255,255);
    circle(x,y,4);
  }
  }
  path.unshift(y);


  translate(0.9*windowWidth/3, 0);
  stroke(0,255,0);
  line(x - 0.9*windowWidth/3, y, 0, path[0]);
  fill(0,200,200);
  stroke(0,200,200);
  circle(0, path[0],7);
  beginShape();
  noFill();
  stroke(255,255,0);
  for (let i = 0; i < path.length; i++) {
    vertex(i, path[i]);
  }
  endShape();

  time += 0.06;

  if (path.length > 600) {
    path.pop();
  }
  stroke(250,150,200);
  text('No. of epycles',-1.2*width/2,20+height/2);
  text('value of increase of n',150-1.2*width/2,20+height/2);
  text('0 or 1 switch',300-1.2*width/2,20+height/2);
}
