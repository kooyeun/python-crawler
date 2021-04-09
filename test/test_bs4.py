from bs4 import BeautifulSoup

html='''
					<td class="title black">
						<div class="tit3" data-no="10">
							<a href="/movie/bi/mi/basic.nhn?code=189075" title="자산어보">자산어보</a>
						</div>
					</td>
'''

# 1. tag searching
def ex01():
    bs = BeautifulSoup(html,'html.parser')
    #print(bs)

    tag_td = bs.td
    #print(tag_td)

    #tag_a = bs.a
    tag_a =  bs.td.a
    print(tag_a)

    #None
    tag_h1 = bs.td.h1
    print(tag_h1)

# 2. attribute searching
def ex02():
    bs = BeautifulSoup(html,'html.parser')
    # tag_td = bs.find('td',attrs={'class':'title'})
    tag_td = bs.find('td', attrs={'class': ['title','black']})
    print(tag_td)

    tag_div = bs.find('div',attrs={'class':'tit3','data-no':'10'})
    print(tag_div)


if __name__ == '__main__':
    #ex01()
    ex02()