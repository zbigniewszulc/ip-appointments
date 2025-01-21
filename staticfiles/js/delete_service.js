document.addEventListener("DOMContentLoaded", function() {
    const modalTitle = document.getElementById('deleteModalLabel');
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let serviceId = this.getAttribute('data-service-id');
            let serviceName = this.getAttribute('data-service-name');
            if (serviceId) {
                let deleteUrl = this.getAttribute('data-url');
                document.getElementById('serviceId').value = serviceId;
                document.getElementById('deleteForm').action = deleteUrl;
                // Override modal title with the relevant service name
                modalTitle.innerText = `Delete Service: ${serviceName}`;
            } else {
                alert('Unexpected Error: No service ID found.');
            }
        });
    });
});
