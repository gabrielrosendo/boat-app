var currentImageIndex = 0;
var images = [
  'static/images/galerySample/yacht1/pic1.jpg',
  'static/images/galerySample/yacht1/pic2.jpg',
  'static/images/galerySample/yacht1/pic3.jpg',
  'static/images/galerySample/yacht1/pic4.jpg',
  'static/images/galerySample/yacht1/pic5.jpg',
  'static/images/galerySample/yacht1/pic6.jpg'
];

function showImage(imageSrc) {
    var expandedImg = document.getElementById("expandedImg");
    expandedImg.src = imageSrc;
    var modal = document.getElementsByClassName("modal")[0];
    modal.style.display = "block";
  }
  
function closeImage() {
    var modal = document.getElementsByClassName("modal")[0];
    modal.style.display = "none";
  }


function changeImage(n) {
    currentImageIndex += n;
    if (currentImageIndex < 0) {
      currentImageIndex = images.length - 1;
    } else if (currentImageIndex >= images.length) {
      currentImageIndex = 0;
    }
    var expandedImg = document.getElementById("expandedImg");
    expandedImg.src = images[currentImageIndex];
  }
document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowLeft") {
      changeImage(-1); 
    } else if (event.key === "ArrowRight") {
      changeImage(1); 
    }
  });
