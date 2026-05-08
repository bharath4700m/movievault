const searchInput = document.getElementById("searchInput");
const genreFilter = document.getElementById("genreFilter");

searchInput.addEventListener("input", filterMovies);
genreFilter.addEventListener("change", filterMovies);

function filterMovies(){

    const searchText = searchInput.value.toLowerCase();
    const genreValue = genreFilter.value;

    const movies = document.querySelectorAll(".movie-card");

    movies.forEach(movie => {

        const title = movie.dataset.title.toLowerCase();
        const genre = movie.dataset.genre;

        const matchesSearch = title.includes(searchText);

        const matchesGenre =
            genreValue === "All" || genre === genreValue;

        if(matchesSearch && matchesGenre){
            movie.style.display = "block";
        }
        else{
            movie.style.display = "none";
        }

    });

}