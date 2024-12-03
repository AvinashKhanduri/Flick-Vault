let seats = document.querySelector(".all-seats");
for (let i = 0; i < 59; i++) {
    let randint = Math.floor(Math.random() * 2);
    let booked = randint === 1 ? "booked" : "";
    

    seats.insertAdjacentHTML(
        "beforeend",
        `<input type="checkbox" name="tickets" id="s${i + 2}"/>
        <label for="s${i + 2}" class="seat ${booked}"></label>`
    )
}

let tickets = seats.querySelectorAll("input");
tickets.forEach((ticket) => {
    ticket.addEventListener("change", () => {
        let amount = document.querySelector(".amount").innerHTML;
        let count = document.querySelector(".count").innerHTML;

        amount = Number(amount);
        count = Number(count);

        if (ticket.checked) {
            count += 1;
            amount += 200;
        }
        else {
            count -= 1;
            amount -= 200;
        }
        document.querySelector(".amount").innerHTML = amount;
        document.querySelector(".count").innerHTML = count;
    })
})


function updateFormValues() {
    // Get dynamic values for ticket count and amount
    const ticketCount = document.querySelector('.count').innerText;
    const totalAmount = document.querySelector('.amount').innerText;

    // Set the values of the hidden inputs
    document.getElementById('ticket_count').value = ticketCount;
    document.getElementById('total_amount').value = totalAmount;
}

// Add an event listener to update the form values before submission
document.getElementById('ticket-form').addEventListener('submit', function(e) {
    updateFormValues(); // Update values before submitting the form
});