/**
 * @jest-environment jsdom
 */

// Import JS file to be tested
const formatDate = require('../appointment');

// Mock HTML content
const htmlContent = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Calendar</title>
</head>
<body>
    <div class="calendar">
        <div class="row">
            <div class="col calendar-day">
                <div class="day-number">
                    <span>26 Mon</span>
                </div>
                <ul class="time-slots list-unstyled row">
                    <li class="col">
                        <button type="button" class="btn btn-primary"
                            data-date="2024-08-26"
                            data-time="10:00"
                            data-bs-toggle="modal"
                            data-bs-target="#serviceModal">
                            10:00
                        </button>
                    </li>
                    <li class="col">
                        <button type="button" class="btn btn-primary"
                            data-date="2024-08-26"
                            data-time="11:00"
                            data-bs-toggle="modal"
                            data-bs-target="#serviceModal">
                            11:00
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    
    <!-- Modal -->
    <div class="modal fade" id="serviceModal" tabindex="-1" aria-labelledby="serviceModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="serviceModalLabel">Appointment</h5> <!-- Title populated by JS -->
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form id="bookingForm" method="post">
                    <div class="modal-body">
                        <div class="mb-3">
                            <input type="hidden" name="date" id="modalDate">
                            <input type="hidden" name="time_slot" id="modalTimeSlot">
                            <label for="serviceSelect" class="form-label">Treatment type</label>
                            <select id="serviceSelect" name="service" class="form-select" required>
                                <option value="1" selected>Dental Hygiene</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-6 mx-auto my-4">
                        <button type="button" class="btn btn-lg btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn btn-lg btn-primary">Book</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
`;

beforeAll(() => {
    document.open();
    document.write(htmlContent);
    document.close();

    // Attach event listener to all buttons
    const buttons = document.querySelectorAll('.time-slots button');
    buttons.forEach((button) => {
        button.addEventListener('click', (e) => {
            // Get the date and time from the clicked button's data attributes
            const date = e.target.getAttribute('data-date');
            const timeSlot = e.target.getAttribute('data-time');
            
            // Set modal values
            document.getElementById('modalDate').value = date;
            document.getElementById('modalTimeSlot').value = timeSlot;
            
            // Set modal title
            const formattedDate = formatDate(date);
            document.getElementById('serviceModalLabel').innerText = `Appointment: ${formattedDate} at ${timeSlot}`;
        });
    });
});

test("formatDate function should correctly format the date", () => {
    expect(formatDate("2024-08-26")).toBe("26/08/2024");
});

test("Clicking time slot button should populate modal correctly", () => {
    // Simulate click event on the first button
    const timeSlotButton = document.querySelector('.time-slots button');
    timeSlotButton.click();

    // References to time slot and modal input fields
    const modalDateInput = document.getElementById('modalDate');
    const modalTimeSlotInput = document.getElementById('modalTimeSlot');
    const modalTitle = document.getElementById('serviceModalLabel');

    // Check that the modal inputs are correctly populated
    expect(modalDateInput.value).toBe("2024-08-26");
    expect(modalTimeSlotInput.value).toBe("10:00");

    // Check that the modal title is correctly updated
    expect(modalTitle.innerText).toBe("Appointment: 26/08/2024 at 10:00");
});