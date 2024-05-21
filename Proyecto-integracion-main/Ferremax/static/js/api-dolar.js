const pesos = document.querySelector('#pesos');

document.addEventListener('DOMContentLoaded', () => {
  consultarDolar();
})

function consultarDolar() {
  const URL = 'https://mindicador.cl/api/dolar';

  fetch(URL)
    .then(respuesta => respuesta.json())
    .then(resultado => convertirADolares(resultado.serie[0].valor))
}

function convertirADolares(valorDolar) {
  const dolares_obtenidos = pesos.textContent * (1 / valorDolar)
  const dolares = document.querySelector('#dolares');
  dolares.textContent = dolares_obtenidos.toFixed(2);
}