document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
  
    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    // Basic client-side validation
    if (name.trim() === '' || email.trim() === '' || password.trim() === '') {
      alert('Please fill out all fields');
      return;
    }
  
    // For demonstration, just log the data
    console.log({ name, email, password });
  
    // Here you would usually send the data to a server
    alert('Signup successful!');
  });
  