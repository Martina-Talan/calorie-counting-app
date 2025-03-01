// Your JavaScript script
document.addEventListener('DOMContentLoaded', function() {
    const carbsInput = document.getElementById('carbs-input');
    const proteinInput = document.getElementById('protein-input');
    const fatInput = document.getElementById('fat-input');
    const totalPercentage = document.getElementById('total-percentage');
    
    updateSumDisplay();  // Initialize the sum display on page load

    carbsInput.addEventListener('input', updateSumDisplay);
    proteinInput.addEventListener('input', updateSumDisplay);
    fatInput.addEventListener('input', updateSumDisplay);

    function updateSumDisplay() {
        const carbsValue = parseInt(carbsInput.value) || 0;
        const proteinValue = parseInt(proteinInput.value) || 0;
        const fatValue = parseInt(fatInput.value) || 0;

        const newSum = carbsValue + proteinValue + fatValue;
        totalPercentage.textContent = newSum + '%';
    }
});
