from .utils import make_table


_font_01 = """
　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴ
ＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏ
ｐｑｒｓｔｕｖｗｘｙｚ０１２３４５６７８９
{０}{１}{２}{３}{４}{５}{６}{７}{８}{９}あいうえおかきくけこさ
しすせそたちつてとなにぬねのはひふへほまみ
むめもやゆよらりるれろわをんアイウエオカキ
クケコサシスセソタチツテトナニヌネノハヒフ
ヘホマミムメモヤユヨラリルレロワヲンぁ{○}{✕}
{△}{□}ゃゅょっァィゥェォャュョッがぎぐげござ
じずぜぞだ終づでどばびぶべぼぱぴ序充攻ガギ
"""


_font_02 = """
グゲゴザジズゼゾダ溜貯デドバビブベボパピプ
ぺポヴ（）ー？/、{、}。：{、2}{、3}！「」✓✗{pts}　
零一二三四五六七八九十百千万上下前後左右扉
固閉咮面掛屏風向编集霊取材手入階段動棚冬雑
然人形並止押中何不気者廊犠影輿消鏡見返振美
琴音閒夭井粱兄…写鳥居古牲常敗化除効果低用
感度良高暗遠撮钵力少回復薬葉書容器參精神全
香料強肆静作持位槽清水異{常}黑石付伍带性壊電
灯方闇照出母深雪遺思議械目映鍵地銀製小飾赤
鲭塚式陸丸月漆御捌玫射機＝範纳戸足欠仏像金
"""


_font_03 = """
曲懐燈大青銅墨文字木礼型再生部分破崩彫底梵
浮〇台追屋敷内圧襖無着物明拾軸今開助隙間障
子女斎真救花使呪規家姿撃氷室秘現封印解関記
録光陣緑側穴覚予桜走拡供引装填必要状態邸玄
倉紋院瓦礫庭新館通路眺望夜完峰湧元逢族娘長
髪保存伝承他切替削護在篭淵衝立臨縄和鳴白鎧
時計奈反箪笥行控導錠指置寂打外暖吹込急縛男
溶倒進死殺苦魂憎繋厨号病証亡痛続最初配戻離
選年日午秒枚数退官得点正操術客能調整画牢落
巨半口探格布若連想惹原留床空裂冷流包里悟跡
"""


_font_04 = """
残誰突嫌近螨燭本工事儀柱囲壁散暴定自視根血
骨紫董住趣相当偭値知特表纸仁王炉裏積針巣張
語渡泣描绘簿備变庫橋錡麗皿窓姐色悲々火鉢頑
丈机割霧淼迈景湿含瓶毛同意奇妙塗座代弐片隅
傷箱草吊乱役邪魔来奉痦卷牌毬移土砂武周注穢
蒼伸顏塞碑慰{色}枝壱堂禊先端抜厚竹墓読設黄応
更声量節確認平坂絡有次陽品欲許碧参加準星巴
緒浩私名喜哀補的図基隣獅民車場所話荒言資鍮
象板譜悪章謝道迷示唱報等査広収主別念述員液
傪命绝妻廃墟红理由杭恐俗学各著宗蔵依利境重
"""


_font_05 = """
心失踪报好昨遅腕宿速殊会震村起説題樣択我以
増背帳断潰戦件仕未詳细鎖避対巫達越研究成世
去発実多隠違治執殿建禁折彼凶劇熱憶狂信氏両
首肢昔係驚早岩案角待造呼考赞害過運逃夫既致
法似合情災厄怪界門因社般監鐘測豊富结論忌推
療養葬始直了彩頼胸騷泉楽{彩}限歩鬼幼差訴帰植
怒怖遊誘迫麓幻策{Rune4}碎寒夢教識頭捕謎安{Rune1}{Rune2}酷
怨晴第舞県山{Rune5}祭吉兆南胴警察{Rune3}故捜身歲野児
童届噂{策}師衰弱質問親翌決雛咲壇息友弔守司筋
極虐放協瘴禍刻襲蘇降際登構宮稿〜国仰夹崖蓄
"""


table_jp = {
    "default": make_table(_font_01),
    0xF0: make_table(_font_02),
    0xF1: make_table(_font_03),
    0xF2: make_table(_font_04),
    0xF3: make_table(_font_05),
}
