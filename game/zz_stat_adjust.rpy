# -*- coding: utf-8 -*-
# ============================================================================
#  属性调节面板（独立模组，不改任何原文件）
#  - 游戏内按 F8 随时呼出 / 关闭，不打断剧情
#  - 显示并调节：威慑力(intimidation)、魅力(charisma)，点 −1 / +1 立即生效
#  - 剧情开关：劳伦路线切换、画廊解锁、分支结果勾选
#  - 卸载：删除本文件与 zz_stat_adjust.rpyc 即可
#
#  说明：
#   威慑/魅力只决定各分支的“门槛”，数值越高越好触发；
#   【劳伦淋浴】【劳伦爱情】与【劳伦+娜塔莉亚】是二选一路线，
#   由“劳伦路线”开关（freelauren）决定，和威慑/魅力数值无关。
# ============================================================================

init -1 python:

    # ---- 数值调节：威慑力 / 魅力，范围 0~99 ----
    def zz_clamp_stat(var_name, delta):
        value = getattr(store, var_name, 0)
        value = max(0, min(99, value + delta))
        setattr(store, var_name, value)
        renpy.restart_interaction()
        return value

    # ---- 劳伦路线：love=爱情(淋浴+爱情)，rise=崛起(娜塔莉亚) ----
    def zz_set_route(route):
        setattr(store, "freelauren", route == "rise")
        renpy.restart_interaction()
        return route

    # ---- 画廊解锁：persistent.replay_scenes[id] 取反 ----
    def zz_toggle_scene(scene_id):
        persistent.replay_scenes[scene_id] = not persistent.replay_scenes.get(scene_id, False)
        renpy.restart_interaction()
        return persistent.replay_scenes[scene_id]

    # ---- 分支结果标志取反 ----
    def zz_toggle_bool(flag_name):
        value = getattr(store, flag_name, False)
        setattr(store, flag_name, not value)
        renpy.restart_interaction()
        return not value

    # ---- F8 呼出 / 关闭面板 ----
    def zz_toggle_panel():
        if renpy.get_screen("zz_stat_panel") is not None:
            renpy.hide_screen("zz_stat_panel")
        else:
            renpy.show_screen("zz_stat_panel")
        renpy.restart_interaction()
        return None

    config.keymap['zz_stat_toggle'] = ['K_F8']
    config.underlay.append(renpy.Keymap(zz_stat_toggle=zz_toggle_panel))


# ============================================================================
# 属性调节面板
# ============================================================================
screen zz_stat_panel():
    style_prefix "zzstat"
    modal True
    zorder 2000

    key "dismiss" action Hide("zz_stat_panel")

    frame:
        xalign 0.5
        yalign 0.5
        background "#101010f2"
        padding (38, 28)

        vbox:
            spacing 13

            text "属性调节" size 30 bold True color "#FFD700" xalign 0.5
            text "F8 或点空白处关闭" size 15 color "#AAAAAA" xalign 0.5

            # 威慑力
            hbox:
                spacing 14
                text "威慑力" size 26 color "#FFFFFF" min_width 120 yalign 0.5
                text "[intimidation]" size 30 bold True color "#FF8B00" min_width 70 text_align 0.5 yalign 0.5
                textbutton "−1" action Function(zz_clamp_stat, "intimidation", -1)
                textbutton "+1" action Function(zz_clamp_stat, "intimidation", 1)

            # 魅力
            hbox:
                spacing 14
                text "魅力" size 26 color "#FFFFFF" min_width 120 yalign 0.5
                text "[charisma]" size 30 bold True color "#FF8B00" min_width 70 text_align 0.5 yalign 0.5
                textbutton "−1" action Function(zz_clamp_stat, "charisma", -1)
                textbutton "+1" action Function(zz_clamp_stat, "charisma", 1)

            text "剧情分支门槛：威慑 >3、魅力 >2 已覆盖全部相关分支" size 15 color "#888888"

            null height 2

            text "剧情开关" size 22 bold True color "#FFD700"

            # 劳伦路线（二选一，高亮的是当前路线）
            hbox:
                spacing 8
                textbutton "爱情路线：劳伦淋浴＋劳伦爱情" action Function(zz_set_route, "love") selected (getattr(store, "freelauren", False) == False)
                textbutton "崛起路线：劳伦＋娜塔莉亚" action Function(zz_set_route, "rise") selected (getattr(store, "freelauren", False) == True)

            # 画廊解锁
            hbox:
                spacing 8
                textbutton "画廊·劳伦淋浴" action Function(zz_toggle_scene, "gallery37lc") selected persistent.replay_scenes.get("gallery37lc", False)
                textbutton "画廊·劳伦爱情" action Function(zz_toggle_scene, "gallery38lc") selected persistent.replay_scenes.get("gallery38lc", False)
                textbutton "画廊·劳伦+娜塔莉亚" action Function(zz_toggle_scene, "gallery39lc") selected persistent.replay_scenes.get("gallery39lc", False)

            # 分支结果记录
            hbox:
                spacing 8
                textbutton "罗斯·内射" action Function(zz_toggle_bool, "ros_inside_cum") selected getattr(store, "ros_inside_cum", False)
                textbutton "凯伦·肛交" action Function(zz_toggle_bool, "fuckkarenanal") selected getattr(store, "fuckkarenanal", False)
                textbutton "克洛伊·跨坐" action Function(zz_toggle_bool, "cochloegooverher") selected getattr(store, "cochloegooverher", False)

            textbutton "关 闭" action Hide("zz_stat_panel") xalign 0.5


style zzstat_button:
    size 22
    color "#FFFFFF"
    hover_color "#FFD700"
    background "#333333"
    hover_background "#555555"
    selected_color "#FFD700"
    selected_background "#4a3f00"
    padding (12, 5)

style zzstat_text:
    size 22
