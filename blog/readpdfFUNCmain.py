# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:11:51 2019

@author: Nathan Hilbrands
"""

'''import PyPDF2

pgnfile = open ('pgn+40.pdf', 'rb')
pgnread = PyPDF2.PdfFileReader(pgnfile)
page1 = pgnread.getPage(7)
print(page1.extractText())
'''

def chapterparse(textloc):
    import pandas as pd
    import numpy as np
    import re
    import io
    with io.open(textloc, mode = 'r', encoding = 'utf-8') as in_file:
        timesused = 1
        dfcreated = False               #stores whether data frame has been created yet.
        #print('')
        ofoptions = False
        for line in in_file:
            lineused = False
            if 'Options and their characteristics' in line:
                ofoptions = True
                continue
            if'Description' in line:
                labelline = line.split(' ')
                keyword = labelline[1].strip()      #finds first string that is not 'Descriptinon' sets as key word
                labelindex = -1
                labellist = []
                for item in labelline:              #adds string to keyword if not keyword
                    if item.strip() == keyword:
                        labellist.append(item)
                        labelindex += 1
                    elif item != 'Description':
                        labellist[labelindex] = labellist[labelindex] + ' ' + item
                        lineused = True
            if 'Description' not in line:
                #print(line)
                tempstr = re.split(r'(^[^\d]+)', line)[1:] #splits line into 
                #print(tempstr[0])
                stringsplit = tempstr[1].split(' ')
                #print(stringsplit[0]) 
                #print(stringsplit)
            if tempstr[0].strip() == 'ID':
                    global chapterdf
                    chapterdf = pd.DataFrame(columns = stringsplit)
                    chapterdf.loc['Description'] = labellist 
                    dfcreated = True
                    lineused = True
            if '/' in tempstr[0] and 'spring' not in tempstr[0]:
                slashlabels = tempstr[0].split('/')     #creates list of row names
                slashvalstogether = tempstr[1].split(' ') #splits line into groups of connected by slashes
                slashindex = 0
                unit = slashlabels[-1].split(' ', 1)[-1]
                #print(unit)
                #print(tempstr[0])
                for slash in slashlabels:        
                    slashvallist = []
                    for slashgroup in slashvalstogether:
                        slashvallist.append(slashgroup.split('/')[slashindex]) #adds slash index itme to list that will become dataframe row
                        #print(slashgroup.split('/')[slashindex])
                    if unit not in slash:
                        repeatslash = slash + ' ' + unit
                        timesused+=1
                        if ofoptions:
                            #repeatslash = repeatslash + ' of options'
                            dummy = 1 
                            #print(repeatslash)
                        else:
                            chapterdf.loc[repeatslash] = slashvallist
                    else:
                        if ofoptions:
                            #slash = slash + ' of options'
                            dummy = 1
                        else:
                            chapterdf.loc[slash] = slashvallist        #adds list as row
                    slashindex += 1                                 #moves to next iem
                    lineused = True
            if ' x ' in line:
                xlabels = tempstr[0].split(' x ')
                origarray = tempstr[1].split(' ')
                noxlist = []
                #print(len(xlabels))
                for i in origarray: #adds only non x items to list
                    if i != 'x':
                        noxlist.append(i)
                noxarray = np.array(noxlist)
                noxarray = noxarray.reshape(int(len(noxlist)/len(xlabels)), len(xlabels)) #turns list into array and reshapes it
                j = 0
                for item in xlabels:      #adds correct columns to rows in dataframe
                    if ofoptions:
                    #item = item + ' of options'
                        dummy = 1
                    else:
                        chapterdf.loc[item] = noxarray[:,j]
                        j+=1
                        lineused = True 
            
            elif dfcreated:
                if len(stringsplit) == chapterdf.shape[1] and not lineused:
                    #print(stringsplit)
                    if ofoptions:
                        #chapterdf.loc[tempstr[0] + ' of options'] = stringsplit
                        dummy = 1 
                    else:
                        #print(tempstr[0])
                        if tempstr[0] != '':
                            chapterdf.loc[tempstr[0]] = stringsplit   
    return(chapterdf) 
def main():
    from tika import parser
    import pandas as pd
    globaldfcreated = False
    import io
    global globaldf
    collist = []
    raw = parser.from_file('MPG+.pdf')  #extracts text from PDF
    firsttxt = raw['content']
    #print(type('pgn2.txt'))
    with io.open('pgn2.txt', mode = 'w', encoding = 'utf-8') as f: #saves text in pdf to text file
        f.write(firsttxt)
        
    istech = False
    with io.open('pgn2.txt', mode = 'r', encoding = 'utf-8') as in_file:    
        texti = 0
        for line in in_file:                            #only writing lines with tech data to condensed file named text
            if line.strip() == 'Technical data':
                istech = True
                textloc = 'temp' + str(texti) + ".txt"
                out_file = io.open(textloc, mode = 'w+', encoding = 'utf-8')
                texti +=1 
                continue
            if istech:
                if line.strip() == 'Options and their characteristics' or line.strip().isnumeric() or line == '':
                    istech = False
                    #out_file.truncate(0)
                    if globaldfcreated:                         #appends global df if already created 
                        out_file.close()
                        #print(chapterparse())
                        #print('Global df')
                        globaldf = pd.concat([globaldf, chapterparse(textloc).transpose()], sort = True)
        
                        #out_file.truncate(0)
                    if not globaldfcreated:
                        #print(chapterparse())
                        out_file.close()
                        globaldf = chapterparse(textloc).copy()                        #creates global df if not created
                        globaldf = globaldf.transpose()
                        globaldfcreated = True
                        #print ('Not global df')
                else:
                    out_file.write(line)
                    #print(line)        
    globaldf = globaldf.drop('\n', axis = 1)
    globaldf.to_csv('grippercsv.csv')
    dfhtml = globaldf.to_html()
    with io.open('dfhtmlfile.txt', mode = 'w+', encoding = 'utf-8') as writefile:
        writefile.write(dfhtml)
if __name__ == "__main__":
   main()                  

        
            
        
        
                                        

                
                    
        
 





