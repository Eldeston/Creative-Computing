const noiseScale = 2.0;

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
}

function flowLine(x, y, z, w){
  noFill();
  stroke(255, 255, 255, 64);

  beginShape();
  
  for(let i = 0; i < width; i++){
    let noise0 = perlinCustom(i / width + x * 0.125 + z);
    let noise1 = perlinCustom(i / width - x * 0.25 + z);
    let noise2 = perlinCustom(i / width * 2.0 + x + z);
  
    vertex(i, height / 2 - map((noise0 + noise1 + noise2) * y, -3, 3, -256, 256) + w);
  }
  
  endShape();
}

function draw(){
  background(0, 0, 0, 128);
  
  let secondTime = millis() * 0.001;
  secondTime *= 0.25;

  for(let i = 0; i <= 16; i++){
    flowLine(secondTime, 0.5 + i / 8, 0, 0);
    flowLine(secondTime, 0.5 + i / 8, 120, 0);
  }
}