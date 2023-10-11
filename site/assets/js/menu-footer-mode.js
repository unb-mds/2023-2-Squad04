document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var loader = document.getElementById('loader');
        loader.style.display = 'none';
    }, 1000);
});


const includeHTML = (path, targetElementId) => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    document.getElementById(targetElementId).innerHTML = xhr.responseText;
                    resolve();
                } else {
                    reject(new Error(`Erro: ${path}. Status: ${xhr.status}`));
                }
            }
        };

        xhr.open('GET', path, true);
        xhr.send();
    });
};

//INCLUI O MENU
includeHTML('menu.html', 'menu')
    .then(() => {
        // Obtém o elemento do campo de pesquisa
        var searchInput = document.getElementById('search-input');

        // Evento de tecla enter no campo de pesquisa
        searchInput.addEventListener('keydown', function(event) {
            if (event.keyCode === 13) {
                event.preventDefault();

                // Obtém o valor e redireciona para a página de pesquisa
                var termoPesquisa = searchInput.value;
                window.location.href = 'pesquisar.html?por=' + encodeURIComponent(termoPesquisa);
            }
        });

        // Obtém o elemento do botão de pesquisa
        var searchButton = document.getElementById('search-button');

        searchButton.addEventListener('click', function() {
            // Obtém o valor e redireciona para a página de pesquisa
            var termoPesquisa = searchInput.value;
            window.location.href = 'pesquisar.html?por=' + encodeURIComponent(termoPesquisa);
        });

        // TROCANDO ENTRE MODO ESCURO E MODO CLARO //
        const colorToggleBtn = document.getElementById('color-toggle');
        let isLightMode = localStorage.getItem('isLightMode') === 'true';

        colorToggleBtn.innerText = isLightMode ? "🌒 Modo escuro" : "☀️ Modo claro";

        if (isLightMode) {
            document.body.classList.add('light-mode');
        }

        colorToggleBtn.addEventListener('click', () => {
            isLightMode = !isLightMode;
            document.body.classList.toggle('light-mode', isLightMode);

            localStorage.setItem('isLightMode', isLightMode);

            colorToggleBtn.innerText = isLightMode ? "🌒 Modo escuro" : "☀️ Modo claro";
        });
    })
    .catch((error) => {
        console.error(error);
    });

// INCLUINDO O FOOTER
includeHTML('footer.html', 'footer');