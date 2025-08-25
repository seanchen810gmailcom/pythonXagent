"""
簡單的 Pygame 繪圖與即時塗鴉範例程式

說明:
    這個腳本建立一個 Pygame 視窗，並在一個背景畫布上繪製數種示範圖形（矩形、圓形、橢圓、多邊形、線條、弧線等），
    使用者可以用滑鼠左鍵繪畫、右鍵或中鍵當作橡皮擦來擦除畫布內容。

依賴:
    - pygame

操作方式:
    - 左鍵（mouse button 1）：畫筆（黑色）
    - 中鍵（mouse button 2）：大橡皮擦（用背景色覆蓋）
    - 右鍵（mouse button 3）：小橡皮擦（用背景色覆蓋）
    - 關閉視窗：結束程式

輸入/輸出:
    - 輸入：滑鼠位置與按鍵
    - 輸出：視窗顯示（640x320）與終端印出按鍵事件提示

邊界情況與錯誤模式:
    - 若未安裝 pygame，import 時會發生 ImportError
    - 程式在其他繪圖/視窗系統上以 Pygame 行為為準
    - 程式假設視窗大小固定為 640x320，超出範圍的滑鼠座標會自動被 Pygame 處理

此檔案僅加註解與少量改善（使用 math.pi 取代巨量常數），
程式行為與原本相同，主要目的是讓程式更易於閱讀與維護。
"""

######################匯入模組######################
import math  # 使用 math.pi 表示圓周率
import pygame  # 匯入 Pygame
import sys  # 匯入 sys

######################初始化######################
pygame.init()  # 啟動 Pygame
width = 640  # 設定視窗寬度
height = 320  # 設定視窗高度
clock = pygame.time.Clock()  # 建立 Clock 物件，控制更新速率
######################建立視窗及物件######################
# 設定視窗大小
screen = pygame.display.set_mode((width, height))  # 建立視窗
# 設定視窗標題
pygame.display.set_caption("My Game")  # 設定視窗標題


####################繪製圖形#####################
def draw_demo(surface):
    """在給定的 Surface 上繪製一組示範圖形。

    參數:
        - surface: pygame.Surface 物件，繪製目標畫布

    此函式會一次性在傳入的 surface 上繪製多種靜態示範圖形，包含：
        實心/空心矩形、圓形、橢圓、多邊形、線條、弧線與座標標記等。
    函式不回傳值，直接修改傳入的 surface。
    """

    # 顏色定義
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (220, 50, 50)
    GREEN = (50, 200, 120)
    BLUE = (40, 120, 240)
    YELLOW = (240, 220, 60)
    MAGENTA = (200, 50, 180)

    # 1) 實心矩形與空心矩形
    # pygame.draw.rect(surface, color, rect, width=0)
    # - surface: 要繪製到的 Surface（畫布/視窗）
    # - color: RGB 三元組 (R, G, B)，指定矩形的顏色
    # - rect: 一個 pygame.Rect 或 (x, y, w, h) 四元素元組，表示矩形的左上角座標與寬高
    # - width: 邊線粗細；預設為 0 表示填滿（實心），大於 0 則只畫邊框（空心），數值為像素
    # 以下第一個呼叫畫一個實心紅色矩形 (x=20, y=20, w=120, h=60)
    pygame.draw.rect(surface, RED, pygame.Rect(20, 20, 120, 60))
    # 第二個呼叫畫一個白色空心矩形，邊線寬度為 4 像素 (x=160, y=20, w=120, h=60)
    pygame.draw.rect(surface, WHITE, pygame.Rect(160, 20, 120, 60), 4)

    # 2) 圓形
    # pygame.draw.circle(surface, color, center, radius, width=0)
    # - center: 圓心 (x, y)
    # - radius: 半徑（像素）
    # - width: 邊線寬度，預設 0 表示實心圓；>0 則為空心圓，值為邊框像素
    # 畫一個實心綠色圓，圓心在 (320,50)，半徑 40
    pygame.draw.circle(surface, GREEN, (320, 50), 40)
    # 畫一個小白圓做為中心點標記，半徑 10
    pygame.draw.circle(surface, WHITE, (320, 50), 10)  # 中心點示意

    # 3) 橢圓
    # pygame.draw.ellipse(surface, color, rect, width=0)
    # - rect: 橢圓被限制在此矩形內，矩形的大小決定橢圓的寬與高
    # 以下畫一個填滿的黃色橢圓，範圍為 Rect(400,20,160,60)
    pygame.draw.ellipse(surface, YELLOW, pygame.Rect(400, 20, 160, 60))

    # 4) 多邊形（三角形 + 五邊形示意）
    # pygame.draw.polygon(surface, color, pointlist, width=0)
    # - pointlist: 座標點列表 [(x1,y1),(x2,y2)...]，Pygame 自動連接最後一點回到第一點形成封閉形狀
    # - width: 寬度 0 為填滿多邊形；>0 為只畫邊框，數值為邊線像素
    tri_pts = [(60, 120), (20, 200), (100, 200)]
    # 畫一個填滿的藍色三角形
    pygame.draw.polygon(surface, BLUE, tri_pts)

    pent_pts = [(180, 120), (220, 140), (200, 190), (160, 190), (140, 140)]
    # 畫一個邊線寬度為 3 的五邊形（空心）
    pygame.draw.polygon(surface, MAGENTA, pent_pts, 3)  # 空心五邊形邊線

    # 5) 線條與折線
    # pygame.draw.line(surface, color, start_pos, end_pos, width=1)
    # - start_pos, end_pos: 線段的起點與終點 (x,y)
    # - width: 線寬（像素），預設為 1
    # 下面畫一條白色實線，寬度為 3 像素
    pygame.draw.line(surface, WHITE, (260, 120), (500, 160), 3)

    # pygame.draw.aalines(surface, color, closed, pointlist)
    # - closed: 若為 True，則會自動連回起點形成封閉曲線；False 則為開放的折線
    # - aalines 會用抗鋸齒的方式繪製折線（更平滑），但沒有寬度參數，會以 1 像素線寬繪製
    polyline = [(260, 170), (300, 210), (340, 180), (380, 230)]
    # 畫一組抗鋸齒黑色折線，不封閉
    pygame.draw.aalines(surface, BLACK, False, polyline)

    # 6) 弧線（使用 math.pi 作為圓周率）
    # arc 需要指定矩形範圍與起始/結束角度（以弧度），以下畫一個半圓弧
    # pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1)
    # - rect: 指定弧線所在的矩形區域（弧線為該矩形內的橢圓弧）
    # - start_angle, stop_angle: 弧度為單位，0 為 x 正方向，角度逆時針為正
    # - width: 弧線寬度（像素）
    # 以下繪製從角度 0 (0 弧度) 到 math.pi (約半圓) 的白色弧線，寬度 3
    pygame.draw.arc(surface, WHITE, pygame.Rect(420, 140, 140, 80), 0, math.pi, 3)

    # 7) 小圓點作為座標標記
    # 利用小圓點標示數個座標位置（示意點、錨點等）
    for x, y in [(520, 60), (540, 80), (560, 100)]:
        # 每個小圓為白色，半徑 4（實心）
        pygame.draw.circle(surface, WHITE, (x, y), 4)


####################建立畫布#######################
# 建立背景畫布 (不使用 screen 直接繪製，以便後續覆蓋/擦除)
bg = pygame.Surface((width, height))  # 建立畫布（Surface）
# 畫布底色（用來當作橡皮擦時的填補顏色）
BG_COLOR = (89, 99, 255)
bg.fill(BG_COLOR)  # 將畫布填滿背景色
# 在背景上一次性繪製靜態示例圖形（之後使用者可以在此基礎上畫畫或擦除）
draw_demo(bg)
######################循環偵測######################
# 畫筆與橡皮擦設定（可修改以調整筆觸大小與顏色）
BRUSH_COLOR = (0, 0, 0)  # 畫筆顏色 (黑)
BRUSH_RADIUS = 8  # 畫筆半徑（像素）
# 橡皮擦實際上是用背景顏色覆蓋，因此會將該區還原為 BG_COLOR
ERASER_RIGHT_RADIUS = 12  # 右鍵橡皮擦半徑（小）
ERASER_MIDDLE_RADIUS = ERASER_RIGHT_RADIUS * 3  # 中鍵橡皮擦半徑（大，為右鍵的 3 倍）

# 儲存上一個滑鼠座標以連續繪製（避免斷點）
# 儲存上一個滑鼠座標以連續繪製（避免產生斷點）
last_pos = None

# 主循環：處理事件、讀取滑鼠狀態、在背景上繪製，然後把背景貼到主視窗

while True:
    clock.tick(60)  # 每秒最多更新 60 次
    for event in pygame.event.get():  # 偵測所有事件
        if event.type == pygame.QUIT:  # 如果事件為視窗關閉
            sys.exit()  # 結束程式

        # 可選：按下按鍵時印出事件（保留但非必要）
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("左鍵按下 - 開始畫畫")
            elif event.button == 2:
                print("中鍵按下 - 橡皮擦 (大)")
            elif event.button == 3:
                print("右鍵按下 - 橡皮擦 (小)")

    # 每一幀檢查滑鼠按鍵狀態
    mouse_pressed = pygame.mouse.get_pressed()  # (left, middle, right)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 決定要使用哪個工具與半徑、顏色
    tool_color = None
    tool_radius = None

    if mouse_pressed[0]:
        # 左鍵：畫筆（使用畫筆顏色）
        tool_color = BRUSH_COLOR
        tool_radius = BRUSH_RADIUS
    elif mouse_pressed[1]:
        # 中鍵：大橡皮擦（背景色）
        tool_color = BG_COLOR
        tool_radius = ERASER_MIDDLE_RADIUS
    elif mouse_pressed[2]:
        # 右鍵：小橡皮擦（背景色）
        tool_color = BG_COLOR
        tool_radius = ERASER_RIGHT_RADIUS
    else:
        # 沒有按鍵，重設 last_pos 並不繪圖
        last_pos = None

    # 如果有選定工具則在畫布上繪製（畫筆或橡皮擦）
    if tool_color is not None and tool_radius is not None:
        # 畫出當前圓點
        pygame.draw.circle(bg, tool_color, (mouse_x, mouse_y), tool_radius)

        # 若上個座標存在，畫線連結前後座標以避免斷點
        if last_pos is not None:
            pygame.draw.line(
                bg, tool_color, last_pos, (mouse_x, mouse_y), tool_radius * 2
            )

        # 更新 last_pos 為目前座標
        last_pos = (mouse_x, mouse_y)

    # 將背景畫布繪製到主視窗 (左上角座標 0,0)，再更新顯示
    screen.blit(bg, (0, 0))
    pygame.display.update()
