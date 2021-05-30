import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def train(train_root):
    image_path = os.path.join(train_root, 'annotations','xmls')
    xml_df = xml_to_csv(image_path)
    labels_path = os.path.join(train_root,'train.csv')
    xml_df.to_csv(labels_path, index=None)
    print('> tf_wider_train - Successfully converted xml to csv.')

def val(val_root):
    image_path = os.path.join(val_root, 'annotations','xmls')
    xml_df = xml_to_csv(image_path)
    labels_path = os.path.join(val_root, 'val.csv')
    xml_df.to_csv(labels_path, index=None)
    print('> tf_wider_val -  Successfully converted xml to csv.')


if __name__ == '__main__':
    train_root = '/home/purna/myworkspace/python/tensorflow-2/face-detector/data/tf_wider_train'
    val_root = '/home/purna/myworkspace/python/tensorflow-2/face-detector/data/tf_wider_val'
    train(train_root)
    val(val_root)