import matplotlib.pyplot as plt

#https://blog.csdn.net/Bit_Coders/article/details/121383126
def RGB_to_Hex(rgb):
    """
    RGB格式颜色转换为16进制颜色格式
    Args:
        rgb: tuple

    Returns:
        color: str
    """
    RGB = list(rgb)
    color = '#'
    for i in RGB:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color


def generate_colors(N=12, colormap='hsv'):
    """
    生成颜色列表
    Args:
        N: 生成颜色列表中的颜色个数
        colormap: plt中的色表，如'cool'、'autumn'等

    Returns:
        rgb_list: list, 每个值(r,g,b)在0~255范围
        hex_list: list, 每个值为十六进制颜色码类似：#FAEBD7
    """
    step = max(int(255 / N), 1)
    cmap = plt.get_cmap(colormap)

    rgb_list = []
    hex_list = []
    for i in range(N):
        id = step * i  # cmap(int)->(r,g,b,a) in 0~1
        id = 255 if id > 255 else id
        rgba_color = cmap(id)
        rgb = [int(d * 255) for d in rgba_color[:3]]
        rgb_list.append(tuple(rgb))
        hex_list.append(RGB_to_Hex(rgb))
    return rgb_list, hex_list


def gen_perp_color():

    gray_rgb_list, gray_hex_list = generate_colors(7, 'Greys')# 生成 4个灰色（颜色由浅至深）
    blue_rgb_list, blue_hex_list = generate_colors(10, 'Blues') # 生成 6个蓝色（颜色由浅至深）,
    green_rgb_list, green_hex_list = generate_colors(8, 'Greens_r')# 生成 5个绿色（颜色由深至浅）
    YlOrRd_rgb_list, YlOrRd_hex_list = generate_colors(11, 'hot_r')# 生成 11个黄棕红（颜色由浅至深）


    # print(gray_hex_list[:4]+blue_hex_list[3:10]+green_hex_list+YlOrRd_hex_list)#蓝色取后6个
    return gray_hex_list[1:6]+blue_hex_list[4:]+green_hex_list[3:]+YlOrRd_hex_list #生成26个颜色

if __name__ == '__main__':
    gen_perp_color()