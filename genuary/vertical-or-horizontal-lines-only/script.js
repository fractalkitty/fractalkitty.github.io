let w, n;
function setup() {
  w = min(windowWidth * 0.9, 500);
  canvas = createCanvas(w, w);
  canvas.parent("sketch-container");
  describe(
    "tile with quadrant symmetry with patterns drawn using all horizontal and vertical lines. Some are feather-like, geometrical, or clover-like. "
  );
  stroke(50, 60, 80);
  noLoop();
  strokeWeight(0.5);
}

function draw() {
  push();
  translate(w / 2, w / 2);

  n = int(randomGaussian(10, 50));
  if (n === 0) {
    n = 10;
  }
  background(230, 235, 240);
  for (let j = 0; j < 4; j++) {
    push();
    scale(0.5, 0.5);
    if (j === 0) {
      translate(-w / 2, -w / 2);
    } else if (j === 1) {
      translate(-w / 2, w / 2);
      rotate(-PI / 2);
    } else if (j === 2) {
      translate(w / 2, -w / 2);
      rotate(PI / 2);
    } else {
      translate(w / 2, w / 2);
      rotate(PI);
    }

    for (let i = -w / 2; i < w / 2; i += 0.1) {
      l = int(
        abs(
          random(i, min(i * 1.5, w / 2 - 5 * i)) * sin(i / n) -
            (i / 2) * cos(i / n / 4)
        )
      );
      if (l % 2 === 0) {
        line(i, i, i + l, i);
      } else {
        line(i, i, i, i + l);
      }
    }
    pop();
  }
  pop();
}

function mousePressed() {
  setup();
  draw();
  return false;
}
function touchStarted() {
  if (mouseY < 0 || mouseY > height || mouseX < 0 || mouseX > width) {
    return true; // Let the touch event pass through to other elements
  }
  setup();
  draw();
  // Prevent default touch behavior
  return false;
}

function keyPressed() {
  if (keyCode === 83) {
    save(canvas, "tile", "jpg");
  }
}
