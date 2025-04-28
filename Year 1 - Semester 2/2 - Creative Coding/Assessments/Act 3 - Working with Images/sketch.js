/*

NOTE: for some reason, the image is not working.
Further debugging required.

*/

var imageSource, imageX, imageY;

function preload(){
  imageSource = loadImage('colorWheel.png');
}


function mask(){
  ellipse(200, 200, 250);
}

function setup(){
  createCanvas(400, 400);
  background(0);
  noStroke();
  clip(mask);
  
}

function draw(){
  imageX = random(width);
  imageY = random(height);

  var imageCol = imageSource.get(imageX, imageY);

  fill(imageCol[0], imageCol[1], imageCol[2], 100);
  ellipse(imageX, imageY, 20, 20);

  fill(0);
  textSize(30);
  textAlign(CENTER,CENTER);
  text("HALA, MUMU", 200, 200);
}