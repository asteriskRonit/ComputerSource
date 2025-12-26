document.getElementById('add-product-form').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Product added (simulated)');
  this.reset();
});