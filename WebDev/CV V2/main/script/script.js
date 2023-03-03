window.onscroll = function() {scroll()};       // to trigger "scroll" function on page scroll
window.onload = function() {currentSlide(1)};  // to trigger slideshow on page load

function darkMode(){                         // dark mode
  var element = document.body;
  element.classList.toggle("dark-mode");
}

function scroll(){                                                                              // function to show how far you have scrolled
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;                // in a webpage
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;          
  var scrolled = (winScroll / height) * 100;                                                           
  document.getElementById("progress").style.width = scrolled + "%";                                    
}                                                                                                      

function openNav(){                                              // function to push "all" div to the right
  document.getElementById("nav").style.width = "200px";          // and shows the nav
  document.getElementById("all").style.marginLeft = "200px";
}
function closeNav(){                                             // function to close nav
  document.getElementById("nav").style.width = "0";              // and normalize "all" div position
  document.getElementById("all").style.marginLeft= "0";
}

var slideIndex = 1;                  // function for slideshow
showSlides(slideIndex);
function currentSlide(n){
  showSlides(slideIndex = n);
}
function showSlides(n){
  var i;
  var slides = document.getElementsByClassName("slides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length){
    slideIndex = 1
  }    
  if (n < 1){
    slideIndex = slides.length
  }
  for (i = 0; i < slides.length; i++){
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++){
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}