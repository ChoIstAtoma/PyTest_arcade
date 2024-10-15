import arcade
import tkinter

# 전역 변수 정의
ScreenSizeGetting = tkinter.Tk() # 사용자의 화면 해상도 가져오기
USER_SCREEN_WIDTH = ScreenSizeGetting.winfo_screenwidth() # (전체화면 - 고정)
USER_SCREEN_HEIGHT = ScreenSizeGetting.winfo_screenheight()

ScreenSize = [ScreenSizeGetting.winfo_screenwidth(), ScreenSizeGetting.winfo_screenheight()] # 창 너비, 높이를 가변 객체로 만듦. -> 클래스 안에서 객체의 값을 바꿀 수 있음
ScreenSizeGetting.destroy()
SCREEN_WIDTH = ScreenSize[0] # 창 너비 (창모드)
SCREEN_HEIGHT = ScreenSize[1] # 창 높이 (창모드)

SCREEN_TITLE = "Biorhythm"
scaling = [1] # 스케일링을 가변 객체로 만듦.
SCALING = scaling[0]

FULLSCREEN_RECT = arcade.Rect(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #전체화면 직사각형\

draw_rate = [1/60]
DRAW_RATE = draw_rate[0]

zoomvelue = [1.0] #줌(전체화면에서 화면 비율 유지용)
ZOOM_VELUE = zoomvelue[0]

SoundVelue = [100, 100, 100] #음량 수치
MASTER_VOLUME = SoundVelue[0]
BACKGROUND_VOLUME = SoundVelue[1]
EFFECT_VOLUME = SoundVelue[2]