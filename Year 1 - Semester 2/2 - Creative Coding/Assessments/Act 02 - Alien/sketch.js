function mix(valueX, valueY, mixA){
  // Linear interpolation from GLSL's mix() function
  return (valueY - valueX) * mixA + valueX;
}

function eyes(coordX, coordY, size){
  // Loops multiple circles to create the ollusion of a stretching eyeball
  const eyeLength = 0.5;
  const iterations = 16;
  const stepSize = eyeLength / iterations;
  
  // Eyeball color as white
  fill(255);

  // Iterates over the circles
  for(let stepCurr = 0; stepCurr < eyeLength; stepCurr += stepSize){
    circle(
      mix(coordX, cursorX, stepCurr),
      mix(coordY, cursorY, stepCurr),
      size
    );
    stepCurr += stepSize;
  }
  
  // Draws the pupil as 2 circles
  const pupilSize = size * 0.25;
  
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
  // Renders horn as 2 circles
  // Set color the same as the skin but darker
  fill(0, 150, 0);
  circle(coordX, coordY, size);
  
  // Uses same color as background to mask and make it look like a horn
  fill(220);
  circle(coordX, coordY - 64, size);
}

function mouth(coordX, coordY, size){
  // Renders mouth as 2 circles, same idea as the horn
  fill(0);
  circle(coordX, coordY, size);
  
  fill(0, 180, 0);
  circle(coordX, coordY - 64, size * 0.9);
}

function setup(){
  // Utilize entire screen
  createCanvas(windowWidth, windowHeight);
  // Disable stroke
  noStroke();
}

function draw(){
  background(220);
  // Translates canvas to its center
  translate(width / 2, height / 2);

  // Finds the mouse coordinates since the canvas has been translated
  cursorX = mouseX - height / 2;
  cursorY = mouseY - width / 2;

  // Render all the body parts
  horn(0, 0, 400);
  fill(0, 180, 0);
  circle(0, 256, 512);
  mouth(0, 256, 400);
  eyes(0, 128, 256);
}