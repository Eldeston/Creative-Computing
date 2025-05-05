const noiseScale = 1.0;

let currPoints = [];

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
  return noise(x * noiseScale) * 2.0 - 1.0;
}

function setup(){
  createCanvas(windowWidth, windowHeight);
 
  background(0);

  for(let i = 0; i < 16; i++){
    let pointX = random(width);
    let pointY = random(height);

    currPoints[i] = [pointX, pointY];
  }
}

function draw(){
  background(0, 0, 0, 8);
  
  let secondTime = millis() * 0.001;

  for(let i = 0; i < currPoints.length; i++){
    let currPointX = currPoints[i][0];
    let currPointY = currPoints[i][1];

    currPointX += secondTime * 128.0;
    currPointY += perlinCustom(secondTime) * abs(currPointY - height * 0.5);

    circle(
      coordFract(currPointX, width),
      coordFract(currPointY, height),
      4
    );
  }
}