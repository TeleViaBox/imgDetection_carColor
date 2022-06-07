
# 變更到指定尺寸，長寬邊不足者補黑色
def process_image(img, min_side = 608):
    size = img.shape
    h, w = size[0], size[1]
    scale = max(w, h) / float(min_side)
    new_w, new_h = int(w/scale), int(h/scale)
    resize_img = cv2.resize(img, (new_w, new_h),cv2.INTER_AREA) # 變更尺寸
    if new_w % 2 != 0 and new_h % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2, (min_side-new_h)//2, (min_side-new_w)//2 + 1, (min_side-new_w)//2
    elif new_h % 2 != 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2 + 1, (min_side-new_h)//2, (min_side-new_w)//2, (min_side-new_w)//2
    elif new_h % 2 == 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side-new_h)//2, (min_side-new_h)//2, (min_side-new_w)//2, (min_side-new_w)//2
    else:
        top, bottom, left, right = (min_side-new_h)//2 + 1, (min_side-new_h)//2, (min_side-new_w)//2 + 1, (min_side-new_w)//2
    pad_img = cv2.copyMakeBorder(resize_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0]) 
    return pad_img
