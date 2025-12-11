// Função para atualizar badge do carrinho
function atualizarBadge(total) {
    const badge = document.getElementById("carrinhoQtd");
    if (!badge) return;

    if (total > 0) {
        badge.style.display = "inline-block";
        badge.textContent = total; // número grande e visível
    } else {
        badge.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // carregar quantidade ao abrir
    if (window.USER_IS_LOGGED_IN) {
        fetch("/carrinho/qtd/")
            .then(r => r.json())
            .then(data => atualizarBadge(data.total));
    }

document.addEventListener("click", (e) => {

    // clica em botão com data-id
    const btn = e.target.closest("[data-id]");

    if (!btn) return;

    if (!window.USER_IS_LOGGED_IN) {
        window.location.href = "/login/";
        return;
    }

    const filmeId = btn.dataset.id;

    fetch(`/carrinho/add/${filmeId}/`)
        .then(r => r.json())
        .then(data => {
            if (data.ok) atualizarBadge(data.total);
        });
});

});
