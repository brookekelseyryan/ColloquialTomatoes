import csv
import os


list_of_files = os.listdir()


with open("pos_review.csv", mode="w") as review_file:
    csv_writer = csv.writer(review_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    ctr = 1
    for i in list_of_files:
        if i.split(".")[1] == "py":
            pass
        else:
            file_r = open(i, "r")
            str_copy = ""
            for line in file_r:
                str_copy += line

            csv_writer.writerow([str_copy, "1"])
            str_copy = ""
            file_r.close()
            print(ctr)
            ctr += 1

review_file.close()
