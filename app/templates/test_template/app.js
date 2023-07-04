const moreButtons = document.querySelectorAll(".more");
let expandedCard = null;

moreButtons.forEach(button => {
    button.addEventListener("click", (e) => {
        const card = e.target.closest(".card");
        if (card !== expandedCard) {
            if (expandedCard) {
                resetCard(expandedCard);
            }
            expandCard(card);
            expandedCard = card;
        } else {
            resetCard(card);
            expandedCard = null;
        }
    });
});

function expandCard(card) {
    card.style.height = "400px";
    card.querySelector(".option").style.margin = "53px auto";
    card.querySelector(".description").style.overflow = "scroll";
    card.querySelector(".description").style.maxHeight = "100px";
}

function resetCard(card) {
    card.style.height = ""; // Resets the height to its default value
    card.querySelector(".option").style.margin = "";
    card.querySelector(".description").style.overflow = "";
    card.querySelector(".description").style.maxHeight = "";
}