var carousel = document.querySelector('.carousel');
var cellCount = 9;
var selectedIndex = 0;

var urlParams = new URLSearchParams(window.location.search);
var n_pics = urlParams.get('n_pics');
var cell = urlParams.get('cell').split(',');
var img_path = urlParams.get('img_path');
var img_list = urlParams.get('img_list').split(',');
var img_size = urlParams.get('img_size').split(',');

// const testpara = document.getElementById("test_para")
// testpara.innerHTML = location.href

 if (img_path) {
    n_pics=img_list.length;
}

for (var i = 0; i < n_pics; i++) {
  var div = document.createElement("div");
  div.className = 'carousel__cell';
  div.style.width = cell[0];
  div.style.height = cell[1];
  var ith = Math.round(i*360/n_pics);
  div.style.background = 'hsla('+ ith +', 100%, 50%, 0.8)';
  div.style.transform = 'rotateY('+ith+'deg) translateZ(500px)';
  carousel.appendChild(div);

  if (img_path) {
    var img = document.createElement("img");
    p = img_path+"/"+img_list[i];
    img.src = p;
    img.style.maxWidth = img_size[0];
    img.style.maxHeight = img_size[1];
    div.appendChild(img);
  } else {
    div.innerHTML = i+1
  }
}

function rotateCarousel() {
  var angle = selectedIndex / cellCount * -360;
  carousel.style.transform = 'translateZ(-500px) rotateY(' + angle + 'deg)';
}

var prevButton = document.querySelector('.previous-button');
prevButton.addEventListener( 'click', function() {
  selectedIndex--;
  rotateCarousel();
});

var nextButton = document.querySelector('.next-button');
nextButton.addEventListener( 'click', function() {
  selectedIndex++;
  rotateCarousel();
});

function rotate_periodically() {
  selectedIndex++;
  rotateCarousel();
}
var interval = setInterval(rotate_periodically, 3000)