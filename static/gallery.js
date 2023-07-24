var currentImageIndex = 0;
images = []
async function getImages(boatId) {
  var folderPath = `static/images/gallery/${boatId}/`;
  var images = [];

  try {
    const response = await fetch(folderPath);
    if (!response.ok) {
      console.log(`Error fetching images for Boat ID: ${boatId}`);
      return images;
    }

    const fileNames = await response.text();
    const imageFiles = fileNames.split('\n').filter(fileName => fileName.trim() !== '');

    // Assuming the image file extension is .jpg
    images = imageFiles.map(fileName => `${folderPath}${fileName}`);
  } catch (error) {
    console.log(`Error fetching images for Boat ID: ${boatId}`, error);
  }

  return images;
}


async function showImage(boatId, imageIndex) {
  try {
    var images = await getImages(boatId);
    if (images.length === 0) {
      console.log(`No images found for Boat ID: ${boatId}`);
      return;
    }

    currentImageIndex = imageIndex || 0;
    if (currentImageIndex >= images.length) {
      currentImageIndex = 0;
    }

    var expandedImg = document.getElementById("expandedImg");
    expandedImg.src = images[currentImageIndex];
    var modal = document.getElementsByClassName("modal")[0];
    modal.style.display = "block";
  } catch (error) {
    console.log('Error displaying images:', error);
  }
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
