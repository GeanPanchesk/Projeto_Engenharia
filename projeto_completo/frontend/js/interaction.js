document.querySelectorAll('.carrossel-container').forEach(container => {
  const carrossel = container.querySelector('.carrossel');
  const btnLeft = container.querySelector('.btn-left');
  const btnRight = container.querySelector('.btn-right');

  const scrollAmount = 220;; // rola a largura visível inteira

  btnLeft.addEventListener('click', () => {
    carrossel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });

  btnRight.addEventListener('click', () => {
    carrossel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });
});

const campoBusca = document.getElementById('campoBusca');
const filmes = document.querySelectorAll('.filme');
const secoesParaEsconder = [
  document.getElementById('destaque'),
  document.getElementById('populares'),
  document.getElementById('tituloPopulares'),
  // Adicione aqui outros IDs de seções que você quer esconder
];
const todosH2 = document.querySelectorAll('h2')
const botoes1 = document.querySelectorAll('.btn.btn-right');
const botoes2 = document.querySelectorAll('.btn.btn-left');
campoBusca.addEventListener('input', () => {
  const termo = campoBusca.value.toLowerCase().trim();
  let encontrou = false;

  // Filtra os filmes
  filmes.forEach(filme => {
    const img = filme.querySelector('img');
    const nome = img.alt.toLowerCase();

    if (nome.includes(termo) && termo !== '') {
      filme.style.display = 'block';
      encontrou = true;
    } else {
      filme.style.display = 'none';
    }
  });

  //remove 
  if (termo !== '') {
    // Esconde os botões quando tem texto na busca
    botoes1.forEach(botao => botao.style.display = 'none');
  } else {
    // Mostra os botões quando a busca estiver vazia
    botoes1.forEach(botao => botao.style.display = '');
  }
  if (termo !== '') {
    
    botoes2.forEach(botao => botao.style.display = 'none');
  } else {
    botoes2.forEach(botao => botao.style.display = '');
  }
  if (termo !== '') {
    secoesParaEsconder.forEach(secao => {
      if (secao) secao.style.display = 'none';
    });
    todosH2.forEach(h2 => {
      h2.style.display = 'none'
    });
  } else {
    secoesParaEsconder.forEach(secao => {
      if (secao) secao.style.display = '';
    });

    filmes.forEach(filme => {
      filme.style.display = 'block';
    });
  }
});