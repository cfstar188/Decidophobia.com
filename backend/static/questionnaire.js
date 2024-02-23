// Function to open the popup
function openPopup() {
    document.getElementById("myPopup").style.display = "block";
}

// Function to submit the form
function submitForm() {
    document.getElementById("myPopup").style.display = "none";
    document.getElementById("preferencesForm").submit();
    //Need to send result pages to the user
}

// Function to automatically open the popup on page load
window.onload = function () {
    openPopup();
};

//page switch from home page to questionnaire page
function switchPage() {
    
}