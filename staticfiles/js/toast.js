// All Django messages will use this toast to display their content
$(document).ready(function () { 
    // Time delay between each toast (milliseconds)
    var delay = 2000; 
    // Iterate over each toast 
    $('.toast').each(function(index) { 
        // Show each toast with a delay 
        setTimeout(() => $(this).toast('show'), delay * index); 
    }); 

    // still required - according to documentation
    $('[data-bs-toggle="popover"]').popover(); 
    $('#openingHours').on('click', function(e) {
        // Prevent default action
        e.preventDefault();

        $(this).popover('toggle');
    }); 
});