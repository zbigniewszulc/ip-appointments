document.addEventListener("DOMContentLoaded", function() {
    var cancelButtons = document.querySelectorAll('.cancel-btn');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var appointmentId = this.getAttribute('data-appointment-id');
            if (appointmentId) {
                var cancelUrl = this.getAttribute('data-url');
                document.getElementById('appointmentId').value = appointmentId;
                document.getElementById('cancelForm').action = cancelUrl;
            } else {
                alert('Unexpected Error: No appointment ID found. Please contact us.');
            }
        });
    });
});