let products = [];
fetch('data/products.json')
  .then(r => r.json())
  .then(data => {
    products = [].concat(...Object.values(data));
    renderGrid(products);

    document.getElementById('searchBox').addEventListener('input', e => {
      const term = e.target.value.toLowerCase();
      renderGrid(products.filter(p => p.name.toLowerCase().includes(term)));
    });
  });

function renderGrid(list) {
  const grid = document.getElementById('productGrid');
  grid.innerHTML = '';
  list.forEach(p => {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `
      <img src="assets/placeholder.png" alt="${p.name}" />
      <h3>${p.name}</h3>
      <p><strong>Brand:</strong> ${p.brand}</p>
      <p><strong>Price:</strong> Rs. ${p.price}</p>
      <button onclick="location.href='#contact'">Enquiry</button>`;
    grid.appendChild(card);
  });
}
