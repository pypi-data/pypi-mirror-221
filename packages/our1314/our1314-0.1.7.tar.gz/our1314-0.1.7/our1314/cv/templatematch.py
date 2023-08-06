import cv2
import numpy as np
import halcon
from our1314.myutils.myutils import rad
from halcon.numpy_interop import himage_as_numpy_array, himage_from_numpy_array

class templateMatch():
    def __init__(self, src, coord):
        
        c1,r1,c2,r2 = coord
        region = halcon.gen_rectangle1(int(r1),int(c1),int(r2),int(c2))
        temp = halcon.reduce_domain(src, region=region)
        model = halcon.create_scaled_shape_model(temp, 5, -rad(10.0), rad(20.0), rad(0.3657), 0.8, 1/0.8, 0.01, ['none', 'nopregeneration'], 'use_polarity', [10,30,30], 10)
        pass


if __name__ == '__main__':
    from our1314.cv.mouseselect import mouseSelect

    path = 'd:/desktop/1.jpg'
    src = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)#type:np.ndarray
    a = mouseSelect(src)

    coord = a.pt1[0], a.pt1[1], a.pt2[0], a.pt2[1]
    src = himage_from_numpy_array(src)
    match = templateMatch(src, coord)


    