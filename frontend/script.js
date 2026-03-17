const API_URL = "http://127.0.0.1:8000"; // URL backend

async function loadCharts() { // Busca e exibe os charts
    const loading = document.getElementById("loading");
    const chartsDiv = document.getElementById("charts");

    try { // Chama o endpoint
        const response = await fetch(`${API_URL}/charts`);
        const data = await response.json();

        loading.style.display = "none";

        const now = new Date().toLocaleTimeString("pt-BR");
        document.getElementById("last-updated").textContent = `Atualizado às ${now}`;

        data.tracks.forEach(track => {
            const card = document.createElement("div");
            card.classList.add("track-card");

            const youtubeEmbed = track.youtube_id // Monta o mini player (se tiver youtube_id)
                ? `<div class="yt-wrapper">
                        <iframe
                            class="yt-player"
                            data-src="https://www.youtube.com/embed/${track.youtube_id}?autoplay=1&mute=1&controls=0&modestbranding=1&loop=1&playlist=${track.youtube_id}&enablejsapi=1"
                            frameborder="0"
                            allow="autoplay; encrypted-media"
                            allowfullscreen>
                        </iframe>
                        <button class="btn-sound" onclick="toggleSound(this, '${track.youtube_id}')">🔇</button>
                   </div>`
                : "";

            card.innerHTML = `      
                <div class="track-position-badge">#${track.position}</div>
                <div class="track-cover-wrapper">
                    <img class="track-cover" src="${track.cover}" alt="${track.name}">
                    ${youtubeEmbed}
                </div>
                <div class="track-info">
                    <div class="track-name">${track.name}</div>
                    <div class="track-artist">${track.artist}</div>
                    <div class="track-album">${track.album}</div>
                    <a class="btn-spotify" href="${track.spotify_url}" target="_blank">
                        Ouvir no Spotify
                    </a>
                </div>
            `;

const videoSrc = track.youtube_id // URL do vídeo pra carregar 
    ? `https://www.youtube.com/embed/${track.youtube_id}?autoplay=1&mute=1&controls=0&modestbranding=1&loop=1&playlist=${track.youtube_id}&enablejsapi=1`
    : null;

card.addEventListener("mouseenter", () => {
    const iframe = card.querySelector(".yt-player");
    if (iframe && videoSrc) {
        iframe.src = videoSrc;
    }
});

card.addEventListener("mouseleave", () => {
    const iframe = card.querySelector(".yt-player");
    const btn = card.querySelector(".btn-sound");
    if (iframe) {
        iframe.src = "";
        if (btn) btn.textContent = "🔇";
    }
});

            chartsDiv.appendChild(card);
        });

    } catch (error) {
        loading.textContent = "Erro ao carregar os charts. Verifique se o servidor está rodando.";
        console.error(error);
    }
}

function toggleSound(btn, videoId) {
    const iframe = btn.closest(".yt-wrapper").querySelector(".yt-player");
    const isMuted = btn.textContent === "🔇";
    const baseSrc = `https://www.youtube.com/embed/${videoId}?autoplay=1&mute=${isMuted ? 0 : 1}&controls=0&modestbranding=1&loop=1&playlist=${videoId}`;
    iframe.src = baseSrc;
    btn.textContent = isMuted ? "🔊" : "🔇";
}

loadCharts();