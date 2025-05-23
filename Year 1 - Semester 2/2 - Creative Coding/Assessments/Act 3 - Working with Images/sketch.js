// Sets the bokeh or circle size
const bokehSize = 16;
// Sets the bokeh count
// The higher the faster the image gets revealed
const bokehCount = 16;

let imageSource;

function mask(){
  // Use a circle for the mask
  circle(width * 0.5, height * 0.5, Math.min(width, height));
}

function getBokeh(){
  // Use JavaScript's in built function because it's faster
  const coordX = Math.random();
  const coordY = Math.random();

  // Get bokeh color but scale it to the image's resolution to fit
  const bokehCol = imageSource.get(coordX * imageSource.width, coordY * imageSource.height);

  // Use 
  fill(bokehCol[0], bokehCol[1], bokehCol[2], 100);
  circle(coordX * width, coordY * height, bokehSize);
}

function preload(){
  // Preload image to save on memory
  imageSource = loadImage('desertNight.jpg');
}

function setup(){
  // Utilize entire screen
  createCanvas(windowWidth, windowHeight);
  // Set initial background to black
  background(0);
  // Disable stroke
  noStroke();
  // Mask the canvas
  clip(mask);
}

function draw(){
  // Render multiple bokeh shapes dependant on whether it renders the bokeh image faster
  for(let i = 0; i < bokehCount; i++){
    getBokeh();
  }

  // Render a black text to reveal a hidden message at the end
  fill(255);
  textSize(32);
  textAlign(CENTER,CENTER);
  text("The Bokeh (Pointellism) \nEffect", width * 0.5, height * 0.9);
}