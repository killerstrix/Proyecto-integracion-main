const carrito = document.querySelector('#carrito');
const listaProductos = document.querySelector('#lista-productos');
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const vaciarCarrito = document.querySelector('#vaciar-carrito');
const comprar = document.querySelector('#comprar');
let articulosCarrito = [];

cargarEventListeners();

function cargarEventListeners() {
  comprar.addEventListener('click', obtenerTotal);

  listaProductos.addEventListener('click', agregarProducto);

  carrito.addEventListener('click', eliminarProducto);

  document.addEventListener('DOMContentLoaded', () => {
    articulosCarrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carritoHTML();
  })

  vaciarCarrito.addEventListener('click', () => {
    articulosCarrito = [];
    limpiarHTML();
    sincronizarStorage();
  });
}

function agregarProducto(e) {
  e.preventDefault();
  if (e.target.classList.contains('agregar-carrito')) {
    const productoSeleccionado = e.target.parentElement.parentElement;
    leerDatosProducto(productoSeleccionado);
  }
}

function eliminarProducto(e) {
  if (e.target.classList.contains('borrar-productos')) {
    const ProductoID = e.target.getAttribute('data-id');

    articulosCarrito = articulosCarrito.filter(producto => producto.id !== ProductoID);
    carritoHTML();
  }
}

function leerDatosProducto(producto) {

  const infoProducto = {
    nombre: producto.querySelector('h4').textContent,
    precio: producto.querySelector('span').textContent,
    imagen: producto.querySelector('img').src,
    id: producto.querySelector('a').getAttribute('data-id'),
    cantidad: 1
  }

  const existe = articulosCarrito.some(producto => producto.id === infoProducto.id);
  if (existe) {
    const productos = articulosCarrito.map(producto => {
      if (producto.id === infoProducto.id) {
        producto.cantidad++;
        return producto;
      } else {
        return producto;
      }
    });
    articulosCarrito = [...productos];
  } else {
    articulosCarrito = [...articulosCarrito, infoProducto]
  }
  console.log(articulosCarrito)
  carritoHTML();
}

function carritoHTML() {

  limpiarHTML();

  articulosCarrito.forEach(producto => {
    const { imagen, nombre, precio, cantidad, id } = producto;
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>
        <img src="${imagen}" width="100">
      </td>
      <td>
        ${nombre}
      </td>
      <td>
        ${precio}
      </td>
      <td>
        ${cantidad}
      </td>
      <td>
        <a href="#" class="borrar-productos" data-id="${id}"> X</a>
      </td>
    `;

    contenedorCarrito.appendChild(row);
  })

  const total = articulosCarrito.reduce((acc, producto) => acc + producto.precio * producto.cantidad, 0);
  const rowTotal = document.createElement('tr');
  rowTotal.innerHTML = `
    <td colspan="4" style="text-align: right;">Total:</td>
    <td><span id="total-compra">$${total}</span></td>
  `;
  contenedorCarrito.appendChild(rowTotal);

  sincronizarStorage();
}

function sincronizarStorage() {
  localStorage.setItem('carrito', JSON.stringify(articulosCarrito));
}

function limpiarHTML() {
  while (contenedorCarrito.firstChild) {
    contenedorCarrito.removeChild(contenedorCarrito.firstChild);
  }
}

function obtenerTotal() {
  const total = document.querySelector("#total-compra").textContent;
  console.log(total)
}