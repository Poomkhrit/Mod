document.addEventListener('DOMContentLoaded', () => {
    const gameContainer = document.getElementById('game-container');
    
    // Example code to load and display an asset
    const img = document.createElement('img');
    img.src = 'Assets/icon.png';  // Replace with the actual path to your asset
    gameContainer.appendChild(img);

    // Add your game logic here
});