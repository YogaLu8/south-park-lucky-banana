#在定义角色
define k = Character("Kenny", color = "#ff9900", image= "kenny")
define b = Character("Butters", color = "#ffcc00", image= "butters")
define s = Character("Stan", color = "#4662e0", image= "stan")
define ky = Character("kyle", color = "#46e058", image = "kyle")
define d = Character("Dick", color = "#82510c",image ="dick")
define mr = Character("MR.HanKey", color = "#82510c",image ="mrhankey")
define ko = Character("Kobe", color = "#663e06",image ="kobe")
define m = Character("Michael", color = "#000000", image= "goth")
define pe = Character("Peter", color = "#000000", image= "red")
define c = Character("Cartman", color = "#b8b617", image= "cartman")
define z = Character("佐巴扬", color = "#7ba16e",image = "zuobayang")
define p = Character("观众")
define h = Character("主持人")
define t = Character("老师")
define who = Character("???")
define n = Character("Autumn HanKey",image = "wife")
define w = Character("Weedy", color = "#e046c1", image = "weddy")
image side zuobayang = im.Scale("zuobayang.png",280,280)
image side cartman = im.Scale("cartman.png",280,280)
image side wife = im.Scale("wife.png",230,420)
image side red = im.Scale("red normal.png",280,280)
image side goth = im.Scale("goth normal.png",280,280)
image side mrhankey = im.Scale("mr.png",230,420)
image side weddy = im.Scale("weddy normal 1.png",280,280)
image side kobe = im.Scale("kobe normal.png",280,280)
image side kyle = im.Scale("kyle normal 1.png",280,280)
image side kenny = im.Scale("kenny normal.png",280,280)
image side butters = im.Scale("butters normal 1.png",280,280)
image side stan = im.Scale("stan normal.png",280,280)
image side dick = im.Scale("dick normal.png",280,280)
#在start之前初始化一个flag,包含了玩家做过的某一个选择

define config.main_menu_music = "audio/song.mp3" 

default torch = False
default toy = False
default kobe_help = False
default weddy_help = False
default music = False
default note = False
default ball = False
default persistent.endings_unlocked = []
#启动器开启之后触发
label start:
    stop music fadeout 1.0 #不要等号直接加数字
    scene bg busstop
    with fade 
# 这里的with语句决定了需要使用的转场效果名。最常用的转场效果是dissolve(溶解)。另一个有用
# 的转场效果是fade(褪色)，能让[界面褪为全黑]，然后逐渐亮起成新的界面。

#播放音乐使用play music语句 存放在game/audioo文件下 
    # 如果去掉文件扩展名符合py变量命名规则 英文字母数字下划线
    # 直接play music southpark 

    # play music "audio/illurock.ogg" fadeout 1.0 fadein 1.0 渐入渐出
    # queue music "audio/next_track.opus 当前音乐播放完后播放的音频文件
    # stop music 结束当前音乐
    # 音效! 不会循环播放 play sound "路径"
    "非盈利粉丝向作品"
    "南方公园》版权归 Comedy Central 及 Matt Stone、Trey Parker 所有"
    "本作品仅供学习交流，禁止商业用途"
    "🎵南方公园的小曲"
    "是否播放?"

menu:
    "播放":
        jump music

    "谁喜欢听啊":
        play music "audio/cat.mp3" fadein 1.0
        jump story

label music:
    play music "audio/southpark.MP3" fadeout 1.0
    $ music = True #通过 符号$ 文本被识别为py语句 修改
    "这是一个没有暴力温馨的地方...(省略)"
    queue music "audio/cat.mp3" fadein 1.0
    jump story

label story:

    "南方公园的某一天"
    "上午--公交车站"
    "巴特斯站在站牌下傻笑 肯尼站在另一边"
    show butters normal 1
    with dissolve 

    "这是巴特 南方公园里平平无奇的一个怂蛋"
    b normal 2 "今天天气真好！适合在外面玩！但是妈妈说我要先去教堂！"
    b normal 3 "因为耶稣不喜欢我昨天用手电筒照邻居家的狗..."
    b normal 4 "我觉得耶稣有点小气 肯尼你说耶稣会把我打进地狱吗？"
    hide butters
    with dissolve

    show kenny lookright
    with dissolve

    k "*********"
    "肯尼说了句话,没人能听懂"

    b "什么?"
    k angry "*******!"
    b "哦哦! 好的!"
    "巴特其实什么也没听懂--"
    "但巴特斯永远说--好的!"
    "所以他活得久..."

    "飞车驶来，看见站牌下站着肯尼，加速开走"
    "寒风像镰刀一样划过肯尼发红的面颊"
    show kenny sick
    "肯尼紧紧地裹紧自己的橘黄色卫衣"

    "为什么肯尼总是穿着那件寒酸的衣服,发着含糊不清的口音"

    "因为他是南方公园最贫穷的孩子 哦不 可怜的肯尼"
    
    "因为他是个连饭都吃不起的孩子 哦不 可怜的肯尼"

    show kenny angry 

    "因为他是个--"

    k "******* (翻译:嘿! 你个混蛋! 我都听见了! stop!)"
    
    hide kenny

    show kenny normal 
    show butters normal 1 at right
    with dissolve

#需要检查flag的时候,请使用if语句
if music:
    show kenny lookup

    "多么棒的一天啊"

    show kenny sick 
    show butters normal 4
    with dissolve
    "因为你播放了世界上最动听的音乐"
    stop music fadeout 2.0
    pause 0.5
    jump playground
else:
    show kenny lookup
    with dissolve
    "很普通的一天"

    show kenny sick 
    show butters normal 4
    with dissolve
    "因为你没播放世界上最动听的音乐!!!!!"
    stop music fadeout 2.0
    pause 0.5
    jump playground

label playground:
    pause 0.5
    play music "audio/meet.mp3" fadein 2.0
    scene bg playground
    with fade
    "上午--学校操场"
    show stan normal at left 
    show kyle chew 1 
    show kenny normal at right
    with dissolve

    "第一节课下课后"
    "斯坦、凯尔、肯尼站在操场边 凯尔嘴里塞满了东西"
    show kenny lookleft
    play sound eat
    show kyle chew
    "凯尔一直在嚼东西"
    show stan normal 1
    show kyle chew 3
   
    s "伙计们! 你们看昨天放屁兄弟的电影预告了吗?"
    
    show kyle chew 1
    show stan normal 2
    play sound eat
    s "真是太他妈有意思了! 我真的迫不及待了"
    show stan normal 3
    show kyle chew 3
   
    s "据说这次填了不少第一部的坑"
    show stan normal 2
    show kyle chew 2
    play sound eat
    

    s "话说今天怎么没有看到卡特曼那个死肥猪"
    show kyle chew 3
    show stan normal
    show kenny sick 
    play sound eat
    s "好吧 伙计们"
    show stan normal 3
    show kyle chew 1
   
    s "其实我从刚才就注意到了"
    show stan normal 2
    show kyle chew 3
  
    s "凯子 你嘴里吃什么呢!?"
    show kyle normal 1
    show kenny lookleft
    show stan normal
    ky "幸运香蕉啊 你们不知道吗"
    show stan hungry
    s "什么!"
    k "** 翻译:什么!??"
    "幸运香蕉是这群小屁孩里流传的传说"

    show banana lucky:
        zoom 0.4
        xalign 0.86
        yalign 0.05
    with dissolve
    show kenny lookup
    "据说南方公园产出的香蕉每年有极小的概率会变成幸运香蕉"
    "吃下幸运香蕉能够让人变得无比强运"
    "对 就是这么无聊"
    show kenny lookleft
    show kyle lookleft
    show stan normal 2
    s "快告诉我哪里有!?"
    hide banana
    show stan angry 4
    ky normal 2 "在卡特曼那边买的"
    ky "但是--"
    with vpunch
    s "不是...什么玩意?"
    with hpunch
    s angry 1 "你几把信了?"
    ky lookleft "我信啊!"
    ky normal 4 "他说他表哥吃了之后中了彩票!"
    s "..."
    with hpunch

    s angry 2 "那个死肥猪没有表哥!"
    with vpunch
    ky angry 1 "他说有!"
    s angry 1 "我说他有七千块零花钱,你信吗!?"
    ky angry 2 "我信啊! 他昨天刚买了GTA6!"
    with vpunch
    s angry 3 "那他妈是用他妈信用卡刷的!"

    with hpunch
    ky angry 3 "那也是钱啊!"
    k sleepy "****** 翻译:真的能发财!"
    show kyle lookleft
    s normal 2 "肯尼你激动个蛋 攒个五毛钱都得两三天"
    show kenny angry
    ky normal 4 "哈哈哈哈哈"
    k "等我攒够钱买香蕉了就能变有钱!"
    k sick "到时候就不用天天吃过期的速冻饼了!"
    ky normal 2 "老兄 这好像不是速冻饼的问题 那是你爸挥金如土的问题"
    show stan normal
    show kenny normal
    show kyle chew 3
    "就在男孩们聊得如火如荼的时候"
    "有一位挺着大胃袋--"
    "哦不对..."
    "是我们的大骨架男孩卡特曼晃晃悠悠走了过来"
    hide stan 
    hide kenny
    hide kyle
    show cartman 2 at truecenter:
        zoom 0.75
    with dissolve
    with hpunch
    c "啦啦啦啦啦 我听见有人在聊我最新的产品"
    c "没错，我就是那个卖香蕉的人 5块8一根，童叟无欺，概不退款"
    s "你这香蕉哪来的"
    c "进货渠道是商业机密，斯坦 你这种穷人思维永远理解不了商业"
    s "你哪来的商业，你妈给你零花钱--"
    with vpunch
    c "我妈给我零花钱，我把零花钱变成资本，资本生资本"
    c "这叫资本主义，斯坦"
    c "你以后会懂的 哦不! 你大概不会懂，因为你家只有你爸一个人上班"
    s "我爸是地质学家!"
    show cartman 4:
        zoom 1.5
    with None
    with vpunch
    c "地质学家赚几个钱?"
    s "..."
    k "****** 翻译: 我只有五毛钱"
    show cartman 2 at truecenter:
        zoom 0.75
    c "哦 肯尼 我的老朋友~"
    c "我来给你做一个专门的分期方案"
    c "首付五毛，剩下五块三，每天利息百分之十 分三十天还清"
    with hpunch
    ky "你这个死肥猪疯了吧! 那加起来是二十块钱!"
    c "这是复利, 凯尔 这是金融常识"
    with vpunch
    ky "这是高利贷--"
    c "这是创业 凯尔，你永远不会成为一个创业者 因为你只会嫉妒别人成功"
    ky "我嫉妒你什么了!"
    show cartman 3:
        zoom 1.5
    with None
    with hpunch
    c "嫉妒我的商业头脑!"
    hide cartman
    show kenny normal
    with dissolve
    "此时 肯尼打算做..."

menu banana:
    "攒钱买香蕉":
        jump story2
    "还是算了吧":
        stop music fadeout 1.0
        jump end1

label end1:
    play music "audio/sad.mp3"
    pause 0.5
    show kenny sick
    k "心想: 算了 还是放弃吧"
    k "心想: 我不应该把希望寄托在这个上的"
    k "心想: 我果然还是做不到啊..."
    "肯尼转身离开了"
    scene bg busstop
    with fade
    show kenny sleepy
    with dissolve
    b "肯尼 你怎么了?"
    show kenny sick
    k "**** 翻译: 我放弃了"
    b "哦！那挺好的！我妈妈说放弃也是一种智慧！虽然我爸爸说放弃的人都是废物！"
    b "但他们两个说的可能都对！"
    show kenny lookleft
    b "肯尼你要不要跟我一起去教堂？耶稣会帮你的！"
    k sleepy "******** 翻译: 耶稣帮不了我"
    b "你怎么知道？你试过吗？"
    k sick "..."
    b "我爸爸说，不信耶稣的人都会下地狱 肯尼你不想下地狱吧？"
    with hpunch
    k "我他妈已经在地狱了"
    "这一句肯尼说得很清楚"
    scene bg black
    with fade
    "什么都没改变..."

    "结局一 失败的肯尼"
    $ unlock_ending("end1")

menu:
    "回到前一个选项":
        stop music fadeout 0.5
        play music "audio/meet.mp3"
        scene bg playground
        show kenny normal
        jump banana
    "返回主菜单":
        return

label story2:
    k lookright "*****!! 翻译: 我要买"
    c "好,成交"
    show kenny lookleft
    s "肯尼你疯了!你连饭都吃不起"
    k angry "****** 翻译: 饭天天都可以不吃 发财的机会只有一次"
    s "..."
    show kenny lookright
    c "你看 肯尼在你们这群穷人里 是最懂行的!"
    show kenny lookleft
    with vpunch
    ky "你他妈说谁是穷人!"
    show kenny lookright
    c "凯尔，你妈是律师，你让她来告我啊"
    c "那就让她来啊！你妈连你爸强奸都告不赢，还告我？"
    show kenny lookleft
    with vpunch
    ky "操你妈, 卡特曼!"
    show kenny lookright
    with vpunch
    c "操你妈, 凯尔!"
    show kenny sick
    s "你们两个能不能别他妈吵了!"
    show kenny sleepy
    "于是肯尼决定攒钱买幸运香蕉"
    "他的目标很简单——五块八 他的起点也很简单——五毛"
    "差五块三"
    k "但是我要去哪里赚钱呢"
menu:
    "去教室转转":
        jump class
    "报名打自由搏击":
        jump boxing

label boxing:
    with hpunch
    stop music fadeout 0.5
    play sound "audio/danger.mp3"
    k angry "WAAAAAAIT WHAAAAAAAAAT????"
    with hpunch
    k "**************!****!! 翻译: 一连串的*俚语*"
    with hpunch
    k "****** 翻译: *俚语* 你认真的吗?! 让我去!?"
    stop music fadeout 0.5
    scene bg black
    with fade
    play sound wu
    with vpunch
    k "**... 翻译: 哦不.. 好难受"
    "肯尼突然觉得眼前一片漆黑"
    "他被一股神秘的力量卷走 变得无法动弹"
    k "***..."
    "可怜的肯尼 被玩弄于股掌之间"
    "更可怜的是，这种事他每周都要经历一次 而且从来没有人问他愿不愿意"
    "因为问了也没用，他说的没人听得懂"
    scene bg boxing ring
    with fade
    play music fight
    "等肯尼再次睁开眼睛时候 他已经被带到了拳击擂台"
    "拳击擂台 灯光刺眼 观众喧闹"
    k sick "啊啊啊啊啊啊!!!!"
    "只见主持人高举手臂 面向观众"
    h "女士们！先生们！欢迎来到今晚的自由搏击擂台！！"
    play sound cheer2
    h "尖叫声在哪里！！让我听到你们的呐喊！！"
    with vpunch
    with hpunch
    p "欢呼声!!!"
    h "今晚，将会有两位强者站上这块擂台！"
    k "**** 翻译: 现在退票还来得及吗..."
    h "这一场对决，将会出乎所有人的预料！！"
    h "一边，是我们连续三年守住王座，未尝败绩的卫冕之王！！"
    with hpunch
    h "Dick!"
    with vpunch
    p "DICK! DICK! DICK!"
    d "..."
    h "但是今晚！有一个人，敢于站出来向王座发起冲击！"
    h "他就是今晚的挑战者--！！"
    k "..."
    h "他就是!-- "

menu:
    "逆风倒霉蛋-肯尼":
        jump box2
    "脆骨小虫-肯尼":
        jump box2
    "炼狱疯拳-肯尼":
        jump box2

label box2:
    play sound cheer
    h "哈哈哈 谁在乎呢? 好了! 现在来到赛前垃圾话环节"
    h "两位选手! 请移步到擂台中央!面对面!输出你们想说的话!"
    show kenny sick at left
    show dick normal at right
    with vpunch
    h "来吧! 让我们看看!火药味!"
    d "擂台上面我会好好收拾你！打完之后你连走路都做不到！"
    d 2 "你知道我为什么三年不败吗？"
    d "因为我每天早上四点起床，吞下八个生鸡蛋，打沙袋打到手出血"
    d angry "你知道我为什么这么强吗？"
    with vpunch
    d "因为我恨--我恨所有人"
    with vpunch
    d "我恨你，我恨观众，我恨这个擂台!"
    show kenny sleepy
    d normal 2 "你想知道我最恨谁吗?"
    with vpunch
    d angry "我最恨我自己! 因为我每天都要对着镜子说，迪克，你是最强的"
    with vpunch
    d "但我他妈不信!我他妈一次都不信!!"
    "迪克滔滔不绝地说着自己的无聊经历"
    p "..."
    k sick "***** 翻译: 我该怎么办!"

menu fight:
    "认怂":
        jump box3
    "死斗":
        stop music fadeout 0.5
        jump box4

label box3:
    stop music fadeout 0.5
    play music sad
    k sleepy "********* 翻译: 饶了我吧 我这就从擂台下滚下去"
    d normal 2 "切 果然是没骨气的小鬼"
    show kenny lookright
    d angry "你知道吗，我最讨厌你这种人 不是因为你弱, 是因为你连试都不敢试"
    d normal 2 "我每天早上四点起床 你呢？你几点起？"
    k sleepy "******* 翻译: 我每天都被我爸吵醒,没有固定时间"
    d confused "那你也比我强... 至少你还有个爸"
    show dick angry
    k lookright "..."
    d normal "算了 滚吧"
    k sleepy "..."
    hide kenny 
    play sound boom
    "肯尼双腿发软 扶着围栏晃晃悠悠地走下楼梯"
    "迪克这句话说得很轻松 因为他不知道..."
    "肯尼从楼梯上摔下去的时候，后脑勺撞到了擂台边的铁柱子"
    with vpunch
    k "!!!"
    "咚!!!!!!!!!!!!"
    k "饿啊----"
    with vpunch
    with hpunch
    h "啊!肯尼选手摔下擂台!出事了!"
    h "医疗队!医疗队!"
    h "好吧, 我们的赞助商跑路了 我们没预算"
    h "总之谁先下去看看?"

    play sound bone
    scene bg black
    with fade
    show kenny dead 
    with dissolve
    "肯尼躺在擂台下面，眼睛变成叉叉"
    "哦不 可怜的肯尼"
    scene bg boxing ring
    with fade
    show stan banana at left
    with dissolve
    s "omg 他们杀了肯尼 你们这群混蛋!"
    scene bg black
    with fade
    "肯尼的死因被定性为意外 没有人为此负责"
    "主办方赔了肯尼家两百块 肯尼他爸当天就拿去买了彩票"
    "结局二 擂台的可怜虫"
    $ unlock_ending("end2")
menu:
    "回到上个选项":
        scene bg boxing ring
        stop music fadeout 0.5
        play music fight
        hide stan
        show kenny sick at left
        show dick normal at right
        jump fight
    "回到主菜单":
        return

label box4:
    play music fight2 fadeout 0.5
    play sound zip
    "肯尼站直了身体"
    k angry "********!! 翻译:GodDamn!!!!!"
    "肯尼摘下了自己帽子"
    with vpunch
    k fight 1 "我受够了!"
    d confused "...?"
    k fight 3 "不管在那个傻逼动画还是这个破游戏里"
    k fight 1 "我总是一次又一次的被各种操蛋的原因搞死"
    k fight 2 "我死了170多次..."
    k fight 1 "被车撞、被火烧、被电死、被老鼠咬死"
    k fight 3 "我心爱的妹妹总说我是个英雄"
    k fight 1 "但我不是,我只是渴望..."
    d "什么?"
    with vpunch
    k fight 2 "钱"
    with hpunch
    k fight 3 "我要为了钱 为了钞票 战斗--!!!"
    play sound cheer2
    d normal 2 "...你知道吗"
    d angry "我打了三年拳...我赚的钱全给我妈看病了"
    d "但是她上个月走了"
    d "所以你说你要为了钱战斗"
    d "我他妈一点都不想笑"
    d normal "但我要笑..."
    d "因为... 我妈--"
    with hpunch
    d "因为我他妈不笑难道哭嘛?"
    with hpunch
    d "哈哈哈哈哈!!!!!!!"
    with hpunch
    show dick normal at center
    with None
    show kenny dead at left
    with dissolve 
    "迪克大笑 然后冲上来，一拳打在肯尼脸上 肯尼倒地"
    k "饿啊!! 呵...!!"
    h "Dick选手一拳狠狠击中肯尼选手的面部! 肯尼选手发出了惨叫! 摔倒在了擂台上!"
    p "喝啊啊啊啊啊啊!!!!!!"
    h "果然王者的位置是无法撼动的! "
    h "裁判开始读秒! 一! 二! 三! "
    show kenny dead 2
    show dick confused
    with vpunch
    k "咳咳.."
    h "天哪! 多么顽强! 肯尼选手还试图挣扎着想要爬起来!"
    k dead 3 "根本..不痛不痒 你这个嗯造蛋白粉的秃子"
    d angry "从来没有人敢这么和我说话!!!!!!!!!"
    with hpunch
    "Dick使出本场最大的劲 挥着拳头向肯尼砸去"
    show dick angry at left
    with dissolve
    scene bg black
    with fade
    "一瞬间 全场都安静了"
    "哦不 可怜虫肯尼..."
    "难道 阿尼真的又要挂掉了吗"
    scene bg boxing ring
    show dick dead at left
    h "等下!! Dick选手发生了异常 他的动作停下来了!!"
    play sound cheer2
    with hpunch
    h "Dick.. Dick选手倒下了!!"
    hide dick
    with dissolve
    with vpunch
    with hpunch
    p "喝啊啊啊啊!"
    h "这不是被击倒！拳王 Dick 突发身体急症！他倒下去了！！"
    h "裁判开始读秒!"
    "八...九...十"
    "KO!"
    h "真是难以置信! 我宣布,肯尼成为了新一届的拳王!!! 奖金是-----"
    show kenny winner
    with dissolve
    with vpunch
    with hpunch
    h "十万美刀!!!!!!!"
    k "..."
    p "欢呼声!!!!!"
    p "我的天! 没想到他真的赢了"
    p "妈妈啊 我要去天台!!"
    s "omg 阿尼杀了迪克!!! 干得漂亮"
    scene bg black
    with fade
    stop music fadeout 1.0
    play music meet
    "赛后媒体大肆炒作肯尼 “神秘一击击溃不败拳王”"
    "可实际上所有人都清楚这只是一场倒霉的突发疾病"
    "但是起码靠着这笔奖金,肯尼一家不用再过着拮据的生活"
    "大概..."
    s "听说肯尼家的钱已经快被他老爸造完了"
    ky "难以置信! 明明刚刚才拿到那么大笔奖金"
    k "难道...我还是逃不出贫困吗?"
    "肯尼他爸用了三天时间就把钱花光了"
    "买了一辆二手雪地摩托，十箱威士忌，和一个会说话的耶稣玩偶"
    "那个玩偶只会说一句话--"
    "耶稣爱你胜过金钱"
    s "肯尼 至少你家现在有个耶稣玩偶了"
    ky "肯尼往好处想 你爸至少没把钱拿去赌"
    k "他赌了啊!"
    "这一句肯尼说的很清楚"
    ky "哦 那没事了"

    "结局三 金钱的泡影"
    $ unlock_ending("end3")
menu:
    "回到上个选项":
        stop music fadeout 0.5
        play music fight
        scene bg boxing ring
        hide stan
        show kenny sick at left
        show dick normal at right
        jump fight
    "回到主菜单":
        return

label class:
    scene bg class 1
    with fade
    stop music fadeout 0.5
    play music class1
    "上午--教室"
    show kenny 
    k lookleft "..."
    k lookright "..."
    "家政课结束后,肯尼被老师留下来谈话"
    show kenny sick
    t "阿尼 你的情况真的很特殊"
    t "虽然你课堂表现不错 缝纫 清洁 做装饰都很出色"
    show kenny sleepy
    t "但你们上家政课的原因 是为了嫁给一个好老公"
    show kenny sick
    play sound hurt2
    t "说白了 像你这样穷酸的小孩, 去当佣人给有钱人洗马桶都不够格的"
    show kenny lookup
    with None
    show drama 1:
        zoom 0.4
        xalign 0.5
        yalign 0.03
    with dissolve
    t "老师真的建议你转去隔壁的手工课"
    with None
    t "这也是为了你的前程考虑"
    with vpunch
    with hpunch
    k sick "****!! **!!! 翻译: 我才不要! 我一定会挂掉的!"
    hide drama 1
    with dissolve
    show kenny lookright
    t "你看，你手工课的成绩是B+，家政课是A- "
    "但家政课A-有什么用呢？你连个像样的厨房都没有"
    t "你家有厨房吗"
    k normal "***** 翻译: 哦! 我家有一个打火机"
    show kenny lookright
    with vpunch
    t "打火机不算厨房"
    k sleepy "***** 翻译: 哦那就是没有"
    show kenny lookright
    t "阿尼 你一定要好好考虑 老师这是为了你好"
    with hpunch
    k angry "***! 翻译: 为我好个屁!"
    t "什么?"
    k lookright "哦!没事"
    "肯尼这句说的很清楚"
    t "那好吧 没什么事了 你走吧"
    k sick "**!**** 翻译: 天杀的! 真的没人在乎我的感受吗"
    show kenny sleepy
    "在原作里 肯尼每集都会以离奇的方式死掉 次集又复活"
    k lookleft "算了 还是出去透透气吧"
    show kenny lookleft at left
    k "说不定有机会攒钱买幸运香蕉!"
    who "嘿! 肯尼 等一下!"
    k lookright "...?"
    hide kenny
    show weddy normal 1
    with dissolve
    w "那个.. 我有事情想要请你帮忙"
    "温迪 学校里很受欢迎的女生 平时待人友好"
    "也是肯尼好友斯坦的女朋友"
    hide weddy
    with dissolve
    show kenny lookright at left
    show weddy left 1 at right
    k "******* 翻译: 什么事情?"
    w left 2 "我的笔记本不见了 我找了很久都没找到"
    w left 3 "里面写满了家政课的笔记"
    w left 4 "求你了 帮帮我一起找好吗"
    w left 2 "那本笔记真的对我很重要"
    w left 3 "应该就掉在这附近"
    w left 5 "我真的不知道应该怎么办了..."
    w left 2 "下周要参加家政比赛 如果我赢了，我可以拿到奖学金"
    w left 4 "我需要那笔奖学金 因为我不想以后嫁给一个有钱的老公然后天天在家里等他回来"
    w left 2 "我想做个独立女性 你懂吗? 肯尼"
    k "** 翻译: 我懂"
    "面对温迪的请求 肯尼的想法是?"
menu help:
    "帮助温迪":
        jump help1
    "不帮助温迪":
        jump help2

label help2:
    k lookup "******** 翻译: 抱歉温迪 刚才老师留我谈话耽误好久了"
    k lookright "******* 翻译: 你找别人帮忙吧"
    w left 6 "好吧 我理解"
    w left 5 "每个人都有自己的事情 对不起打扰你了"
    w left 7 "希望我的笔记本过段时间 能够自己出现吧"
    w left 5 "再见了肯尼"
    hide weddy
    with dissolve
    k lookleft "还是先离开教室吧"
    "..."
    "温迪后来在垃圾桶里自己找到了笔记本 她不知道肯尼曾经有过机会帮她"
    jump class2

label help1:
    k "******* 翻译: 我会留意你的笔记本的"
    w left 3 "真的吗! 太好了!"
    w left 2 "谢谢你肯尼! 你真是个善良的人"
    w left 4 "找到笔记本 我一定会报答你的"
    "在南方公园, 这个词通常没有任何实际意义 肯尼以为报答就是亲一下"
    w left 3 "那我先离开继续找了, 再见"
    hide weddy
    with dissolve
    "接受任务--寻找温迪的笔记本"
    $weddy_help =True
    k lookleft "还是先离开教室吧"
    jump class2

label class2:
    scene bg black
    with fade
    "目标--攒够5.8美金"
    scene bg class 2
    with fade
    "上午--走廊"
    "走廊上的学生寥寥无几"
    show kenny lookleft with dissolve
    k lookright "..."
    k "我该去哪里呢?"

menu:
    "搜刮垃圾桶":
        jump rubbish
    "前往篮球场":
        jump ball

label rubbish:
    k sleepy "心想: 没想到在学校也得掏垃圾桶"
    k sick "心想: 里面说不定会有些什么"
    play sound rubbish
    k angry "豁出去了!"
    hide kenny
    with dissolve
    "肯尼硬着头皮把手伸进漆黑的垃圾桶，指尖立刻蹭上黏糊糊、已经发酸的过期酸奶残渣！"
    k "...?呕..."
    "肯尼好像触碰到了某样物体"
    show rubbish:
        zoom 0.4
        xalign 0.5
        yalign 0.5
    with dissolve
    "获得道具-- 一袋腐烂发粘的垃圾"
    with vpunch
    k "***** 翻译: God DAmn!!!"
    k "心想: *俚语* 你再逗我吗!???? 我的手粘死了"
    hide rubbish
    "还要继续掏垃圾桶吗?"

menu:
    "继续":
        jump rubbish2
    "结束":
        jump lr

label rubbish2:
    play sound rubbish
    "肯尼忍着手上黏糊糊的馊味，再次把手伸进漆黑的垃圾桶里"
    k "...?"
    "肯尼好像触碰到了某样物体"
    show hat:
        zoom 0.4
        xalign 0.5
        yalign 0.5
    with dissolve
    "获得道具-- MR.Hat"
    k "心想: Mr.Hat!??? 帽子上面还沾着半块干掉的披萨 为什么在这"
    k "心想: 留着吧 或许之后会派上用场"
    hide hat
    $ toy = True
    "还要继续掏垃圾桶吗?"

menu:
    "继续":
        jump rubbish3
    "结束":
        jump lr

label rubbish3:
    if weddy_help:
        play sound rubbish
        "肯尼强忍着刺鼻的腐臭味，再次把手伸进了漆黑的垃圾桶里"
        k "...?"
        "肯尼好像触碰到了某样物体"
        show note:
            zoom 0.4
            xalign 0.5
            yalign 0.5
        with dissolve
        k "心想: 一本笔记本...书页上还溅上了可乐污渍！上面写着温迪的名字"
        k "心想: 看来我得找个机会还给她"
        $note = True
        hide note
    else:
        "肯尼再次把手伸进了漆黑的垃圾桶里"
        k "...?"
        "肯尼好像触碰到了某样物体"
        show rubbish:
            zoom 0.4
            xalign 0.5
            yalign 0.5
        with dissolve
        "获得道具-- 又一袋黏糊腐烂垃圾"
        with vpunch
        k "********* 翻译: 一连串激烈的*俚语*"
        k "心想: 能不能别搞我了 手上的臭味洗都洗不掉！"
        hide rubbish
    "还要继续掏垃圾桶吗?"
menu rubbish_end:
    "掏到底!":
        jump end4
    "离开垃圾桶":
        jump lr

label end4:
    play sound rubbish
    "不知怎么的"
    "面对眼前臭气熏天的垃圾桶，肯尼越掏越上头"
    "贫困的生活早已让他习惯在垃圾堆里面翻找有用的东西"
    "肯尼竟然产生了一丝快感"
    "肯尼不在乎自己滂臭的 沾满各种酱料的手"
    "只是一味的掏垃圾桶"
    "肯尼好像触碰到了某样物体"
    show money:
            zoom 0.4
            xalign 0.5
            yalign 0.5
    with dissolve
    "获得道具-- 一沓被油腻酱汁浸透的钞票"
    with vpunch
    k "*激动* 呀吼!!!!!!!!!"
    scene bg black
    with fade
    "很显然 那一沓钱够买好几盒幸运香蕉了"
    "但肯尼不知道的是，那沓钱是卡特曼藏在垃圾桶里的"
    "是他卖幸运香蕉收的货款 有整整四十美刀"
    "第二天卡特曼发现了，把肯尼堵在厕所里打了一顿，把钱抢回去了"
    show cartman 2 at truecenter:
        zoom 0.75
    with dissolve 
    c "你知道你偷了谁的钱吗，肯尼？"
    c "你--!"
    with vpunch
    c "你偷了卡特曼企业的流动资金--"
    c "你知道这意味着什么吗？"
    with vpunch
    c "这意味着我的供应链断了, 意味着我下周没法进货, 意味着我失去了整整一周的销售额!"
    show cartman 3 at truecenter:
        zoom 1.55
    with None
    with hpunch
    c "你一个翻垃圾桶的，毁了一个创业者的梦想!"
    with vpunch
    c "你他妈真是个混蛋，肯尼!"
    k "******* 翻译: 那是我从垃圾桶里掏出来的"
    with hpunch
    c "你不知道垃圾桶是我的办公场所吗！你他妈这是入室盗窃！"
    k "..."
    show cartman 2 at truecenter:
        zoom 0.75
    c "算了 我打你一顿, 这事情就这么算了"
    "第二天, 卡特曼还顺便告诉了全校肯尼翻垃圾桶的事"
    "结局四-- 意外财物"
    $ unlock_ending("end4")
menu:
    "回到上一个选项":
        scene bg class 2
        jump rubbish_end
    "回到主菜单":
        return

label lr:
    show kenny sick
    k "心想: 啊啊啊脏死了! 我就不应该把希望寄托在这上"
    show kenny sleepy
    "肯尼为自己翻垃圾桶的举动感到心酸"
    "但肯尼心酸只持续了两秒"
    show kenny sick
    "因为他闻到自己手上的味道之后，心酸变成了恶心"
    show kenny lookleft 
    pause 0.5
    k lookright "接下来该去哪呢"
    with dissolve

menu:
    "前往篮球场":
        jump ball
        
    "前往下水道":
        jump shit

label shit:
    k sick "心想: 我身上的味道难闻的就和屎一样"
    k normal "心想: 等一下 这让我想起了一位老朋友 或许他能帮助我!"
    stop music fadeout 0.5
    play music under
    scene bg under
    with fade
    show kenny lookright at left
    with dissolve
    "上午-- 下水道"
    "肯尼偷偷顺着生锈的铁梯子爬下幽深的下水道"
    k sick "******* 翻译：我的手闻起来臭得要命 希望汉基先生能够听见我的愿望"
    k "******! 翻译: 汉基先生! 你在这里吗 我有一个愿望?"
    k "****** 翻译：汉基先生！我想来许愿！我想要一根传说中的幸运香蕉！"
    k sleepy "******* 翻译：只要吃下幸运香蕉，我家就可以摆脱穷苦日子了！求求你赐予我好运吧！"
    "下水道里空荡荡的 回应肯尼的只有从管道流下的潺潺污水"
    with vpunch
    k angry "*****!! 翻译: 该死的便便! 我再也不相信圣诞节了!"
    play sound shit
    k lookright "...?"
    hide kenny
    show mr at truecenter
    with dissolve
    stop music fadeout 0.5
    play music christmas
    with vpunch
    mr "你好~~~~~~~啊!"
    k "****!! 翻译: 汉基先生!!"
    mr "天哪! 谢谢你的来访 但是在这里每天都是圣诞节!"
    mr "所以当我说你好的时候,你应该也对我说你好啊汉基先生!"
    mr "来试试看! 说你好啊!!"
    "这时你会做"

menu:
    "你好~~~~~~~啊!!汉基先生!!":
        jump hello
    "沉默":
        jump rude

label rude:
    k "..."
    mr "..."
    k "...?"
    mr "......叹气"
    mr "好吧 现在是什么猫猫狗狗都能来下水道了"
    mr "你知道吗，二十年前，来下水道许愿的人还要预约 但现在呢--"
    mr "现在随便一个穿橙色兜帽的小孩都能爬下来跟我许愿"
    with hpunch
    c "这就是通货膨胀!"
    jump shit2

label hello:
    with vpunch
    k "**---- 翻译: 你好~~~~~~啊!!!"
    mr "真是个有礼貌的好孩子!欢迎你!"
    jump shit2

label shit2:
    mr "孩子 你这次特地来访是为了什么呢?"
    k "***... 翻译: 我想要许--"
    play sound eat
    mr "嗯...嚼嚼"
    k "**.. 翻译: 我想---"
    play sound eat
    mr "哦吼哦...嚼..."
    play sound laugh1
    hide mr
    show kenny angry 
    stop music fadeout 0.5
    with hpunch
    k "****!! 翻译: 最近是很流行听别人说话的时候吃东西吗!!"
    mr "......"
    play music christmas fadein 1.0
    hide kenny
    show mr at truecenter
    mr "哦 抱歉"
    mr "好吧 说吧 你想要什么"
    k "我想要一根传说中的幸运香蕉!"
    k "Wait...?"
    hide mr
    with None
    show banana 1:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve
    "肯尼这时才定睛一看，汉基先生手里正捏着一截黄黄的香蕉，小口小口地啃着"
    hide banana
    with None
    show mr at truecenter
    with dissolve
    mr "哦呵呵 真巧 我正吃着香蕉呢"
    mr "我这根可不是许愿获得的哦"
    mr "肯尼，世上没有凭空掉下来的好运 许愿是换不来香蕉的"
    mr  "不劳而获的幸运根本就不存在 想要拿到香蕉，你必须靠自己劳动，挣到5.8美金"
    mr  "不要总想着靠奇迹一步登天改变家里的困境"
    mr "听着肯尼--"
    mr "我在这下水道住了二十年 我见过无数人来许愿"
    mr "他们想要钱，想要女人，想要耶稣显灵"
    mr "你知道他们最后都得到了什么吗？"
    hide mr
    show kenny lookright
    k "***** 翻译: 什么?"
    mr "..."
    mr "什么都没有-- 是的 什么都没有"
    hide kenny 
    show mr at truecenter
    mr "因为这是个下水道，不是许愿池"
    mr "我老婆喝醉了会往这里面吐, 这就是这里唯一会发生的事"
    hide mr
    show kenny lookright
    k "***** 翻译: 那你为什么住在这里"
    mr "因为这里房租便宜"
    show kenny sleepy
    mr "肯尼 这就是成年人的生活 你迟早会懂的"
    show kenny lookright
    mr "但是我可以给你一点机会 下水道这里堆积了一大堆废弃垃圾，如果你愿意帮我清理疏通水沟，我可以付给你工钱！"
    k "心想: 又来!?????"
menu:
    "清理垃圾":
        jump ql
    "不清理":
        jump bql

label bql:
    show kenny lookleft at left 
    with dissolve
    k "***! 翻译: 我拒绝!"
    show kenny lookright
    mr "好吧 孩子我知道这活干着挺脏挺累的"
    mr "但你知道吗，我年轻的时候也拒绝过很多活--"
    mr "现在我在下水道住"
    k angry "..."
    mr "我不是在威胁你-- 我只是在陈述一个事实"
    k sick "心想: 我再也不想碰屎尿屁了"
    scene bg black
    with fade
    k sleepy "心想: 看来只能去篮球场碰碰运气了"
    jump ball

label ql:
    hide mr
    show kenny sleepy 
    k "***** 翻译: 好吧 我来清理垃圾"
    hide kenny
    show mr at truecenter
    stop music fadeout 0.5
    play sound plate fadein 0.5
    mr "太好了! 我就知道你是一个好孩子! 你先清理那边的--"
    with vpunch
    with hpunch
    k "...!!??"
    mr "叹气..."
    play music christmas fadein 0.5
    k "****** 翻译: 那是什么动静?"
    n "亲~~~~爱的! 门外的是谁! 是送布娃娃的~~~来了吗?"
    mr "那是我可爱的妻子--奥颂! 她靠伏特加过圣诞"
    n "而这里... 每天!都是圣诞节~~~"
    hide mr with dissolve

    show kenny lookright
    n "孩子的... 嗝! 新布娃~~娃还没做好~~吗??"
    with hpunch
    n "你! 能不能办事效率高一点 孩子天天..吵着要!!"
    show kenny lookleft
    with hpunch
    mr "那不是你的责任吗!?"
    show kenny lookright
    n "没有啊~~~~ 我又不会缝!补~~"
    show kenny lookleft
    with hpunch
    mr "要不是你!之前吐在布娃娃身上!!"
    show kenny sleepy
    with hpunch
    n "你她娘的..吼我!!你居然敢!!!!!"
    show kenny lookleft
    mr "抱歉肯尼 我只是实话实说 我来处理这一切吧"
    show kenny lookright
    with hpunch
    n "你处理什么！你连个下水道都修不好！你二十年了修好过什么！"
    show kenny lookleft
    with hpunch
    mr "你喝醉了，你什么都不知道！"
    show kenny lookright
    with hpunch
    n "我喝醉是因为你--！因为你我他妈才喝醉的！"
    show kenny lookleft
    with hpunch
    mr "你认识我之前就喝了!"
    show kenny sick
    with hpunch
    n "那是因为我预感到我会认识你！"
    mr "...."
    show kenny sleepy
    mr "肯尼, 你现在外面等一下"
    hide kenny with dissolve
    "汉基先生扶着喝醉的妻子送进了他在下水道的房子"
    show mr at truecenter
    with dissolve
    mr "孩子 你也跟着进来吧"
    "肯尼进入了汉基先生的房子"
    scene bg room
    with fade
    show mr at right
    show kenny lookup at left
    pause 0.5
    with None
    show kenny lookright
    mr "正如你所见 我的小孩急需一个布娃娃玩具"
    with hpunch
    n "我急需更多的伏特加!!!!!!"
    mr "好吧 孩子 你身上有类似的东西吗?"
    if toy:
        menu ifhat:
            "交出Mr.Hat":
                jump end5
            "不交出":
                jump end6
    else:
        k "******** 翻译: 抱歉 我没有那种东西"
        jump end6
    label end5:
        show mr 
        show hat:
            zoom 0.4
            xalign 0.5
            yalign 0.5
    with dissolve
    "失去道具-- Mr.Hat"
    hide hat with dissolve
    $ toy = False
    mr "哦里哈! 太好啦!!"
    mr "真是太感谢你了孩子"
    mr "为了补偿你 我这还有根香蕉就免费给你吧!"
    mr "本来想请你帮忙收拾垃圾的 现在不用啦!!"
    hide mr
    show kenny lookleft at center
    with dissolve
    with hpunch
    n "你给他香蕉干嘛！那是我的香蕉！"
    show kenny lookright
    with hpunch
    mr "你又不吃香蕉！"
    show kenny lookleft
    with hpunch
    n "我不吃！但我也不给你！那是我的！"
    show kenny lookright
    with hpunch
    mr "那是我从超市买的！"
    show kenny lookleft
    with hpunch
    n "你买的！你什么时候买过东西！你有钱吗！"
    show kenny sleepy
    with hpunch
    mr "我有--"
    with hpunch
    n "你有个屁！你兜里比下水道还干净！"
    mr "..."
    show kenny lookright
    mr "肯尼, 拿着香蕉 快走吧..."
    k "*激动* 哦吼!!!"
    scene bg black
    with fade
    "肯尼高兴地拿着香蕉爬出肮脏的下水道后..."
    "肯尼把那根香蕉吃了 他太饿了, 所以他不在乎上面有什么"
    k sick "**!*******!!!"
    show kenny angry with dissolve
    "翻译: *俚语*你这香蕉皮上怎么还沾屎啊!!!"
    hide kenny with dissolve
    "..."
    "肯尼没有变得有钱, 但他那天晚上没有饿肚子"
    "这或许是本集唯一一个肯尼吃到东西的结局"
    "结局五-- 香蕉味的排泄物"
    $ unlock_ending("end5")
    menu:
        "回到上一个选项":
            hide kenny
            scene bg room
            show mr at right
            show kenny lookleft at left
            jump ifhat
        "回到主菜单":
            return

    label end6:
        mr "哦不 孩子..."
        show kenny sleepy 
        mr "好吧... 那你只能去打扫垃圾了 辛苦你了"
        show kenny lookleft
        with hpunch
        n "你让他打扫垃圾？你确定？上次那个小孩打扫垃圾，掉进污水里淹死了！"
        show kenny lookright
        with hpunch
        mr "那是他自己跳下去的！"
        show kenny lookleft
        with hpunch
        n "他为什么跳下去！"
        show kenny lookright
        with hpunch
        mr "因为他想帮我们捡布娃娃！"
        show kenny sleepy 
        with hpunch
        n "布娃娃掉污水里了？"
        with hpunch
        mr "对!"
        with hpunch
        n "那你还让这个小孩去打扫垃圾！"
        with hpunch
        mr "我没有让他跳下去"
        with hpunch
        n "你让他打扫垃圾！垃圾在污水旁边！污水里有布娃娃！"
        with hpunch
        mr "那是另一回事！"
        show kenny lookright
        mr "肯尼，你别听她的 她很激动, 她喝多了"
        scene bg under
        with fade
        stop music fadeout 0.5
        play music under
        show kenny sick at left
        "肯尼无可奈何，只能重新回到又脏又臭的下水道水沟"
        play sound bag
        k sleepy "******* 翻译：天哪，我居然还是逃不掉清理下水道的活儿……"
        "肯尼挽起衣袖，硬着头皮弯腰，伸手捞起水面上一团团漂浮的垃圾"
        "浑浊发绿的污水不时溅到肯尼的裤腿与手臂，那股难闻的臭味浸透了他的衣服"
        scene bg under
        with fade
        "时间一点点流逝，水沟里面堵塞的杂物终于全部清理干净，水道重新通畅"
        show mr at truecenter
        with dissolve
        mr "哇，干得相当不错！水沟已经疏通开啦！"
        mr "既然你踏踏实实付出劳动，这是属于你的酬劳"
        hide mr 
        show money 2:
            zoom 1.5
            xalign 0.5
            yalign 0.4
        with dissolve
        "获得道具-- 6美金"
        hide money
        show kenny sleepy
        k "*松一口气* ******* 翻译：终于挣到钱！这下可以去买幸运香蕉了！"
        hide kenny
        play sound drop
        "肯尼顺着铁梯子爬出阴森的下水道, 他身上现在沾满下水道的污秽气味"
        with hpunch
        with vpunch
        k "....!???"
        play sound drop2
        scene bg black
        with fade
        "肯尼身体失去重心，从高高的管道上面直直向后摔落！"
        play sound bone
        "他重重砸进下方浑浊翻滚的墨绿色污水之中！"
        show kenny dead 
        with dissolve
        "哦不 可怜的肯尼"
        hide kenny
        "..."
        "六美金沉到了下水道底"
        "肯尼的尸体在下水道里泡了三天, 第四天被水冲走了"
        "之后肯尼出现在学校操场, 没有人问他这几天去哪了"
        "结局六-- 下水道的悲剧"
        $ unlock_ending("end6")
    menu:
        "回到前一个选项":
            scene bg room
            stop music fadeout 0.5
            play music christmas
            show mr at right
            show kenny lookright at left
            jump ifhat
        "返回主菜单":
            return

label ball:
    stop music fadeout 0.5
    play music bigold
    scene bg ball
    with fade
    "中午-- 篮球场"
    "肯尼绕道来到学校后院的篮球场 空无一人"
    who "*叹气声*"
    k "...?"
    show kobe sit at right
    with dissolve
    "科比一个人坐在球场中线，脚边躺着一颗漏气的篮球"
    k "心想: 老大! 他怎么独自坐在那里"
    show kenny lookright at left
    with dissolve
    k "***** 翻译: 老大!? 你中午不休息坐在这干嘛!"
    with vpunch
    ko sit 1 "哦! my Man!"
    ko "这不是我的橘色兜帽小子肯尼吗!"
    ko sit "Oh My Bad... 我今天的训练计划泡汤了..."
    show kenny sick
    ko sit 2 "我每天中午都会加练后仰跳投, 今天一来，球直接瘪了, 完全没法打"
    show kobe sit 
    "科比低头凝视那颗泄气的篮球，双拳不自觉紧紧攥起，恨的肤色都黑了一号"
    show kenny lookright
    ko sit 3 "我什么都做不了 Bro..."
    ko sit 4 "我不甘心就这样中断训练 距离校内选拔赛已经越来越近"
    show kenny sleepy
    ko sit 1 "可我现在就像失去螺旋桨的飞机, 只能重重地摔在地上 shit!!!"
    with hpunch
    ko sit 4 "WHAT CAN I SAYYY??"
    k angry "******* 翻译: 这个破学校就没什么备用球了吗"
    ko sit 2 "体育老师不在,备用球全部锁在仓库"
    ko sit "我现在一分钱都没有"
    show kenny sleepy
    "面对昔日威风的老大沦落至此,肯尼决定..."
menu:
    "交出仅有的0.5美金 帮助老大":
        jump yes
    "无能为力,继续自己找赚钱机会":
        jump no

label yes:
    $ kobe_help = True
    k normal "******* 翻译：我这里刚好有攒的钱，先借你用吧"
    ko sit 1 "Thanks MY man"
    with vpunch
    show kenny lookright
    ko sit 2 "但是老大从来不白拿任何人东西"
    ko sit 3 "如果你能想办法打开仓库的门 获得篮球带给我的话"
    ko sit 4 "老大绝对不会浪费这次机会 这次选拔赛 我必须赢!"
    ko sit 3 "你知道为什么我必须赢吗？"
    k lookright "**** 翻译: 为什么?"
    with vpunch
    ko sit 2 "因为我小女儿和老婆在看, 她们答应来看我打选拔赛"
    ko sit 3 "老婆说如果我再输，她就带小孩回娘家"
    ko sit "所以我必须赢 Bro，你懂吗？我必须赢"
    k "..."
    ko sit "拜托了 这是老大第一次求人"
    "接受任务-- 想办法打开仓库"
    ko sit 2 "再次感谢你 小子"
    hide kobe with dissolve
    k lookleft "看来得去一趟仓库了"
    hide kenny with dissolve
    "肯尼默默离开篮球场"
    jump class3

label no:
    k lookright "******* 翻译：抱歉老大……我现在也很缺钱，要攒钱买幸运香蕉"
    ko "我理解 每个人都有自己要拼的东西"
    ko sit 3"我也是 哪怕球瘪了我也练脚步--"
    hide kobe 
    with dissolve
    "科比站起身，顶着正午大太阳，原地一遍遍练脚步 出手姿势 滞空动作"
    "哪怕没有球，他也一秒不休息"
    show kenny lookleft
    k "还是去别处看看吧"
    hide kenny 
    with dissolve
    "正午的球场依旧空旷安静, 肯尼默默转身离开"
    "..."
    "科比后来在那次选拔赛上输了"
    "因为没有球训练，他的状态下滑了百分之六十九 他从此再也没能回到巅峰"
    "因为愧对于妻子, 他私自带着小女儿乘坐直升机回家"
    "后来的事情, 你们也知道了"
    "..."
    "而肯尼，至死都不知道自己曾经离改变一个人的命运那么近"
    jump class3

menu class3:
    "先回一趟教室":
        jump class4
    "直接前往仓库":
        jump gate

label class4:
    stop music fadeout 1.0
    play music class1
    scene bg class 2
    with fade
    "中午-- 走廊"
    if weddy_help and note:
        show weddy normal 1
        with dissolve
        "温迪出现在走廊"
        show kenny lookright at left
        show weddy left 1 at right
        with dissolve
        w "嗨! 中午好 肯尼"
        k "*** 翻译: 中午好 温迪"
        w left 5 "嗨.. 那个.. 肯尼 你还记得上午我拜托你的事情吗?"
        show kenny lookup
        w left 6 "关于我失踪笔记本的事情..."
        show kenny sick
        w left 7 "我还是没找到它的下落"
        show kenny lookright
        w left 2 "我想说"
        w left 3 "你有发现什么线索吗 肯尼?"
        "肯尼的回答是..."
        menu:
            "交出笔记本":
                jump give_note
            "私吞笔记本":
                jump no_note
    elif weddy_help: 
        show weddy normal 1
        with dissolve
        "温迪出现在走廊"
        show kenny lookright at left
        show weddy left 1 at right
        with dissolve
        w "嗨! 中午好 肯尼"
        k "*** 翻译: 中午好 温迪"
        w left 5 "嗨.. 那个.. 肯尼 你还记得上午我拜托你的事情吗?"
        show kenny lookup
        w left 6 "关于我失踪笔记本的事情..."
        show kenny sick
        w left 7 "我还是没找到它的下落"
        show kenny lookright
        w left 2 "我想说"
        w left 3 "你有发现什么线索吗 肯尼?"
        k sick "***** 翻译: 抱歉 我这边也没有线索"
        show kenny lookright
        w left 5 "糟糕..."
        w left 6 "那我还是去别处找找吧"
        w left 7 "再见了肯尼"
        hide weddy with dissolve
        k "心想: 可惜没能找到笔记本呢"
        k lookleft "前往仓库转转吧"
        hide kenny with dissolve
        jump gate

    else:
        "走廊人空空的,什么事情都没发生"
        k "直接去仓库吧"
        jump gate

label no_note:
    k sick "***** 翻译: 抱歉 我这边也没有线索"
    show kenny lookright
    w left 5 "糟糕..."
    w left 6 "那我还是去别处找找吧"
    w left 7 "再见了肯尼"
    hide weddy with dissolve
    k "心想: 总觉得笔记本能在其他地方派上用场"
    k lookleft "前往仓库转转吧"
    hide kenny with dissolve
    jump gate
label give_note:
    k "****** 翻译: 我发现它了在--"
    show kenny sick
    "肯尼想起了翻垃圾桶时不愉快的回忆..."
    k "** 翻译: 算了 管他呢"
    "失去道具-- 温迪的笔记本"
    $note = False
    w left 4 "哦! 天呐 我是说 谢谢你!!"
    w left 3 "这个给你 说不定对你有帮助"
    show torch:
            zoom 0.4
            xalign 0.5
            yalign 0.5
    with dissolve
    "获得道具-- 手电筒"
    hide torch
    $ torch = True
    w left 1 "肯尼 你真是个大好人!"
    hide weddy
    with dissolve
    show kenny normal 
    "等温迪离开后"
    stop music fadeout 0.5
    play sound laugh2
    k sick "******** 翻译: GodDamn! 那个女人居然不给我钱!!"
    play music class1 fadein 1.0
    k sleepy "心想: 算了 留着吧 说不定有什么用"
    jump gate

label gate:
    stop music fadeout 1.0
    play music wind2
    scene bg gate
    with fade
    "中午-- 仓库大门外"
    "仓库外的过道上，呼啸的穿堂风卷着地上细碎的纸屑与灰土来回打着旋"
    "乌云压得很低，天色昏沉沉的，一阵一阵的大风刮过，连墙角的碎石子都被吹得滚动"
    k "就是这里了,仓库! 希望可以找到些什么"
    k "...?"
    stop music fadeout 1.0
    play music goth1 fadein 1.0
    show red right 
    show goth high at right
    with dissolve
    "两名哥特学生斜倚在门口，堵住了门"
    "哥特帮的孩子们都是刻板的哥特文化追随者"
    "他们几乎不去上学，更喜欢整天闲坐着，抽抽烟，喝喝咖啡"
    "他们总是谈论着生活是多么痛苦及没有意义"
    "他们家一般都挺有钱的"
    with None
    show kenny lookright at left
    k "**** 翻译:啊...你们好?"
    show goth 1
    with hpunch
    pe left 3 "嘿 这人是谁?"
    show red left 1
    m 2 "这大概就是人们常说的鲜嫩小屁孩"
    show kenny angry
    pe left 2 "快滚开小鬼 这里是歌特帮的地盘"
    pe left 4 "只有哥特酷小孩才能进入"
    show goth high
    show kenny sick
    m 3 "皮特, 别那么快拒绝 先听听他要什么"
    pe amazed "他要进去"
    m 4 "我知道他要进去, 但我们要先羞辱他, 这是流程"
    pe left 1 "哦对 抱歉"
    m high "你想进仓库?"
    k sleepy "*** **** 翻译: 求求你了 让我进--"
    m 1 "为什么?"
    k lookright "我想找点东西"
    pe left 2"就你这样的, 你说你要找东西?"
    show goth 1
    pe left 2 "不可能! 我们不可能按照你的要求去做"
    show goth high
    show kenny lookright
    pe left 3 "看看你这身打扮 从头发到鞋子 一副穷小孩的样子"
    pe left 4 "你根本就不懂什么是酷--"
    show goth 1
    show kenny sick
    pe left 2 "什么是黑暗!!!!"
    m 3 "你以为黑暗是穷吗"
    show red right
    show kenny sick
    pe left 2 "是啊 小屁孩 告诉你吧"
    pe "黑暗是每天早上醒来，发现自己的生活毫无意义"
    pe left 4 "黑暗是坐在教室里，听着老师讲那些你永远不会用到的东西"
    show red right
    m high "黑暗是看着你爸开着宝马去上班，你妈在瑜伽课上跟别的男人调情"
    m 1 "你那种穷，那种饿，那种死来死去——"
    m 4 "那叫惨 不叫黑暗"
    pe left 1 "说得对!"
    m 3 "穿上正确的服装, 拿着咖啡杯, 叼着香烟再来找我们吧"
    show goth high
    pe left 1 "嘻嘻嘻嘻嘻"
    show kenny lookright
    "肯尼陷入了困境 此时他应该..."
    if note:
        menu:
            "交出温迪的笔记本":
                jump goth1
            "尬聊黑暗":
                jump goth2
    else:
        menu fire:
            "尬聊黑暗":
                jump goth2
            "正面冲突":
                jump goth3

label goth3:
    with hpunch
    k angry "****! 翻译: 你们俩几把谁啊!"
    show red left 3
    m normal "什么?"
    k "两个嘉豪!"
    "肯尼这句说的很清楚"
    pe "你死定了!"
    show red at left with dissolve
    show kenny sick
    hide kenny
    with dissolve
    with hpunch
    "皮特推了肯尼一把"
    show goth read
    with vpunch
    k sick "啊!"
    m read "皮特! 别动手!"
    "迈克尔举手想拦, 手里夹着烟斗"
    show kenny fire 1 at left
    show red left 4 at center
    show goth read 2
    with dissolve
    "烟斗滑了出去 砸在肯尼肩膀上"
    with vpunch
    k "啊啊啊啊!!!"
    "肯尼吓了一跳，往后退"
    play sound boom2
    "*咣当*"
    show kenny fire 2
    with hpunch
    "肯尼脚后跟撞到垃圾桶"
    "垃圾桶倒了, 里面的酒洒在肯尼衣服上"
    with vpunch
    k "啊啊啊啊啊啊啊啊啊!"
    "火顺着裤子往上爬, 肯尼往后退"
    "退到墙壁, 附近还有三个油桶"
    with vpunch
    pe "快---"
    with vpunch
    m read 3 "跑!!!!!!"
    play sound boom2
    scene bg black
    with vpunch
    scene bg fire
    with hpunch
    "*剧烈的爆炸*"
    play sound boom2
    "..."
    play sound boom2
    scene bg black
    with fade
    "消防车来的时候，仓库已经烧了一半"
    "皮特和迈克尔都受到了中度烧伤 被紧急送往南方公园医院治疗"
    scene bg kenny
    with fade
    "消防员最后找到了肯尼的橙色兜帽"
    "他妈来认尸, 看了一眼就走了"
    "他妹把兜帽带回家，挂在墙上"
    "..."
    "我们学到了什么--"
    "不要玩火, 我的朋友们"
    "结局八-- 肮脏的烟火"
    $ unlock_ending("end8")
    menu:
        "回到上一个选项":
            scene bg gate
            show red left 1
            show goth high at right
            show kenny lookright at left
            jump fire
        "回到主菜单":
            return


label goth1:
    "失去道具-- 温迪的笔记本"
    $ note = False
    show goth 1
    k angry "****** 翻译: 等一下! 你们看这个"
    pe left 1 "...? 一本肮脏的笔记本"
    m normal "有趣... 递给我看看有多酷..."
    "肯尼把脏兮兮的笔记本递了过去"
    show red left 3
    "肯尼把温迪遗落的笔记本递过去,哥特头目迈克尔接过来随手翻开"
    hide kenny
    hide goth
    hide red
    with dissolve
    show goth read 
    m read "...嗯..."
    m "...嗯"
    hide goth
    show red amazed 2
    pe amazed 2 "..哦?"
    hide red
    show goth read 2
    with vpunch
    m read 2 "...哈!.."
    hide goth
    show red amazed
    pe amazed "..啊..?!"
    hide red
    "一页又一页，迈克尔越往下翻阅，神情渐渐严肃"
    show goth read 2
    with dissolve
    m "*咋舌*...天哪..."
    m read 3 "这居然是学校学生写的!"
    with vpunch
    m 4 "你听这段——"
    "我每天早上醒来，第一件事就是问自己，我为什么要活着"
    "答案是没有答案, 但我不在乎, 因为问这个问题本身就是活着的意义"
    hide goth
    show red amazed 2
    pe amazed 2"哇~!"
    hide red
    show goth read 3
    with vpunch
    m "还有这段--"
    show goth read 4
    "他们告诉我，我要做一个好女孩 好女孩要温柔，要体贴，要会做饭"
    "我想问，如果我不想做呢？如果我想做一个坏女孩呢？如果我想在午夜十二点穿着黑裙子在街上抽烟呢？"
    m read 4 "我以为这所学校全是麻木的乖乖学生"
    m "没有想到学校里面居然有人思考如此深刻..."
    m "能写出这么厌世, 清醒的东西"
    with vpunch
    pe "这他妈太酷啦!"
    with vpunch
    m 4 "这他妈才是黑暗!"
    show red amazed 
    show goth normal at right
    show kenny lookright at left
    with dissolve
    m 4 "行吧 这份文字值得尊重, 够格踏入黑暗 你可以进去, 我们不会拦你了"
    m 3 "皮特, 让他进去吧"
    pe left 3 "破例一次"
    "..."
    "顺便说一句--"
    "后面的内容全是如何用微波炉做蛋糕, 如何叠出漂亮的餐巾花"
    "但迈克尔没往后翻, 他翻到第二页就哭了"
    jump open1


label goth2:
    show goth 1
    show red left 3
    with vpunch
    k angry "****！翻译：我可去你们的吧！以为成天摆张臭脸喝咖啡抽大烟就叫黑暗？"
    k "我比你们更懂黑暗!"
    show goth normal
    k sick"我已经死过好多回了 车祸、失火、各种各样离奇的死法"
    k lookup"前一秒刚刚咽下最后一口气，第二天又醒过来继续熬日子"
    k angry"每一天都在重复忍受窘迫,饥饿还有旁人的嘲笑!"
    k sick"眼睁睁看着家里一团糟，看着父母无休止地争吵，而我还有个妹妹要带"
    pe left 4 "哇哦..."
    pe "*眉毛一挑，原先嘲讽的笑意僵在脸上*"
    show goth normal
    "迈克尔抱着胳膊,斜着眼打量着肯尼,依旧保持着一副嘉豪姿态"
    "他没有突然深沉,只是有点被噎住"
    show red right
    m 3 "行啊,听上去够惨的"
    show kenny lookright
    m 4 "但别误会,我可不是被你的悲惨经历打动了"
    m 2 "只是...呵 我在想--"
    k "*** 翻译: 什么?"
    show red amazed
    m "我在想, 如果我是你 我早自杀了"
    k sleepy "..."
    m read 2 "我是认真的 我他妈每天坐在家里喝咖啡，我都想自杀"
    show kenny lookright
    m read 4 "你都死了几百次 还想着整点事情做"
    m read 3 "你他妈比我有种多了"
    pe "迈克尔, 你说这个干嘛!"
    with hpunch
    m 3 "我说的是实话"
    pe "哥特帮从不说实话！哥特帮只会说生活毫无意义！"
    with hpunch
    pe "妈的 你疯了!"
    with hpunch
    m 2 "我清醒得很！"
    show red left 3
    pe "..."
    m high "算了皮特 放他进去--"
    show red right
    m read "但是记住! 不要到处嚷嚷是哥特帮放你进去的！我可不想别的蠢货学你！"
    pe "切!"
    "皮特不情愿地让出了位置"
    "..."
    "后来迈克尔承认那天--"
    "单纯是自己抽high才放过肯尼"
    jump open1

label open1:
    scene bg black
    with fade
    stop music
    "肯尼推开仓库的门"
    play sound door
    with vpunch
    k "...!"
    "*门突然被关上的声音*"
    "肯尼回头, 漆黑一片"
    k "****!! 翻译: 喂! 放我出去"
    "没有人回答, 哥特帮的声音从墙那边传过来，但听起来很远"
    "房间内寂静得很, 没有灯光"
    k "心想: 什么都看不见..."
    if torch:
            play sound torch
            "肯尼打开了手电筒"
            "使用道具-- 手电筒"
            scene bg office
            with fade
            play music office
            "光柱切开了黑暗, 仓库里的东西一样一样显出来"
            "肯尼回头--"
            "原来门的位置只剩下一面普普通通的 刷着白漆的墙"
            "上面放着奇怪的熊形玩偶服宣传海报"
            k "心想: 门呢?"
            "然后光柱照到了一个纸箱"

            if kobe_help:
                "肯尼打开了纸箱"
                show ball at truecenter:
                    zoom 1.3
                with dissolve
                "获得道具-- 篮球"
                $ ball = True
                hide ball
                with dissolve
                k "心想: 得拿回去给老大"
                "然后光柱照到了另一个纸箱"
                jump office1
            else:
                label office1:
                    k "...?"
                    "纸箱上写着幸运香蕉——卡特曼企业"
                    "纸箱里面是空的 旁边有一张进货单--"
                    "普通香蕉，一箱三十根，进货价十五美金 平均每根--"
                    with vpunch
                    k "心想: 五毛钱!"
                    "卡特曼一根卖五块八 利润率是百分之91.3.8.0.0.0.0.0"
                    "肯尼站在仓库里，盯着那张进货单看了很久"
                    "然后他看见了另一样东西 在纸箱下面，压着一张手写的纸--"
                    "上面写着卡特曼的营销计划："
                    c "第一步：散布幸运香蕉的传说"
                    c "第二步：让凯尔先买，凯尔会跟所有人说"
                    c "第三步：饥饿营销，每天只卖十根"
                    c "第四步：涨价"
                    c "第五步：推出会员制，月费三块，可以优先购买"
                    c "第六步：推出幸运香蕉保险，如果吃了没效果，可以退一半钱，但要先交两块保险费"
                    "最后一行写着--"
                    c " 第七步：等所有人都买就跑路 反正我四年级"
                    with vpunch
                    k "这个死肥猪!"
                    play sound door
                    "肯尼这句话说的很清楚"
                    "肯尼回头 门不知何时又出现了"
                    "肯尼把进货单折起来，塞进兜里 离开了仓库"
                    jump cartman
    else:
        "肯尼走了三步--"
        " 第一步, 他听见自己的脚步声"
        "第二步, 他听见自己的呼吸声"
        "第三步, 他什么都听不见了"
        "然后他看见了一扇门--"
        "那扇门异常地亮, 亮得不像是一扇门 像是有人把太阳塞进了门框里"
        "肯尼朝那扇门走去"
        play sound drop3
        with vpunch
        k "...!!!"
        "肯尼一脚踩空 整个人向前栽下去, 他伸手想抓什么, 什么都没抓到"
        "..."
        play music backroom fadein 0.5
        scene bg backroom
        with pixellate
        with vpunch
        "*落地声*"
        show kenny sick with dissolve
        k "!!!"
        "湿漉漉的地板很好地接住了肯尼的脸"
        "他闻到了味道 潮湿的, 发霉的, 像地下室一样的味道"
        "未知时间-- LEVEL 0"
        show kenny lookup
        "他抬起头--"
        "荧光灯在他头顶嗡嗡响"
        show kenny lookleft
        "天花板是黄色的 墙是黄色的 地毯是黄色的"
        show kenny lookright
        "房间向四面八方延伸，看不到尽头"
        k "**** 翻译: 这是什么鬼地方?"
        with hpunch
        k "***! 翻译: 有人吗?"
        "没有人回答"
        k sleepy "心想: 我感觉真的很不好"
        "..."
        "肯尼知道 他得想办法出去--"
        "但肯尼出不去了 或者说出口在别的地方 要找到出口救需要运气"
        "如果他有好运，他就会有一个手电筒"
        "但他没有手电筒, 所以他出现在这个地方"
        "*嗡嗡* *嗡嗡*"
        "..."
        "结局七-- 黄色的房间"
        $ unlock_ending("end7")
    menu:
        "回到主菜单":
            return

label cartman:
    stop music 
    play music last fadein 1.0
    scene bg gate
    with fade
    "肯尼走出仓库, 却不知有位在门口等候他多时"
    show cartman 2 at truecenter:
        zoom 0.75
    with dissolve 
    c "肯尼~ My Friend~~!"
    c "你能不能告诉我--"
    show cartman 4:
        zoom 1.5
    with None
    with vpunch
    c "你手里那张纸是什么呢?"
    k "..."
    c "我看见了!"
    with hpunch
    c "那张进货单, 是我的商业机密"
    show cartman 2 at truecenter:
        zoom 0.75
    with None
    c "现在的情况很简单..." 
    c "*叹息声*"
    c "你他妈完蛋了...肯尼"
    play sound gun1
    "卡特曼掏出一把手枪"
    "*上膛声*"
    with vpunch
    k "****!! 翻译: 我操! 你疯了吗!?"
    c "我没疯, 相反呢 我很清醒"
    c "你知道我为了这批香蕉投了多少吗？"
    show cartman 3 at truecenter:
        zoom 1.55
    with None
    with hpunch
    c "十五美金!整整十五美金!"
    with vpunch
    c " 我把所有库存都压上了, 我连我妈的信用卡都刷爆了"
    with vpunch
    c "你毁了我一个下午的销售额"
    c "所以--"
    show cartman 2 at truecenter:
        zoom 0.75
    with None
    with hpunch
    c "你他妈就是个混蛋!"
    play sound gun2
    c "..."
    "卡特曼抬起手枪"
    with vpunch
    "*开枪声*"
    "子弹擦着肯尼的耳朵飞过去 打在仓库的墙上 溅出一串火星"
    play sound gun1
    k "*****! 翻译: 你他妈真开枪啊!!"
    c "废话 我说了要杀了你"
    play sound gun2
    c "..."
    c "你以为我在和你开玩笑?"
    with vpunch
    "*开枪声*"
    "这次终于打在肯尼脚边 地上炸开一小撮土"
    play sound gun1
    "面对持枪的卡特曼 肯尼选择..."
menu lastchoice:
    "逃跑":
        jump run
    "谈判":
        jump negotiate

label negotiate:
    with hpunch
    k "**!! 翻译: 等等!!"
    show cartman 3 at truecenter:
                            zoom 1.55
    with None
    c "等什么?"
    k "****** 翻译: 我把进货单还你! 你放我走!"
    c "..."
    "卡特曼歪着头 想了几秒"
    show cartman 2 at truecenter:
                            zoom 0.75
    c "好吧"
    c "你把进货单给我 我会考虑放过你"
    k "**! 翻译:真的?"
    c "我说了 我会考虑"
    "肯尼掏出那张皱巴巴的进货单 递给了卡特曼"
    c "好朋友"
    "卡特曼接过 打开看了一眼 折好塞进兜里"
    k "***** 翻译: 那我现在可以走了吗"
    "肯尼转身打算跑路"
    show cartman 4:
                zoom 1.5
    with None
    c "..."
    c "肯尼"
    c "你知道我刚才为什么要想几秒吗?"
    k "...?"
    c "我在想 你有没有告诉别人"
    c "现在确认了 你没有告诉任何人"
    c "因为你刚才还在拿它换命"
    c "所以这件事情 只有你和我知道"
    "卡特曼举起枪"
    with hpunch
    k "****** 翻译: 你说了会考虑放过我"
    with vpunch
    c "我说了我会考虑"
    c "我考虑了--"
    play sound gun2
    c "我决定不放"
    hide cartman
    with vpunch
    with hpunch
    "*开枪声*"
    "子弹打中肯尼的胸口 他往后倒下 直直地摔在仓库门口"
    "橙色的兜帽散开 盖住了脸"
    "卡特曼掏出进货单 撕成碎片 扔在尸体上"
    c "商业机密只有一个人知道 才叫商业机密"
    scene bg black
    with fade
    play sound plane
    "三分钟后"
    "*螺旋桨声*"
    ko "肯尼...?"
    with hpunch
    ko "nonoNONOOO!"
    with hpunch
    ko "PLEASE!"
    ko "肯尼 别睡着!!"
    with hpunch
    ko "有人吗!!! 这里有人中枪了!!!"
    "肯尼最后一次睁开眼睛--"
    "然后他闭上了"
    "结局十一 -- 背叛"
    $ unlock_ending("end11")
menu:
    "回到上一个选项":
        scene bg gate
        show cartman 2 at truecenter:
                                zoom 0.75
        jump lastchoice
    "回到主菜单":
        return





label run:
    "肯尼转身就跑"
    c "跑啊! 你跑啊!"
    c "我看你往哪跑!"
    play sound gun2
    "肯尼往操场方向跑 卡特曼在后面追"
    "一个四年级的胖子举着枪 追一个穿橙色兜帽的穷小孩"
    with vpunch
    "*开枪声*"
    play sound gun1 
    c "操! 我这枪准星是歪的!"
    k "******* 翻译: 你这枪也是偷的?"
    c "关你屁事!"
    play sound plane
    "然后--"
    "天上"
    with vpunch
    stop music fadeout 0.5
    play music bigold
    who "肯尼!!!!"
    c "...?"
    "*螺旋桨音效*"
    scene bg sky
    with fade
    show plane at truecenter:
        zoom 2.8
    with dissolve
    "..."
    show kobe plane
    with dissolve
    ko "My man! 肯尼!"
    ko "我找你半天了!"
    ko "快上来!!"
    scene bg gate
    with fade
    "直升机开始下降 螺旋桨搅起的风吹得卡特曼的肥肉乱颤"
    show cartman 3 at truecenter:
        zoom 1.55
    c "shit! God Damn!!"
    k "*******! 翻译: 老大你怎么来了?"
    ko "我看见他跟着你!"
    k "他他妈要杀我!!"
    "肯尼这句话说的很清楚"
    ko "什么!?"
    show cartman 2 at truecenter:
        zoom 0.75
    with None
    c "科比, 这不关你的事"
    with hpunch
    ko "你他妈拿枪指着我的man 叫不关我的事?"
    c "*叹息声*"
    with vpunch
    show cartman 3 at truecenter:
        zoom 1.55
    play sound gun2
    c "他不是你的兄弟! 他就是个臭翻垃圾桶的!"
    "*开枪声*"
    "子弹打穿了直升机的后窗"
    ko "肯尼!快!!"
    hide cartman
    "肯尼冲过去 抓住了起落架"
    "卡特曼站在地上 举着枪 看着他们飞走"
    stop music fadeout 0.5
    play music last fadein 0.5
    c "..."
    show cartman 3 at truecenter:
        zoom 1.55
    with None
    with vpunch
    with hpunch
    c "肯尼!!!!!"
    c "你以为你能跑走吗?"
    "卡特曼一把抓住起落架 跟着爬上了"
    show cartman 4:
        zoom 1.5
    with None
    c "我做买卖从来不亏本"
    c "今天你死定了"
    scene bg sky
    with fade
    show plane at truecenter:
        zoom 2.8
    with dissolve
    with hpunch
    "直升机开始摇晃"
    z "科比! 我们的尾桨出现问题了!"
    z "我要迫降!"
    c "不准迫降! 我要先解决肯尼!"
    with vpunch
    with hpunch
    "直升机剧烈倾斜"
    "肯尼死死抓住起落架"
    "卡特曼也死死抓住"
    "风很大 下面是一片树林"
    if ball:
        "此时肯尼想起了他兜里的东西"
        "科比让他拿的那个篮球!"
        k "老大!!"
        ko "What??"
        k "接住!!!!"
        show ball at truecenter:
                            zoom 1.3
        with dissolve
        "科比从兜里掏出篮球"
        hide ball with dissolve
        "科比把球砸向卡特曼"
        with vpunch
        c "什么--"
        with hpunch
        "篮球正中卡特曼的脸"
        "卡特曼手一松 他掉了下去"
        with vpunch
        with hpunch
        c "饿啊!!!!"
        show cartman 3 at truecenter:
            zoom 1.55
        with dissolve
        c "哦 shit..."
        with vpunch
        with hpunch
        c "肯尼!!!!!!"
        with vpunch
        with hpunch
        c "我他妈一定会报仇的!!!"
        hide cartman with dissolve
        play sound leaves
        "卡特曼的声音被螺旋桨盖住"
        "他掉进下面的灌木丛里"
        "灌木丛里传来一声闷响"
        "然后是一声惨叫"
        c "啊啊啊啊!!! 我的胃袋!!!!!!!"
        "直升机飞远了"
        "..."
        scene bg black
        with fade
        stop music
        play music song
        "肯尼最后安全地回到了南方公园"
        "他把进货单贴在了学校公告栏上"
        "卡特曼的香蕉生意当天就破产了"
        "卡特曼在灌木丛里躺了三个小时 才被人发现"
        "他的腿断了 打了石膏 现在拄了拐杖"
        "但他没有选择报警"
        "因为如果报警 警察就会发现他的枪"
        "所以 从中我们学到了什么--?"
        c "我学到了 不要相信穷人 他们会偷你的东西"
        k "我学到了 钱不是最重要的"
        ky "我学到了 卡特曼是个混蛋"
        c "你他妈!!"
        "TRUE END"
        "结局十-- 帮助"
        $ unlock_ending("end10")
        "感谢您的游玩"
        "本集完"
        return

    else:
        "但肯尼兜里什么都没有"
        "没有篮球 没有道具 什么都没有"
        "只有一张进货单"
        if note:
            "哦 还有一本笔记本"
            "但这有什么用呢?"
            jump badend
        elif toy:
            "什么 还有Mr.Hat?"
            "这玩意你留着干什么呢?"
            jump badend
        else:
            label badend:
                            "卡特曼爬到起落架上 举枪对准肯尼"
                            show cartman 2 at truecenter:
                                                        zoom 0.75
                            with dissolve 
                            c "卡特曼爬到起落架上 举枪对准肯尼"
                            play sound gun2
                            c "撒由那拉 肯尼"
                            hide cartman
                            with vpunch
                            "*开枪声*"
                            with vpunch
                            with hpunch
                            k "啊啊啊啊!"
                            "肯尼躲开了"
                            with hpunch
                            with vpunch
                            stop music fadeout 0.5
                            play music bigold
                            "但直升机猛地一晃"
                            "子弹打中了佐巴扬"
                            with hpunch
                            with vpunch
                            z "啊啊啊啊啊!!!"
                            z "...!"
                            "佐巴杨的头歪了下去 他的手从操作杆上滑落"
                            with hpunch
                            ko "佐巴扬!!"
                            "佐巴扬没有回答"
                            with vpunch
                            with hpunch
                            "直升机开始旋转"
                            ko "nonoNONOOOOOOOO!"
                            "科比扑向操作杆 但是太晚了"
                            "尾桨坏了 飞行员死了 后面还有个死胖子在开枪"
                            show cartman 3 at truecenter:
                                                        zoom 1.55
                            with dissolve
                            with vpunch
                            c "科比!拉起来!快拉起来!"
                            "众所周知 科比不会开飞机"
                            "肯尼挂在起落架上 眼看就地面越来越近"
                            k "呜哇!!!!!!!!!!!"
                            ko "sorry kids"
                            c "不!!!!!!!!"
                            play sound boom2
                            scene bg black
                            with vpunch
                            scene bg fire
                            with hpunch
                            "*剧烈的爆炸*"
                            play sound boom2
                            "..."
                            play sound boom2
                            "一团火球升起来"
                            "黑烟 火光 碎片"
                            "开始时树冠烧着了"
                            "紧接着整片树林开始烧"
                            "..."
                            scene bg black
                            with fade
                            "三天后"
                            "消防员才把火扑灭"
                            "他们在烧焦的树林里找到了三具尸体"
                            "奇怪的是最后一具尸体 消防员找了很久"
                            "最终他们只找到了一顶橙色兜帽"
                            "虽然烧焦了 并且只剩一半 但还能看出来是橙色"
                            "从中我们学到什么--"
                            "孩子们不要相信佐巴扬"
                            ko "曼巴OUT"
                            "结局九-- 凌晨四点南方公园的太阳"
                            $ unlock_ending("end9")
                            menu:
                                "回到主菜单":
                                    return






    















        #简单的位置关键字left right center默认剧中 truecenter 水平居中

#关于image 必须包含 标签 和 一个以上的属性
#Ren’Py会在images目录下搜索图像文件，可以通过启动器(launcher)的“打开目录”选项里选择“images”完成配置。
#RenPy能使用PNG或者WEBP文件作为角色美术资源JPG、JPEG、PNG或者WEBP文件作为背景美术资源。文件的命名相当重要Renpy将使用除去扩展名后强制字母变为小写的文件名来作为图象名。

#scene语句 清楚所有的图像限时一个背景图像
#show语句显示任务 
# 给定tag标签时，每次只能展示一副图像。
# 当拥有同样tag标签的第二副图像需要展示时，它会直接替换第一副图像