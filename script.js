// Aqui você pode adicionar interatividade ao seu site, como:
// - Filtrar skins
// - Mostrar detalhes ao clicar no botão "Ver Detalhes"
// - Adicionar um carrossel de imagens
// - etc.

console.log("Script carregado!");

// Exemplo básico: adicionar um evento de clique aos botões de "Ver Detalhes"
const detailButtons = document.querySelectorAll('.skin-item button');

detailButtons.forEach(button => {
    button.addEventListener('click', function() {
        alert('Detalhes da skin serão exibidos aqui!');
        // Em uma aplicação real, você buscaria os detalhes da skin correspondente
        // e os exibiria em algum lugar da página.
    });
});