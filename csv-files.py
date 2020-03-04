import csv

# reading
# with open('C:\\Users\\one-mapo\\Desktop\\file.csv','r',encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for line in csv_reader:
#         print(line[0])

# writing
# with open('C:\\Users\\one-mapo\\Desktop\\file.csv','r',encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('C:\\Users\\one-mapo\\Desktop\\new.csv','w') as new_csv_file:
#         csv_writer = csv.writer(new_csv_file)
#         for line in csv_reader:
#             new_line = line
#             csv_writer.writerow(new_line)

with open('C:\\Users\\one-mapo\\Desktop\\file.csv','r',encoding='utf-8',newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file,quotechar='"',delimiter=',',quoting=csv.QUOTE_ALL)
    with open('C:\\Users\\one-mapo\\Desktop\\new.csv','w',encoding='utf-8',newline='') as new_csv_file:
        field_names = ['email']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=field_names, delimiter=',')
        csv_writer.writeheader()
        for line in csv_reader:
            record = line['Agent email']
            if record not in ("",None):
                csv_writer.writerow({'email':record})