window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.NavBarDesign');
    if (window.pageYOffset > 0) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

