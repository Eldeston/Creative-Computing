const noiseScale = 1.0;
const pointCount = 16;

let seed = 0;
let pointCoords = [];

function squared(x){
  return x * x;
}

function mix(x, y, z){
  return x + (y - x) *z;
}

function coordFract(x, axis){
  // return x;
  return fract(x / axis) * axis;
}

function perlinCustom(x){
  return noise(x) * 2.0 - 1.0;
}

function setup(){
  createCanvas(windowWidth, windowHeight);
  
  background(0);
}

function draw(){
  background(0, 0, 0, exp(-frameCount * 0.01));
  
  noStroke();
  
  let secondTime = millis() * 0.001;

  for(let i = 0; i < pointCoords.length; i++){
    let currPointX = pointCoords[i][0];
    let currPointY = pointCoords[i][1];
    
    currPointX += secondTime * 128.0;
    currPointY += map(noise(secondTime * 0.125 + pointCoords[i][2] * 128.0), 0, 1, -256, 256);
  
    stroke(0, 0, 0, 0);
    fill(pointCoords[i][4], pointCoords[i][5], pointCoords[i][6]);
    circle(
      coordFract(currPointX, width),
      coordFract(currPointY, height),
      4
    );
  }
}

function mousePressed(){
  for(let i = 0; i < pointCount; i++){
    let currPointX = random(windowWidth);
    let currPointY = random(windowHeight * 0.4, windowHeight * 0.6);

    let colorR = random(255.0);
    let colorG = random(255.0);
    let colorB = random(255.0);

    pointCoords.push([currPointX, currPointY, random(-1.0, 1.0), 0, colorR, colorG, colorB]);
  }
}