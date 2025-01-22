document.addEventListener("DOMContentLoaded", function() {
    var cancelButtons = document.querySelectorAll('.cancel-btn');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var appointmentId = this.getAttribute('data-appointment-id');
            var appointmentDate = this.getAttribute('data-appointment-date');
            var appointmentTimeSlot = this.getAttribute('data-time-slot');
            if (appointmentId) {
                var cancelUrl = this.getAttribute('data-url');
                document.getElementById('appointmentId').value = appointmentId;
                document.getElementById('cancelForm').action = cancelUrl;
                document.getElementById('cancel-appointment').innerText = `Appointment: ${appointmentDate} at ${appointmentTimeSlot}`;
            } else {
                alert('Unexpected Error: No appointment ID found. Please contact us.');
            }
        });
    });
});