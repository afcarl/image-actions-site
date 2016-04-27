import csv
from BeautifulSoup import BeautifulSoup as bs

output = []
output_map = {}
headers = ['HITId', 'Input.ImageUrl', 'Input.ActionTag']
tag_header_prefix = "Answer.tag"
number_tags_per_image = 10
tag_headers = [tag_header_prefix + str(i) for i in range(1, number_tags_per_image + 1)]
print tag_headers

row_html_head = '<div class="row">\
  <div class="col-md-4"><img src="{0}" class="img-responsive"></div>\
  <div class="col-md-8">\
    <table class="table table-striped">\
      <thead>\
        <tr>\
          <th>Attribute</th>\
          <th>Value</th>\
        </tr>\
      </thead>\
      <tbody>\n'

row_html_tail = '</tbody>\
    </table>\
  </div>\
</div>\n'


with open('Batch_2373231_batch_results.tsv', 'rU') as tsv:
    records = csv.DictReader(tsv, dialect=csv.excel_tab)
    for row in records:
        if row['Input.ImageUrl'] not in output_map:
            output_map[row['Input.ImageUrl']] = []
        output_map[row['Input.ImageUrl']].append(row)

print output_map

with open('output.html', 'w') as file:
    for ImageUrl in output_map.keys():
        rows = output_map[ImageUrl]

        for row in rows:
            row_string = row_html_head.format(ImageUrl)

            row_string += '<th>ImageUrl</th><td>{0}</td>\n'.format(row[header]

            for tag_header in tag_headers:
                row_string += '<tr>\n'
                row_string += '<th>{0}</th><td>{1}</td>\n'.format(tag_header, row[tag_header])
                row_string += '</tr>\n'

            for header in headers:
                row_string += '<tr>\n'
                if header is 'Input.ImageUrl':
                    row_string += '<th>ImageUrl</th><td>{0}</td>\n'.format(row[header].split('/')[-1])
                else:
                    row_string += '<th>{0}</th><td>{1}</td>\n'.format(header, row[header])
                row_string += '</tr>\n'

            row_string += row_html_tail

        soup = bs(row_string)
        file.write(soup.prettify())
