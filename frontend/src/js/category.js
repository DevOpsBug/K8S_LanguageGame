// Map of languages to flag image paths
const flagImages = {
    english: 'https://devopsbug.com/media/projects/openlingua/images/flags/united-26967.svg',
    italian: 'https://devopsbug.com/media/projects/openlingua/images/flags/italy-162326.svg',
    german: 'https://devopsbug.com/media/projects/openlingua/images/flags/germany-4894687.svg',

};

// Map of categories to image paths
const categoryImages = {
    fruits: 'https://devopsbug.com/media/projects/openlingua/images/categories/fruit-4202929_640.png',
    vegetables: 'https://devopsbug.com/media/projects/openlingua/images/categories/vegetables-1105635_640.jpg',
    animals: 'https://devopsbug.com/media/projects/openlingua/images/categories/zoo-7417502_640.png',
};

// Parse language from query parameters
const urlParams = new URLSearchParams(window.location.search);
const selectedLanguage = urlParams.get('language');

// Set the flag for the selected language
const languageFlagElement = document.getElementById('languageFlag');
if (selectedLanguage && flagImages[selectedLanguage]) {
    languageFlagElement.src = flagImages[selectedLanguage];
    languageFlagElement.alt = `${selectedLanguage} flag`;
} else {
    console.error('Invalid or missing language selection');
    languageFlagElement.style.display = 'none'; // Hide the flag image if no valid selection
}

// Dynamically render category tiles with images
function renderCategoryTiles() {
    const categoryContainer = document.getElementById('categorySelection');

    Object.entries(categoryImages).forEach(([category, imageUrl]) => {
        const tile = document.createElement('div');
        tile.className = 'category-tile';
        tile.onclick = () => selectCategory(category);

        // Create an image element for the category
        const img = document.createElement('img');
        img.src = imageUrl;
        img.alt = `${category} image`;
        img.className = 'category-image';

        // Create a label for the category
        const label = document.createElement('div');
        label.textContent = category.charAt(0).toUpperCase() + category.slice(1); // Capitalize first letter
        label.className = 'category-label';

        // Append the image and label to the tile
        tile.appendChild(img);
        tile.appendChild(label);

        // Append the tile to the container
        categoryContainer.appendChild(tile);
    });
}

// Handle category selection and navigate to game.html
function selectCategory(category) {
    const queryString = `?language=${selectedLanguage}&category=${category}`;
    window.location.href = `game.html${queryString}`;
}

// Render category tiles on load
document.addEventListener('DOMContentLoaded', renderCategoryTiles);
