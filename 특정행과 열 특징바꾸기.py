#엑셀을 활성화 시키고 sheet에 가져올 수 있도록 넣는다.
import openpyxl

wb=openpyxl.load_workbook('merged_01.xlsx')
sheet=wb.active #활성되는 엑셀을 담는다.
sheet #여기에 엑셀의 전체 시트가 담기면서 엑셀에 대한 수정이 가능해진다.

#셀에 담긴 폰트를 변경할 내용을 담는다.
font_15=Font(name='맑은 고딕',size=15,bold=True) #

# 짝수열에 대한 폰트 변경
for col in sheet['A2:C28']:  #엑셀파일의 행과 열 전체 선택
     for cell in range(3):
        if(cell%2==0):
            col[cell].font=font_15  #각셀에 대한 폰트 변경 방법


# 짝수행의 폰트 변경
b=list(sheet.columns)  #열을 리스트로 만들어 28번 반복할 수 있도록 한다.
b

for col in b:
    for i in range(28):
        if(i%2==0):
            col[i].font=font_15