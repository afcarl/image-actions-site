import csv

output = []
header = ['HITId', 'AssignmentId', 'WorkerId', 'Input.image_url']
tag_header_prefix = "Answer.tag"
number_tags_per_image = 1
tag_headers = [tag_header_prefix + str(i) for i in range(1, number_tags_per_image + 1)]
print tag_headers

with open('Batch_2359893_batch_results.tsv', 'rU') as tsv:
    records = csv.DictReader(tsv, dialect=csv.excel_tab)
    for row in records:
        for tag_header in tag_headers:
            new_row = [row[x] for x in header]
            new_row.append(row[tag_header])
            if len(str(row[tag_header])) > 2:
                output.append(new_row)

print output

with open('records-100.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['HITId', 'AssignmentId', 'WorkerId', 'ImageUrl', 'ActionTag'])
    for row in output:
        writer.writerow(row)
