fetch('http://127.0.0.1:8000/products/')
  .then(response => response.json())
  .then(data => {
    // Обрабатывайте полученные данные и отображайте их на вашем front-end
    console.log(data);
  })
  .catch(error => console.error('Ошибка при получении данных:', error));
