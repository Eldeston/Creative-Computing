// Wheel function, allows me to reuse the wheels
function wheel(coordX, coordY, outer, inner){
  // Saves the current transformation
  // This is to reset the position and don't need to undo the transformations for each wheel
  push();

  // Translate origin for the position of the wheel
  translate(coordX, coordY);
  // Rotate wheel at 100 times a second
  rotate(-millis() * 0.01)

  // Tiyre of the wheel
  fill(0)
  circle(0, 0, outer)

  // Rim of the wheel
  fill(90)
  circle(0, 0, inner)
  
  // Designs the rim by using asterisk
  fill(45)
  textAlign(CENTER);
  textSize(outer * 1.8)
  text('*', 0, 42 * 1.8)
  
  // Designs the rim by using circle
  fill(255)
  circle(0, 0, inner * 0.33333333)

  // Resets to last transformation saved
  pop();
}

// Foundation function
// Contains the basic shapes for the base of the car
function foundation(coordX, coordY, foundationWidth, foundationHeight){
  const foundationOriginX = coordX - foundationWidth * 0.5
  const foundationOriginY = coordY - foundationHeight * 0.5
  
  fill(15, 180, 30)
  rect(foundationOriginX, foundationOriginY, foundationWidth, foundationHeight)
  
  fill(128)
  rect(foundationOriginX, foundationOriginY + 15, foundationWidth, foundationHeight * 0.1)
}

// Hood function
// Contains the basic shapes for the hood of the car
function hood(coordX, coordY, hoodWidth, hoodHeight, hoodHoof, windowScale){
  fill(15, 180, 30)
  quad(
    coordX, coordY,
    coordX + hoodWidth, coordY,
    coordX + hoodWidth, coordY + hoodHeight,
    coordX - hoodHoof, coordY + hoodHeight
  )
  
  let oneMinusScale = 1.0 - windowScale
  let windowX = coordX + oneMinusScale * hoodWidth
  let windowY = coordY + oneMinusScale * hoodHeight
  
  fill(15, 180, 180)
  quad(
    windowX, windowY,
    windowX + hoodWidth * windowScale - 15, windowY,
    windowX + hoodWidth * windowScale - 15, windowY + hoodHeight * windowScale,
    windowX - hoodHoof, windowY + hoodHeight * windowScale
  )
}

// Set up function
function setup(){
  // Create initial canvas with specified sizes
  createCanvas(windowWidth, windowHeight);
}

// Draw function
function draw(){
  // Shape layering depends on code order
  // Use fill() before a shape to color a shape
  // Same is applied for stroke but colors only the lines
  
  // fill(value/color/hex)
  // fill(red, green, blue)

  // Draw background, takes in 3 or 1 input
  // Accepts names of colors
  // Accepts ranges 0-255
  // Acccepts hex values

  // background(value/color/hex)
  // background(red, green, blue)
  background(255);
  
  // Translate orgin to 0, 0
  // translate(height / 2, width / 2)
  
  // Disable strokes
  noStroke()
  
  // Set car origin
  const carOriginX = width / 2;
  const carOriginY = height / 2
  
  hood(carOriginX - 75, carOriginY - 90, 90, 60, 45, 0.8)
  foundation(carOriginX, carOriginY, 360, 75)
  
  wheel(carOriginX - 90, carOriginY + 45, 75, 45)
  wheel(carOriginX + 90, carOriginY + 45, 75, 45)
}