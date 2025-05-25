// Sets the number of lanes
const lanes = 16;
// Sets the number of vehicles
const vehicles = 16;

// Sets frog speed
const frogSpeed = 64.0;
// Sets vehicle speed
const vehicleSpeed = 16.0;

// Sets frog size
const frogSize = 32;
// Sets half the size of the frog
// Useful for setting bounding boxes
const frogSizeHalf = frogSize * 0.5;

// Sets car size
const vehicleSizeX = 128;
const vehicleSizeY = 32;
// Sets half the size of the vehicle's dimensions
const vehicleSizeHalfX = vehicleSizeX * 0.5;
const vehicleSizeHalfY = vehicleSizeY * 0.5;

// Sets street padding
const paddingX = 128;
const paddingY = 1;

// Gets the inverse of lanes
const lanesInv = 1 / lanes;
// Generates an array and gets its keys from an iterator
const lanePos = [...Array(lanes - 1).keys()];

// Tracks frog data
let frogData;
// Tracks vehicle data
let vehicleData = [];

// For game menu
let gameMenu = true;
// Tracks game state
let gameFreeze = false;

class vehicle{
    constructor(){
        // Randomize vehicle color
        this.color = color(
            Math.random() * 255,
            Math.random() * 255,
            Math.random() * 255
        );

        // Set new lane for the vehicle
        this.vehiclePos = createVector(
            Math.random() * windowWidth,
            (random(lanePos) + 1) * lanesInv * height
        );

        // Randomize vehicle direction
        this.direction = Math.random() * 2.0 - 1.0;
    }

    updateCar(){
        // Update vehicle by moving 4 steps ahead
        // this.direction will determine the direction of the offset
        this.vehiclePos.x += this.direction * vehicleSpeed;
    }

    boundCar(){
        // Check if vehicle is outside bounds
        if(
            this.vehiclePos.x >= (windowWidth + paddingX) ||
            this.vehiclePos.x <= -paddingX
        ){
            // Randomize vehicle direction
            this.direction = Math.random() * 2.0 - 1.0;
            // Set new lane for the vehicle
            this.vehiclePos.set(
                random([-paddingX, windowWidth + paddingX]),
                (random(lanePos) + 1) * lanesInv * height
            );
        }
    }

    displayCar(){
        // Randomize vehicle color
        fill(this.color);
        rect(this.vehiclePos.x, this.vehiclePos.y, vehicleSizeX, vehicleSizeY);
    }
}

class frog{
    constructor(){
        // Set frog position
        this.frogPos = createVector(windowWidth * 0.5, 0);
    }

    updateFrog(){
        // Update frog by moving at random values
        this.frogPos.y += Math.random() * frogSpeed;
    }

    displayFrog(){
        // Display green frog
        fill(0, 255, 0);
        square(this.frogPos.x, this.frogPos.y, 32);
    }

    collideFrog(vehicle){
        // Check if frog has crossed the street
        if(
            this.frogPos.y - frogSizeHalf >= (windowHeight + paddingY) ||
            this.frogPos.y + frogSizeHalf <= -paddingY
        ){
            fill(255);
            textSize(32);
            background(0, 255, 0);
            textAlign(CENTER, CENTER);
            text("Press SPACE to Start", windowWidth * 0.5, windowHeight * 0.5);

            // Freeze game
            gameFreeze = true;
            // Reset frog position
            this.frogPos.set(windowWidth * 0.5, 0);
        }

        // Check if frog has collided with vehicle
        if(
            this.frogPos.x - frogSizeHalf <= vehicle.vehiclePos.x + vehicleSizeHalfX &&
            this.frogPos.x + frogSizeHalf >= vehicle.vehiclePos.x - vehicleSizeHalfX &&
            this.frogPos.y - frogSizeHalf <= vehicle.vehiclePos.y + vehicleSizeHalfY &&
            this.frogPos.y + frogSizeHalf >= vehicle.vehiclePos.y - vehicleSizeHalfY
        ){
            fill(255);
            textSize(32);
            background(255, 0, 0);
            textAlign(CENTER, CENTER);
            text("Game Over", windowWidth * 0.5, windowHeight * 0.45);
            text("Press 'r' to restart", windowWidth * 0.5, windowHeight * 0.55);

            // Freeze game
            gameFreeze = true;
            // Reset frog position
            this.frogPos.set(windowWidth * 0.5, 0);
        }
    }
}

function setup(){
    // Create a responsive canvas
    createCanvas(windowWidth, windowHeight);

    // Disable stroke
    noStroke();
    // Render rectangle from center
    rectMode(CENTER);

    // Initialize frog data
    frogData = new frog();
    // Intitialize vehicle data
    for(let i = 0; i < vehicles; i++) vehicleData[i] = new vehicle();
}

function draw(){
    // Render game menu and stop the draw function
    if(gameMenu){
        fill(255);
        textSize(32);
        background(50);
        textAlign(CENTER, CENTER);
        text("Crossy Roads", windowWidth * 0.5, windowHeight * 0.45);
        text("Press SPACE to Start", windowWidth * 0.5, windowHeight * 0.55);
        return;
    }

    // Freeze game when game state is readhed (loss or victory)
    if(gameFreeze) return;

    // Set street black
    background(0);

    // Display frog
    frogData.displayFrog();

    // Loop through all the vehicles
    for(let vehicle of vehicleData){
        // Display, update, and check for bounding boxes for the car
        vehicle.displayCar();
        vehicle.updateCar();
        vehicle.boundCar();

        // Check if frog has collided with vehicle
        frogData.collideFrog(vehicle);
    }
}

function keyPressed(){
    // Move frog by updating position
    if(key == 'w') frogData.updateFrog();
    // When 'r' is pressed, restart game
    if(key == 'r') gameFreeze = false;
    // When space is pressed, start game
    if(key == ' ') gameMenu = false;
}
