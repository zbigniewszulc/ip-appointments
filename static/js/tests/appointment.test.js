/**
 * @jest-environment jsdom
 */

// Import JS file to be tested
const formatDate = require('../appointment');

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("appointment/templates/appointment/calendar.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

test("formatDate function should correctly format the date", () => {
    expect(formatDate("2024-08-26")).toBe("26/08/2024");
});