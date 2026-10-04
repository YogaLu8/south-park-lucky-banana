# 结局图鉴数据
init python:
    endings_data = [
        {
            "id": "end1",
            "name": "失败的肯尼",
            "desc": "你放弃了。第二天你又来了。什么都没变。",
            "hint": "在操场上，选择放弃。"
        },
        {
            "id": "end2",
            "name": "擂台的可怜虫",
            "desc": "你走下擂台。后脑勺撞到了铁柱子。",
            "hint": "在拳击擂台上，选择认怂。"
        },
        {
            "id": "end3",
            "name": "金钱的泡影",
            "desc": "你赢了十万。你爸三天就花完了。",
            "hint": "在拳击擂台上，选择死斗。"
        },
        {
            "id": "end4",
            "name": "意外财物",
            "desc": "你掏到一沓钱。那是卡特曼的货款。",
            "hint": "在垃圾桶里，一直掏到底。"
        },
        {
            "id": "end5",
            "name": "香蕉味的排泄物",
            "desc": "你吃到了一根沾了东西的香蕉。至少你没饿肚子。",
            "hint": "在下水道，把 Mr.Hat 交给汉基先生。"
        },
        {
            "id": "end6",
            "name": "下水道的悲剧",
            "desc": "你掉进污水里。六美金沉到了底。",
            "hint": "在下水道，清理垃圾，但不交出 Mr.Hat。"
        },
        {
            "id": "end7",
            "name": "黄色的房间",
            "desc": "你推开一扇门。你切出去了。你在 Level 0。",
            "hint": "没有手电筒，进入仓库。"
        },
        {
            "id": "end8",
            "name": "肮脏的烟火",
            "desc": "迈克尔的烟斗掉了。油桶倒了。你烧起来了。",
            "hint": "在仓库门口，选择正面冲突。"
        },
        {
            "id": "end9",
            "name": "凌晨四点南方公园的太阳",
            "desc": "子弹打中了佐巴杨。直升机坠毁了。",
            "hint": "没有篮球，在飞机上逃跑。"
        },
        {
            "id": "end10",
            "name": "帮助",
            "desc": "篮球正中卡特曼的脸。他掉下去了。你活下来了。",
            "hint": "帮温迪拿手电筒，帮科比拿篮球。在飞机上逃跑。",
            "true_end": True
        },
        {
            "id": "end11",
            "name": "背叛",
            "desc": "你把发票交给卡特曼。他说他会考虑。他考虑完了。",
            "hint": "面对持枪的卡特曼，选择谈判。"
        },
    ]

init python:
    def unlock_ending(end_id):
        if end_id not in persistent.endings_unlocked:
            persistent.endings_unlocked.append(end_id)
            renpy.notify("解锁结局：" + get_ending_name(end_id))

    def get_ending_name(end_id):
        for e in endings_data:
            if e["id"] == end_id:
                return e["name"]
        return "???"

    def is_ending_unlocked(end_id):
        return end_id in persistent.endings_unlocked

    def get_unlock_progress():
        return len(persistent.endings_unlocked), len(endings_data)