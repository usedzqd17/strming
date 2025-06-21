
  const carousel = document.getElementById("carousel");
  const leftBtn = document.querySelector(".arrow.left");
  const rightBtn = document.querySelector(".arrow.right");

  leftBtn.addEventListener("click", () => {
    carousel.scrollBy({ left: -300, behavior: "smooth" });
  });

  rightBtn.addEventListener("click", () => {
    carousel.scrollBy({ left: 300, behavior: "smooth" });
  });

  // Fonction de recherche
  const searchInput = document.getElementById("searchInput");

  searchInput.addEventListener("input", () => {
    const searchTerm = searchInput.value.toLowerCase();

    const allCards = document.querySelectorAll(".card, .mini-card, .mini-card2");

    allCards.forEach((card) => {
      const titleSpan = card.querySelector(".stats span");
      const titleText = titleSpan?.textContent.toLowerCase() || "";

      if (titleText.includes(searchTerm)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });



