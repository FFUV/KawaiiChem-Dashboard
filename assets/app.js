// app.js

document.addEventListener('DOMContentLoaded', function () {
    // Anime.js animation for fadeInUp effect
    anime.timeline({
        targets: '.plot',
        easing: 'easeOutQuad',
        duration: 1000,
        delay: function (el, i) {
            return i * 100;
        },
        translateY: [20, 0],
        opacity: [0, 1],
        loop: false
    });

    // Cute cursor
    document.body.style.cursor = 'url("path_to_cute_cursor.png"), auto';

    // Create anime elements
    var animeContainer = document.getElementById('anime-container');

    for (var i = 0; i < 10; i++) {
        var animeElement = document.createElement('div');
        animeElement.className = 'anime-element';
        animeElement.style.left = Math.random() * window.innerWidth + 'px';
        animeElement.style.top = Math.random() * window.innerHeight + 'px';

        animeContainer.appendChild(animeElement);

        // Anime.js animation for interactive movement
        anime({
            targets: animeElement,
            translateX: function () {
                return anime.random(-50, 50) + 'vw';
            },
            translateY: function () {
                return anime.random(-20, 20) + 'vh';
            },
            scale: function () {
                return anime.random(1, 2);
            },
            easing: 'easeInOutQuad',  // Cute easing for a kawaii feel
            duration: 3000,
            loop: true
        });
    }
});
