# 读取BD的书签时间
def readtxt(path):
    f = open(path)
    line = f.readline()
    while line:
        line = line.strip('\n')
        bd_TimePointTags.append(line)
        line = f.readline()
    f.close()


# BD格式【hh:mm:ss.mss （小时:分钟:秒:帧），其中一秒1000ms】
# 转换为CUE格式【mm:ss:ff （分钟:秒:帧），其中一秒75帧】
def conversion(bd_TimePointTag):
    bd_TimePointTag_hh = bd_TimePointTag[0:2]

    bd_TimePointTag_mm = bd_TimePointTag[3:5]

    bd_TimePointTag_ss = bd_TimePointTag[6:8]

    bd_TimePointTag_ms = bd_TimePointTag[9:]

    cue_TimePointTags_mm = str(int(bd_TimePointTag_hh) * 60 + int(bd_TimePointTag_mm))
    cue_TimePointTags_ss = str(bd_TimePointTag_ss)
    cue_TimePointTags_ff = str(int(float(bd_TimePointTag_ms) / 1000 * 75))
    if len(cue_TimePointTags_mm) == 1:
        cue_TimePointTags_mm = "0" + cue_TimePointTags_mm

    if len(cue_TimePointTags_ff) == 1:
        cue_TimePointTags_ff = "0" + cue_TimePointTags_ff

    cue_TimePointTag = cue_TimePointTags_mm + ":" + cue_TimePointTags_ss + ":" + cue_TimePointTags_ff
    return cue_TimePointTag


def Conversions(bd_TimePointTags):
    for x in bd_TimePointTags:
        cue_TimePointTags.append(conversion(x))

    return cue_TimePointTags


def write2cue(cue_TimePointTags):
    f = open('loveless.cue', 'w', encoding='GBK')
    f.writelines("REM DATE 2020\n")
    f.writelines("PERFORMER \"miku\"\n")
    f.writelines("TITLE \"mm2020 live\"\n")
    f.writelines("FILE \"2020.wav\" WAVE\n")
    k = 1
    for x in cue_TimePointTags:
        if k < 10:
            f.writelines("  TRACK 0" + str(k) + " AUDIO\n")
        else:
            f.writelines("  TRACK " + str(k) + " AUDIO\n")

        f.writelines("    TITLE \"" + str(k) + "\"\n")

        f.writelines("    INDEX 01 " + x + "\n")
        k += 1
    f.close()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    path = "loveless.txt"
    bd_TimePointTags = []
    cue_TimePointTags = []
    readtxt(path)

    print(bd_TimePointTags)
    cue_TimePointTags = Conversions(bd_TimePointTags)
    print(cue_TimePointTags)
    write2cue(cue_TimePointTags)
