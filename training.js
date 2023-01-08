/***************** 
 * Training Test *
 *****************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'training';  // from the Builder filename that created this script
let expInfo = {
    'participant': '1',
    'bb': '1',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code
import * as pd from 'pandas';
import * as time from 'time';
import * as random from 'random';

// Run 'Before Experiment' code from code_5
/* Syntax Error: Fix Python code */
// Run 'Before Experiment' code from mp_choose_code

var taskatime;
function get_taskatime(sec) {
    taskatime = taskctimer.getTime();
    taskatime = Number.parseInt(Math.round((sec - taskatime), 0));
    return taskatime;
}
taskatime = "";
taskafeedback = "";
image_left = "model_pattern/0_1.png";
image_right = "model_pattern/0_2.png";
image_mid = "model_pattern/0_1.png";
pattern_count = 0;

// Run 'Before Experiment' code from mp_feedback_code
taska_text_color = "white";
pattern_correct_count = 0;

// Run 'Before Experiment' code from feedback_code_2
import * as random from 'random';
import {stats} from 'scipy';
var mpfeedback_text, resultA_range, result_list, rowcount, taskchose_text, taskscore_text;
taskchose_text = "";
taskscore_text = "";
mpfeedback_text = "\u70b9\u51fb\u8fdb\u5165\u4e0b\u4e00\u8f6e\u5c1d\u8bd5";
rowcount = 0;
result_list = [];
resultA_range = pd.read_excel("\u9884\u5b9e\u9a8c\u6570\u636e.xlsx");
resultA_range = resultA_range["mp"].dropna();

// Run 'Before Experiment' code from two_back_num_react_code

var taskbtime;
function get_taskbtime(sec) {
    var taskbtime;
    taskbtime = taskctimer.getTime();
    taskbtime = Number.parseInt(Math.round((sec - taskbtime), 0));
    return taskbtime;
}

// Run 'Before Experiment' code from two_back_num_feedback_code
two_back_feedback_text = "";
taskb_text_color = "white";
taskbtime = "";
n_back_correct_count = 0;

// Run 'Before Experiment' code from feedback_code_3
import * as random from 'random';
var nbfeedback_text, resultB_range, rowbcount, taskchose_text, taskscore_text;
taskchose_text = "";
taskscore_text = "";
rowbcount = 0;
nbfeedback_text = "\u70b9\u51fb\u8fdb\u5165\u4e0b\u4e00\u8f6e\u5c1d\u8bd5";
resultB_range = pd.read_excel("\u9884\u5b9e\u9a8c\u6570\u636e.xlsx");
resultB_range = resultB_range["nb"].dropna();

// Run 'Before Experiment' code from VS_react_code
import * as psychopy from 'psychopy';
var taskctimer;
taskctimer = new psychopy.core.Clock();

var taskctime;
function get_taskctime(esc) {
    var taskctime;
    taskctime = taskctimer.getTime();
    taskctime = Number.parseInt(Math.round((esc - taskctime), 0));
    return taskctime;
}

// Run 'Before Experiment' code from VS_feedback_code
taskcnum = 0;
correct_feedback = "";
react = pd.read_excel("visual_search_pic_answer.xlsx");
vsdata = react.loc[taskcnum];
vsdata = vsdata.slice(1);
Temp_List = np.array(vsdata).tolist();
Temp_List_correct = 0;
taskc_text_color = "white";
vs_correct_count = 0;

// Run 'Before Experiment' code from feedback_code
import * as random from 'random';
var resultC_range, rowccount, taskchose_text, taskscore_text, vsfeedback_text;
taskchose_text = "";
taskscore_text = "";
vsfeedback_text = "\u70b9\u51fb\u8fdb\u5165\u4e0b\u4e00\u8f6e\u5c1d\u8bd5";
rowccount = 0;
resultC_range = pd.read_excel("\u9884\u5b9e\u9a8c\u6570\u636e.xlsx");
resultC_range = resultC_range["vs"].dropna();

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setpRoutineBegin());
flowScheduler.add(setpRoutineEachFrame());
flowScheduler.add(setpRoutineEnd());
flowScheduler.add(training_introRoutineBegin());
flowScheduler.add(training_introRoutineEachFrame());
flowScheduler.add(training_introRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
const trials_6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_6LoopBegin(trials_6LoopScheduler));
flowScheduler.add(trials_6LoopScheduler);
flowScheduler.add(trials_6LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': '指导语/测验总指导语/测验总指导语.png', 'path': '指导语/测验总指导语/测验总指导语.png'},
    {'name': 'mp说明.png', 'path': 'mp说明.png'},
    {'name': 'nb说明.png', 'path': 'nb说明.png'},
    {'name': 'VS指导语.png', 'path': 'VS指导语.png'},
    {'name': '指导语/测验总指导语/训练阶段指导语.png', 'path': '指导语/测验总指导语/训练阶段指导语.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var setpClock;
var text_4;
var image;
var firstbutton_2;
var training_introClock;
var image_2;
var key_resp_7;
var model_pattern_introClock;
var model_pattern_introduce;
var key_resp_6;
var model_patternClock;
var mp_image_left;
var mp_image_right;
var mp_image_mid;
var key_resp_5;
var mp_showtime1;
var mpfeedbackClock;
var mp_image_left2;
var mp_image_right2;
var mp_image_mid2;
var mp_feedback;
var feedback_AClock;
var feedback_polygon_2;
var showresult1_2;
var taskscore_text1_2;
var feedback_button_2;
var two_back_introClock;
var key_resp_4;
var two_back_introduce;
var n_backClock;
var two_back_num_text;
var key_resp_3;
var two_back_num_showtime_text;
var n_backfeedbackClock;
var two_back_feedback_text1;
var two_back_showtime_text2;
var feedback_BClock;
var feedback_polygon_3;
var showresult1_3;
var taskscore_text1_3;
var feedback_button_3;
var vsintroClock;
var VS_intro_image;
var key_resp_2;
var visual_SearchClock;
var VSimage_path;
var VSimage;
var key_resp;
var taskctime_text;
var vsfeedbackClock;
var VSimage_2;
var taskc_text;
var taskctime_text2;
var tackcnum_addClock;
var feedbackClock;
var feedback_polygon;
var showresult1;
var taskscore_text1;
var feedback_button;
var endClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "setp"
  setpClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '您好，欢迎您参加本次实验，本实验主要考察您的决策能力，实验流程由一个训练阶段以及四个正式阶段组成，预计用时为45分钟，请点击下方按钮开启本次实验\n',
    font: 'Microsoft YaHei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : '指导语/测验总指导语/测验总指导语.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.92, 1.08],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  firstbutton_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'firstbutton_2',
    text: '欢迎参与此次实验，点击此处开始吧！',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.4)],
    letterHeight: 0.05,
    size: [0.9, 0.1]
  });
  firstbutton_2.clock = new util.Clock();
  
  // Initialize components for Routine "training_intro"
  training_introClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : '指导语/测验总指导语/训练阶段指导语.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.92, 1.08],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "model_pattern_intro"
  model_pattern_introClock = new util.Clock();
  model_pattern_introduce = new visual.ImageStim({
    win : psychoJS.window,
    name : 'model_pattern_introduce', units : undefined, 
    image : 'mp说明.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.92, 1.08],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "model_pattern"
  model_patternClock = new util.Clock();
  mp_image_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_left', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mp_image_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_right', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mp_image_mid = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_mid', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mp_showtime1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'mp_showtime1',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0.7, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "mpfeedback"
  mpfeedbackClock = new util.Clock();
  mp_image_left2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_left2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mp_image_right2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_right2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  mp_image_mid2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mp_image_mid2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mp_feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'mp_feedback',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "feedback_A"
  feedback_AClock = new util.Clock();
  feedback_polygon_2 = new visual.Rect ({
    win: psychoJS.window, name: 'feedback_polygon_2', 
    width: [1.4, 0.9][0], height: [1.4, 0.9][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.7098, 0.2941, (- 0.749)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  showresult1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'showresult1_2',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  taskscore_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskscore_text1_2',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  feedback_button_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'feedback_button_2',
    text: '',
    fillColor: [0.0824, (- 0.6627), 0.7725],
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.35)],
    letterHeight: 0.03,
    size: [0.8, 0.1]
  });
  feedback_button_2.clock = new util.Clock();
  
  // Initialize components for Routine "two_back_intro"
  two_back_introClock = new util.Clock();
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from var_2b_begin_code
  /* Syntax Error: Fix Python code */
  two_back_introduce = new visual.ImageStim({
    win : psychoJS.window,
    name : 'two_back_introduce', units : undefined, 
    image : 'nb说明.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.92, 1.08],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "n_back"
  n_backClock = new util.Clock();
  // Run 'Begin Experiment' code from two_back_num_react_code
  /* Syntax Error: Fix Python code */
  two_back_num_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_back_num_text',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  two_back_num_showtime_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_back_num_showtime_text',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0.7, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "n_backfeedback"
  n_backfeedbackClock = new util.Clock();
  two_back_feedback_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_back_feedback_text1',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  two_back_showtime_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_back_showtime_text2',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0.7, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "feedback_B"
  feedback_BClock = new util.Clock();
  feedback_polygon_3 = new visual.Rect ({
    win: psychoJS.window, name: 'feedback_polygon_3', 
    width: [1.4, 0.9][0], height: [1.4, 0.9][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.7098, 0.2941, (- 0.749)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  showresult1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'showresult1_3',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  taskscore_text1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskscore_text1_3',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  feedback_button_3 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'feedback_button_3',
    text: '',
    fillColor: [0.0824, (- 0.6627), 0.7725],
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.35)],
    letterHeight: 0.03,
    size: [0.6, 0.1]
  });
  feedback_button_3.clock = new util.Clock();
  
  // Initialize components for Routine "vsintro"
  vsintroClock = new util.Clock();
  VS_intro_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'VS_intro_image', units : undefined, 
    image : 'VS指导语.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.92, 1.08],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "visual_Search"
  visual_SearchClock = new util.Clock();
  // Run 'Begin Experiment' code from VS_react_code
  VSimage_path = `visual_search_pic/${taskcnum}.png`;
  
  VSimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'VSimage', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  taskctime_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskctime_text',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0.7, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "vsfeedback"
  vsfeedbackClock = new util.Clock();
  // Run 'Begin Experiment' code from VS_feedback_code
  /* Syntax Error: Fix Python code */
  VSimage_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'VSimage_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  taskc_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskc_text',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  taskctime_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskctime_text2',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0.7, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "tackcnum_add"
  tackcnum_addClock = new util.Clock();
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_polygon = new visual.Rect ({
    win: psychoJS.window, name: 'feedback_polygon', 
    width: [1.4, 0.9][0], height: [1.4, 0.9][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0.7098, 0.2941, (- 0.749)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  showresult1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'showresult1',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  taskscore_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'taskscore_text1',
    text: '',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0.0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  feedback_button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'feedback_button',
    text: '',
    fillColor: [0.0824, (- 0.6627), 0.7725],
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.35)],
    letterHeight: 0.03,
    size: [0.6, 0.1]
  });
  feedback_button.clock = new util.Clock();
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '恭喜你完成训练阶段！！',
    font: 'MicroSoft YaHei',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var setpComponents;
function setpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'setp' ---
    t = 0;
    setpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setpComponents = [];
    setpComponents.push(text_4);
    setpComponents.push(image);
    setpComponents.push(firstbutton_2);
    
    for (const thisComponent of setpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var newsave;
function setpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'setp' ---
    // get current time
    t = setpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *firstbutton_2* updates
    if (t >= 0 && firstbutton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      firstbutton_2.tStart = t;  // (not accounting for frame time here)
      firstbutton_2.frameNStart = frameN;  // exact frame index
      
      firstbutton_2.setAutoDraw(true);
    }

    if (firstbutton_2.status === PsychoJS.Status.STARTED) {
      // check whether firstbutton_2 has been pressed
      if (firstbutton_2.isClicked) {
        if (!firstbutton_2.wasClicked) {
          // store time of first click
          firstbutton_2.timesOn.push(firstbutton_2.clock.getTime());
          firstbutton_2.numClicks += 1;
          // store time clicked until
          firstbutton_2.timesOff.push(firstbutton_2.clock.getTime());
        } else {
          // update time clicked until;
          firstbutton_2.timesOff[firstbutton_2.timesOff.length - 1] = firstbutton_2.clock.getTime();
        }
        if (!firstbutton_2.wasClicked) {
          // end routine when firstbutton_2 is clicked
          continueRoutine = false;
          newsave = time.perf_counter();
        }
        // if firstbutton_2 is still clicked next frame, it is not a new click
        firstbutton_2.wasClicked = true;
      } else {
        // if firstbutton_2 is clicked next frame, it is a new click
        firstbutton_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if firstbutton_2 hasn't started / has finished
      firstbutton_2.clock.reset();
      // if firstbutton_2 is clicked next frame, it is a new click
      firstbutton_2.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setpComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var timecoder;
function setpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'setp' ---
    for (const thisComponent of setpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code
    timecoder = t;
    
    psychoJS.experiment.addData('firstbutton_2.numClicks', firstbutton_2.numClicks);
    psychoJS.experiment.addData('firstbutton_2.timesOn', firstbutton_2.timesOn);
    psychoJS.experiment.addData('firstbutton_2.timesOff', firstbutton_2.timesOff);
    // the Routine "setp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_7_allKeys;
var training_introComponents;
function training_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'training_intro' ---
    t = 0;
    training_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    training_introComponents = [];
    training_introComponents.push(image_2);
    training_introComponents.push(key_resp_7);
    
    for (const thisComponent of training_introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function training_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'training_intro' ---
    // get current time
    t = training_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_5
    /* Syntax Error: Fix Python code */
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of training_introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function training_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'training_intro' ---
    for (const thisComponent of training_introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "training_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(model_pattern_introRoutineBegin(snapshot));
      trials_2LoopScheduler.add(model_pattern_introRoutineEachFrame());
      trials_2LoopScheduler.add(model_pattern_introRoutineEnd(snapshot));
      const trials_1LoopScheduler = new Scheduler(psychoJS);
      trials_2LoopScheduler.add(trials_1LoopBegin(trials_1LoopScheduler, snapshot));
      trials_2LoopScheduler.add(trials_1LoopScheduler);
      trials_2LoopScheduler.add(trials_1LoopEnd);
      trials_2LoopScheduler.add(feedback_ARoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedback_ARoutineEachFrame());
      trials_2LoopScheduler.add(feedback_ARoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_1;
function trials_1LoopBegin(trials_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 32, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_1'
    });
    psychoJS.experiment.addLoop(trials_1); // add the loop to the experiment
    currentLoop = trials_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_1 of trials_1) {
      snapshot = trials_1.getSnapshot();
      trials_1LoopScheduler.add(importConditions(snapshot));
      trials_1LoopScheduler.add(model_patternRoutineBegin(snapshot));
      trials_1LoopScheduler.add(model_patternRoutineEachFrame());
      trials_1LoopScheduler.add(model_patternRoutineEnd(snapshot));
      trials_1LoopScheduler.add(mpfeedbackRoutineBegin(snapshot));
      trials_1LoopScheduler.add(mpfeedbackRoutineEachFrame());
      trials_1LoopScheduler.add(mpfeedbackRoutineEnd(snapshot));
      trials_1LoopScheduler.add(trials_1LoopEndIteration(trials_1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_4 of trials_4) {
      snapshot = trials_4.getSnapshot();
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(two_back_introRoutineBegin(snapshot));
      trials_4LoopScheduler.add(two_back_introRoutineEachFrame());
      trials_4LoopScheduler.add(two_back_introRoutineEnd(snapshot));
      const trials_3LoopScheduler = new Scheduler(psychoJS);
      trials_4LoopScheduler.add(trials_3LoopBegin(trials_3LoopScheduler, snapshot));
      trials_4LoopScheduler.add(trials_3LoopScheduler);
      trials_4LoopScheduler.add(trials_3LoopEnd);
      trials_4LoopScheduler.add(feedback_BRoutineBegin(snapshot));
      trials_4LoopScheduler.add(feedback_BRoutineEachFrame());
      trials_4LoopScheduler.add(feedback_BRoutineEnd(snapshot));
      trials_4LoopScheduler.add(trials_4LoopEndIteration(trials_4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 32, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(n_backRoutineBegin(snapshot));
      trials_3LoopScheduler.add(n_backRoutineEachFrame());
      trials_3LoopScheduler.add(n_backRoutineEnd(snapshot));
      trials_3LoopScheduler.add(n_backfeedbackRoutineBegin(snapshot));
      trials_3LoopScheduler.add(n_backfeedbackRoutineEachFrame());
      trials_3LoopScheduler.add(n_backfeedbackRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_6;
function trials_6LoopBegin(trials_6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_6'
    });
    psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
    currentLoop = trials_6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_6 of trials_6) {
      snapshot = trials_6.getSnapshot();
      trials_6LoopScheduler.add(importConditions(snapshot));
      trials_6LoopScheduler.add(vsintroRoutineBegin(snapshot));
      trials_6LoopScheduler.add(vsintroRoutineEachFrame());
      trials_6LoopScheduler.add(vsintroRoutineEnd(snapshot));
      const trials_5LoopScheduler = new Scheduler(psychoJS);
      trials_6LoopScheduler.add(trials_5LoopBegin(trials_5LoopScheduler, snapshot));
      trials_6LoopScheduler.add(trials_5LoopScheduler);
      trials_6LoopScheduler.add(trials_5LoopEnd);
      trials_6LoopScheduler.add(tackcnum_addRoutineBegin(snapshot));
      trials_6LoopScheduler.add(tackcnum_addRoutineEachFrame());
      trials_6LoopScheduler.add(tackcnum_addRoutineEnd(snapshot));
      trials_6LoopScheduler.add(feedbackRoutineBegin(snapshot));
      trials_6LoopScheduler.add(feedbackRoutineEachFrame());
      trials_6LoopScheduler.add(feedbackRoutineEnd(snapshot));
      trials_6LoopScheduler.add(trials_6LoopEndIteration(trials_6LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 32, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_5'
    });
    psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
    currentLoop = trials_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_5 of trials_5) {
      snapshot = trials_5.getSnapshot();
      trials_5LoopScheduler.add(importConditions(snapshot));
      trials_5LoopScheduler.add(visual_SearchRoutineBegin(snapshot));
      trials_5LoopScheduler.add(visual_SearchRoutineEachFrame());
      trials_5LoopScheduler.add(visual_SearchRoutineEnd(snapshot));
      trials_5LoopScheduler.add(vsfeedbackRoutineBegin(snapshot));
      trials_5LoopScheduler.add(vsfeedbackRoutineEachFrame());
      trials_5LoopScheduler.add(vsfeedbackRoutineEnd(snapshot));
      trials_5LoopScheduler.add(trials_5LoopEndIteration(trials_5LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_6LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _key_resp_6_allKeys;
var model_pattern_introComponents;
function model_pattern_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'model_pattern_intro' ---
    t = 0;
    model_pattern_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from model_pattern_begin_code
    /* Syntax Error: Fix Python code */
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    model_pattern_introComponents = [];
    model_pattern_introComponents.push(model_pattern_introduce);
    model_pattern_introComponents.push(key_resp_6);
    
    for (const thisComponent of model_pattern_introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function model_pattern_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'model_pattern_intro' ---
    // get current time
    t = model_pattern_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *model_pattern_introduce* updates
    if (t >= 0.0 && model_pattern_introduce.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      model_pattern_introduce.tStart = t;  // (not accounting for frame time here)
      model_pattern_introduce.frameNStart = frameN;  // exact frame index
      
      model_pattern_introduce.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of model_pattern_introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function model_pattern_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'model_pattern_intro' ---
    for (const thisComponent of model_pattern_introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from model_pattern_begin_code
    taskctimer.reset();
    
    key_resp_6.stop();
    // the Routine "model_pattern_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pattern_count;
var LR;
var mp_correct;
var image_left;
var image_right;
var image_mid;
var _key_resp_5_allKeys;
var model_patternComponents;
function model_patternRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'model_pattern' ---
    t = 0;
    model_patternClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from mp_choose_code
    pattern_count = random.randint(1, 9999);
    LR = random.randint(1, 2);
    if ((LR === 1)) {
        mp_correct = "j";
    } else {
        mp_correct = "f";
    }
    image_left = `model_pattern/${pattern_count}_1.png`;
    image_right = `model_pattern/${pattern_count}_2.png`;
    image_mid = `model_pattern/${pattern_count}_${LR}.png`;
    
    mp_image_left.setImage(image_left);
    mp_image_right.setImage(image_right);
    mp_image_mid.setImage(image_mid);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    model_patternComponents = [];
    model_patternComponents.push(mp_image_left);
    model_patternComponents.push(mp_image_right);
    model_patternComponents.push(mp_image_mid);
    model_patternComponents.push(key_resp_5);
    model_patternComponents.push(mp_showtime1);
    
    for (const thisComponent of model_patternComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var routineForceEnded;
function model_patternRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'model_pattern' ---
    // get current time
    t = model_patternClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from mp_choose_code
    taskatime = get_taskatime(30);
    if ((taskatime === 0)) {
        continueRoutine = false;
        routineForceEnded = true;
        trials_1.finished = true;
    }
    
    
    // *mp_image_left* updates
    if (t >= 0.0 && mp_image_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_left.tStart = t;  // (not accounting for frame time here)
      mp_image_left.frameNStart = frameN;  // exact frame index
      
      mp_image_left.setAutoDraw(true);
    }

    
    // *mp_image_right* updates
    if (t >= 0.0 && mp_image_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_right.tStart = t;  // (not accounting for frame time here)
      mp_image_right.frameNStart = frameN;  // exact frame index
      
      mp_image_right.setAutoDraw(true);
    }

    
    // *mp_image_mid* updates
    if (t >= 0.0 && mp_image_mid.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_mid.tStart = t;  // (not accounting for frame time here)
      mp_image_mid.frameNStart = frameN;  // exact frame index
      
      mp_image_mid.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_5.keys == mp_correct) {
            key_resp_5.corr = 1;
        } else {
            key_resp_5.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *mp_showtime1* updates
    if (t >= 0.0 && mp_showtime1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_showtime1.tStart = t;  // (not accounting for frame time here)
      mp_showtime1.frameNStart = frameN;  // exact frame index
      
      mp_showtime1.setAutoDraw(true);
    }

    
    if (mp_showtime1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mp_showtime1.setText(taskatime, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of model_patternComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function model_patternRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'model_pattern' ---
    for (const thisComponent of model_patternComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_5.keys === undefined) {
      if (['None','none',undefined].includes(mp_correct)) {
         key_resp_5.corr = 1;  // correct non-response
      } else {
         key_resp_5.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    psychoJS.experiment.addData('key_resp_5.corr', key_resp_5.corr);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "model_pattern" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskafeedback;
var taska_text_color;
var mpfeedbackComponents;
function mpfeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mpfeedback' ---
    t = 0;
    mpfeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    mp_image_left2.setImage(image_left);
    mp_image_right2.setImage(image_right);
    mp_image_mid2.setImage(image_mid);
    // Run 'Begin Routine' code from mp_feedback_code
    if ((key_resp_5.corr !== 1)) {
        taskafeedback = "\u9519\u8bef";
        taska_text_color = "red";
        trials_1.finished = true;
    } else {
        if ((key_resp_5.corr === 1)) {
            taskafeedback = "\u6b63\u786e";
            taska_text_color = "greenyellow";
        }
    }
    pattern_correct_count += 1;
    
    // keep track of which components have finished
    mpfeedbackComponents = [];
    mpfeedbackComponents.push(mp_image_left2);
    mpfeedbackComponents.push(mp_image_right2);
    mpfeedbackComponents.push(mp_image_mid2);
    mpfeedbackComponents.push(mp_feedback);
    
    for (const thisComponent of mpfeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function mpfeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mpfeedback' ---
    // get current time
    t = mpfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mp_image_left2* updates
    if (t >= 0.0 && mp_image_left2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_left2.tStart = t;  // (not accounting for frame time here)
      mp_image_left2.frameNStart = frameN;  // exact frame index
      
      mp_image_left2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mp_image_left2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mp_image_left2.setAutoDraw(false);
    }
    
    // *mp_image_right2* updates
    if (t >= 0.0 && mp_image_right2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_right2.tStart = t;  // (not accounting for frame time here)
      mp_image_right2.frameNStart = frameN;  // exact frame index
      
      mp_image_right2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mp_image_right2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mp_image_right2.setAutoDraw(false);
    }
    
    // *mp_image_mid2* updates
    if (t >= 0.0 && mp_image_mid2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_image_mid2.tStart = t;  // (not accounting for frame time here)
      mp_image_mid2.frameNStart = frameN;  // exact frame index
      
      mp_image_mid2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mp_image_mid2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mp_image_mid2.setAutoDraw(false);
    }
    
    // *mp_feedback* updates
    if (t >= 0.0 && mp_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mp_feedback.tStart = t;  // (not accounting for frame time here)
      mp_feedback.frameNStart = frameN;  // exact frame index
      
      mp_feedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mp_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mp_feedback.setAutoDraw(false);
    }
    
    if (mp_feedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mp_feedback.setColor(new util.Color(taska_text_color), false);
      mp_feedback.setText(taskafeedback, false);
    }
    // Run 'Each Frame' code from mp_feedback_code
    taskatime = get_taskatime(30);
    if ((taskatime === 0)) {
        continueRoutine = false;
        routineForceEnded = true;
        trials_1.finished = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of mpfeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mpfeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mpfeedback' ---
    for (const thisComponent of mpfeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskresultA;
var taskchose_text;
var taskscore_text;
var mpfeedback_text;
var feedback_AComponents;
function feedback_ARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_A' ---
    t = 0;
    feedback_AClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code_2
    taskresultA = Math.round((30 + ((70 * stats.percentileofscore(resultA_range, pattern_correct_count)) / 100)), 2);
    taskchose_text = `您选择执行的任务是：任务A`;
    taskscore_text = `您本轮任务的评分是：${taskresultA}`;
    rowcount += 1;
    if ((rowcount === 4)) {
        mpfeedback_text = "\u4efb\u52a1A\u8bad\u7ec3\u5df2\u5b8c\u6210\uff0c\u70b9\u51fb\u8fdb\u5165\u4efb\u52a1B\u8bad\u7ec3\u9636\u6bb5";
    }
    
    // keep track of which components have finished
    feedback_AComponents = [];
    feedback_AComponents.push(feedback_polygon_2);
    feedback_AComponents.push(showresult1_2);
    feedback_AComponents.push(taskscore_text1_2);
    feedback_AComponents.push(feedback_button_2);
    
    for (const thisComponent of feedback_AComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_ARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_A' ---
    // get current time
    t = feedback_AClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_polygon_2* updates
    if (t >= 0.0 && feedback_polygon_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_polygon_2.tStart = t;  // (not accounting for frame time here)
      feedback_polygon_2.frameNStart = frameN;  // exact frame index
      
      feedback_polygon_2.setAutoDraw(true);
    }

    
    // *showresult1_2* updates
    if (t >= 0.0 && showresult1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      showresult1_2.tStart = t;  // (not accounting for frame time here)
      showresult1_2.frameNStart = frameN;  // exact frame index
      
      showresult1_2.setAutoDraw(true);
    }

    
    if (showresult1_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      showresult1_2.setText(taskchose_text, false);
    }
    
    // *taskscore_text1_2* updates
    if (t >= 0.0 && taskscore_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskscore_text1_2.tStart = t;  // (not accounting for frame time here)
      taskscore_text1_2.frameNStart = frameN;  // exact frame index
      
      taskscore_text1_2.setAutoDraw(true);
    }

    
    if (taskscore_text1_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      taskscore_text1_2.setText(taskscore_text, false);
    }
    
    // *feedback_button_2* updates
    if (t >= 0 && feedback_button_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_button_2.tStart = t;  // (not accounting for frame time here)
      feedback_button_2.frameNStart = frameN;  // exact frame index
      
      feedback_button_2.setAutoDraw(true);
    }

    
    if (feedback_button_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      feedback_button_2.setText(mpfeedback_text, false);
    }
    if (feedback_button_2.status === PsychoJS.Status.STARTED) {
      // check whether feedback_button_2 has been pressed
      if (feedback_button_2.isClicked) {
        if (!feedback_button_2.wasClicked) {
          // store time of first click
          feedback_button_2.timesOn.push(feedback_button_2.clock.getTime());
          feedback_button_2.numClicks += 1;
          // store time clicked until
          feedback_button_2.timesOff.push(feedback_button_2.clock.getTime());
        } else {
          // update time clicked until;
          feedback_button_2.timesOff[feedback_button_2.timesOff.length - 1] = feedback_button_2.clock.getTime();
        }
        if (!feedback_button_2.wasClicked) {
          // end routine when feedback_button_2 is clicked
          continueRoutine = false;
        }
        // if feedback_button_2 is still clicked next frame, it is not a new click
        feedback_button_2.wasClicked = true;
      } else {
        // if feedback_button_2 is clicked next frame, it is a new click
        feedback_button_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if feedback_button_2 hasn't started / has finished
      feedback_button_2.clock.reset();
      // if feedback_button_2 is clicked next frame, it is a new click
      feedback_button_2.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_AComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var file_handle;
var pattern_correct_count;
function feedback_ARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_A' ---
    for (const thisComponent of feedback_AComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_button_2.numClicks', feedback_button_2.numClicks);
    psychoJS.experiment.addData('feedback_button_2.timesOn', feedback_button_2.timesOn);
    psychoJS.experiment.addData('feedback_button_2.timesOff', feedback_button_2.timesOff);
    // Run 'End Routine' code from feedback_code_2
    console.log(`模式匹配第${rowcount}轮：${pattern_correct_count}`);
    file_handle = open(`预实验数据未放入/result${expInfo["participant"]}.txt`, {"mode": "a"});
    file_handle.write(`模式匹配第${rowcount}轮：${pattern_correct_count}
    `);
    file_handle.close();
    pattern_correct_count = 0;
    
    // the Routine "feedback_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_4_allKeys;
var two_back_introComponents;
function two_back_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'two_back_intro' ---
    t = 0;
    two_back_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    two_back_introComponents = [];
    two_back_introComponents.push(key_resp_4);
    two_back_introComponents.push(two_back_introduce);
    
    for (const thisComponent of two_back_introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function two_back_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'two_back_intro' ---
    // get current time
    t = two_back_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *two_back_introduce* updates
    if (t >= 0.0 && two_back_introduce.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_back_introduce.tStart = t;  // (not accounting for frame time here)
      two_back_introduce.frameNStart = frameN;  // exact frame index
      
      two_back_introduce.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of two_back_introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var two_back_list;
var two_back_count;
var two_back_correct;
var two_back_feedback_text;
var two_back_num;
var two_back_img;
function two_back_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'two_back_intro' ---
    for (const thisComponent of two_back_introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_4.stop();
    // Run 'End Routine' code from var_2b_begin_code
    taskctimer.reset();
    two_back_list = [];
    two_back_count = 0;
    two_back_correct = "";
    two_back_feedback_text = "";
    two_back_num = random.randint(0, 9);
    two_back_img = `pic/${two_back_num}.png`;
    
    // the Routine "two_back_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var n_backComponents;
function n_backRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'n_back' ---
    t = 0;
    n_backClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from two_back_num_react_code
    two_back_num = random.randint(0, 9);
    two_back_list.push(two_back_num);
    if ((two_back_count >= 2)) {
        two_back_correct = two_back_list[(two_back_count - 2)];
        if ((two_back_count === 2)) {
            taskctimer.reset();
        }
    }
    
    two_back_num_text.setText(two_back_num);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    n_backComponents = [];
    n_backComponents.push(two_back_num_text);
    n_backComponents.push(key_resp_3);
    n_backComponents.push(two_back_num_showtime_text);
    
    for (const thisComponent of n_backComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var duration;
function n_backRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'n_back' ---
    // get current time
    t = n_backClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from two_back_num_react_code
    if ((two_back_count < 2)) {
        taskbtime = 30;
        duration = 2;
    } else {
        if ((two_back_count >= 2)) {
            taskbtime = get_taskbtime(30);
            duration = 30;
        }
    }
    if ((taskbtime === 0)) {
        taskbtime = 0;
        continueRoutine = false;
        routineForceEnded = true;
    }
    
    
    // *two_back_num_text* updates
    if (t >= 0.0 && two_back_num_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_back_num_text.tStart = t;  // (not accounting for frame time here)
      two_back_num_text.frameNStart = frameN;  // exact frame index
      
      two_back_num_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (two_back_num_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      two_back_num_text.setAutoDraw(false);
    }
    
    if (two_back_num_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      two_back_num_text.setColor(new util.Color([1.0, 1.0, 1.0]), false);
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_3.keys == two_back_correct) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *two_back_num_showtime_text* updates
    if (t >= 0.0 && two_back_num_showtime_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_back_num_showtime_text.tStart = t;  // (not accounting for frame time here)
      two_back_num_showtime_text.frameNStart = frameN;  // exact frame index
      
      two_back_num_showtime_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (two_back_num_showtime_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      two_back_num_showtime_text.setAutoDraw(false);
    }
    
    if (two_back_num_showtime_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      two_back_num_showtime_text.setText(taskbtime, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of n_backComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function n_backRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'n_back' ---
    for (const thisComponent of n_backComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from two_back_num_react_code
    two_back_count += 1;
    
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(two_back_correct)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "n_back" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskb_text_color;
var n_backfeedbackComponents;
function n_backfeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'n_backfeedback' ---
    t = 0;
    n_backfeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from two_back_num_feedback_code
    if ((((key_resp_3.corr !== 1) && (two_back_count >= 3)) && (taskbtime !== 0))) {
        two_back_feedback_text = "\u9519\u8bef";
        taskb_text_color = "red";
        trials_3.finished = true;
    } else {
        if ((((key_resp_3.corr === 1) && (two_back_count >= 3)) && (taskbtime !== 0))) {
            two_back_feedback_text = "+";
            taskb_text_color = "white";
        } else {
            if ((taskbtime === 0)) {
                two_back_feedback_text = "\u65f6\u95f4\u5230\uff01";
                taskb_text_color = "red";
                trials_3.finished = true;
            }
        }
    }
    n_back_correct_count += 1;
    
    two_back_feedback_text1.setColor(new util.Color(taskb_text_color));
    two_back_feedback_text1.setText(two_back_feedback_text);
    two_back_showtime_text2.setColor(new util.Color('white'));
    two_back_showtime_text2.setText(taskbtime);
    // keep track of which components have finished
    n_backfeedbackComponents = [];
    n_backfeedbackComponents.push(two_back_feedback_text1);
    n_backfeedbackComponents.push(two_back_showtime_text2);
    
    for (const thisComponent of n_backfeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function n_backfeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'n_backfeedback' ---
    // get current time
    t = n_backfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from two_back_num_feedback_code
    if ((two_back_count < 2)) {
        taskbtime = 30;
    } else {
        if ((two_back_count >= 2)) {
            taskbtime = get_taskbtime(30);
        }
    }
    
    
    // *two_back_feedback_text1* updates
    if (t >= 0.0 && two_back_feedback_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_back_feedback_text1.tStart = t;  // (not accounting for frame time here)
      two_back_feedback_text1.frameNStart = frameN;  // exact frame index
      
      two_back_feedback_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (two_back_feedback_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      two_back_feedback_text1.setAutoDraw(false);
    }
    
    // *two_back_showtime_text2* updates
    if (t >= 0.0 && two_back_showtime_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_back_showtime_text2.tStart = t;  // (not accounting for frame time here)
      two_back_showtime_text2.frameNStart = frameN;  // exact frame index
      
      two_back_showtime_text2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (two_back_showtime_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      two_back_showtime_text2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of n_backfeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function n_backfeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'n_backfeedback' ---
    for (const thisComponent of n_backfeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskresultB;
var nbfeedback_text;
var feedback_BComponents;
function feedback_BRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_B' ---
    t = 0;
    feedback_BClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code_3
    taskresultB = Math.round((30 + ((70 * stats.percentileofscore(resultB_range, n_back_correct_count)) / 100)), 2);
    taskchose_text = `您选择执行的任务是：任务B`;
    taskscore_text = `您本轮任务的评分是：${taskresultB}`;
    rowbcount += 1;
    if ((rowbcount === 4)) {
        nbfeedback_text = "\u4efb\u52a1B\u8bad\u7ec3\u5df2\u5b8c\u6210\uff0c\u70b9\u51fb\u8fdb\u5165\u4efb\u52a1C\u8bad\u7ec3\u9636\u6bb5";
    }
    
    // keep track of which components have finished
    feedback_BComponents = [];
    feedback_BComponents.push(feedback_polygon_3);
    feedback_BComponents.push(showresult1_3);
    feedback_BComponents.push(taskscore_text1_3);
    feedback_BComponents.push(feedback_button_3);
    
    for (const thisComponent of feedback_BComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback_BRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_B' ---
    // get current time
    t = feedback_BClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_polygon_3* updates
    if (t >= 0.0 && feedback_polygon_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_polygon_3.tStart = t;  // (not accounting for frame time here)
      feedback_polygon_3.frameNStart = frameN;  // exact frame index
      
      feedback_polygon_3.setAutoDraw(true);
    }

    
    // *showresult1_3* updates
    if (t >= 0.0 && showresult1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      showresult1_3.tStart = t;  // (not accounting for frame time here)
      showresult1_3.frameNStart = frameN;  // exact frame index
      
      showresult1_3.setAutoDraw(true);
    }

    
    if (showresult1_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      showresult1_3.setText(taskchose_text, false);
    }
    
    // *taskscore_text1_3* updates
    if (t >= 0.0 && taskscore_text1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskscore_text1_3.tStart = t;  // (not accounting for frame time here)
      taskscore_text1_3.frameNStart = frameN;  // exact frame index
      
      taskscore_text1_3.setAutoDraw(true);
    }

    
    if (taskscore_text1_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      taskscore_text1_3.setText(taskscore_text, false);
    }
    
    // *feedback_button_3* updates
    if (t >= 0 && feedback_button_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_button_3.tStart = t;  // (not accounting for frame time here)
      feedback_button_3.frameNStart = frameN;  // exact frame index
      
      feedback_button_3.setAutoDraw(true);
    }

    
    if (feedback_button_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      feedback_button_3.setText(nbfeedback_text, false);
    }
    if (feedback_button_3.status === PsychoJS.Status.STARTED) {
      // check whether feedback_button_3 has been pressed
      if (feedback_button_3.isClicked) {
        if (!feedback_button_3.wasClicked) {
          // store time of first click
          feedback_button_3.timesOn.push(feedback_button_3.clock.getTime());
          feedback_button_3.numClicks += 1;
          // store time clicked until
          feedback_button_3.timesOff.push(feedback_button_3.clock.getTime());
        } else {
          // update time clicked until;
          feedback_button_3.timesOff[feedback_button_3.timesOff.length - 1] = feedback_button_3.clock.getTime();
        }
        if (!feedback_button_3.wasClicked) {
          // end routine when feedback_button_3 is clicked
          continueRoutine = false;
        }
        // if feedback_button_3 is still clicked next frame, it is not a new click
        feedback_button_3.wasClicked = true;
      } else {
        // if feedback_button_3 is clicked next frame, it is a new click
        feedback_button_3.wasClicked = false;
      }
    } else {
      // keep clock at 0 if feedback_button_3 hasn't started / has finished
      feedback_button_3.clock.reset();
      // if feedback_button_3 is clicked next frame, it is a new click
      feedback_button_3.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_BComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var n_back_correct_count;
function feedback_BRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_B' ---
    for (const thisComponent of feedback_BComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_button_3.numClicks', feedback_button_3.numClicks);
    psychoJS.experiment.addData('feedback_button_3.timesOn', feedback_button_3.timesOn);
    psychoJS.experiment.addData('feedback_button_3.timesOff', feedback_button_3.timesOff);
    // Run 'End Routine' code from feedback_code_3
    file_handle = open(`预实验数据未放入
    esult${expInfo["participant"]}.txt`
    , {"mode": "a"});
    file_handle.write(`2back第${rowbcount}轮：${n_back_correct_count}
    `);
    file_handle.close();
    n_back_correct_count = 0;
    
    // the Routine "feedback_B" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskcnum;
var _key_resp_2_allKeys;
var vsintroComponents;
function vsintroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'vsintro' ---
    t = 0;
    vsintroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from VS_begin_code
    taskcnum = random.randint(1, 499);
    
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    vsintroComponents = [];
    vsintroComponents.push(VS_intro_image);
    vsintroComponents.push(key_resp_2);
    
    for (const thisComponent of vsintroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function vsintroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'vsintro' ---
    // get current time
    t = vsintroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *VS_intro_image* updates
    if (t >= 0.0 && VS_intro_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VS_intro_image.tStart = t;  // (not accounting for frame time here)
      VS_intro_image.frameNStart = frameN;  // exact frame index
      
      VS_intro_image.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of vsintroComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vsintroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'vsintro' ---
    for (const thisComponent of vsintroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from VS_begin_code
    taskctimer.reset();
    
    key_resp_2.stop();
    // the Routine "vsintro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var correct_feedback;
var vsdata;
var Temp_List;
var VS_right_react;
var _key_resp_allKeys;
var visual_SearchComponents;
function visual_SearchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'visual_Search' ---
    t = 0;
    visual_SearchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from VS_react_code
    correct_feedback = "";
    vsdata = react.loc[taskcnum];
    vsdata = vsdata.slice(1);
    Temp_List = np.array(vsdata).tolist();
    VS_right_react = Temp_List[Temp_List_correct];
    VSimage_path = `visual_search_pic/${taskcnum}.png`;
    vsdata = react.loc[taskcnum];
    vsdata = vsdata.slice(1);
    Temp_List = np.array(vsdata).tolist();
    
    VSimage.setImage(VSimage_path);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    visual_SearchComponents = [];
    visual_SearchComponents.push(VSimage);
    visual_SearchComponents.push(key_resp);
    visual_SearchComponents.push(taskctime_text);
    
    for (const thisComponent of visual_SearchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var taskc_text_color;
function visual_SearchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'visual_Search' ---
    // get current time
    t = visual_SearchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from VS_react_code
    taskctime = get_taskctime(30);
    if ((taskctime === 0)) {
        taskctime = 0;
        correct_feedback = "\u65f6\u95f4\u5230\uff01\uff01";
        taskc_text_color = "red";
        trials_5.finished = true;
        continueRoutine = false;
        routineForceEnded = true;
    }
    
    
    // *VSimage* updates
    if (t >= 0.0 && VSimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VSimage.tStart = t;  // (not accounting for frame time here)
      VSimage.frameNStart = frameN;  // exact frame index
      
      VSimage.setAutoDraw(true);
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (VSimage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      VSimage.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'u', 'h', 'j'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == VS_right_react) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *taskctime_text* updates
    if (t >= 0.0 && taskctime_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskctime_text.tStart = t;  // (not accounting for frame time here)
      taskctime_text.frameNStart = frameN;  // exact frame index
      
      taskctime_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (taskctime_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      taskctime_text.setAutoDraw(false);
    }
    
    if (taskctime_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      taskctime_text.setText(taskctime, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of visual_SearchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function visual_SearchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'visual_Search' ---
    for (const thisComponent of visual_SearchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(VS_right_react)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var vsfeedbackComponents;
function vsfeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'vsfeedback' ---
    t = 0;
    vsfeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from VS_feedback_code
    taskctime = get_taskctime(30);
    vs_correct_count += 1;
    if (((key_resp.corr === 1) && (taskctime !== 0))) {
        correct_feedback = "\u6b63\u786e";
        taskc_text_color = "greenyellow";
        Temp_List_correct += 1;
    } else {
        if (((key_resp.corr === 0) && (taskctime !== 0))) {
            correct_feedback = "\u9519\u8bef";
            taskc_text_color = "red";
            trials_5.finished = true;
        } else {
            if ((taskctime === 0)) {
                taskctime = 0;
                correct_feedback = "\u65f6\u95f4\u5230\uff01\uff01";
                taskc_text_color = "red";
                trials_5.finished = true;
            }
        }
    }
    
    VSimage_2.setImage(VSimage_path);
    taskc_text.setColor(new util.Color(taskc_text_color));
    taskc_text.setText(correct_feedback);
    // keep track of which components have finished
    vsfeedbackComponents = [];
    vsfeedbackComponents.push(VSimage_2);
    vsfeedbackComponents.push(taskc_text);
    vsfeedbackComponents.push(taskctime_text2);
    
    for (const thisComponent of vsfeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function vsfeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'vsfeedback' ---
    // get current time
    t = vsfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from VS_feedback_code
    /* Syntax Error: Fix Python code */
    
    // *VSimage_2* updates
    if (t >= 0.0 && VSimage_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VSimage_2.tStart = t;  // (not accounting for frame time here)
      VSimage_2.frameNStart = frameN;  // exact frame index
      
      VSimage_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (VSimage_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      VSimage_2.setAutoDraw(false);
    }
    
    // *taskc_text* updates
    if (t >= 0 && taskc_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskc_text.tStart = t;  // (not accounting for frame time here)
      taskc_text.frameNStart = frameN;  // exact frame index
      
      taskc_text.setAutoDraw(true);
    }

    frameRemains = 0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (taskc_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      taskc_text.setAutoDraw(false);
    }
    
    // *taskctime_text2* updates
    if (t >= 0.0 && taskctime_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskctime_text2.tStart = t;  // (not accounting for frame time here)
      taskctime_text2.frameNStart = frameN;  // exact frame index
      
      taskctime_text2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (taskctime_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      taskctime_text2.setAutoDraw(false);
    }
    
    if (taskctime_text2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      taskctime_text2.setText(taskctime, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of vsfeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vsfeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'vsfeedback' ---
    for (const thisComponent of vsfeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from VS_feedback_code
    /* Syntax Error: Fix Python code */
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tackcnum_addComponents;
function tackcnum_addRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tackcnum_add' ---
    t = 0;
    tackcnum_addClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    tackcnum_addComponents = [];
    
    for (const thisComponent of tackcnum_addComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function tackcnum_addRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tackcnum_add' ---
    // get current time
    t = tackcnum_addClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of tackcnum_addComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tackcnum_addRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tackcnum_add' ---
    for (const thisComponent of tackcnum_addComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "tackcnum_add" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskresultC;
var vsfeedback_text;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    taskresultC = Math.round((30 + ((70 * stats.percentileofscore(resultB_range, vs_correct_count)) / 100)), 2);
    taskchose_text = `您选择执行的任务是：任务C`;
    taskscore_text = `您本轮任务的评分是：${taskresultC}`;
    rowccount += 1;
    if ((rowccount === 4)) {
        vsfeedback_text = "\u4efb\u52a1C\u8bad\u7ec3\u5df2\u5b8c\u6210\uff0c\u70b9\u51fb\u7ed3\u675f\u8bad\u7ec3\u9636\u6bb5";
    }
    
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_polygon);
    feedbackComponents.push(showresult1);
    feedbackComponents.push(taskscore_text1);
    feedbackComponents.push(feedback_button);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_polygon* updates
    if (t >= 0.0 && feedback_polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_polygon.tStart = t;  // (not accounting for frame time here)
      feedback_polygon.frameNStart = frameN;  // exact frame index
      
      feedback_polygon.setAutoDraw(true);
    }

    
    // *showresult1* updates
    if (t >= 0.0 && showresult1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      showresult1.tStart = t;  // (not accounting for frame time here)
      showresult1.frameNStart = frameN;  // exact frame index
      
      showresult1.setAutoDraw(true);
    }

    
    if (showresult1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      showresult1.setText(taskchose_text, false);
    }
    
    // *taskscore_text1* updates
    if (t >= 0.0 && taskscore_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taskscore_text1.tStart = t;  // (not accounting for frame time here)
      taskscore_text1.frameNStart = frameN;  // exact frame index
      
      taskscore_text1.setAutoDraw(true);
    }

    
    if (taskscore_text1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      taskscore_text1.setText(taskscore_text, false);
    }
    
    // *feedback_button* updates
    if (t >= 0 && feedback_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_button.tStart = t;  // (not accounting for frame time here)
      feedback_button.frameNStart = frameN;  // exact frame index
      
      feedback_button.setAutoDraw(true);
    }

    
    if (feedback_button.status === PsychoJS.Status.STARTED){ // only update if being drawn
      feedback_button.setText(vsfeedback_text, false);
    }
    if (feedback_button.status === PsychoJS.Status.STARTED) {
      // check whether feedback_button has been pressed
      if (feedback_button.isClicked) {
        if (!feedback_button.wasClicked) {
          // store time of first click
          feedback_button.timesOn.push(feedback_button.clock.getTime());
          feedback_button.numClicks += 1;
          // store time clicked until
          feedback_button.timesOff.push(feedback_button.clock.getTime());
        } else {
          // update time clicked until;
          feedback_button.timesOff[feedback_button.timesOff.length - 1] = feedback_button.clock.getTime();
        }
        if (!feedback_button.wasClicked) {
          // end routine when feedback_button is clicked
          continueRoutine = false;
        }
        // if feedback_button is still clicked next frame, it is not a new click
        feedback_button.wasClicked = true;
      } else {
        // if feedback_button is clicked next frame, it is a new click
        feedback_button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if feedback_button hasn't started / has finished
      feedback_button.clock.reset();
      // if feedback_button is clicked next frame, it is a new click
      feedback_button.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var vs_correct_count;
var Temp_List_correct;
function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_button.numClicks', feedback_button.numClicks);
    psychoJS.experiment.addData('feedback_button.timesOn', feedback_button.timesOn);
    psychoJS.experiment.addData('feedback_button.timesOff', feedback_button.timesOff);
    // Run 'End Routine' code from feedback_code
    console.log(`视觉搜索第${rowccount}轮：${vs_correct_count}
    `);
    file_handle = open(`预实验数据未放入
    esult${expInfo["participant"]}.txt`
    , {"mode": "a"});
    file_handle.write(`视觉搜索第${rowccount}轮：${vs_correct_count}
    `);
    file_handle.close();
    vs_correct_count = 0;
    taskcnum = 0;
    Temp_List_correct = 0;
    
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
