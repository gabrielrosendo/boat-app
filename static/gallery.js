function showInquiryPopup() {
  document.getElementById('inquiryPopup').style.display = 'flex';
}

function closeInquiryPopup() {
  document.getElementById('inquiryPopup').style.display = 'none';
}
document.addEventListener('DOMContentLoaded', function() {
  var popup = document.getElementById('inquiryPopup');

  window.addEventListener('click', function(event) {
    if (event.target === popup) {
      closeInquiryPopup();
    }
  });

})
var currentImageIndex = 0;

var idData = document.getElementById("data-id");
var boatId = idData.getAttribute('data-boat-id');

var galleryData = document.getElementById("gallery-data");
var imagesData = galleryData.getAttribute("data-images"); // Retrieve the 'data-images' attribute correctly
var images = JSON.parse(imagesData)

for (var i = 0; i < images.length; i++) {
  images[i] = '/static/images/gallery/' + boatId + '/' + images[i];
}

console.log(images);

function showImage(imagePath) {
  var expandedImg = document.getElementById("expandedImg");
  expandedImg.src = imagePath;
  expandedImg.alt = "Expanded Image";
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
