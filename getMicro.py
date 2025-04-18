from bs4 import BeautifulSoup
import csv

# HTML content
html_content = """
<article class="entry">
        <time datetime="2025-01-27">Day 37: (27 Jan 2025)</time>
        <p>
          A beautiful day, a mindful meditation, and an intimate conversation with a crow.
        </p>
      </article>
      <article class="entry">
        <time datetime="2025-01-26">Day 36: (26 Jan 2025)</time>
        <p>The intensity of some looks...</p>
        <a href="#lightbox-31">
          <img src="../assets/01-26-25.jpeg" alt="A large wide white oak in a meadow." />
        </a>
        <div id="lightbox-31" class="lightbox">
          <a href="#">
            <img src="../assets/01-26-25.jpeg" alt="A large wide white oak in a meadow." />
          </a>
        </div>
      </article>
      <article class="entry">
        <time datetime="2025-01-25">Day 35: (25 Jan 2025)</time>
        <p>A friend reaches wide for a hug.</p>
        <a href="#lightbox-30">
          <img src="../assets/01-25-25.JPG" alt="A large wide white oak in a meadow." />
        </a>
        <div id="lightbox-30" class="lightbox">
          <a href="#">
            <img src="../assets/01-25-25.JPG" alt="A large wide white oak in a meadow." />
          </a>
        </div>
      </article>
      <article class="entry">
        <time datetime="2025-01-24">Day 34: (24 Jan 2025)</time>
        <p>
          A hyperfocused day, but a nice walk in the sunshine.
        </p>
      </article>
      <article class="entry">
        <time datetime="2025-01-23">Day 33: (23 Jan 2025)</time>
        <p>
          Bushtits everywhere! The sun beckons me earlier each morn.
        </p>
      </article>
      <article class="entry">
        <time datetime="2025-01-22">Day 32: (22 Jan 2025)</time>
        <p>
          The moon has been beneath my feet for the past few days. I want a glimpse.
        </p>
      </article>
      <article class="entry">
        <time datetime="2025-01-21">Day 31: (21 Jan 2025)</time>
        <p>A friend reached for Saturn.</p>
        <a href="#lightbox-29">
          <img src="../assets/01-21-25.JPG" alt="A tree limb with a star (venus) at its tip." />
        </a>
        <div id="lightbox-29" class="lightbox">
          <a href="#">
            <img src="../assets/01-21-25.JPG" alt="A tree limb with a star (venus) at its tip." />
          </a>
        </div>
      </article>
      <article class="entry">
        <time datetime="2025-01-">Day 30: (20 Jan 2025)</time>
        <p>I find myself being molded by what I chose to note and observe.</p>
      </article>
      <article class="entry">
        <time datetime="2025-01-19">Day 29: (19 Jan 2025)</time>
        <p>
          I watched sea-foam skate, rocks make comet trails in waves, and
          oystercatchers dodged a wave.
        </p>
      </article>
      <article class="entry">
        <time datetime="2025-01-18">Day 28: (18 Jan 2025)</time>
        <p>Some trees remind you of how young you are.</p>
        <a href="#lightbox-28">
          <img src="../assets/01-18-25.jpg" alt="A walnut tree with high contrast in shadows and light and texture." />
        </a>
        <div id="lightbox-28" class="lightbox">
          <a href="#">
            <img src="../assets/01-18-25.jpg"
              alt="A walnut tree with high contrast in shadows and light and texture." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-17">Day 27: (17 Jan 2025)</time>
        <p>
          I took a moment to stop thinking and just knit with a soft wool
          green yarn.
        </p>
      </article>

      <article class="entry">
        <time datetime="2025-01-16">Day 26: (16 Jan 2025)</time>
        <p>
          Walking meditation - 8 steps as I breathe in and 7 as I breathe out
          - this must be my polyrhythm.
        </p>
      </article>

      <article class="entry">
        <time datetime="2025-01-15">Day 24: (15 Jan 2025)</time>
        <p>A misty day - in many ways.</p>
      </article>

      <article class="entry">
        <time datetime="2025-01-14">Day 23: (14 Jan 2025)</time>
        <p>A reflecting day.</p>
      </article>

      <article class="entry">
        <time datetime="2025-01-13">Day 23: (13 Jan 2025)</time>
        <p>I watched fluffy robins bathe vigorously in the birdbath.</p>
      </article>

      <article class="entry">
        <time datetime="2025-01-12">Day 22: (12 Jan 2025)</time>
        <p>A walk with a friend, a finished hat, existence contemplated.</p>
      </article>

      <article class="entry">
        <time datetime="2025-01-11">Day 21: (11 Jan 2025)</time>
        <p>
          A thought today: What is it to hold the geometry of self? What are
          your faces, vertices, edges? Your Chirality?
        </p>
      </article>

      <article class="entry">
        <time datetime="2025-01-10">Day 20: (10 Jan 2025)</time>
        <p>
          A walk in the fields at night was just delightful. The birds,
          Jupiter, the waxing moon, and cackling geese filled my soul.
        </p>
        <a href="#lightbox-20">
          <img src="../assets/01-10-25.JPG"
            alt="A song sparrow with opacity on a branch at night. composite with sky, stars, and tinting." />
        </a>
        <div id="lightbox-20" class="lightbox">
          <a href="#">
            <img src="../assets/01-10-25.JPG"
              alt="A song sparrow with opacity on a branch at night. composite with sky, stars, and tinting." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-09">Day 19: (9 Jan 2025)</time>
        <p>Oh my crows - I am grateful you are here with me.</p>
        <a href="#lightbox-19">
          <img src="../assets/01-09-25.JPG"
            alt="A crow in flight with the sun catching its wings and the moon below. Edited with texture and vignette." />
        </a>
        <div id="lightbox-19" class="lightbox">
          <a href="#">
            <img src="../assets/01-09-25.JPG"
              alt="A crow in flight with the sun catching its wings and the moon below. Edited with texture and vignette." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-08">Day 18: (8 Jan 2025)</time>
        <p>Robins bring me to a present moment.</p>
        <a href="#lightbox-18">
          <img src="../assets/01-08-25.JPG" alt="A robin on a branch with the waxing moon behind their head at dusk." />
        </a>
        <div id="lightbox-18" class="lightbox">
          <a href="#">
            <img src="../assets/01-08-25.JPG"
              alt="A robin on a branch with the waxing moon behind their head at dusk." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-07">Day 17: (7 Jan 2025)</time>
        <p>Puddles reflect forest by my muddy feet. A moment of awe.</p>
      </article>

      <article class="entry">
        <time datetime="2024-01-06">Day 16: (6 Jan 2025)</time>
        <p>
          The sun is out! Went for a walk where the river overflowing takes
          the trail and the kingfisher calls.
        </p>
      </article>

      <article class="entry">
        <time datetime="2025-01-05">Day 15: (5 Jan 2025)</time>
        <p>The wonders we find on walks:</p>
        <a href="#lightbox-15">
          <img src="../assets/01-05-25.JPG" alt="A small mushroom growing on the moss of a tree." />
        </a>
        <div id="lightbox-15" class="lightbox">
          <a href="#">
            <img src="../assets/01-05-25.JPG" alt="A small mushroom growing on the moss of a tree." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-04">Day 14: (4 Jan 2025)</time>
        <p>Reading and knitting all day.</p>
        <a href="#lightbox-14">
          <img src="../assets/01-04-25.JPG" alt="A partially knitted hat on circular needles." />
        </a>
        <div id="lightbox-14" class="lightbox">
          <a href="#">
            <img src="../assets/01-04-25.JPG" alt="A partially knitted hat on circular needles." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-03">Day 13: (3 Jan 2025)</time>
        <p>
          Tea, code, reading, and a walk. Over 18 goldfinches together - such
          communal bathers. I saw the moon! Finally the clouds opened enough.
        </p>
      </article>

      <article class="entry">
        <time datetime="2025-01-02">Day 12: (2 Jan 2025)</time>
        <p>A foggy day - mentally and physically.</p>
        <a href="#lightbox-12">
          <img src="../assets/01-02-25.JPG" alt="A turkey on a porch at a door (black and white)." />
        </a>
        <div id="lightbox-12" class="lightbox">
          <a href="#">
            <img src="../assets/01-02-25.JPG" alt="A turkey on a porch at a door (black and white)." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2025-01-01">Day 11: (1 Jan 2025)</time>
        <p>I didn't realize turkeys go door-to-door.</p>
        <a href="#lightbox-11">
          <img src="../assets/01-01-25.JPG" alt="A turkey on a porch at a door (black and white)." />
        </a>
        <div id="lightbox-11" class="lightbox">
          <a href="#">
            <img src="../assets/01-01-25.JPG" alt="A turkey on a porch at a door (black and white)." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2024-12-30">Day 10: (31 Dec 2024)</time>
        <p>
          A swollen river brought the end of so many paths to me. A point of
          reflection and birdwatching while retracing my steps - A walk of
          capillaries.
        </p>
      </article>

      <article class="entry">
        <time datetime="2024-12-30">Day 9: (30 Dec 2024)</time>
        <p>A long stretch and time for doodles.</p>
      </article>

      <article class="entry">
        <time datetime="2024-12-29">Day 8: (29 Dec 2024)</time>
        <p>Oh moss - you amaze me - a world within a world.</p>
        <a href="#lightbox-8">
          <img src="../assets/12-29-24.JPG"
            alt="A northern shoveler tail with head under water - black and white with vignette." />
        </a>
        <div id="lightbox-8" class="lightbox">
          <a href="#">
            <img src="../assets/12-29-24.JPG"
              alt="A northern shoveler tail with head under water - black and white with vignette." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2024-12-28">Day 7: (28 Dec 2024)</time>
        <p>
          A day of sorting books and decluttering while it drizzles.
          Yellow-rumped warblers chase each other and the wind nudges for
          attention every now and then.
        </p>
      </article>

      <article class="entry">
        <time datetime="2024-12-27">Day 6: (27 Dec 2024)</time>
        <p>
          I saw 8 northern harriers hunting together - what a sight! Also -
          lot's of northern shoveler tails.
        </p>
        <a href="#lightbox-6">
          <img src="../assets/12-27-24.JPG"
            alt="A northern shoveler tail with head under water - black and white with vignette." />
        </a>
        <div id="lightbox-6" class="lightbox">
          <a href="#">
            <img src="../assets/12-27-24.JPG"
              alt="A northern shoveler tail with head under water - black and white with vignette." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2024-12-26">Day 5: (26 Dec 2024)</time>
        <p>
          Games of Splendor, drive-by birding, and a walk in the sunshine with
          my mom by a lake.
        </p>
      </article>

      <article class="entry">
        <time datetime="2024-12-25">Day 4: (25 Dec 2024)</time>
        <p>Rainy walk + pumpkin soup + mint tea - a simple day</p>
      </article>

      <article class="entry">
        <time datetime="2024-12-24">Day 3: (24 Dec 2024)</time>
        <p>I saw a light in the forest. Practicing contentment today.</p>
        <a href="#lightbox-3">
          <img src="../assets/12-24-24.JPG"
            alt="A drop of water on a twig with moss inside and a beam of light shining toward the viewer - a sparkle." />
        </a>
        <div id="lightbox-3" class="lightbox">
          <a href="#">
            <img src="../assets/12-24-24.JPG"
              alt="A drop of water on a twig with moss inside and a beam of light shining toward the viewer - a sparkle." />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2024-12-23">Day 2: (23 Dec 2024)</time>
        <p>Sometimes I feel like I live in a painting.</p>
        <a href="#lightbox-2">
          <img src="../assets/12-23-24.JPG" alt="pond with vignette and painting texture" />
        </a>
        <div id="lightbox-2" class="lightbox">
          <a href="#">
            <img src="../assets/12-23-24.JPG" alt="pond with vignette and painting texture" />
          </a>
        </div>
      </article>

      <article class="entry">
        <time datetime="2024-12-22">Day 1: (22 Dec 2024)</time>
        <p>
          My red oak friend's arms hold a habitat of moss an ferns that greet
          me on my walk with soggy shoes. I glimpsed the blue sky for a moment
          today.
        </p>
      </article>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the entries
entries = soup.find_all('article', class_='entry')

# Prepare CSV data
csv_data = []
for entry in entries:
    date = entry.find('time')['datetime']
    text = entry.find('p').text.strip()
    img_tag = entry.find('img')
    img_filename = img_tag['src'].split('/')[-1] if img_tag else None
    csv_data.append([date, text, img_filename])

# Write to CSV
csv_filename = 'micro_entries.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Text', 'Image Filename'])
    writer.writerows(csv_data)

print(f"CSV file '{csv_filename}' has been created successfully.")
