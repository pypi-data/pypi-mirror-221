import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap

# 獲取當前檔案位址
currentfilepath = __file__

# 刪去__file__中最後面自"\"開始的字串(刪除檔名)
motherpath = currentfilepath[:-len(currentfilepath.split('\\')[-1])]

fontpath = Path(mpl.get_data_path(), motherpath+"\FONT\\futura medium bt.ttf")
fontpath_bold = Path(mpl.get_data_path(), motherpath+"\FONT\Futura Heavy font.ttf")
fontpath_black = Path(mpl.get_data_path(), motherpath+"\FONT\Futura Extra Black font.ttf")

# 初始化
def init(style='default',figsize=(10,8),background=True):
    global theme
    if style == 'default'or style == 'light_background' or style == 'light':
        theme = 'default'
        plt.style.use(theme)
    elif style == 'dark_background' or style == 'dark':
        theme = 'dark_background'
        plt.style.use(theme)
    
    # size
    plt.rcParams['figure.figsize'] = figsize


    # 設定facecolor
    if background == True:
        plt.gca().set_facecolor(colorlist('bg'))
    else: pass


# 色票(顏色選用優先級)
def colorlist(index):
    if type(index) == list:
        return index
    else:
        str(index)
        if index in ['bg', 'bg1', 'bg2', 'fg', '1', '2', '3', '4', 'rfg']:
            if theme == 'default':
                colorseries = {'bg': '#D9EEFD',
                            'bg1': '#D9EEFD',
                            'bg2': '#F7DCD1',
                            'rfg': '#F5F5F5',
                            'fg': '#111111',
                            '1': '#0A9CCF',
                            '2': '#AC005A',
                            '3': '#A19253',
                            '4': '#A43713'}
                return colorseries[index]
                            
            elif theme == 'dark_background':
                colorseries = {'bg': '#122D64',
                            'bg1': '#122D64',
                            'bg2': '#122D64',
                            'rfg': '#080808',
                            'fg': '#EEEEEE',
                            '1': '#0A9CCF',
                            '2': '#AC005A',
                            '3': '#A19253',
                            '4': '#A43713'}
                return colorseries[index]
        else:
            return index
    
def cmaplist(index):
    str(index)
    if index in ['-28','28','-27','-26','-25','-24','-23','-22','22','23','24','25','26','27','12','13','14','15','-12','-13','-14','-15']:
        if theme == 'default':
            if index == '15':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#47A7DE','#D5EDD5','#E08A16','#AB503B'])
            if index == '14':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#47A7DE','#E08A16','#AB503B'])
            if index == '13':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#D5EDD5','#AB503B'])
            if index == '12':
                return LinearSegmentedColormap.from_list('mycmap', ['#47A7DE','#E08A16'])

            if index == '-15': # reversed 1
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#E08A16','#D5EDD5','#47A7DE','#454FB4'])
            if index == '-14': # reversed 1 but 4 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#E08A16','#47A7DE','#454FB4'])
            if index == '-13': # reversed 1 but 3 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#D5EDD5','#454FB4'])
            if index == '-12': # reversed 1 but 2 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#E08A16','#47A7DE'])

            if index == '28':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F','#CF725E','#BB8263'])        
            if index == '27':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F','#CF725E','#BB8263'])
            if index == '26':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F','#CF725E'])
            if index == '25':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F'])
            if index == '24':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A'])
            if index == '23':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4'])
            if index == '22':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF'])

            if index == '-28': # reversed 2
                return LinearSegmentedColormap.from_list('mycmap', ['#BB8263','#CF725E','#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE','#EEEEEE']) 
            if index == '-27': # reversed 2
                return LinearSegmentedColormap.from_list('mycmap', ['#BB8263','#CF725E','#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-26': # reversed 2 but 6 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#CF725E','#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-25':
                return LinearSegmentedColormap.from_list('mycmap', ['#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-24':
                return LinearSegmentedColormap.from_list('mycmap', ['#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-23':
                return LinearSegmentedColormap.from_list('mycmap', ['#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-22':
                return LinearSegmentedColormap.from_list('mycmap', ['#F2CABF','#EEEEEE'])
        
        
        elif theme == 'dark_background':
            if index == '15':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#47A7DE','#D5EDD5','#E08A16','#AB503B'])
            if index == '14':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#47A7DE','#E08A16','#AB503B'])
            if index == '13':
                return LinearSegmentedColormap.from_list('mycmap', ['#454FB4','#D5EDD5','#AB503B'])
            if index == '12':
                return LinearSegmentedColormap.from_list('mycmap', ['#47A7DE','#E08A16'])

            if index == '-15': # reversed 1
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#E08A16','#D5EDD5','#47A7DE','#454FB4'])
            if index == '-14': # reversed 1 but 4 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#E08A16','#47A7DE','#454FB4'])
            if index == '-13': # reversed 1 but 3 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#AB503B','#D5EDD5','#454FB4'])
            if index == '-12': # reversed 1 but 2 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#E08A16','#47A7DE'])
                    
            if index == '27':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F','#CF725E','#BB8263'])
            if index == '26':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F','#CF725E'])
            if index == '25':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A','#DB997F'])
            if index == '24':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4','#DCB29A'])
            if index == '23':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF','#F1C9B4'])
            if index == '22':
                return LinearSegmentedColormap.from_list('mycmap', ['#EEEEEE','#F2CABF'])
              
            if index == '-27': # reversed 2
                return LinearSegmentedColormap.from_list('mycmap', ['#BB8263','#CF725E','#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-26': # reversed 2 but 6 colors
                return LinearSegmentedColormap.from_list('mycmap', ['#CF725E','#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-25':
                return LinearSegmentedColormap.from_list('mycmap', ['#DB997F','#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-24':
                return LinearSegmentedColormap.from_list('mycmap', ['#DCB29A','#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-23':
                return LinearSegmentedColormap.from_list('mycmap', ['#F1C9B4','#F2CABF','#EEEEEE'])
            if index == '-22':
                return LinearSegmentedColormap.from_list('mycmap', ['#F2CABF','#EEEEEE'])
    else: 
        return index

# LABEL設定
'''
默認下系統會在使用者繪製不同種類的圖形添加LABEL計數，依種類分開計數，無法在圖例中顯示出來的LABEL不用計數；使用者依然可以手動為LABEL賦值進行覆蓋
'''
# 點狀圖
SCATTERNO = 0
# 折線圖
PLOTNO = 0
# 直方圖
HISTNO = 0
# 橫向長條圖
BARHNO = 0
# 縱向長條圖
BARNO = 0

def getSCATTERNO():
    global SCATTERNO
    SCATTERNO += 1
    label = 'SCATTER'+str(SCATTERNO)
    return label

def getPLOTNO():
    global PLOTNO
    PLOTNO += 1
    label = 'PLOT'+str(PLOTNO)
    return label

def getHISTNO():
    global HISTNO
    HISTNO += 1
    label = 'HIST'+str(HISTNO)
    return label

def getBARHNO():
    global BARHNO
    BARHNO += 1
    label = 'BARH'+str(BARHNO)
    return label

def getBARNO():
    global BARNO
    BARNO += 1
    label = 'BAR'+str(BARNO)
    return label


# 存檔
def savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0.1, transparent=False):
    plt.savefig(filename, dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad_inches,transparent=transparent)

# 標題
def title(title, color='fg', font=fontpath_bold, fontsize=30):
    plt.suptitle(title, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize))

# 標題
def lefttitle(title, loc='left', color='1', font=fontpath_bold, fontsize=24):
    plt.gca().set_title(title, loc=loc,color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize))

# 標題
def righttitle(title, loc='right', color='2', font=fontpath_bold, fontsize=24):
    plt.gca().set_title(title, loc=loc,color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize))


# 圖表
def subplot(nrows=1, ncols=1, index=1, figsize=(8,10), **kwargs):
    return plt.subplots(nrows, ncols, index, figsize=figsize, **kwargs)

# scatter繪圖
def scatter(x, y, color='fg', linewidth=2, linestyle='-', label=getSCATTERNO(), **kwargs):
    plt.scatter(x, y, color=colorlist(color), linewidth=linewidth, label=label, linestyle=linestyle, **kwargs)

# plot繪圖
def plot(x, y, color='fg', linewidth=2, linestyle='-', label=getPLOTNO(),**kwargs):
    plt.plot(x, y, color=colorlist(color), linewidth=linewidth, label=label,linestyle=linestyle, **kwargs)

# boxplot繪圖
def boxplot(x, vert=True, patch_artist=True, showmeans = True, showcaps = True, showbox = True, widths = 0.5, boxfacecolor='1', boxcolor='fg', boxlinewidth=3, capcolor='fg', caplinewidth=3, whiskercolor='fg', whiskerlinewidth=3, fliercolor='fg', fliermarkeredgecolor='fg', flierlinewidth=3, mediancolor='fg', medianlinewidth=3, meancolor='fg', meanmarker='D', meanmarkeredgecolor='fg', meanmarkerfacecolor='2', meansize=20, meanmarkeredgewidth=3, **kwargs):
    plt.boxplot(x, vert=vert, patch_artist=patch_artist, showmeans = showmeans, showcaps = showcaps, showbox = showbox, widths = widths, boxprops=dict(facecolor=colorlist(boxfacecolor), color=colorlist(boxcolor), linewidth = boxlinewidth), capprops=dict(color=colorlist(capcolor), linewidth = caplinewidth), whiskerprops=dict(color=colorlist(whiskercolor), linewidth = whiskerlinewidth), flierprops=dict(color=colorlist(fliercolor), markeredgecolor=colorlist(fliermarkeredgecolor), linewidth = flierlinewidth), medianprops=dict(color=colorlist(mediancolor), linewidth = medianlinewidth), meanprops=dict(marker=meanmarker, markeredgecolor=colorlist(meanmarkeredgecolor), markerfacecolor=colorlist(meanmarkerfacecolor), markersize=meansize, markeredgewidth = meanmarkeredgewidth), **kwargs)

# contour繪圖
def contour(x, y, z, colors='fg', levels=10, linewidths=2, clabel=True, fontsize=12, color='fg', **kwargs):
    CS = plt.contour(x, y, z, colors=colorlist(colors), levels=levels, linewidths=linewidths, **kwargs)
    if clabel == True:
        CL = CS.clabel(fontsize=fontsize, colors=colorlist(color), inline=True)

# contourf繪圖
def contourf(x, y, z, levels=10, cmap='2', contour=True, clabel=True,linewidths=1.5, color='fg', **kwargs):
    if contour == True:
        CS = plt.contour(x, y, z, colors=colorlist(color), levels=levels, linewidths=linewidths)
    if clabel == True:
        CL = CS.clabel(fontsize=8, colors=colorlist(color), inline=True)
    plt.contourf(x, y, z, cmap=cmaplist(cmap), **kwargs)

# colorbar顯示
def colorbar(ticks,label=' ', orientation='vertical',shrink=0.95, aspect=20, labelsize=16, font=fontpath, color='fg',**kwargs):
    if orientation == 'v' or 'V':
        orientation = 'vertical'
    elif orientation == 'h' or 'H':
        orientation = 'horizontal'
    CB = plt.colorbar(orientation=orientation, shrink=shrink, aspect=aspect, label=label, **kwargs)
    CB.ax.tick_params(labelsize=labelsize, labelcolor=colorlist(color), color=colorlist(color))
    CB.ax.set_ylabel(label, fontproperties=fm.FontProperties(fname=font, size=labelsize), color=colorlist(color))
    CB.ax.set_yticks(ticks,ticks, fontproperties=fm.FontProperties(fname=font, size=labelsize))
    CB.ax.yaxis.set_tick_params(color=colorlist(color), labelcolor=colorlist(color))
    CB.outline.set_color(colorlist(color))
    CB.outline.set_linewidth(2)

# 直方圖
def hist(x, bins=5, color='1', edgecolor='fg', linewidth=3, label=getHISTNO(), **kwargs):
    plt.hist(x, bins=bins, color=colorlist(color), edgecolor=colorlist(edgecolor), linewidth=linewidth, label=label,**kwargs)

# 橫向長條圖
def barh(x, y, width=0.8, color='1', edgecolor='fg', linewidth=3, label=getBARHNO(), **kwargs):
    plt.barh(x, y, height=width, color=colorlist(color), edgecolor=colorlist(edgecolor), linewidth=linewidth, label=label, **kwargs)

# 縱向長條圖
def bar(x, y, width=0.8, color='1', edgecolor='fg', linewidth=3, label=getBARNO(), **kwargs):
    plt.bar(x, y, width=width,color=colorlist(color), edgecolor=colorlist(edgecolor), linewidth=linewidth, label=label, **kwargs)

# 圓餅圖
def pie(x, labels=None, colors=None, explode=None, autopct=None, shadow=False, startangle=90, pctdistance=0.6, labeldistance=1.1, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, **kwargs):
    plt.pie(x, labels=labels, colors=colorlist(colors), explode=explode, autopct=autopct, shadow=shadow, startangle=startangle, pctdistance=pctdistance, labeldistance=labeldistance, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, **kwargs)

# 標籤
def xlabel(xlabel, color='fg', font=fontpath, fontsize=24, **kwargs):
    plt.xlabel(xlabel, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)
def ylabel(ylabel, color='fg', font=fontpath, fontsize=24, **kwargs):
    plt.ylabel(ylabel, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)

# 刻度
def xticks(ticks, labels, color='fg', font=fontpath, fontsize=18, **kwargs):
    plt.xticks(ticks, labels, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)
def yticks(ticks, labels, color='fg', font=fontpath, fontsize=18, **kwargs):
    plt.yticks(ticks, labels, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)
def xyticks(xticks, xlabels, yticks, ylabels, color='fg', font=fontpath, fontsize=18, **kwargs):
    plt.xticks(xticks, xlabels, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)
    plt.yticks(yticks, ylabels, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)

# 限制
def xlim(xmin=None, xmax=None, **kwargs):
    plt.xlim(xmin, xmax, **kwargs)
def ylim(ymin=None, ymax=None, **kwargs):
    plt.ylim(ymin, ymax, **kwargs)
def xylim(xmin=None, xmax=None, ymin=None, ymax=None, **kwargs):
    plt.xlim(xmin, xmax, **kwargs)
    plt.ylim(ymin, ymax, **kwargs)

# 畫指數
def xscale(scale, **kwargs):
    plt.xscale(scale, **kwargs)
def yscale(scale, **kwargs):
    plt.yscale(scale, **kwargs)

def xlog(base=10, **kwargs):
    plt.xscale('log', base=base, **kwargs)
def ylog(base=10, **kwargs):
    plt.yscale('log', base=base, **kwargs)

# 畫網格
def grid(b=None, which='major', axis='both', color='fg', linestyle=':', linewidth=0.5, **kwargs):
    plt.grid(b, which=which, axis=axis, color=colorlist(color), linestyle=linestyle, linewidth=linewidth, **kwargs)

# spines
def spines(top=True, right=True, bottom=True, left=True, color='fg', linewidth=3, **kwargs):
    plt.gca().spines['top'].set_visible(top)
    plt.gca().spines['right'].set_visible(right)
    plt.gca().spines['bottom'].set_visible(bottom)
    plt.gca().spines['left'].set_visible(left)
    plt.gca().spines['top'].set_color(colorlist(color))
    plt.gca().spines['right'].set_color(colorlist(color))
    plt.gca().spines['bottom'].set_color(colorlist(color))
    plt.gca().spines['left'].set_color(colorlist(color))
    plt.gca().spines['top'].set_linewidth(linewidth)
    plt.gca().spines['right'].set_linewidth(linewidth)
    plt.gca().spines['bottom'].set_linewidth(linewidth)
    plt.gca().spines['left'].set_linewidth(linewidth)

# axhline 水平線
def axhline(y=0, color='fg', linestyle='dashed', linewidth=3, **kwargs):
    plt.axhline(y=y, color=colorlist(color), linestyle=linestyle, linewidth=linewidth, **kwargs)

# axvline 垂直線
def axvline(x=0, color='fg', linestyle='dashed', linewidth=3, **kwargs):
    plt.axvline(x=x, color=colorlist(color), linestyle=linestyle, linewidth=linewidth, **kwargs)

# 圖例legend
def legend(loc='best', fontsize=18, labelcolor='fg', frameon=True, framealpha=1, facecolor='rfg', edgecolor='fg', edgewidth=2 ,roundedge=False, **kwargs):
    LG = plt.gca().legend(loc=loc, fontsize=fontsize, labelcolor=colorlist(labelcolor), frameon=frameon, framealpha=framealpha, prop=fm.FontProperties(fname=fontpath, size=fontsize), facecolor=colorlist(facecolor), edgecolor=colorlist(edgecolor), **kwargs)
    if roundedge == False:
        LG.get_frame().set_boxstyle('Round', pad=0.2, rounding_size=-0.01)
    LG.get_frame().set_linewidth(edgewidth)

# 文字
def text(x, y, text, color='fg', font=fontpath, fontsize=20, **kwargs):
    plt.text(x, y, text, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)

# 帶有標籤的文字
'''
標籤為反白的文字，背景需為鋪色矩形
'''
def labeltext(x, y, w, h,label='LABEL TEXT', text='NORMAL TEXT', color='2', font=fontpath, fontsize=19, **kwargs):
    # 先繪製label的矩形背景
    plt.gca().add_patch(plt.Rectangle((x-0.05*w, y-0.1*h), width=w, height=h, color=colorlist(color), alpha=1))
    # 再繪製label文字於矩形中
    plt.text(x, y, label, color='#EEEEEE', fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)
    # 在label之後繪製text文字
    plt.text(x+w, y, text, color=colorlist(color), fontproperties=fm.FontProperties(fname=font, size=fontsize), **kwargs)

# 設定尺寸
def figsize(width, height):
    plt.rcParams['figure.figsize'] = width, height

# 顯示
def show():
    plt.show()

# 清除
def clf():
    plt.clf()

# 關閉
def close():
    plt.close()
















