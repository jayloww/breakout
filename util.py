def cords_in_rect(x, y, rect_x, rect_y, rect_w, rect_h):
    return rect_x <= x <= rect_x + rect_w and rect_y <= y <= rect_y + rect_h
