import csv
import os
import urllib


def main():
    cnt = 0
    with open('corn_maize_images.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) >= 4:
                url = row[4]
                disease = row[2]
                if disease == '':
                    disease = 'healthy'

                filename = disease + '/' + str(i) + '.jpg'

                if not os.path.exists(disease):
                    os.mkdir(disease)

                try:
                    if not os.path.exists(filename):
                        urllib.urlretrieve(url, filename)
                    cnt += 1
                except:
                    with open('log.txt', 'a') as f:
                        f.write('err getting: ' + url)
                    print 'err getting: ' + url + '\n'

            if cnt % 20 == 0:
                print str(cnt) + ' images retrieved'


if __name__ == '__main__':
    main()
