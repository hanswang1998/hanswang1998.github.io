#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 一月 05, 2023, at 21:10
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
import pandas as pd
import time
import random
# Run 'Before Experiment' code from code_5
#training_intro_text="""欢迎您进入训练阶段，在本阶段您的主要目标是学习和熟悉以下三种任
#务的玩法和计分方式，您会依次学习任务A、任务B、任务C的玩法和计分方
#式，每个任务需要学习四次才可进入下一个任务的训练阶段。请按下空格键
#开启任务A的学习。"""
#showtext=""
#
#temp_count=0
# Run 'Before Experiment' code from mp_choose_code
def get_taskatime(sec):
    taskatime=taskctimer.getTime()
    taskatime=int(round(sec-taskatime,0))
    return taskatime
taskatime=""
taskafeedback=""
image_left="model_pattern/0_1.png"
image_right="model_pattern/0_2.png"
image_mid="model_pattern/0_1.png"
pattern_count=0
# Run 'Before Experiment' code from mp_feedback_code
taska_text_color="white"
pattern_correct_count=0
# Run 'Before Experiment' code from feedback_code_2
import random
from scipy import stats 
taskchose_text=""
taskscore_text=""
mpfeedback_text="点击进入下一轮尝试"
rowcount=0
result_list=[]
resultA_range=pd.read_excel("预实验数据.xlsx")
resultA_range=resultA_range["mp"].dropna()
# Run 'Before Experiment' code from two_back_num_react_code
def get_taskbtime(sec):
    taskbtime=taskctimer.getTime()
    taskbtime=int(round(sec-taskbtime,0))
    return taskbtime

# Run 'Before Experiment' code from two_back_num_feedback_code
two_back_feedback_text=""
taskb_text_color="white"
taskbtime=""
n_back_correct_count=0
# Run 'Before Experiment' code from feedback_code_3
import random
taskchose_text=""
taskscore_text=""
rowbcount=0
nbfeedback_text="点击进入下一轮尝试"
resultB_range=pd.read_excel("预实验数据.xlsx")
resultB_range=resultB_range["nb"].dropna()
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
vs_correct_count=0
# Run 'Before Experiment' code from feedback_code
import random
taskchose_text=""
taskscore_text=""
vsfeedback_text="点击进入下一轮尝试"
rowccount=0
resultC_range=pd.read_excel("预实验数据.xlsx")
resultC_range=resultC_range["vs"].dropna()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'training'  # from the Builder filename that created this script
expInfo = {
    'participant': '1',
    'bb': '1',
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
    originPath='C:\\Users\\why\\Desktop\\动态决策测验psychopy\\training.py',
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
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
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
text_4 = visual.TextStim(win=win, name='text_4',
    text='您好，欢迎您参加本次实验，本实验主要考察您的决策能力，实验流程由一个训练阶段以及四个正式阶段组成，预计用时为45分钟，请点击下方按钮开启本次实验\n',
    font='Microsoft YaHei',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='测验总指导语.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
firstbutton_2 = visual.ButtonStim(win, 
    text='欢迎参与此次实验，点击此处开始吧！', font='Microsoft YaHei',
    pos=(0, -0.4),
    letterHeight=0.05,
    size=(0.9,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='firstbutton_2'
)
firstbutton_2.buttonClock = core.Clock()

# --- Initialize components for Routine "training_intro" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='训练阶段指导语.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.92, 1.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

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

# --- Initialize components for Routine "mpfeedback" ---
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

# --- Initialize components for Routine "feedback_A" ---
feedback_polygon_2 = visual.Rect(
    win=win, name='feedback_polygon_2',
    width=(1.4, 0.9)[0], height=(1.4, 0.9)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7098, 0.2941, -0.7490],
    opacity=None, depth=0.0, interpolate=True)
showresult1_2 = visual.TextStim(win=win, name='showresult1_2',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
taskscore_text1_2 = visual.TextStim(win=win, name='taskscore_text1_2',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_button_2 = visual.ButtonStim(win, 
    text='', font='MicroSoft YaHei',
    pos=(0,-0.35),
    letterHeight=0.03,
    size=(0.8,0.1), borderWidth=0.0,
    fillColor=[0.0824, -0.6627, 0.7725], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='feedback_button_2'
)
feedback_button_2.buttonClock = core.Clock()

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

# --- Initialize components for Routine "feedback_B" ---
feedback_polygon_3 = visual.Rect(
    win=win, name='feedback_polygon_3',
    width=(1.4, 0.9)[0], height=(1.4, 0.9)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.7098, 0.2941, -0.7490],
    opacity=None, depth=0.0, interpolate=True)
showresult1_3 = visual.TextStim(win=win, name='showresult1_3',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
taskscore_text1_3 = visual.TextStim(win=win, name='taskscore_text1_3',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_button_3 = visual.ButtonStim(win, 
    text='', font='MicroSoft YaHei',
    pos=(0,-0.35),
    letterHeight=0.03,
    size=(0.6,0.1), borderWidth=0.0,
    fillColor=[0.0824, -0.6627, 0.7725], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='feedback_button_3'
)
feedback_button_3.buttonClock = core.Clock()

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

# --- Initialize components for Routine "tackcnum_add" ---

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
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
taskscore_text1 = visual.TextStim(win=win, name='taskscore_text1',
    text='',
    font='MicroSoft YaHei',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_button = visual.ButtonStim(win, 
    text='', font='MicroSoft YaHei',
    pos=(0,-0.35),
    letterHeight=0.03,
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

# --- Initialize components for Routine "end" ---
text = visual.TextStim(win=win, name='text',
    text='恭喜你完成训练阶段！！',
    font='MicroSoft YaHei',
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
setpComponents = [text_4, image, firstbutton_2]
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
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *firstbutton_2* updates
    if firstbutton_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        firstbutton_2.frameNStart = frameN  # exact frame index
        firstbutton_2.tStart = t  # local t and not account for scr refresh
        firstbutton_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstbutton_2, 'tStartRefresh')  # time at next scr refresh
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
# Run 'End Routine' code from code
timecoder=t
# the Routine "setp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "training_intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
training_introComponents = [image_2, key_resp_7]
for thisComponent in training_introComponents:
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

# --- Run Routine "training_intro" ---
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
        image_2.setAutoDraw(True)
    
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
    # Run 'Each Frame' code from code_5
    #for i in range(0,100000):
    #    temp_count +=1
    #if temp_count %800000 ==0:
    #    showtext=training_intro_text[0:int(temp_count/800000)]
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_intro" ---
for thisComponent in training_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "training_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=10.0, method='random', 
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
    
    # --- Prepare to start Routine "model_pattern_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from model_pattern_begin_code
    
        
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
        
        # *model_pattern_introduce* updates
        if model_pattern_introduce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            model_pattern_introduce.frameNStart = frameN  # exact frame index
            model_pattern_introduce.tStart = t  # local t and not account for scr refresh
            model_pattern_introduce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(model_pattern_introduce, 'tStartRefresh')  # time at next scr refresh
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
    # the Routine "model_pattern_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_1 = data.TrialHandler(nReps=32.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_1')
    thisExp.addLoop(trials_1)  # add the loop to the experiment
    thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    for thisTrial_1 in trials_1:
        currentLoop = trials_1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
        if thisTrial_1 != None:
            for paramName in thisTrial_1:
                exec('{} = thisTrial_1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "model_pattern" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from mp_choose_code
        
        pattern_count+=1
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
            if taskatime == 0:
                continueRoutine = False
                routineForceEnded = True
                trials_1.finished = True
                
            
            # *mp_image_left* updates
            if mp_image_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_left.frameNStart = frameN  # exact frame index
                mp_image_left.tStart = t  # local t and not account for scr refresh
                mp_image_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_left, 'tStartRefresh')  # time at next scr refresh
                mp_image_left.setAutoDraw(True)
            
            # *mp_image_right* updates
            if mp_image_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_right.frameNStart = frameN  # exact frame index
                mp_image_right.tStart = t  # local t and not account for scr refresh
                mp_image_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_right, 'tStartRefresh')  # time at next scr refresh
                mp_image_right.setAutoDraw(True)
            
            # *mp_image_mid* updates
            if mp_image_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_mid.frameNStart = frameN  # exact frame index
                mp_image_mid.tStart = t  # local t and not account for scr refresh
                mp_image_mid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_mid, 'tStartRefresh')  # time at next scr refresh
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
        # store data for trials_1 (TrialHandler)
        trials_1.addData('key_resp_5.keys',key_resp_5.keys)
        trials_1.addData('key_resp_5.corr', key_resp_5.corr)
        if key_resp_5.keys != None:  # we had a response
            trials_1.addData('key_resp_5.rt', key_resp_5.rt)
        # the Routine "model_pattern" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mpfeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        mp_image_left2.setImage(image_left)
        mp_image_right2.setImage(image_right)
        mp_image_mid2.setImage(image_mid)
        # Run 'Begin Routine' code from mp_feedback_code
        
        if key_resp_5.corr !=1 :
            taskafeedback="错误"
            taska_text_color = "red"
            trials_1.finished=True
        elif key_resp_5.corr==1:
            taskafeedback="正确"
            taska_text_color = "greenyellow"
        pattern_correct_count+=1
        # keep track of which components have finished
        mpfeedbackComponents = [mp_image_left2, mp_image_right2, mp_image_mid2, mp_feedback]
        for thisComponent in mpfeedbackComponents:
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
        
        # --- Run Routine "mpfeedback" ---
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
                mp_image_left2.setAutoDraw(True)
            if mp_image_left2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_left2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_left2.tStop = t  # not accounting for scr refresh
                    mp_image_left2.frameNStop = frameN  # exact frame index
                    mp_image_left2.setAutoDraw(False)
            
            # *mp_image_right2* updates
            if mp_image_right2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_right2.frameNStart = frameN  # exact frame index
                mp_image_right2.tStart = t  # local t and not account for scr refresh
                mp_image_right2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_right2, 'tStartRefresh')  # time at next scr refresh
                mp_image_right2.setAutoDraw(True)
            if mp_image_right2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_right2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_right2.tStop = t  # not accounting for scr refresh
                    mp_image_right2.frameNStop = frameN  # exact frame index
                    mp_image_right2.setAutoDraw(False)
            
            # *mp_image_mid2* updates
            if mp_image_mid2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mp_image_mid2.frameNStart = frameN  # exact frame index
                mp_image_mid2.tStart = t  # local t and not account for scr refresh
                mp_image_mid2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mp_image_mid2, 'tStartRefresh')  # time at next scr refresh
                mp_image_mid2.setAutoDraw(True)
            if mp_image_mid2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mp_image_mid2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mp_image_mid2.tStop = t  # not accounting for scr refresh
                    mp_image_mid2.frameNStop = frameN  # exact frame index
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
            taskatime=get_taskatime(30)
            if taskatime == 0:
                continueRoutine = False
                routineForceEnded = True
                trials_1.finished = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mpfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mpfeedback" ---
        for thisComponent in mpfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        thisExp.nextEntry()
        
    # completed 32.0 repeats of 'trials_1'
    
    
    # --- Prepare to start Routine "feedback_A" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code_2
    taskresultA=round(30+70*stats.percentileofscore(resultA_range,pattern_correct_count )/100,2)
    taskchose_text=f"您选择执行的任务是：任务A"
    taskscore_text=f"您本轮任务的评分是：{taskresultA}"
    rowcount+=1
    if rowcount == 4:
        mpfeedback_text="任务A训练已完成，点击进入任务B训练阶段"
        
    # keep track of which components have finished
    feedback_AComponents = [feedback_polygon_2, showresult1_2, taskscore_text1_2, feedback_button_2]
    for thisComponent in feedback_AComponents:
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
    
    # --- Run Routine "feedback_A" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_polygon_2* updates
        if feedback_polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_polygon_2.frameNStart = frameN  # exact frame index
            feedback_polygon_2.tStart = t  # local t and not account for scr refresh
            feedback_polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_polygon_2, 'tStartRefresh')  # time at next scr refresh
            feedback_polygon_2.setAutoDraw(True)
        
        # *showresult1_2* updates
        if showresult1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showresult1_2.frameNStart = frameN  # exact frame index
            showresult1_2.tStart = t  # local t and not account for scr refresh
            showresult1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showresult1_2, 'tStartRefresh')  # time at next scr refresh
            showresult1_2.setAutoDraw(True)
        if showresult1_2.status == STARTED:  # only update if drawing
            showresult1_2.setText(taskchose_text, log=False)
        
        # *taskscore_text1_2* updates
        if taskscore_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskscore_text1_2.frameNStart = frameN  # exact frame index
            taskscore_text1_2.tStart = t  # local t and not account for scr refresh
            taskscore_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskscore_text1_2, 'tStartRefresh')  # time at next scr refresh
            taskscore_text1_2.setAutoDraw(True)
        if taskscore_text1_2.status == STARTED:  # only update if drawing
            taskscore_text1_2.setText(taskscore_text, log=False)
        
        # *feedback_button_2* updates
        if feedback_button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_button_2.frameNStart = frameN  # exact frame index
            feedback_button_2.tStart = t  # local t and not account for scr refresh
            feedback_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_button_2, 'tStartRefresh')  # time at next scr refresh
            feedback_button_2.setAutoDraw(True)
        if feedback_button_2.status == STARTED:  # only update if drawing
            feedback_button_2.setText(mpfeedback_text, log=False)
        if feedback_button_2.status == STARTED:
            # check whether feedback_button_2 has been pressed
            if feedback_button_2.isClicked:
                if not feedback_button_2.wasClicked:
                    feedback_button_2.timesOn.append(feedback_button_2.buttonClock.getTime()) # store time of first click
                    feedback_button_2.timesOff.append(feedback_button_2.buttonClock.getTime()) # store time clicked until
                else:
                    feedback_button_2.timesOff[-1] = feedback_button_2.buttonClock.getTime() # update time clicked until
                if not feedback_button_2.wasClicked:
                    continueRoutine = False  # end routine when feedback_button_2 is clicked
                    None
                feedback_button_2.wasClicked = True  # if feedback_button_2 is still clicked next frame, it is not a new click
            else:
                feedback_button_2.wasClicked = False  # if feedback_button_2 is clicked next frame, it is a new click
        else:
            feedback_button_2.wasClicked = False  # if feedback_button_2 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_A" ---
    for thisComponent in feedback_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from feedback_code_2
    print(f"模式匹配第{rowcount}轮：{pattern_correct_count}")
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"模式匹配第{rowcount}轮：{pattern_correct_count}\n")
    file_handle.close()
    pattern_correct_count=0
    # the Routine "feedback_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 10.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=10.0, method='random', 
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
    
    # --- Prepare to start Routine "two_back_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
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
        
        # *two_back_introduce* updates
        if two_back_introduce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_back_introduce.frameNStart = frameN  # exact frame index
            two_back_introduce.tStart = t  # local t and not account for scr refresh
            two_back_introduce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_back_introduce, 'tStartRefresh')  # time at next scr refresh
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
    trials_3 = data.TrialHandler(nReps=32.0, method='random', 
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
            
            # *two_back_num_text* updates
            if two_back_num_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_num_text.frameNStart = frameN  # exact frame index
                two_back_num_text.tStart = t  # local t and not account for scr refresh
                two_back_num_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_num_text, 'tStartRefresh')  # time at next scr refresh
                two_back_num_text.setAutoDraw(True)
            if two_back_num_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_num_text.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_num_text.tStop = t  # not accounting for scr refresh
                    two_back_num_text.frameNStop = frameN  # exact frame index
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
                two_back_num_showtime_text.setAutoDraw(True)
            if two_back_num_showtime_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_num_showtime_text.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_num_showtime_text.tStop = t  # not accounting for scr refresh
                    two_back_num_showtime_text.frameNStop = frameN  # exact frame index
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
        n_back_correct_count+=1
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 32.0 repeats of 'trials_3'
    
    
    # --- Prepare to start Routine "feedback_B" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code_3
    taskresultB=round(30+70*stats.percentileofscore(resultB_range,n_back_correct_count )/100,2)
    taskchose_text=f"您选择执行的任务是：任务B"
    taskscore_text=f"您本轮任务的评分是：{taskresultB}"
    rowbcount+=1
    if rowbcount == 4:
        nbfeedback_text="任务B训练已完成，点击进入任务C训练阶段"
    # keep track of which components have finished
    feedback_BComponents = [feedback_polygon_3, showresult1_3, taskscore_text1_3, feedback_button_3]
    for thisComponent in feedback_BComponents:
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
    
    # --- Run Routine "feedback_B" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_polygon_3* updates
        if feedback_polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_polygon_3.frameNStart = frameN  # exact frame index
            feedback_polygon_3.tStart = t  # local t and not account for scr refresh
            feedback_polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_polygon_3, 'tStartRefresh')  # time at next scr refresh
            feedback_polygon_3.setAutoDraw(True)
        
        # *showresult1_3* updates
        if showresult1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showresult1_3.frameNStart = frameN  # exact frame index
            showresult1_3.tStart = t  # local t and not account for scr refresh
            showresult1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showresult1_3, 'tStartRefresh')  # time at next scr refresh
            showresult1_3.setAutoDraw(True)
        if showresult1_3.status == STARTED:  # only update if drawing
            showresult1_3.setText(taskchose_text, log=False)
        
        # *taskscore_text1_3* updates
        if taskscore_text1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskscore_text1_3.frameNStart = frameN  # exact frame index
            taskscore_text1_3.tStart = t  # local t and not account for scr refresh
            taskscore_text1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskscore_text1_3, 'tStartRefresh')  # time at next scr refresh
            taskscore_text1_3.setAutoDraw(True)
        if taskscore_text1_3.status == STARTED:  # only update if drawing
            taskscore_text1_3.setText(taskscore_text, log=False)
        
        # *feedback_button_3* updates
        if feedback_button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_button_3.frameNStart = frameN  # exact frame index
            feedback_button_3.tStart = t  # local t and not account for scr refresh
            feedback_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_button_3, 'tStartRefresh')  # time at next scr refresh
            feedback_button_3.setAutoDraw(True)
        if feedback_button_3.status == STARTED:  # only update if drawing
            feedback_button_3.setText(nbfeedback_text, log=False)
        if feedback_button_3.status == STARTED:
            # check whether feedback_button_3 has been pressed
            if feedback_button_3.isClicked:
                if not feedback_button_3.wasClicked:
                    feedback_button_3.timesOn.append(feedback_button_3.buttonClock.getTime()) # store time of first click
                    feedback_button_3.timesOff.append(feedback_button_3.buttonClock.getTime()) # store time clicked until
                else:
                    feedback_button_3.timesOff[-1] = feedback_button_3.buttonClock.getTime() # update time clicked until
                if not feedback_button_3.wasClicked:
                    continueRoutine = False  # end routine when feedback_button_3 is clicked
                    None
                feedback_button_3.wasClicked = True  # if feedback_button_3 is still clicked next frame, it is not a new click
            else:
                feedback_button_3.wasClicked = False  # if feedback_button_3 is clicked next frame, it is a new click
        else:
            feedback_button_3.wasClicked = False  # if feedback_button_3 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_BComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_B" ---
    for thisComponent in feedback_BComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from feedback_code_3
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"2back第{rowbcount}轮：{n_back_correct_count}\n")
    file_handle.close()
    n_back_correct_count=0
    
    # the Routine "feedback_B" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 10.0 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "vsintro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
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
        
        # *VS_intro_image* updates
        if VS_intro_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            VS_intro_image.frameNStart = frameN  # exact frame index
            VS_intro_image.tStart = t  # local t and not account for scr refresh
            VS_intro_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(VS_intro_image, 'tStartRefresh')  # time at next scr refresh
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
    # the Routine "vsintro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=32.0, method='random', 
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
        
        # --- Prepare to start Routine "visual_Search" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from VS_react_code
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
                trials_5.finished = True
                continueRoutine = False
                routineForceEnded = True
                
            
            # *VSimage* updates
            if VSimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VSimage.frameNStart = frameN  # exact frame index
                VSimage.tStart = t  # local t and not account for scr refresh
                VSimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VSimage, 'tStartRefresh')  # time at next scr refresh
                VSimage.setAutoDraw(True)
            if VSimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > VSimage.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    VSimage.tStop = t  # not accounting for scr refresh
                    VSimage.frameNStop = frameN  # exact frame index
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
                taskctime_text.setAutoDraw(True)
            if taskctime_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskctime_text.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    taskctime_text.tStop = t  # not accounting for scr refresh
                    taskctime_text.frameNStop = frameN  # exact frame index
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
        # store data for trials_5 (TrialHandler)
        trials_5.addData('key_resp.keys',key_resp.keys)
        trials_5.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials_5.addData('key_resp.rt', key_resp.rt)
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
        vs_correct_count+=1
        if key_resp.corr==1 and taskctime!=0:
            correct_feedback='正确'
            taskc_text_color='greenyellow'
            Temp_List_correct+=1
        elif key_resp.corr==0 and taskctime!=0:
            correct_feedback='错误'
            taskc_text_color='red'
            trials_5.finished = True
        elif taskctime==0:
            taskctime=0
            correct_feedback='时间到！！'
            taskc_text_color='red'
            trials_5.finished = True
            
            
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
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        thisExp.nextEntry()
        
    # completed 32.0 repeats of 'trials_5'
    
    
    # --- Prepare to start Routine "tackcnum_add" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    tackcnum_addComponents = []
    for thisComponent in tackcnum_addComponents:
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
    
    # --- Run Routine "tackcnum_add" ---
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
        for thisComponent in tackcnum_addComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tackcnum_add" ---
    for thisComponent in tackcnum_addComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_4
    taskcnum+=1
    Temp_List_correct=0
    # the Routine "tackcnum_add" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    taskresultC=round(30+70*stats.percentileofscore(resultB_range,vs_correct_count )/100,2)
    taskchose_text=f"您选择执行的任务是：任务C"
    taskscore_text=f"您本轮任务的评分是：{taskresultC}"
    rowccount+=1
    if rowccount == 4:
        vsfeedback_text="任务C训练已完成，点击结束训练阶段"
    # keep track of which components have finished
    feedbackComponents = [feedback_polygon, showresult1, taskscore_text1, feedback_button]
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
            feedback_polygon.setAutoDraw(True)
        
        # *showresult1* updates
        if showresult1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showresult1.frameNStart = frameN  # exact frame index
            showresult1.tStart = t  # local t and not account for scr refresh
            showresult1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showresult1, 'tStartRefresh')  # time at next scr refresh
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
            taskscore_text1.setAutoDraw(True)
        if taskscore_text1.status == STARTED:  # only update if drawing
            taskscore_text1.setText(taskscore_text, log=False)
        
        # *feedback_button* updates
        if feedback_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_button.frameNStart = frameN  # exact frame index
            feedback_button.tStart = t  # local t and not account for scr refresh
            feedback_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_button, 'tStartRefresh')  # time at next scr refresh
            feedback_button.setAutoDraw(True)
        if feedback_button.status == STARTED:  # only update if drawing
            feedback_button.setText(vsfeedback_text, log=False)
        if feedback_button.status == STARTED:
            # check whether feedback_button has been pressed
            if feedback_button.isClicked:
                if not feedback_button.wasClicked:
                    feedback_button.timesOn.append(feedback_button.buttonClock.getTime()) # store time of first click
                    feedback_button.timesOff.append(feedback_button.buttonClock.getTime()) # store time clicked until
                else:
                    feedback_button.timesOff[-1] = feedback_button.buttonClock.getTime() # update time clicked until
                if not feedback_button.wasClicked:
                    continueRoutine = False  # end routine when feedback_button is clicked
                    None
                feedback_button.wasClicked = True  # if feedback_button is still clicked next frame, it is not a new click
            else:
                feedback_button.wasClicked = False  # if feedback_button is clicked next frame, it is a new click
        else:
            feedback_button.wasClicked = False  # if feedback_button is clicked next frame, it is a new click
        
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
    trials_6.addData('feedback_button.numClicks', feedback_button.numClicks)
    if feedback_button.numClicks:
       trials_6.addData('feedback_button.timesOn', feedback_button.timesOn)
       trials_6.addData('feedback_button.timesOff', feedback_button.timesOff)
    else:
       trials_6.addData('feedback_button.timesOn', "")
       trials_6.addData('feedback_button.timesOff', "")
    # Run 'End Routine' code from feedback_code
    file_handle=open(f"result{expInfo['participant']}.txt",mode='a')
    file_handle.write(f"视觉搜索第{rowccount}轮：{vs_correct_count}\n")
    file_handle.close()
    vs_correct_count=0
    
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 10.0 repeats of 'trials_6'


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
