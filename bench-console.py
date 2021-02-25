from decimal import *
import time
import shutil
import zipfile

#config
RUN_TIME = 60;

default_b1 = 626;
default_b2 = 19550516;
default_b3 = 7214769;
default_b4 = 33477349;
default_b5 = 4867;

k_1 = Decimal(1) / Decimal(default_b1);
k_2 = Decimal(0.3) / Decimal(default_b2);
k_3 = Decimal(5) / Decimal(default_b3);
k_4 = Decimal(3) / Decimal(default_b4);
k_5 = Decimal(0.7) / Decimal(default_b5);

res_1 = 0;
res_2 = 0;
res_3 = 0;
res_4 = 0;
res_5 = 0;

#1
def copy_files():
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        count += 1;
        shutil.copyfile(r'files/image.jpg', r'temp/image.jpg');
        if (time.time() >= time_end):
            return count;

#2
def find_hash(file):
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        with open(file, 'r') as read_file:
            for line in read_file:
                new_line = line.strip('\n')
                count += 1;
                if (time.time() >= time_end):
                    return count;

#3
def test_integer():
    time_end = time.time() + RUN_TIME;
    count = 0;
    b = 0;
    while True:
        count += 1;
        b += 22226545*22+26216*222+88**88*88;
        if (time.time() >= time_end):
            return count;

#4
def test_float():
    time_end = time.time() + RUN_TIME;
    count = 0;
    b = 0.1;
    while True:
        count += 1;
        b += 0.01;
        if (time.time() >= time_end):
            return count;

#5
def create_archive():
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        count += 1;
        newzip=zipfile.ZipFile(r'temp/images.zip','w');
        newzip.write(r'files/image.jpg');
        if (time.time() >= time_end):
            return count;


r1 = copy_files();
print(r1);
r2 = find_hash('files/PRO_WPA.txt');
print(r2);
r3 = test_integer();
print(r3);
r4 = test_float();
print(r4);
r5 = create_archive();
print(r5);

calc_1 = r1 * k_1;
calc_2 = r2 * k_2;
calc_3 = r3 * k_3;
calc_4 = r4 * k_4;
calc_5 = r5 * k_5;

result = calc_1 + calc_2 + calc_3 + calc_4 + calc_5;
print('%.1f' % result)










