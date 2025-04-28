function setup(){
  createCanvas(512, 512);
}


function mix(valueX, valueY, mixA){
  return (valueY - valueX) * mixA + valueX;
}

function eyes(coordX, coordY, size){
  fill(255);
  circle(coordX, coordY, size);
  
  let stepCurr = 0;
  let stepSize = 0.5 / 16;
  
  for(iteration = 0; iteration < 16; iteration++){
    circle(
      mix(coordX, cursorX, stepCurr),
      mix(coordY, cursorY, stepCurr),
      size
    );
    stepCurr += stepSize;
  }
  
  let pupilSize = size * 0.25;
  
  fill(0, 0, 255);
  circle(
    mix(coordX, cursorX, 0.75),
    mix(coordY, cursorY, 0.75),
    pupilSize
  );
  
  fill(0);
  circle(
    mix(coordX, cursorX, 0.75),
    mix(coordY, cursorY, 0.75),
    pupilSize * 0.8
  );
}

function horn(coordX, coordY, size){
  fill(0, 150, 0);
  circle(coordX, coordY, size);
  
  fill(220);
  circle(coordX, coordY - 64, size);
}

function mouth(coordX, coordY, size){
  fill(0);
  circle(coordX, coordY, size);
  
  fill(0, 180, 0);
  circle(coordX, coordY - 64, size * 0.9);
}

function draw(){
  cursorX = mouseX - height / 2;
  cursorY = mouseY - width / 2;

  background(220);
  translate(width / 2, height / 2);
  
  noStroke();

  horn(0, 0, 400);
  
  fill(0, 180, 0);
  circle(0, 256, 512);
  
  mouth(0, 256, 400);
  
  eyes(0, 128, 256);
}