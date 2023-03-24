function calculateLove() {
    var name1 = document.getElementById("name1").value.toLowerCase();
    var name2 = document.getElementById("name2").value.toLowerCase();
    var lovePercentage = Math.floor(Math.random() * 100) + 1; // Generate a random number between 1 and 100
    var result = document.getElementById("result");
    result.innerHTML = name1 + " and " + name2 + " have a " + lovePercentage + "% love match!"; // Display the result
    
}

document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    calculateLove(); // Call the function to calculate the love percentage
});
