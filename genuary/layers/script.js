//genuary day 2
let w, n;
let c = [50, 60, 80];
function setup() {
  cnv = createCanvas((w = 500), w);
  noLoop();
  strokeWeight(0.25);
  n = int(random(40, 60));
  for (let i = -10; i < n; i++) {
    nm = random(-2, 20);
    r1 = random(-50, 180);
    fill(c[0] + r1, c[1] + r1, c[2] + r1);
    stroke(c[0] - r1, c[1] - r1, c[2] - r1, 100);
    beginShape();

    for (let j = 0; j <= width; j++) {
      vertex(
        j,
        (height / n) * i +
          (nm / 5) * cos(j / 15 - nm / 4) * sin(j / 25 - nm / 4) +
          cos(j / 50 - nm / 4) * sin(j / 100 - nm * i) * nm +
          random(-1, 1) * sin(j / 100)
      );
    }
    vertex(width, height);
    vertex(0, height);
    endShape();
  }
  for (let i = 0; i < 100000; i++) {
    r1 = random(-50, 180);
    stroke(c[0] + r1, c[1] + r1, c[2] + r1);
    point(random(0, width), random(0, height));
  }
}
function touchStarted() {
  if (mouseY < 0 || mouseY > height || mouseX < 0 || mouseX > width) {
    return true; // Let the touch event pass through to other elements
  }
  setup();
  // Prevent default touch behavior
  return false;
}

function keyPressed() {
  if (keyCode === 83) {
    save(cnv, "layer", "jpg");
  }
}
