Life in Santa County — Standalone Mods
Two independent, drop-in mods for Life in Santa County (Ren'Py).
They only add new files; no original game file is touched. Delete the files to uninstall.

  【醒目提示 · IMPORTANT】中文基础开发，mod 均为简体中文
  本组模组以简体中文为基础开发，所有模组的界面与提示文本均为 简体中文（Simplified Chinese）。
  - Mod 1 的称呼替换基于纯文本替换，可叠加在任意语言 / 汉化包之上生效；
  - Mod 2 的状态面板（F8）界面文字为简体中文。
  These mods are developed on a Simplified-Chinese base; all in-game UI text is Simplified Chinese. Mod 1's nickname substitution works on top of any language / fan-translation pack, while Mod 2's stat panel UI is in Simplified Chinese.

Mod 1 — zz_relation_mod.rpy · Relationship / nickname replacement
Rewrites how characters address each other per speaker: one rule for what Lauren calls you,
another for what you call Lauren, and so on. It is plain text substitution applied right before
a line is shown, so it also works on top of any language / fan translation.
- No hotkey — active as soon as the game starts.
- 
- Edit the ② replacement rules block near the top of the file, save, restart the game.
- A global fallback also covers menus and the phone UI, so the word "friend" does not leak through.
- 
Mod 2 — zz_stat_adjust.rpy · Stat / branch panel

Press F8 in game to open or close the panel. It does not interrupt the story.
- Shows and adjusts intimidation and charisma (0–99), applied immediately.
- Lauren route switch (love route / rise route).
- Gallery unlocks (Lauren shower / Lauren love / Lauren + Natalia).
- Branch flags (Rose creampie / Karen anal / Chloe cowgirl).
- 
Install
1. Copy the .rpy file(s) from game/ into your game's game/ folder, e.g.
...\Life in Santa County\game\
2. Start the game. Ren'Py compiles the new .rpy into a .rpyc by itself on first launch.
3. That's it — nothing else to configure.
The zz_ prefix is only about load order: it makes the file load after screens.rpy,
which Mod 1 needs in order to override the dialogue screen.
Uninstall
Delete the matching .rpy and .rpyc files from the game/ folder.

Notes
- Built for the PC (Windows) release of Life in Santa County.
- Ship only the .rpy: if you already have a stale .rpyc of the same name, delete it and let
the engine rebuild it.
- Mod 1 re-defines the screen say screen. If a future game update changes that screen a lot,
the mod may need a refresh.
中文速览

两个独立模组，放进游戏的 game\ 目录即生效，不改动任何原文件，删掉即卸载。
- zz_relation_mod.rpy — 关系/称呼替换：可按"谁在说话"分别改，比如劳伦叫你什么、你叫劳伦什么互不影响。不用按键，进游戏就生效；要改内容就改文件顶部"② 替换规则"。
