// Waits for the DOM content to be fully loaded before executing scripts
document.addEventListener('DOMContentLoaded', function(){
    // Get information from input and buttons adn store in variables
    // Use constants to save memory
    const literCost = document.getElementById('costPerLiter');
    const liters = document.getElementById('liters');
    const calculateButton = document.getElementById('calculateButton');
    const totalCostDisplay = document.getElementById('totalCost');
    
    // If the button is clicked, execute selected function
    calculateButton.addEventListener('click', calculateTotalCost);
    
    // Calculates the total cost of petrol from input and updates the result to the display
    function calculateTotalCost(){
        // Get values from inputs and convert them to floats
        const costPerLiter = parseFloat(literCost.value);
        const litersPurchased = parseFloat(liters.value);
        
        // Calculate total cost
        const totalCost = costPerLiter * litersPurchased;
        
        // Format result to 2 decimal places and update the display
        totalCostDisplay.textContent = `£${totalCost.toFixed(2)}`;
    }
});