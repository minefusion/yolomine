from ultralytics import Explorer
from ultralytics.data.converter import convert_coco

def convert_automine():
    cls91to80 = False
    annotations_dir = "/home/zhanjun/PHD/datasets/automine-2d/images/annotations"
    #convert_coco(labels_dir=annotations_dir,use_segments=False,cls91to80=False)

    annotations_dir_128 = "/home/zhanjun/PHD/datasets/automine-2d-128/images/annotations"
    convert_coco(labels_dir=annotations_dir_128,use_segments=False,cls91to80=False)

    #False
    # multi
    #WARNING train2017/003210.png: ignoring corrupt image/label: negative label values [         -1]

    #yolo train data=./automine-2d.yaml model=yolov8n.yaml epochs=1 lr0=0.01
    # yolo explorer
    # yolo settings reset


def find_similar(image_file):
   
    # Create an Explorer object
    explorer = Explorer(data='automine-2d.yaml', model='automine-2d.pt')

    # Create embeddings for your dataset
    explorer.create_embeddings_table()

    # Search for similar images to a given image/images
    #dataframe = explorer.get_similar(img=image_file)

    # Or search for similar images to a given index/indices
    #dataframe = explorer.get_similar(idx=0)
    df = explorer.sql_query("WHERE labels LIKE '%Mining-Truck%'")
 
    print(df[0])


ds = find_similar("/home/zhanjun/mine.png")
print(ds)