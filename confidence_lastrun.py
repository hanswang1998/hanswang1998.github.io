#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 一月 08, 2023, at 16:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
from scipy import stats 
# Run 'Before Experiment' code from code_3
polygon1h=0.4
polygon2h=0.4
polygon3h=0.4
VAR1 =50
VAR2 =50
VAR3 =50
# Run 'Before Experiment' code from trail_code
import pandas as pd
import numpy as np
total_time_zero =1
showtime=0
Totaltime=6000
tasktrmainingtime=0
total_trial_show_count=16
total_trial_show=f"剩余轮次：{total_trial_show_count}"
###时间显示模块
def getdowntime(totaltime):
    t=time.perf_counter()
    timecoder=int(round(totaltime-t+newsave,0)-1)
    sec=round(timecoder%60,0)
    minute=timecoder/60
    strminute=str(int(minute))
    strsec=str(int(sec))
    if sec >=10 and sec != 60:
        showtime=f"剩余时间：{strminute}:{strsec}"
    elif sec <10:
        showtime=f"剩余时间：{strminute}:0{strsec}"
    elif sec == 60:
        showtime=f"剩余时间：{strminute}:00"
    return showtime,timecoder
# Run 'Before Experiment' code from mp_choose_code
def get_taskatime(sec):
    taskatime=taskctimer.getTime()
    taskatime=int(round(sec-taskatime,0))
    return taskatime
taskatime=""
taskafeedback=""
# Run 'Before Experiment' code from mp_feedback_code
taska_text_color="white"
# Run 'Before Experiment' code from var_2b_begin_code
n_back_correct_count=0
# Run 'Before Experiment' code from two_back_num_react_code
def get_taskbtime(sec):
    taskbtime=taskctimer.getTime()
    taskbtime=int(round(sec-taskbtime,0))
    return taskbtime

# Run 'Before Experiment' code from two_back_num_feedback_code
two_back_feedback_text=""
taskb_text_color="white"
taskbtime=""
# Run 'Before Experiment' code from VS_react_code
import psychopy
taskctimer=psychopy.core.Clock()
def get_taskctime(esc):
    taskctime=taskctimer.getTime()
    taskctime=int(round(esc-taskctime,0))
    return taskctime
# Run 'Before Experiment' code from VS_feedback_code
taskcnum=0
correct_feedback=""
react=pd.read_excel("visual_search_pic_answer.xlsx")
vsdata=react.loc[taskcnum]
vsdata=vsdata[1:]
Temp_List =np.array(vsdata).tolist()
Temp_List_correct=0
taskc_text_color='white'
# Run 'Before Experiment' code from feedback_code
import random
confidence_rate=["50%","60%","70%","80%","90%","100%"]
taskchose_text=""
taskscore_text=""
finalscore_text=""
yes_or_no=["是","否"]
bfbutton=False
check_confidence=None
check_yes_or_no=None

resultA_range=pd.read_excel("预实验数据.xlsx")
resultA_range=resultA_range["mp"].dropna()
resultB_range=pd.read_excel("预实验数据.xlsx")
resultB_range=resultB_range["nb"].dropna()
resultC_range=pd.read_excel("预实验数据.xlsx")
resultC_range=resultC_range["vs"].dropna()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'confidence'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\why\\Desktop\\动态决策测验psychopy\\confidence_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setp" ---
firstbutton_2 = visual.ButtonStim(win, 
    text='欢迎参与此次实验，点击屏幕开始吧！', font='Microsoft YaHei',
    pos=(0, 0),
    letterHeight=0.05,
    size=(1.4,0.9), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='firstbutton_2'
)
firstbutton_2.buttonClock = core.Clock()

# --- Initialize components for Routine "confidence_intro" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='指导语/元认知指导语/元认知指导语1.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "confidence_intro_2" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='指导语/元认知指导语/元认知指导语2.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "confidence_intro_3" ---
button = visual.ButtonStim(win, 
    text='Click here', font='Arvo',
    pos=(0, -0.45),
    letterHeight=0.05,
    size=(0.9,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='指导语/元认知指导语/元认知指导语3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92,1.08),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "timecoder" ---

# --- Initialize components for Routine "choose" ---
TaskAimage = visual.ImageStim(
    win=win,
    name='TaskAimage', 
    image='模式匹配.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.2), size=(0.26, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TaskBimage = visual.ImageStim(
    win=win,
    name='TaskBimage', 
    image='n_back.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(0.26, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TaskCimage = visual.ImageStim(
    win=win,
    name='TaskCimage', 
    image='视觉搜索.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.2), size=(0.26, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
describevalue_text = visual.TextStim(win=win, name='describevalue_text',
    text='当前任务的价值',
    font='MicroSoft YaHei',
    pos=(0, -0.15), height=0.03, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
TaskApolygon = visual.Rect(
    win=win, name='TaskApolygon',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, -0.3), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, 1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
TaskAbutton = visual.ButtonStim(win, 
    text=None, font='Arvo',
    pos=(-0.5, 0.2),
    letterHeight=0.05,
    size=(0.26, 0.16), borderWidth=1.0,
    fillColor=[1.0000, 0.2549, -0.0431], borderColor=None,
    color=[-1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=0.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='TaskAbutton'
)
TaskAbutton.buttonClock = core.Clock()
TaskBpolygon = visual.Rect(
    win=win, name='TaskBpolygon',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, -0.35), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, 1.0000, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
TaskCimagepolygon = visual.Rect(
    win=win, name='TaskCimagepolygon',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, -0.4), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, 1.0000, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
TaskBimagebutton = visual.ButtonStim(win, 
    text=None, font='Arvo',
    pos=(0, 0.2),
    letterHeight=0.05,
    size=(0.26, 0.16), borderWidth=0.0,
    fillColor=[0.0000, 0.0000, 0.0000], borderColor=[1.0000, 0.2549, -0.0431],
    color=[-1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=0.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='TaskBimagebutton'
)
TaskBimagebutton.buttonClock = core.Clock()
TaskCimagebutton = visual.ButtonStim(win, 
    text=None, font='Arvo',
    pos=(0.5, 0.2),
    letterHeight=0.05,
    size=(0.26, 0.16), borderWidth=0.0,
    fillColor=[0.0000, 0.0000, 0.0000], borderColor=None,
    color=[-1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=0.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='TaskCimagebutton'
)
TaskCimagebutton.buttonClock = core.Clock()
valueA_text = visual.TextStim(win=win, name='valueA_text',
    text='',
    font='MicroSoft YaHei',
    pos=(-0.1, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
valueB_text = visual.TextStim(win=win, name='valueB_text',
    text='',
    font='MicroSoft YaHei',
    pos=(-0.1, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
valueC_text = visual.TextStim(win=win, name='valueC_text',
    text='',
    font='MicroSoft YaHei',
    pos=(-0.1, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
showtime_text = visual.TextStim(win=win, name='showtime_text',
    text='',
    font='MicroSoft YaHei',
    pos=(0.45, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
showscore_text = visual.TextStim(win=win, name='showscore_text',
    text=None,
    font='MicroSoft YaHei',
    pos=(-0.45, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
# Run 'Begin Experiment' code from trail_code
import time
t=0
tasknumber=0
trailcount=0
poly_list=[0.4,0.4,0.4]
ThisTrailScore=0
checkmove=None
TaskAdesicribe_text = visual.TextStim(win=win, name='TaskAdesicribe_text',
    text='任务A',
    font='MicroSoft YaHei',
    pos=(-0.5, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
TaskBdesicribe_text = visual.TextStim(win=win, name='TaskBdesicribe_text',
    text='任务B',
    font='MicroSoft YaHei',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
TaskCdesicribe_text = visual.TextStim(win=win, name='TaskCdesicribe_text',
    text='任务C',
    font='MicroSoft YaHei',
    pos=(0.5, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
showappendscore_text = visual.TextStim(win=win, name='showappendscore_text',
    text=None,
    font='MicroSoft YaHei',
    pos=(-0.15, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-0.0039, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);

# --- Initialize components for Routine "model_pattern_intro" ---
model_pattern_introduce = visual.ImageStim(
    win=win,
    name='model_pattern_introduce', 
    image='mp说明.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "model_pattern" ---
# Run 'Begin Experiment' code from mp_choose_code
image_left="model_pattern/0_1.png"
image_right="model_pattern/0_2.png"
image_mid="model_pattern/0_1.png"
pattern_count=0
mp_image_left = visual.ImageStim(
    win=win,
    name='mp_image_left', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mp_image_right = visual.ImageStim(
    win=win,
    name='mp_image_right', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mp_image_mid = visual.ImageStim(
    win=win,
    name='mp_image_mid', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3,0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_5 = keyboard.Keyboard()
mp_showtime1 = visual.TextStim(win=win, name='mp_showtime1',
    text='',
    font='MicroSoft YaHei',
    pos=(0.7, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "tasckafeedback" ---
mp_image_left2 = visual.ImageStim(
    win=win,
    name='mp_image_left2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mp_image_right2 = visual.ImageStim(
    win=win,
    name='mp_image_right2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mp_image_mid2 = visual.ImageStim(
    win=win,
    name='mp_image_mid2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3,0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mp_feedback = visual.TextStim(win=win, name='mp_feedback',
    text='',
    font='MicroSoft YaHei',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "two_back_intro" ---
key_resp_4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from var_2b_begin_code


two_back_introduce = visual.ImageStim(
    win=win,
    name='two_back_introduce', 
    image='nb说明.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "n_back" ---
# Run 'Begin Experiment' code from two_back_num_react_code


two_back_num_text = visual.TextStim(win=win, name='two_back_num_text',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
two_back_num_showtime_text = visual.TextStim(win=win, name='two_back_num_showtime_text',
    text='',
    font='MicroSoft YaHei',
    pos=(0.7, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "n_backfeedback" ---
two_back_feedback_text1 = visual.TextStim(win=win, name='two_back_feedback_text1',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
two_back_showtime_text2 = visual.TextStim(win=win, name='two_back_showtime_text2',
    text='',
    font='MicroSoft YaHei',
    pos=(0.70, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "vsintro" ---
VS_intro_image = visual.ImageStim(
    win=win,
    name='VS_intro_image', 
    image='VS指导语.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "visual_Search" ---
# Run 'Begin Experiment' code from VS_react_code
VSimage_path=f"visual_search_pic/{taskcnum}.png"
VSimage = visual.ImageStim(
    win=win,
    name='VSimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.2, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
taskctime_text = visual.TextStim(win=win, name='taskctime_text',
    text='',
    font='MicroSoft YaHei',
    pos=(0.7, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "vsfeedback" ---
# Run 'Begin Experiment' code from VS_feedback_code


VSimage_2 = visual.ImageStim(
    win=win,
    name='VSimage_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.2, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
taskc_text = visual.TextStim(win=win, name='taskc_text',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
taskctime_text2 = visual.TextStim(win=win, name='taskctime_text2',
    text='',
    font='MicroSoft YaHei',
    pos=(0.7, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "feedback" ---
feedback_polygon = visual.Rect(
    win=win, name='feedback_polygon',
    width=(1.4, 0.9)[0], height=(1.4, 0.9)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7098, 0.2941, -0.7490],
    opacity=None, depth=0.0, interpolate=True)
showresult1 = visual.TextStim(win=win, name='showresult1',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
taskscore_text1 = visual.TextStim(win=win, name='taskscore_text1',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
finalscore_text1 = visual.TextStim(win=win, name='finalscore_text1',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
feedback_button = visual.ButtonStim(win, 
    text='点击进入下一个选择', font='MicroSoft YaHei',
    pos=(0,-0.35),
    letterHeight=0.05,
    size=(0.6,0.1), borderWidth=0.0,
    fillColor=[0.0824, -0.6627, 0.7725], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='feedback_button'
)
feedback_button.buttonClock = core.Clock()
# Run 'Begin Experiment' code from feedback_code
TotalScoreCount=0
confidence_slider = visual.Slider(win=win, name='confidence_slider',
    startValue=50, size=(0.5, 0.05), pos=(0, -0.2), units=None,
    labels=confidence_rate, ticks=(50, 60, 70, 80, 90,100), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=[0.3569, 1.0000, -0.6314], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-6, readOnly=False)
confidence_text = visual.TextStim(win=win, name='confidence_text',
    text='您对上一个问题回答正确的信心水平是：',
    font='MicroSoft YaHei',
    pos=(0, -0.10), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
yes_or_no_slider = visual.Slider(win=win, name='yes_or_no_slider',
    startValue=None, size=(0.1, 0.03), pos=(0, 0.0), units=None,
    labels=yes_or_no, ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=[0.3569, 1.0000, -0.6314], lineColor='White', colorSpace='rgb',
    font='Microsoft YaHei', labelHeight=0.02,
    flip=False, ori=0.0, depth=-8, readOnly=False)
yes_or_no_answer_text = visual.TextStim(win=win, name='yes_or_no_answer_text',
    text='您认为本轮选择的任务是否是最优选项？',
    font='MicroSoft YaHei',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "end" ---
text = visual.TextStim(win=win, name='text',
    text='恭喜你完成实验！！',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setpComponents = [firstbutton_2]
for thisComponent in setpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *firstbutton_2* updates
    if firstbutton_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        firstbutton_2.frameNStart = frameN  # exact frame index
        firstbutton_2.tStart = t  # local t and not account for scr refresh
        firstbutton_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstbutton_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'firstbutton_2.started')
        firstbutton_2.setAutoDraw(True)
    if firstbutton_2.status == STARTED:
        # check whether firstbutton_2 has been pressed
        if firstbutton_2.isClicked:
            if not firstbutton_2.wasClicked:
                firstbutton_2.timesOn.append(firstbutton_2.buttonClock.getTime()) # store time of first click
                firstbutton_2.timesOff.append(firstbutton_2.buttonClock.getTime()) # store time clicked until
            else:
                firstbutton_2.timesOff[-1] = firstbutton_2.buttonClock.getTime() # update time clicked until
            if not firstbutton_2.wasClicked:
                continueRoutine = False  # end routine when firstbutton_2 is clicked
                newsave=time.perf_counter()
            firstbutton_2.wasClicked = True  # if firstbutton_2 is still clicked next frame, it is not a new click
        else:
            firstbutton_2.wasClicked = False  # if firstbutton_2 is clicked next frame, it is a new click
    else:
        firstbutton_2.wasClicked = False  # if firstbutton_2 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setp" ---
for thisComponent in setpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('firstbutton_2.numClicks', firstbutton_2.numClicks)
if firstbutton_2.numClicks:
   thisExp.addData('firstbutton_2.timesOn', firstbutton_2.timesOn)
   thisExp.addData('firstbutton_2.timesOff', firstbutton_2.timesOff)
else:
   thisExp.addData('firstbutton_2.timesOn', "")
   thisExp.addData('firstbutton_2.timesOff', "")
# the Routine "setp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "confidence_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    confidence_introComponents = [image, key_resp_7]
    for thisComponent in confidence_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidence_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidence_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidence_intro" ---
    for thisComponent in confidence_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials_5.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials_5.addData('key_resp_7.rt', key_resp_7.rt)
    # the Routine "confidence_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "confidence_intro_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    confidence_intro_2Components = [image_2, key_resp_8]
    for thisComponent in confidence_intro_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidence_intro_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            image_2.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidence_intro_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidence_intro_2" ---
    for thisComponent in confidence_intro_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    trials_5.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials_5.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "confidence_intro_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "confidence_intro_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    confidence_intro_3Components = [button, image_3, key_resp_9]
    for thisComponent in confidence_intro_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "confidence_intro_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *button* updates
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button.started')
            button.setAutoDraw(True)
        if button.status == STARTED:
            # check whether button has been pressed
            if button.isClicked:
                if not button.wasClicked:
                    button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                    button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
                else:
                    button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
                if not button.wasClicked:
                    continueRoutine = False  # end routine when button is clicked
                    trials_5.finished = True
                    newsave=time.perf_counter()
                button.wasClicked = True  # if button is still clicked next frame, it is not a new click
            else:
                button.wasClicked = False  # if button is clicked next frame, it is a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            image_3.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidence_intro_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "confidence_intro_3" ---
    for thisComponent in confidence_intro_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       trials_5.addData('button.timesOn', button.timesOn)
       trials_5.addData('button.timesOff', button.timesOff)
    else:
       trials_5.addData('button.timesOn', "")
       trials_5.addData('button.timesOff', "")
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials_5.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials_5.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "confidence_intro_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_5'


# --- Prepare to start Routine "timecoder" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_4
timecoder=t
# keep track of which components have finished
timecoderComponents = []
for thisComponent in timecoderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "timecoder" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in timecoderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "timecoder" ---
for thisComponent in timecoderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "timecoder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=16.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "choose" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    valueA_text.setText('\n')
    valueB_text.setText('aaaaaa\n')
    valueC_text.setText('aaaaaa\n')
    # Run 'Begin Routine' code from trail_code
    valueA_text.setText(f"任务A价值:{VAR1}")
    valueB_text.setText(f"任务B价值:{VAR2}")
    valueC_text.setText(f"任务C价值:{VAR3}")
    showscore_text.setText(f"累计积分：{TotalScoreCount}")
    showappendscore_text.setText(f"+{ThisTrailScore}")
    count=0
    Totaltime=Totaltime-tasktrmainingtime
    total_trial_show=f"剩余轮次：{total_trial_show_count}"
    
    # keep track of which components have finished
    chooseComponents = [TaskAimage, TaskBimage, TaskCimage, describevalue_text, TaskApolygon, TaskAbutton, TaskBpolygon, TaskCimagepolygon, TaskBimagebutton, TaskCimagebutton, valueA_text, valueB_text, valueC_text, showtime_text, showscore_text, TaskAdesicribe_text, TaskBdesicribe_text, TaskCdesicribe_text, showappendscore_text]
    for thisComponent in chooseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choose" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TaskAimage* updates
        if TaskAimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskAimage.frameNStart = frameN  # exact frame index
            TaskAimage.tStart = t  # local t and not account for scr refresh
            TaskAimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskAimage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskAimage.started')
            TaskAimage.setAutoDraw(True)
        
        # *TaskBimage* updates
        if TaskBimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskBimage.frameNStart = frameN  # exact frame index
            TaskBimage.tStart = t  # local t and not account for scr refresh
            TaskBimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskBimage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskBimage.started')
            TaskBimage.setAutoDraw(True)
        
        # *TaskCimage* updates
        if TaskCimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskCimage.frameNStart = frameN  # exact frame index
            TaskCimage.tStart = t  # local t and not account for scr refresh
            TaskCimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskCimage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskCimage.started')
            TaskCimage.setAutoDraw(True)
        
        # *describevalue_text* updates
        if describevalue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            describevalue_text.frameNStart = frameN  # exact frame index
            describevalue_text.tStart = t  # local t and not account for scr refresh
            describevalue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(describevalue_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'describevalue_text.started')
            describevalue_text.setAutoDraw(True)
        
        # *TaskApolygon* updates
        if TaskApolygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskApolygon.frameNStart = frameN  # exact frame index
            TaskApolygon.tStart = t  # local t and not account for scr refresh
            TaskApolygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskApolygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskApolygon.started')
            TaskApolygon.setAutoDraw(True)
        if TaskApolygon.status == STARTED:  # only update if drawing
            TaskApolygon.setSize((polygon1h, 0.03), log=False)
        
        # *TaskAbutton* updates
        if TaskAbutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            TaskAbutton.frameNStart = frameN  # exact frame index
            TaskAbutton.tStart = t  # local t and not account for scr refresh
            TaskAbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskAbutton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskAbutton.started')
            TaskAbutton.setAutoDraw(True)
        if TaskAbutton.status == STARTED:
            # check whether TaskAbutton has been pressed
            if TaskAbutton.isClicked:
                if not TaskAbutton.wasClicked:
                    TaskAbutton.timesOn.append(TaskAbutton.buttonClock.getTime()) # store time of first click
                    TaskAbutton.timesOff.append(TaskAbutton.buttonClock.getTime()) # store time clicked until
                else:
                    TaskAbutton.timesOff[-1] = TaskAbutton.buttonClock.getTime() # update time clicked until
                if not TaskAbutton.wasClicked:
                    continueRoutine = False  # end routine when TaskAbutton is clicked
                    tasknumber="A"
                    
                        
                TaskAbutton.wasClicked = True  # if TaskAbutton is still clicked next frame, it is not a new click
            else:
                TaskAbutton.wasClicked = False  # if TaskAbutton is clicked next frame, it is a new click
        else:
            TaskAbutton.wasClicked = False  # if TaskAbutton is clicked next frame, it is a new click
        
        # *TaskBpolygon* updates
        if TaskBpolygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskBpolygon.frameNStart = frameN  # exact frame index
            TaskBpolygon.tStart = t  # local t and not account for scr refresh
            TaskBpolygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskBpolygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskBpolygon.started')
            TaskBpolygon.setAutoDraw(True)
        if TaskBpolygon.status == STARTED:  # only update if drawing
            TaskBpolygon.setSize((polygon2h, 0.03), log=False)
        
        # *TaskCimagepolygon* updates
        if TaskCimagepolygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskCimagepolygon.frameNStart = frameN  # exact frame index
            TaskCimagepolygon.tStart = t  # local t and not account for scr refresh
            TaskCimagepolygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskCimagepolygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskCimagepolygon.started')
            TaskCimagepolygon.setAutoDraw(True)
        if TaskCimagepolygon.status == STARTED:  # only update if drawing
            TaskCimagepolygon.setSize((polygon3h, 0.03), log=False)
        
        # *TaskBimagebutton* updates
        if TaskBimagebutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            TaskBimagebutton.frameNStart = frameN  # exact frame index
            TaskBimagebutton.tStart = t  # local t and not account for scr refresh
            TaskBimagebutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskBimagebutton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskBimagebutton.started')
            TaskBimagebutton.setAutoDraw(True)
        if TaskBimagebutton.status == STARTED:
            # check whether TaskBimagebutton has been pressed
            if TaskBimagebutton.isClicked:
                if not TaskBimagebutton.wasClicked:
                    TaskBimagebutton.timesOn.append(TaskBimagebutton.buttonClock.getTime()) # store time of first click
                    TaskBimagebutton.timesOff.append(TaskBimagebutton.buttonClock.getTime()) # store time clicked until
                else:
                    TaskBimagebutton.timesOff[-1] = TaskBimagebutton.buttonClock.getTime() # update time clicked until
                if not TaskBimagebutton.wasClicked:
                    continueRoutine = False  # end routine when TaskBimagebutton is clicked
                    tasknumber="B"
                TaskBimagebutton.wasClicked = True  # if TaskBimagebutton is still clicked next frame, it is not a new click
            else:
                TaskBimagebutton.wasClicked = False  # if TaskBimagebutton is clicked next frame, it is a new click
        else:
            TaskBimagebutton.wasClicked = False  # if TaskBimagebutton is clicked next frame, it is a new click
        
        # *TaskCimagebutton* updates
        if TaskCimagebutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            TaskCimagebutton.frameNStart = frameN  # exact frame index
            TaskCimagebutton.tStart = t  # local t and not account for scr refresh
            TaskCimagebutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskCimagebutton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskCimagebutton.started')
            TaskCimagebutton.setAutoDraw(True)
        if TaskCimagebutton.status == STARTED:
            # check whether TaskCimagebutton has been pressed
            if TaskCimagebutton.isClicked:
                if not TaskCimagebutton.wasClicked:
                    TaskCimagebutton.timesOn.append(TaskCimagebutton.buttonClock.getTime()) # store time of first click
                    TaskCimagebutton.timesOff.append(TaskCimagebutton.buttonClock.getTime()) # store time clicked until
                else:
                    TaskCimagebutton.timesOff[-1] = TaskCimagebutton.buttonClock.getTime() # update time clicked until
                if not TaskCimagebutton.wasClicked:
                    continueRoutine = False  # end routine when TaskCimagebutton is clicked
                    tasknumber="C"
                    
                TaskCimagebutton.wasClicked = True  # if TaskCimagebutton is still clicked next frame, it is not a new click
            else:
                TaskCimagebutton.wasClicked = False  # if TaskCimagebutton is clicked next frame, it is a new click
        else:
            TaskCimagebutton.wasClicked = False  # if TaskCimagebutton is clicked next frame, it is a new click
        
        # *valueA_text* updates
        if valueA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valueA_text.frameNStart = frameN  # exact frame index
            valueA_text.tStart = t  # local t and not account for scr refresh
            valueA_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valueA_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valueA_text.started')
            valueA_text.setAutoDraw(True)
        
        # *valueB_text* updates
        if valueB_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valueB_text.frameNStart = frameN  # exact frame index
            valueB_text.tStart = t  # local t and not account for scr refresh
            valueB_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valueB_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valueB_text.started')
            valueB_text.setAutoDraw(True)
        
        # *valueC_text* updates
        if valueC_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valueC_text.frameNStart = frameN  # exact frame index
            valueC_text.tStart = t  # local t and not account for scr refresh
            valueC_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valueC_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valueC_text.started')
            valueC_text.setAutoDraw(True)
        
        # *showtime_text* updates
        if showtime_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showtime_text.frameNStart = frameN  # exact frame index
            showtime_text.tStart = t  # local t and not account for scr refresh
            showtime_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showtime_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'showtime_text.started')
            showtime_text.setAutoDraw(True)
        if showtime_text.status == STARTED:  # only update if drawing
            showtime_text.setText(total_trial_show, log=False)
        
        # *showscore_text* updates
        if showscore_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showscore_text.frameNStart = frameN  # exact frame index
            showscore_text.tStart = t  # local t and not account for scr refresh
            showscore_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showscore_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'showscore_text.started')
            showscore_text.setAutoDraw(True)
        # Run 'Each Frame' code from trail_code
        ###时间显示模块
        
        showtime,timecoder= getdowntime(Totaltime)
        ###动效价值条块
        if checkmove == "A" and count<30:
            polygon1h -=0.08/30
            polygon2h +=0.04/30
            polygon3h +=0.04/30
            count +=1
            
        if checkmove == "B" and count<30:
            polygon1h +=0.04/30
            polygon2h -=0.08/30
            polygon3h +=0.04/30 
            count +=1
         
        if checkmove =="C" and count<30:
            polygon1h +=0.04/30
            polygon2h +=0.04/30
            polygon3h -=0.08/30
            count +=1
        if timecoder <= 0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
            total_time_zero =0
        
        
        # *TaskAdesicribe_text* updates
        if TaskAdesicribe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskAdesicribe_text.frameNStart = frameN  # exact frame index
            TaskAdesicribe_text.tStart = t  # local t and not account for scr refresh
            TaskAdesicribe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskAdesicribe_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskAdesicribe_text.started')
            TaskAdesicribe_text.setAutoDraw(True)
        
        # *TaskBdesicribe_text* updates
        if TaskBdesicribe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskBdesicribe_text.frameNStart = frameN  # exact frame index
            TaskBdesicribe_text.tStart = t  # local t and not account for scr refresh
            TaskBdesicribe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskBdesicribe_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskBdesicribe_text.started')
            TaskBdesicribe_text.setAutoDraw(True)
        
        # *TaskCdesicribe_text* updates
        if TaskCdesicribe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TaskCdesicribe_text.frameNStart = frameN  # exact frame index
            TaskCdesicribe_text.tStart = t  # local t and not account for scr refresh
            TaskCdesicribe_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TaskCdesicribe_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TaskCdesicribe_text.started')
            TaskCdesicribe_text.setAutoDraw(True)
        
        # *showappendscore_text* updates
        if showappendscore_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showappendscore_text.frameNStart = frameN  # exact frame index
            showappendscore_text.tStart = t  # local t and not account for scr refresh
            showappendscore_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showappendscore_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'showappendscore_text.started')
            showappendscore_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in chooseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choose" ---
    for thisComponent in chooseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('TaskAbutton.numClicks', TaskAbutton.numClicks)
    if TaskAbutton.numClicks:
       trials.addData('TaskAbutton.timesOn', TaskAbutton.timesOn)
       trials.addData('TaskAbutton.timesOff', TaskAbutton.timesOff)
    else:
       trials.addData('TaskAbutton.timesOn', "")
       trials.addData('TaskAbutton.timesOff', "")
    trials.addData('TaskBimagebutton.numClicks', TaskBimagebutton.numClicks)
    if TaskBimagebutton.numClicks:
       trials.addData('TaskBimagebutton.timesOn', TaskBimagebutton.timesOn)
       trials.addData('TaskBimagebutton.timesOff', TaskBimagebutton.timesOff)
    else:
       trials.addData('TaskBimagebutton.timesOn', "")
       trials.addData('TaskBimagebutton.timesOff', "")
    trials.addData('TaskCimagebutton.numClicks', TaskCimagebutton.numClicks)
    if TaskCimagebutton.numClicks:
       trials.addData('TaskCimagebutton.timesOn', TaskCimagebutton.timesOn)
       trials.addData('TaskCimagebutton.timesOff', TaskCimagebutton.timesOff)
    else:
       trials.addData('TaskCimagebutton.timesOn', "")
       trials.addData('TaskCimagebutton.timesOff', "")
    # Run 'End Routine' code from trail_code
    trailcount+=3
    checkmove=None
    # the Routine "choose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "model_pattern_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from model_pattern_begin_code
    if tasknumber!="A":
        continueRoutine = False
        routineForceEnded = True
    
    pattern_correct_count=0    
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    model_pattern_introComponents = [model_pattern_introduce, key_resp_6]
    for thisComponent in model_pattern_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "model_pattern_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from model_pattern_begin_code
        if timecoder <= 0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
            total_time_zero =0
        
        # *model_pattern_introduce* updates
        if model_pattern_introduce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            model_pattern_introduce.frameNStart = frameN  # exact frame index
            model_pattern_introduce.tStart = t  # local t and not account for scr refresh
            model_pattern_introduce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(model_pattern_introduce, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'model_pattern_introduce.started')
            model_pattern_introduce.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in model_pattern_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "model_pattern_intro" ---
    for thisComponent in model_pattern_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from model_pattern_begin_code
    taskctimer.reset()
    
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "model_pattern_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=30.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "model_pattern" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from mp_choose_code
        if tasknumber!="A":
            continueRoutine = False
            routineForceEnded = True
            trials_4.finished=True
        pattern_count=random.randint(1,9999)
        LR=random.randint(1,2)
        if LR == 1:
            mp_correct="j"
        else:
            mp_correct="f"
        image_left=f"model_pattern/{pattern_count}_1.png"
        image_right=f"model_pattern/{pattern_count}_2.png"
        image_mid=f"model_pattern/{pattern_count}_{LR}.png"
        mp_image_left.setImage(image_left)
        mp_image_right.setImage(image_right)
        mp_image_mid.setImage(image_mid)
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        model_patternComponents = [mp_image_left, mp_image_right, mp_image_mid, key_resp_5, mp_showtime1]
        for thisComponent in model_patternComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "model_pattern" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from mp_choose_code
            taskatime=get_taskatime(30)
            if taskatime==0:
                taskatime=0
                continueRoutine = False
                routineForceEnded = True
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            # *mp_image_left* updates
            if mp_image_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_left.frameNStart = frameN  # exact frame index
                mp_image_left.tStart = t  # local t and not account for scr refresh
                mp_image_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_left.started')
                mp_image_left.setAutoDraw(True)
            
            # *mp_image_right* updates
            if mp_image_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_right.frameNStart = frameN  # exact frame index
                mp_image_right.tStart = t  # local t and not account for scr refresh
                mp_image_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_right.started')
                mp_image_right.setAutoDraw(True)
            
            # *mp_image_mid* updates
            if mp_image_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_mid.frameNStart = frameN  # exact frame index
                mp_image_mid.tStart = t  # local t and not account for scr refresh
                mp_image_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_mid, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_mid.started')
                mp_image_mid.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=["f","j"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_5.keys == str(mp_correct)) or (key_resp_5.keys == mp_correct):
                        key_resp_5.corr = 1
                    else:
                        key_resp_5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *mp_showtime1* updates
            if mp_showtime1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_showtime1.frameNStart = frameN  # exact frame index
                mp_showtime1.tStart = t  # local t and not account for scr refresh
                mp_showtime1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_showtime1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_showtime1.started')
                mp_showtime1.setAutoDraw(True)
            if mp_showtime1.status == STARTED:  # only update if drawing
                mp_showtime1.setText(taskatime, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in model_patternComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "model_pattern" ---
        for thisComponent in model_patternComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
            # was no response the correct answer?!
            if str(mp_correct).lower() == 'none':
               key_resp_5.corr = 1;  # correct non-response
            else:
               key_resp_5.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_4 (TrialHandler)
        trials_4.addData('key_resp_5.keys',key_resp_5.keys)
        trials_4.addData('key_resp_5.corr', key_resp_5.corr)
        if key_resp_5.keys != None:  # we had a response
            trials_4.addData('key_resp_5.rt', key_resp_5.rt)
        # the Routine "model_pattern" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "tasckafeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mp_image_left2.setImage(image_left)
        mp_image_right2.setImage(image_right)
        mp_image_mid2.setImage(image_mid)
        # Run 'Begin Routine' code from mp_feedback_code
        if tasknumber!="A":
            continueRoutine = False
            routineForceEnded = True
            trials_4.finished = True
        else:
            if key_resp_5.corr !=1 :
                taskafeedback="错误"
                taska_text_color = "red"
                trials_4.finished=True
            elif key_resp_5.corr==1:
                taskafeedback="正确"
                taska_text_color = "greenyellow"
        
        # keep track of which components have finished
        tasckafeedbackComponents = [mp_image_left2, mp_image_right2, mp_image_mid2, mp_feedback]
        for thisComponent in tasckafeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tasckafeedback" ---
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mp_image_left2* updates
            if mp_image_left2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_left2.frameNStart = frameN  # exact frame index
                mp_image_left2.tStart = t  # local t and not account for scr refresh
                mp_image_left2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_left2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_left2.started')
                mp_image_left2.setAutoDraw(True)
            if mp_image_left2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_left2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_left2.tStop = t  # not accounting for scr refresh
                    mp_image_left2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mp_image_left2.stopped')
                    mp_image_left2.setAutoDraw(False)
            
            # *mp_image_right2* updates
            if mp_image_right2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_right2.frameNStart = frameN  # exact frame index
                mp_image_right2.tStart = t  # local t and not account for scr refresh
                mp_image_right2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_right2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_right2.started')
                mp_image_right2.setAutoDraw(True)
            if mp_image_right2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_right2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_right2.tStop = t  # not accounting for scr refresh
                    mp_image_right2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mp_image_right2.stopped')
                    mp_image_right2.setAutoDraw(False)
            
            # *mp_image_mid2* updates
            if mp_image_mid2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_mid2.frameNStart = frameN  # exact frame index
                mp_image_mid2.tStart = t  # local t and not account for scr refresh
                mp_image_mid2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_mid2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_image_mid2.started')
                mp_image_mid2.setAutoDraw(True)
            if mp_image_mid2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_mid2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_mid2.tStop = t  # not accounting for scr refresh
                    mp_image_mid2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mp_image_mid2.stopped')
                    mp_image_mid2.setAutoDraw(False)
            
            # *mp_feedback* updates
            if mp_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_feedback.frameNStart = frameN  # exact frame index
                mp_feedback.tStart = t  # local t and not account for scr refresh
                mp_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mp_feedback.started')
                mp_feedback.setAutoDraw(True)
            if mp_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_feedback.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_feedback.tStop = t  # not accounting for scr refresh
                    mp_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mp_feedback.stopped')
                    mp_feedback.setAutoDraw(False)
            if mp_feedback.status == STARTED:  # only update if drawing
                mp_feedback.setColor(taska_text_color, colorSpace='rgb', log=False)
                mp_feedback.setText(taskafeedback, log=False)
            # Run 'Each Frame' code from mp_feedback_code
            if taskatime==0:
                taskatime=0
                continueRoutine = False
                routineForceEnded = True
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tasckafeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tasckafeedback" ---
        for thisComponent in tasckafeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from mp_feedback_code
        pattern_correct_count+=1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        thisExp.nextEntry()
        
    # completed 30.0 repeats of 'trials_4'
    
    
    # --- Prepare to start Routine "two_back_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # Run 'Begin Routine' code from var_2b_begin_code
    if tasknumber!="B":
        continueRoutine = False
        routineForceEnded = True
    # keep track of which components have finished
    two_back_introComponents = [key_resp_4, two_back_introduce]
    for thisComponent in two_back_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "two_back_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from var_2b_begin_code
        if timecoder <= 0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
            total_time_zero =0
        
        # *two_back_introduce* updates
        if two_back_introduce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_back_introduce.frameNStart = frameN  # exact frame index
            two_back_introduce.tStart = t  # local t and not account for scr refresh
            two_back_introduce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_back_introduce, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two_back_introduce.started')
            two_back_introduce.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in two_back_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "two_back_intro" ---
    for thisComponent in two_back_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # Run 'End Routine' code from var_2b_begin_code
    taskctimer.reset()
    two_back_list=[]
    two_back_count=0
    two_back_correct=""
    two_back_feedback_text=""
    two_back_num=random.randint(0,9)    
    two_back_img=f"pic/{two_back_num}.png"
    
    # the Routine "two_back_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=40.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "n_back" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from two_back_num_react_code
        if tasknumber!="B":
            continueRoutine = False
            routineForceEnded = True
            trials_3.finished = True
            
        two_back_num=random.randint(0,9)    
        two_back_list.append(two_back_num)
        
        if two_back_count >=2:
            two_back_correct = two_back_list[two_back_count-2]
            if two_back_count ==2:
                taskctimer.reset()
        two_back_num_text.setText(two_back_num)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        n_backComponents = [two_back_num_text, key_resp_3, two_back_num_showtime_text]
        for thisComponent in n_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "n_back" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from two_back_num_react_code
            if two_back_count <2:
                taskbtime=30
                duration=2
            elif two_back_count >=2:    
                taskbtime=get_taskbtime(30)
                duration=30
            
            if taskbtime==0:
                taskbtime=0
                continueRoutine = False
                routineForceEnded = True
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            # *two_back_num_text* updates
            if two_back_num_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_num_text.frameNStart = frameN  # exact frame index
                two_back_num_text.tStart = t  # local t and not account for scr refresh
                two_back_num_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_num_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_back_num_text.started')
                two_back_num_text.setAutoDraw(True)
            if two_back_num_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_num_text.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_num_text.tStop = t  # not accounting for scr refresh
                    two_back_num_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two_back_num_text.stopped')
                    two_back_num_text.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_3.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=["1","2","3","4","5","6","7","8","9","0"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_3.keys == str(two_back_correct)) or (key_resp_3.keys == two_back_correct):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *two_back_num_showtime_text* updates
            if two_back_num_showtime_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_num_showtime_text.frameNStart = frameN  # exact frame index
                two_back_num_showtime_text.tStart = t  # local t and not account for scr refresh
                two_back_num_showtime_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_num_showtime_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_back_num_showtime_text.started')
                two_back_num_showtime_text.setAutoDraw(True)
            if two_back_num_showtime_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_num_showtime_text.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_num_showtime_text.tStop = t  # not accounting for scr refresh
                    two_back_num_showtime_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two_back_num_showtime_text.stopped')
                    two_back_num_showtime_text.setAutoDraw(False)
            if two_back_num_showtime_text.status == STARTED:  # only update if drawing
                two_back_num_showtime_text.setText(taskbtime, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in n_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "n_back" ---
        for thisComponent in n_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from two_back_num_react_code
        two_back_count+=1
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(two_back_correct).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('key_resp_3.keys',key_resp_3.keys)
        trials_3.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_3.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "n_back" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "n_backfeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from two_back_num_feedback_code
        
        
        if tasknumber!="B":
            continueRoutine = False
            routineForceEnded = True
            trials_3.finished = True
        else:
            if key_resp_3.corr !=1 and two_back_count>=3 and taskbtime!=0:
                two_back_feedback_text="错误"
                taskb_text_color = "red"
                trials_3.finished=True
            elif key_resp_3.corr==1 and two_back_count>=3 and taskbtime!=0:
                two_back_feedback_text="+"
                taskb_text_color = "white"
            elif taskbtime==0: 
                two_back_feedback_text="时间到！"
                taskb_text_color = "red"
                trials_3.finished=True
        
        two_back_feedback_text1.setColor(taskb_text_color, colorSpace='rgb')
        two_back_feedback_text1.setText(two_back_feedback_text)
        two_back_showtime_text2.setColor('white', colorSpace='rgb')
        two_back_showtime_text2.setText(taskbtime)
        # keep track of which components have finished
        n_backfeedbackComponents = [two_back_feedback_text1, two_back_showtime_text2]
        for thisComponent in n_backfeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "n_backfeedback" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from two_back_num_feedback_code
            
            if two_back_count <2:
                taskbtime=30
            elif two_back_count >=2:    
                taskbtime=get_taskbtime(30)
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            # *two_back_feedback_text1* updates
            if two_back_feedback_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_feedback_text1.frameNStart = frameN  # exact frame index
                two_back_feedback_text1.tStart = t  # local t and not account for scr refresh
                two_back_feedback_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_feedback_text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_back_feedback_text1.started')
                two_back_feedback_text1.setAutoDraw(True)
            if two_back_feedback_text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_feedback_text1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_feedback_text1.tStop = t  # not accounting for scr refresh
                    two_back_feedback_text1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two_back_feedback_text1.stopped')
                    two_back_feedback_text1.setAutoDraw(False)
            
            # *two_back_showtime_text2* updates
            if two_back_showtime_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_showtime_text2.frameNStart = frameN  # exact frame index
                two_back_showtime_text2.tStart = t  # local t and not account for scr refresh
                two_back_showtime_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_showtime_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_back_showtime_text2.started')
                two_back_showtime_text2.setAutoDraw(True)
            if two_back_showtime_text2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_showtime_text2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_showtime_text2.tStop = t  # not accounting for scr refresh
                    two_back_showtime_text2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'two_back_showtime_text2.stopped')
                    two_back_showtime_text2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in n_backfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "n_backfeedback" ---
        for thisComponent in n_backfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from two_back_num_feedback_code
        n_back_correct_count+=1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 40.0 repeats of 'trials_3'
    
    
    # --- Prepare to start Routine "vsintro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from VS_begin_code
    if tasknumber!="C":
        continueRoutine = False
        routineForceEnded = True
    vs_correct_count=0
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    vsintroComponents = [VS_intro_image, key_resp_2]
    for thisComponent in vsintroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "vsintro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from VS_begin_code
        if timecoder <= 0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
            total_time_zero =0
        
        # *VS_intro_image* updates
        if VS_intro_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            VS_intro_image.frameNStart = frameN  # exact frame index
            VS_intro_image.tStart = t  # local t and not account for scr refresh
            VS_intro_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(VS_intro_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'VS_intro_image.started')
            VS_intro_image.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsintroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "vsintro" ---
    for thisComponent in vsintroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from VS_begin_code
    taskctimer.reset()
    taskcnum=random.randint(1,499)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "vsintro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=32.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "visual_Search" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from VS_react_code
        if tasknumber != "C":
            continueRoutine = False
            routineForceEnded = True
            VS_right_react='Z'
        else:
            correct_feedback=''
            vsdata=react.loc[taskcnum]
            vsdata=vsdata[1:]
            Temp_List =np.array(vsdata).tolist()
            VS_right_react=Temp_List[Temp_List_correct]
            VSimage_path=f"visual_search_pic/{taskcnum}.png"
            vsdata=react.loc[taskcnum]
            vsdata=vsdata[1:]
        Temp_List =np.array(vsdata).tolist()
        
        
        
        VSimage.setImage(VSimage_path)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        visual_SearchComponents = [VSimage, key_resp, taskctime_text]
        for thisComponent in visual_SearchComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "visual_Search" ---
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from VS_react_code
            taskctime=get_taskctime(30)
            if taskctime==0:
                taskctime=0
                correct_feedback='时间到！！'
                taskc_text_color='red'
                trials_2.finished = True
                continueRoutine = False
                routineForceEnded = True
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            # *VSimage* updates
            if VSimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VSimage.frameNStart = frameN  # exact frame index
                VSimage.tStart = t  # local t and not account for scr refresh
                VSimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VSimage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'VSimage.started')
                VSimage.setAutoDraw(True)
            if VSimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > VSimage.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    VSimage.tStop = t  # not accounting for scr refresh
                    VSimage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'VSimage.stopped')
                    VSimage.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y','u','h','j'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(VS_right_react)) or (key_resp.keys == VS_right_react):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *taskctime_text* updates
            if taskctime_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taskctime_text.frameNStart = frameN  # exact frame index
                taskctime_text.tStart = t  # local t and not account for scr refresh
                taskctime_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taskctime_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taskctime_text.started')
                taskctime_text.setAutoDraw(True)
            if taskctime_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskctime_text.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    taskctime_text.tStop = t  # not accounting for scr refresh
                    taskctime_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taskctime_text.stopped')
                    taskctime_text.setAutoDraw(False)
            if taskctime_text.status == STARTED:  # only update if drawing
                taskctime_text.setText(taskctime, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in visual_SearchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "visual_Search" ---
        for thisComponent in visual_SearchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(VS_right_react).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('key_resp.keys',key_resp.keys)
        trials_2.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials_2.addData('key_resp.rt', key_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        
        # --- Prepare to start Routine "vsfeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from VS_feedback_code
        taskctime=get_taskctime(30)
        if tasknumber != "C":
            continueRoutine = False
            routineForceEnded = True
        else:
            if key_resp.corr==1 and taskctime!=0:
                correct_feedback='正确'
                taskc_text_color='greenyellow'
                Temp_List_correct+=1
            elif key_resp.corr==0 and taskctime!=0:
                correct_feedback='错误'
                taskc_text_color='red'
                trials_2.finished = True
            elif taskctime==0:
                taskctime=0
                correct_feedback='时间到！！'
                taskc_text_color='red'
                trials_2.finished = True
            
            
        VSimage_2.setImage(VSimage_path)
        taskc_text.setColor(taskc_text_color, colorSpace='rgb')
        taskc_text.setText(correct_feedback
)
        # keep track of which components have finished
        vsfeedbackComponents = [VSimage_2, taskc_text, taskctime_text2]
        for thisComponent in vsfeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "vsfeedback" ---
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from VS_feedback_code
            if timecoder <= 0:
                continueRoutine = False
                routineForceEnded = True
                trials.finished = True
                total_time_zero =0
            
            
            # *VSimage_2* updates
            if VSimage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VSimage_2.frameNStart = frameN  # exact frame index
                VSimage_2.tStart = t  # local t and not account for scr refresh
                VSimage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VSimage_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'VSimage_2.started')
                VSimage_2.setAutoDraw(True)
            if VSimage_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > VSimage_2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    VSimage_2.tStop = t  # not accounting for scr refresh
                    VSimage_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'VSimage_2.stopped')
                    VSimage_2.setAutoDraw(False)
            
            # *taskc_text* updates
            if taskc_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                taskc_text.frameNStart = frameN  # exact frame index
                taskc_text.tStart = t  # local t and not account for scr refresh
                taskc_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taskc_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taskc_text.started')
                taskc_text.setAutoDraw(True)
            if taskc_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskc_text.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    taskc_text.tStop = t  # not accounting for scr refresh
                    taskc_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taskc_text.stopped')
                    taskc_text.setAutoDraw(False)
            
            # *taskctime_text2* updates
            if taskctime_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taskctime_text2.frameNStart = frameN  # exact frame index
                taskctime_text2.tStart = t  # local t and not account for scr refresh
                taskctime_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taskctime_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taskctime_text2.started')
                taskctime_text2.setAutoDraw(True)
            if taskctime_text2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskctime_text2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    taskctime_text2.tStop = t  # not accounting for scr refresh
                    taskctime_text2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taskctime_text2.stopped')
                    taskctime_text2.setAutoDraw(False)
            if taskctime_text2.status == STARTED:  # only update if drawing
                taskctime_text2.setText(taskctime, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vsfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "vsfeedback" ---
        for thisComponent in vsfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from VS_feedback_code
        vs_correct_count+=1
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        thisExp.nextEntry()
        
    # completed 32.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    taskresultA=round(30+70*stats.percentileofscore(resultA_range,pattern_correct_count )/100,2)
    taskresultB=round(30+70*stats.percentileofscore(resultB_range,n_back_correct_count )/100,2)
    taskresultC=round(30+70*stats.percentileofscore(resultB_range,vs_correct_count )/100,2)
    taskchose_text=f"您选择执行的任务是：任务{tasknumber}"
    if tasknumber=="A":
        tasktrmainingtime=taskatime
        taskscore_text=f"您本轮任务的评分是：{taskresultA}"
        finalscore_text=f"您所获得的积分是：{round(taskresultA,1)}X{VAR1/100}={round(taskresultA*VAR1/100,1)}"
        ThisTrailScore=round(taskresultA*VAR1/100,1)
        if VAR1>5 and VAR2<95 and VAR3 <95:
            VAR1 -=10
            VAR2 +=5
            VAR3 +=5
            checkmove ="A"
    elif  tasknumber=="B":
        tasktrmainingtime=taskbtime
        taskscore_text=f"您本轮任务的评分是：{taskresultB}"
        finalscore_text=f"您所获得的积分是：{round(taskresultB,1)}X{VAR2/100}={round(taskresultB*VAR2/100,1)}"
        ThisTrailScore=round(taskresultB*VAR2/100,1)
        if VAR2>5 and VAR1<95 and VAR3 <95:
            VAR1+=5
            VAR2-=10
            VAR3+=5
            checkmove = "B"
    elif  tasknumber=="C":
        tasktrmainingtime=taskctime
        taskscore_text=f"您本轮任务的评分是：{taskresultC}"
        finalscore_text=f"您所获得的积分是：{round(taskresultC,1)}X{VAR3/100}={round(taskresultC*VAR3/100,1)}"
        ThisTrailScore=round(taskresultC*VAR3/100,1)
        if VAR3>5 and VAR2<95 and VAR1 <95:
            VAR1+=5
            VAR2+=5
            VAR3-=10
            checkmove = "C"
    TotalScoreCount += ThisTrailScore
    TotalScoreCount = round(TotalScoreCount,1)
    print(taskatime,taskbtime,taskctime)
        
    confidence_slider.reset()
    yes_or_no_slider.reset()
    # keep track of which components have finished
    feedbackComponents = [feedback_polygon, showresult1, taskscore_text1, finalscore_text1, feedback_button, confidence_slider, confidence_text, yes_or_no_slider, yes_or_no_answer_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_polygon* updates
        if feedback_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_polygon.frameNStart = frameN  # exact frame index
            feedback_polygon.tStart = t  # local t and not account for scr refresh
            feedback_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_polygon.started')
            feedback_polygon.setAutoDraw(True)
        
        # *showresult1* updates
        if showresult1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showresult1.frameNStart = frameN  # exact frame index
            showresult1.tStart = t  # local t and not account for scr refresh
            showresult1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showresult1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'showresult1.started')
            showresult1.setAutoDraw(True)
        if showresult1.status == STARTED:  # only update if drawing
            showresult1.setText(taskchose_text, log=False)
        
        # *taskscore_text1* updates
        if taskscore_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskscore_text1.frameNStart = frameN  # exact frame index
            taskscore_text1.tStart = t  # local t and not account for scr refresh
            taskscore_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskscore_text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'taskscore_text1.started')
            taskscore_text1.setAutoDraw(True)
        if taskscore_text1.status == STARTED:  # only update if drawing
            taskscore_text1.setText(taskscore_text, log=False)
        
        # *finalscore_text1* updates
        if finalscore_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finalscore_text1.frameNStart = frameN  # exact frame index
            finalscore_text1.tStart = t  # local t and not account for scr refresh
            finalscore_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finalscore_text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finalscore_text1.started')
            finalscore_text1.setAutoDraw(True)
        if finalscore_text1.status == STARTED:  # only update if drawing
            finalscore_text1.setText(finalscore_text, log=False)
        
        # *feedback_button* updates
        if feedback_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_button.frameNStart = frameN  # exact frame index
            feedback_button.tStart = t  # local t and not account for scr refresh
            feedback_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_button.started')
            feedback_button.setAutoDraw(True)
        if feedback_button.status == STARTED:
            # check whether feedback_button has been pressed
            if feedback_button.isClicked:
                if not feedback_button.wasClicked:
                    feedback_button.timesOn.append(feedback_button.buttonClock.getTime()) # store time of first click
                    feedback_button.timesOff.append(feedback_button.buttonClock.getTime()) # store time clicked until
                else:
                    feedback_button.timesOff[-1] = feedback_button.buttonClock.getTime() # update time clicked until
                if not feedback_button.wasClicked:
                    bfbutton=True
                feedback_button.wasClicked = True  # if feedback_button is still clicked next frame, it is not a new click
            else:
                feedback_button.wasClicked = False  # if feedback_button is clicked next frame, it is a new click
        else:
            feedback_button.wasClicked = False  # if feedback_button is clicked next frame, it is a new click
        # Run 'Each Frame' code from feedback_code
        
        check_confidence=confidence_slider.getRating()
        check_yes_or_no=yes_or_no_slider.getRating()
        if bfbutton == True and check_confidence !=None and check_yes_or_no !=None:
            continueRoutine = False
            routineForceEnded = True
        bfbutton = False
        if total_time_zero ==0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
        if timecoder <= 0:
            continueRoutine = False
            routineForceEnded = True
            trials.finished = True
            total_time_zero =0
        
        # *confidence_slider* updates
        if confidence_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_slider.frameNStart = frameN  # exact frame index
            confidence_slider.tStart = t  # local t and not account for scr refresh
            confidence_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confidence_slider.started')
            confidence_slider.setAutoDraw(True)
        
        # *confidence_text* updates
        if confidence_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_text.frameNStart = frameN  # exact frame index
            confidence_text.tStart = t  # local t and not account for scr refresh
            confidence_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confidence_text.started')
            confidence_text.setAutoDraw(True)
        
        # *yes_or_no_slider* updates
        if yes_or_no_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes_or_no_slider.frameNStart = frameN  # exact frame index
            yes_or_no_slider.tStart = t  # local t and not account for scr refresh
            yes_or_no_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_or_no_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'yes_or_no_slider.started')
            yes_or_no_slider.setAutoDraw(True)
        
        # *yes_or_no_answer_text* updates
        if yes_or_no_answer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes_or_no_answer_text.frameNStart = frameN  # exact frame index
            yes_or_no_answer_text.tStart = t  # local t and not account for scr refresh
            yes_or_no_answer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_or_no_answer_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'yes_or_no_answer_text.started')
            yes_or_no_answer_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback_button.numClicks', feedback_button.numClicks)
    if feedback_button.numClicks:
       trials.addData('feedback_button.timesOn', feedback_button.timesOn)
       trials.addData('feedback_button.timesOff', feedback_button.timesOff)
    else:
       trials.addData('feedback_button.timesOn', "")
       trials.addData('feedback_button.timesOff', "")
    # Run 'End Routine' code from feedback_code
    taskcnum+=1
    Temp_List_correct=0
    bfbutton=False
    check_confidence=None
    check_yes_or_no=None
    
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"模式匹配：{pattern_correct_count}\n")
    file_handle.close()
    pattern_correct_count=0
    
    
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"2back：{n_back_correct_count}\n")
    file_handle.close()
    n_back_correct_count=0
    
    
    
    
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"视觉搜索：{vs_correct_count}\n")
    file_handle.close()
    vs_correct_count=0
    total_trial_show_count-=1
    trials.addData('confidence_slider.response', confidence_slider.getRating())
    trials.addData('confidence_slider.rt', confidence_slider.getRT())
    trials.addData('yes_or_no_slider.response', yes_or_no_slider.getRating())
    trials.addData('yes_or_no_slider.rt', yes_or_no_slider.getRT())
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 16.0 repeats of 'trials'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
