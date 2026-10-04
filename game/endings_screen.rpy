screen endings_gallery():

    tag menu


    ## 内容
    frame:
        background Frame("#000000cc", 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 700
        padding (30, 30)

        vbox:
            spacing 12

            ## 标题
            text "结局图鉴" size 40 color gui.accent_color xalign 0.5
            null height 8

            ## 进度
            $ unlocked, total = get_unlock_progress()
            text "已解锁：[unlocked] / [total]" size 22 color gui.idle_color xalign 0.5
            null height 16

            ## 结局列表
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                ysize 480

                vbox:
                    spacing 10
                    xsize 1000

                    for e in endings_data:

                        if is_ending_unlocked(e["id"]):
                            frame:
                                background Frame("#ffffff22", 10, 10)
                                padding (20, 15)
                                xfill True

                                vbox:
                                    spacing 5
                                    hbox:
                                        spacing 10
                                        if e.get("true_end", False):
                                            text "★" size 24 color gui.accent_color
                                        text e["name"] size 26 color gui.accent_color
                                    text e["desc"] size 18 color gui.idle_color
                                    text "解锁方式：[e['hint']]" size 16 color gui.insensitive_color
                        else:
                            frame:
                                background Frame("#ffffff11", 10, 10)
                                padding (20, 15)
                                xfill True

                                vbox:
                                    spacing 5
                                    text "？？？" size 26 color gui.insensitive_color
                                    text "未解锁" size 18 color gui.insensitive_color

            null height 16

            textbutton "返回" action Return() xalign 0.5