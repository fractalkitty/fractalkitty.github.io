from numbers_parser import Document
from datetime import datetime


def create_birds_html():
    # Clear or create the file first
    with open('./birds/index.html', 'w') as f:
        f.write('')  # Clear contents
        
    doc = Document('./streamof.numbers')
    
    for sheet in doc.sheets:
        if sheet.name == 'Birds':
            table = sheet.tables[0]
            
            for row in table.rows():
                cell = row[0]
                if hasattr(cell, 'value') and cell.value:
                    # Extract just the value part from the cell
                    content = cell.value
                    if isinstance(content, str) and content.strip():
                        with open('./birds/index.html', 'a') as f:
                            f.write(content + '\n')


    # HTML header
    header = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="../css/cinquains.css" />
  <title>Cinquains | stream of me</title>
</head>

<body>
  <nav class="home-nav" role="navigation" aria-label="Return to main navigation">
    <a href="../index.html" class="home-link" aria-label="Return to homepage">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="home-icon">
        <path d="M12 3L4 9v12h16V9l-8-6z" stroke="currentColor" stroke-width="2" fill="none" />
        <path d="M9 22v-8h6v8" stroke="currentColor" stroke-width="2" fill="none" />
      </svg>
    </a>
  </nav>

  <main class="container">
    <div class="cinquains">"""

    # HTML footer
    footer = """
    </div>
  </main>
</body>
</html>"""

    # Clear or create the file first
    with open('./cinquains/index.html', 'w') as f:
        f.write(header)
        
    doc = Document('./streamof.numbers')
    
    for sheet in doc.sheets:
        if sheet.name == 'Cinquains':
            table = sheet.tables[0]
            
            for row in table.rows():
                if hasattr(row[0], 'value') and hasattr(row[1], 'value'):
                    date = row[0].value
                    poem = row[1].value
                    
                    if date and poem and isinstance(date, str) and isinstance(poem, str):
                        # Convert date format
                        try:
                            date_obj = datetime.datetime.strptime(date, '%m/%d/%Y')
                            datetime_str = date_obj.strftime('%Y-%m-%d')
                            display_date = date_obj.strftime('%-m-%-d-%y')
                            
                            # Split poem into lines and create HTML
                            poem_lines = poem.strip().split('\n')
                            poem_html = '\n          '.join(f'<p>{line.strip()}</p>' for line in poem_lines)
                            
                            article = f"""
      <article class="cinquain">
        <time datetime="{datetime_str}">{display_date}</time>
        <div class="poem">
          {poem_html}
        </div>
      </article>"""
                            
                            with open('./cinquains/.html', 'a') as f:
                                f.write(article)
                        except Exception as e:
                            print(f"Error processing row: {e}")

    # Add footer
    with open('./cinquains/index.html', 'a') as f:
        f.write(footer)

def create_cinquains_html():
    # print("Starting Cinquains HTML generation...")
    
    header = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="../css/cinquains.css" />
  <title>Cinquains | stream of me</title>
</head>

<body>
  <nav class="home-nav" role="navigation" aria-label="Return to main navigation">
    <a href="../index.html" class="home-link" aria-label="Return to homepage">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="home-icon">
        <path d="M12 3L4 9v12h16V9l-8-6z" stroke="currentColor" stroke-width="2" fill="none" />
        <path d="M9 22v-8h6v8" stroke="currentColor" stroke-width="2" fill="none" />
      </svg>
    </a>
  </nav>

  <main class="container">
    <div class="cinquains">'''

    footer = '''
    </div>
  </main>
</body>
</html>'''

    with open('./cinquains/index.html', 'w') as f:
        f.write(header)
        
    doc = Document('./streamof.numbers')
    
    for sheet in doc.sheets:
        if sheet.name == 'Cinquains':
            table = sheet.tables[0]
            # print(f"Found Cinquains sheet with {len(table.rows())} rows")
            
            for row in table.rows()[1:]:  # Skip header row
                if len(row) >= 2:
                    date = row[0].value if hasattr(row[0], 'value') else None
                    poem = row[1].value if hasattr(row[1], 'value') else None
                    
                    if date and poem and poem.strip():
                        try:
                            date_obj = date if isinstance(date, datetime) else None
                            if date_obj:
                                datetime_str = date_obj.strftime('%Y-%m-%d')
                                display_date = date_obj.strftime('%-m-%-d-%y')
                                
                                poem_lines = [line.strip() for line in poem.split('\n') if line.strip()]
                                poem_html = '\n          '.join(f'<p>{line}</p>' for line in poem_lines)
                                
                                article = f'''
      <article class="cinquain">
        <time datetime="{datetime_str}">{display_date}</time>
        <div class="poem">
          {poem_html}
        </div>
      </article>'''
                                
                                with open('./cinquains/index.html', 'a') as f:
                                    f.write(article)
                                    
                        except Exception as e:
                            print(f"Error processing row: {e}")

    with open('./cinquains/index.html', 'a') as f:
        f.write(footer)

    # print("HTML generation complete")

def create_distance_html():
    print("Starting Distance HTML generation...")
    
    header = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="../css/distance.css" />
  <title>distance on foot</title>
</head>

<body>
  <nav class="home-nav" role="navigation" aria-label="Return to main navigation">
    <a href="../index.html" class="home-link" aria-label="Return to homepage">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="home-icon">
        <path d="M12 3L4 9v12h16V9l-8-6z" stroke="currentColor" stroke-width="2" fill="none" />
        <path d="M9 22v-8h6v8" stroke="currentColor" stroke-width="2" fill="none" />
      </svg>
    </a>
  </nav>

  <main class="container">
    <h2>distance on foot</h2>
    <p>since 12/22/24</p>
    <div class="year-grid">'''

    footer = '''
    </div>
  </main>
</body>
</html>'''

    with open('./distance/index.html', 'w') as f:
        f.write(header)
        
    doc = Document('./streamof.numbers')
    day_elements = []

    for sheet in doc.sheets:
        if sheet.name == 'Distance':
            table = sheet.tables[0]
            print(f"Found Distance sheet with {len(table.rows())} rows")
            
            for row in table.rows()[1:]:  # Skip header row
                if len(row) >= 3:  # We need at least 3 columns
                    kms = row[1].value if hasattr(row[1], 'value') else None
                    thoughts = row[2].value if hasattr(row[2], 'value') else None
                    
                    if kms is not None and kms < 100:  # Only process if we have a distance
                        try:
                            # Format kms to always have 1 decimal place
                            kms_formatted = f"{float(kms):.1f}"
                            
                            # Create div with or without thoughts
                            if thoughts and thoughts.strip():
                                day_html = f'''
      <div class="day" data-kms="{kms_formatted}">
        <p class="thought">{thoughts.strip()}</p>
      </div>'''
                            else:
                                day_html = f'''
      <div class="day" data-kms="{kms_formatted}"></div>'''
                            
                            day_elements.append(day_html)
                                    
                        except Exception as e:
                            print(f"Error processing row: {e}")

    # Write all day elements except the last four
    with open('./distance/index.html', 'a') as f:
        for day_html in day_elements[:-4]:
            f.write(day_html)
        
        # Wrap the last four in a "final-row" div
        f.write('''
      <div class="final-row">''')
        for day_html in day_elements[-4:]:
            f.write(day_html)
        f.write('''
      </div>''')

        f.write(footer)

    print("HTML generation complete")

def create_micro_html():
    print("Starting Micro HTML generation...")
    
    header = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="../css/micro.css" />
  <title>micro journal | stream of me</title>
</head>

<body>
  <nav class="home-nav" role="navigation" aria-label="Return to main navigation">
    <a href="../index.html" class="home-link" aria-label="Return to homepage">
      <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="home-icon">
        <path d="M12 3L4 9v12h16V9l-8-6z" stroke="currentColor" stroke-width="2" fill="none" />
        <path d="M9 22v-8h6v8" stroke="currentColor" stroke-width="2" fill="none" />
      </svg>
    </a>
  </nav>

  <main class="container">
    <h2>micro journal</h2>
    <div class="micro-entries">'''

    footer = '''
    </div>
  </main>
</body>
</html>'''

    with open('./micro/index.html', 'w') as f:
        f.write(header)
        
    doc = Document('./streamof.numbers')
    lightbox_counter = 1
    start_date = datetime(2024, 12, 22)
    
    for sheet in doc.sheets:
        if sheet.name == 'Micro':
            table = sheet.tables[0]
            print(f"Found Micro sheet with {len(table.rows())} rows")
            
            for row in table.rows()[1:]:  # Skip header row
                if len(row) >= 3:  # We need date, text, and possible image
                    date = row[0].value if hasattr(row[0], 'value') else None
                    text = row[1].value if hasattr(row[1], 'value') else None
                    image = row[2].value if hasattr(row[2], 'value') else None
                    
                    try:
                        # Convert the date string to datetime
                        if isinstance(date, str):
                            date = datetime.strptime(date, '%Y-%m-%d')
                        
                        day_number = (date - start_date).days + 1
                        datetime_str = date.strftime('%Y-%m-%d')
                        display_date = f"Day {day_number}: ({date.strftime('%-d %b %Y')})"
                        
                        # Create article with or without image
                        if image and isinstance(image, str) and image.strip():
                            # Article with image
                            article = f'''
      <article class="entry">
        <time datetime="{datetime_str}">{display_date}</time>
        <p>{text.strip()}</p>
        <a href="#lightbox-{lightbox_counter}">
          <img src="../assets/{image.strip()}" alt="{text.strip()}" loading="lazy" />
        </a>
        <div id="lightbox-{lightbox_counter}" class="lightbox">
          <a href="#">
            <img src="../assets/{image.strip()}" alt="{text.strip()}" />
          </a>
        </div>
      </article>'''
                            lightbox_counter += 1
                        else:
                            # Article without image
                            article = f'''
      <article class="entry">
        <time datetime="{datetime_str}">{display_date}</time>
        <p>{text.strip()}</p>
      </article>'''
                        
                        with open('./micro/index.html', 'a') as f:
                            f.write(article)
                                
                    except Exception as e:
                        print(f"Error processing row: {date}, {text}: {e}")

    with open('./micro/index.html', 'a') as f:
        f.write(footer)

    print("HTML generation complete")

if __name__ == "__main__":
    create_birds_html()
    create_cinquains_html()
    create_distance_html()
    create_micro_html()

    