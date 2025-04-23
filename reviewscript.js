const helpfulButtons = document.querySelectorAll('.helpful-btn');
helpfulButtons.forEach(helpfulButton => {
  helpfulButton.addEventListener('click', increaseCount);
});

function increaseCount() {
  // Select the span with the class 'helpful-count' that is within the same parent element as the button
  const countSpan = this.parentNode.querySelector('.helpful-count');
  let currentCount = parseInt(countSpan.textContent); // Get the current count
  currentCount++; // Increase the count
  countSpan.textContent = currentCount; // Update the count on the page
}

const form = document.getElementById('reviewForm');

form.addEventListener('submit', function (event) {
  event.preventDefault()
  const reviewUserName = document.getElementById('reviewUserName').value || 'Anonymous';
  const reviewTitle = document.getElementById('reviewTitleLabel').value;
  const reviewText = document.getElementById('review').value;
  const rating = document.querySelector('input[name="rating"]:checked') ? document.querySelector('input[name="rating"]:checked').value : 'No rating';
  createReview(reviewUserName, reviewTitle, reviewText, rating);
});

function createReview(userName, title, text, rating) {
  const review = document.createElement('div')
  review.classList.add('review');

  // Creating the review header
  const reviewHeader = document.createElement('div');
  reviewHeader.classList.add('review-header');

  // Adding the username and date to the header
  const reviewUser = document.createElement('span');
  reviewUser.classList.add('review-user');
  reviewUser.textContent = userName;

  const reviewDate = document.createElement('span');
  reviewDate.classList.add('review-date');
  reviewDate.textContent = new Date().toLocaleDateString();

  reviewHeader.appendChild(reviewUser);
  reviewHeader.appendChild(reviewDate);

  // Adding the title, text, and rating to the review
  const reviewTitle = document.createElement('h3');
  reviewTitle.textContent = title;
  const reviewTextParagraph = document.createElement('p');
  reviewTextParagraph.classList.add('review-text');
  reviewTextParagraph.textContent = text;
  const reviewRating = document.createElement('div');
  reviewRating.classList.add('review-rating');

  // Add rating text to the review
  const reviewRatingText = document.createElement('span');
  reviewRatingText.textContent = 'Rating: ';
  reviewRating.appendChild(reviewRatingText);
  reviewRating.appendChild(document.createTextNode(rating));

  // Create the helpful button and count
  const helpfulButton = document.createElement('button');
  helpfulButton.classList.add('helpful-btn');
  helpfulButton.textContent = 'Helpful:';
  helpfulButton.addEventListener('click', increaseCount);

  const helpfulCount = document.createElement('span');
  helpfulCount.textContent = '0';
  helpfulCount.classList.add('helpful-count');

  const helpfulText = document.createElement('span');
  helpfulText.textContent = ' people found this helpful.';

  // Add the helpful button and count to a container
  const helpfulContainer = document.createElement('div');
  helpfulContainer.classList.add('helpful-container');
  helpfulContainer.appendChild(helpfulButton);
  helpfulContainer.appendChild(helpfulCount);
  helpfulContainer.appendChild(helpfulText);

  review.appendChild(reviewHeader);
  review.appendChild(reviewRating);
  review.appendChild(reviewTextParagraph);
  review.appendChild(helpfulContainer);

  // Append the review to the reviews container
  document.getElementById('reviewsContainer')
  reviewsContainer.appendChild(review);

  // Reset the form
  document.getElementById('reviewForm').reset();
}

const languageSelector = document.getElementById('languageSelector');
const texts = {
  en: {
    header: "Product Reviews",
    subheader: "Read what our customers think",
    submitReview: "Submit a Review",
    rating: "Rating: ",
    recentReviews: "Recent Reviews",
    helpful: "Helpful",
    privacyPolicy: "Privacy Policy"
  },
  es: {
    header: "Reseñas de productos",
    subheader: "Lee lo que piensan nuestros clientes",
    submitReview: "Enviar una reseña",
    rating: "Clasificación: ",
    recentReviews: "Reseñas recientes",
    helpful: "Útil",
    privacyPolicy: "Política de privacidad"
  },
  fr: {
    header: "Avis sur les produits",
    subheader: "Lisez ce que nos clients en pensent",
    submitReview: "Soumettre un avis",
    rating: "Évaluation : ",
    recentReviews: "Avis récents",
    helpful: "Utile",
    privacyPolicy: "Politique de confidentialité"
  }
};

languageSelector.addEventListener('change', function () {
  const lang = languageSelector.value;
  document.querySelector('header h1').innerText = texts[lang].header;
  document.querySelector('header p').innerText = texts[lang].subheader;
  document.getElementById('reviewFormTitle').innerText = texts[lang].submitReview;
  document.querySelector('label[for="review"]').innerText = texts[lang].rating;
  document.querySelector('h2').innerText = texts[lang].recentReviews;
  document.querySelectorAll('.helpful-btn').forEach(button => button.innerText = texts[lang].helpful);
  document.querySelector('a').innerText = texts[lang].privacyPolicy;
});

const themeSelector = document.getElementById('colorTheme');

// Event listener for the theme selector
themeSelector.addEventListener('change', function () {
  const selectedTheme = this.value;
  changeTheme(selectedTheme);
});

// Function to change color theme
function changeTheme(theme) {
  document.body.className = `${theme}-theme`;
}

const reviewSorting = document.getElementById('sortReviews');
reviewSorting.addEventListener('change', function () {
  // Get the selected sorting option
  const sortBy = this.value;
  // Call a function to sort the reviews based on the selected option
  sortReviews(sortBy);
});

// Function to sort reviews
function sortReviews(sortBy) {
  const reviewContainer = document.getElementById('reviewsContainer');
  const reviews = reviewContainer.querySelectorAll('.review');
  const reviewsArray = Array.from(reviews);

  // Sorting logic
  reviewsArray.sort((reviewA, reviewB) => {
    if (sortBy === 'date') {
      // Extract dates from the reviews
      const dateA = new Date(reviewA.querySelector('.review-date').textContent);
      const dateB = new Date(reviewB.querySelector('.review-date').textContent);
      // Compare dates
      return dateB - dateA;
    } else if (sortBy === 'rating') {
      const ratingA = parseInt(a.querySelector('review-rating').textContent.split(' ')[1]);
      const ratingB = parseInt(b.querySelector('review-rating').textContent.split(' ')[1]);
      // Compare ratings
      return ratingB - ratingA;
    }
  });

  // Reorder reviews in the container
  reviewsArray.forEach(review => reviewContainer.appendChild(review));
}