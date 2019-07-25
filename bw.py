from PIL import Image

def conv(input_path, output_path):
    col=Image.open(input_path);
    bw=col.convert('L')
    bw.save(output_path)

if __name__ == "__main__":
    conv('a.jpg', 'b.jpg')