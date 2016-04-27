import csv
from BeautifulSoup import BeautifulSoup as bs

output = []
output_map = {}
header = ['HITId', 'Input.image_url']
tag_header_prefix = "Answer.tag"
number_tags_per_image = 1
tag_headers = [tag_header_prefix + str(i) for i in range(1, number_tags_per_image + 1)]
print tag_headers

row_html_head = '<div class="row">\
  <div class="col-md-4"><img src="{0}" class="img-responsive"></div>\
  <div class="col-md-8">\
    <table class="table table-striped">\
      <thead>\
        <tr>\
          <th>Tags</th>\
          <th>HITId</th>\
          <th>ImageUrl</th>\
        </tr>\
      </thead>\
      <tbody>\n'

row_html_tail = '</tbody>\
    </table>\
  </div>\
</div>\n'


with open('Batch_2359893_batch_results.tsv', 'rU') as tsv:
    records = csv.DictReader(tsv, dialect=csv.excel_tab)
    for row in records:
        for tag_header in tag_headers:
            new_row = []
            new_row.append(row[tag_header])
            new_row += [row[x] for x in header]
            if row['HITId'] not in output_map:
                output_map[row['HITId']] = []
            output_map[row['HITId']].append(new_row)

print output_map

with open('output.html', 'w') as file:
    for HITId in output_map.keys():
        rows = output_map[HITId]
        first_row = rows[0]
        row_string = row_html_head.format(first_row[2])

        for row in rows:
            row_string += '<tr>\n'
            for i in range(len(header) + 1):
                if i is 2:
                    row_string += '<td>{0}</td>\n'.format(row[i].split('/')[-1])
                else:
                    row_string += '<td>{0}</td>\n'.format(row[i])
            row_string += '</tr>\n'

        row_string += row_html_tail

        soup = bs(row_string)
        file.write(soup.prettify())
