import pdb
import os
import re


def create_pascal_voc_script(images_path, class_path, out_paths):
    fw = open('restructure_pascal_voc.sh', 'w')
    for fn in os.listdir(class_path):
        mat = re.match(r'(\w+)_(\w+)\.txt', fn)
        if not mat:
            continue

        cat = mat.group(1)
        dset = mat.group(2)
        if dset not in ('train', 'val'):
            continue

        fw.write('mkdir -p {}\n'.format(os.path.join(out_paths[dset], cat)))

        f = open(os.path.join(class_path, fn), 'r')
        for line in f:
            cols = filter(None, line.split(' '))
            im = cols[0].strip()
            stat = cols[1].strip()
            if stat == '1':
                fw.write('cp {} {}\n'.format(
                    '{}.jpg'.format(os.path.join(images_path, im)),
                    '{}.jpg'.format(os.path.join(out_paths[dset], cat, im))
                ))

        fw.write('\n')
    fw.close()

if __name__ == '__main__':
    create_pascal_voc_script(
        images_path='/home/jonathan/Data/pascal/VOC2012/JPEGImages',
        class_path='/home/jonathan/Data/pascal/VOC2012/ImageSets/Main',
        out_paths={
            'train':
            '/home/jonathan/Data/pascal/VOC2012/ImagesByCategory/Train',
            'val':
            '/home/jonathan/Data/pascal/VOC2012/ImagesByCategory/Validate',
        },
    )
