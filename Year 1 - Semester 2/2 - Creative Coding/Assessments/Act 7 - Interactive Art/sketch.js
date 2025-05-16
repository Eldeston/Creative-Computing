// Disables friendly error to increase performance
p5.disableFriendlyErrors = true;

const particles = 4096;
const particleSize = 1;
const particleSpeed = 1.0;

const noiseSpeed = 0.03125;
const noiseScale = 1 / 256;
const noiseRotations = 3 * Math.PI;

let currTime = 0;
let timeSine = 0;
let particleList = [];

class particle{
  constructor(position, velocity){
    // Upon construction of variable, store variables to this class
    this.position = position;
    this.velocity = velocity;
  }

  updateParticle(){
    // Multiply velocity by particleSpeed and add to position to update and move the particle
    this.position.add(this.velocity.mult(particleSpeed));

    // Calculate new velocity vector based on perlin noise
    let angle = noise((this.position.x - mouseX) * noiseScale, (this.position.y - mouseY) * noiseScale, currTime) * noiseRotations;
    // Create a 2D vector and assign new velocity
    this.velocity.set(Math.sin(angle), Math.cos(angle));

    // Finally, color the particle according to current velocity and time
    stroke(Math.abs(this.velocity.x) * 255, Math.abs(this.velocity.y) * 255, timeSine);

    // Check if particle goes outside the window borders and reset position
    if(this.position.x > windowWidth || this.position.x < 0 || this.position.y > windowHeight || this.position.y < 0) this.position.set(Math.random() * windowWidth, Math.random() * windowHeight);
  }

  displayParticle(){
    // Simply display the particle with a point
    point(this.position.x, this.position.y);
  }
}

function setup(){
  // Utilize full window size
  createCanvas(windowWidth, windowHeight);
  // Set stroke thickness
  strokeWeight(particleSize);
  // Don't use fill
  noFill();

  // Set initial background white
  background(0, 0, 0)

  // Generate new particles first on setup
  for(let i = 0; i < particles; i++){
    particleList[i] = new particle(createVector(0, 0), createVector(-1, 0));
  }
}

function windowResized(){
  // Keeps window responsive
  resizeCanvas(windowWidth, windowHeight);
}

function draw(){
  // Calculate time per frame and not per particle to save performance
  currTime = millis() * 0.001 * noiseSpeed;
  // Calculate sine wave with time per frame
  timeSine = Math.sin(currTime) * 128 + 128;

  // Set alpha to 8 to create trails
  background(0, 0, 0, 8);

  // Load, update, and display particles
  for(let i = 0; i < particleList.length; i++){
    particleList[i].updateParticle();
    particleList[i].displayParticle();
  }
}