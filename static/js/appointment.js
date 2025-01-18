// References to time slot buttons and modal input fields
const timeSlotButtons = document.querySelectorAll('.time-slots button');
const modalDateInput = document.getElementById('modalDate');
const modalTimeSlotInput = document.getElementById('modalTimeSlot');
const modalTitle = document.getElementById('serviceModalLabel');
const submitButton = document.getElementById('bookme');
const infoSection = document.getElementById('info');

// Format date to dd/mm/yyyy
function formatDate(dateString) {
    // Split the date string into year, month, day
    const [year, month, day] = dateString.split('-'); 
    // Format the date
    return `${day}/${month}/${year}`; 
}

// Add event listeners to all time slot buttons
for (let button of timeSlotButtons) {
    button.addEventListener("click", (e) => {
        // Get the date and time from the clicked button's data attributes
        let date = e.target.getAttribute('data-date');
        let timeSlot = e.target.getAttribute('data-time');
        let withinDate = e.target.getAttribute('data-within-date');
        let withinTime = e.target.getAttribute('data-within-time');

        // Format date to dd/mm/yyyy
        let formattedDate = formatDate(date);

        // Set modal's hidden input fields with the clicked button's data
        modalDateInput.value = date; 
        modalTimeSlotInput.value = timeSlot;

        // For appointments in the past
        if (withinDate === 'false' || (withinDate === 'true' && withinTime === 'false')) {
            submitButton.classList.add('d-none');  // Disable the book button
            infoSection.innerHTML = '<p class="my-4 text-center text-danger"><em>Past appointments cannot be booked</em></p>';
        } 

        // Override modal title with formatted date and time
        modalTitle.innerText = `Appointment: ${formattedDate} at ${timeSlot}`;
    });
}

module.exports = formatDate;