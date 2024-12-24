let w, n;
function setup() {
  cnv = createCanvas((w = 500), w);
  stroke(50, 60, 80);
  rectMode(CENTER);

  noLoop();

  strokeWeight(0.5);
  frameRate(2);
}

function draw() {
  push();
  translate(w / 2, w / 2);

  n = int(randomGaussian(10, 50));
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
  draw();
}

function keyPressed() {
  if (keyCode === 83) {
    save(cnv, "tile", "jpg");
  }
}
