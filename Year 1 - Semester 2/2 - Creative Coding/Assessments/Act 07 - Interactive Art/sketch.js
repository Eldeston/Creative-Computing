// Disables friendly error to increase performance
p5.disableFriendlyErrors = true;

const particles = 4096;
const particleSize = 1;
const particleSpeed = 1.0;

const noiseSpeed = 0.03125;
const noiseScale = 1 / 256;
const noiseRotations = 3 * Math.PI;

let gravity = 1;

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
    let angle = noise(this.position.x * noiseScale, this.position.y * noiseScale, currTime) * noiseRotations;
    // Create a 2D vector and assign new velocity
    this.velocity.set(Math.sin(angle), Math.cos(angle));

    // Finally, color the particle according to current velocity and time
    stroke(Math.abs(this.velocity.x) * 255, Math.abs(this.velocity.y) * 255, timeSine);

    // Check if particle goes outside the window borders and reset position
    if(this.position.x > windowWidth || this.position.x < 0 || this.position.y > windowHeight || this.position.y < 0) this.position.set(Math.random() * windowWidth, Math.random() * windowHeight);
  }

  interactParticle(){
    // Find the distance between the shape and mouse position and use an exponent function to change its range from [0, infinity] to [1, 1 / infinity]
    // Multiply mouse length to control the gravity should suck the particles in or push them out on mouse click
    let mouseLength = Math.exp(-dist(this.position.x, this.position.y, mouseX, mouseY) * noiseScale * 4.0) * gravity * 0.1;

    // Move the shapes away from the mouse using a mix function
    // Instead of using a positive interpolation, negate the mouse length so that instead of drawing the shapes into the mouse, it draws it away
    this.position.set(mix(this.position.x, mouseX, mouseLength), mix(this.position.y, mouseY, mouseLength));
  }

  displayParticle(){
    // Simply display the particle with a point
    point(this.position.x, this.position.y);
  }
}

function mix(valueX, valueY, mixA){
  // Linear interpolation from GLSL's mix() function
  return (valueY - valueX) * mixA + valueX;
}

function setup(){
  // Utilize full window size
  createCanvas(windowWidth, windowHeight);
  // Set stroke thickness
  strokeWeight(particleSize);
  // Don't use fill
  noFill();

  // Set initial background black
  background(0, 0, 0, 255)

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
    // Update particle to flow field
    particleList[i].updateParticle();
    // Interact particle with mouse gravity
    particleList[i].interactParticle();
    // Display particle
    particleList[i].displayParticle();
  }
}

function mousePressed(){
  // Change gravity on mouse click
  gravity *= -1;
}