#해당 파트는 Day03 타이머만들기.py에서 배웠던 모듈에 대한 개념도 같이
#알아둘 것

#함수 : 특정 하나의 작업을 진행하기 위해 명령문들을 모아놓은 집합체

#내장 함수 : 파이썬 내부에서 미리 설계 되어진 함수
#   - import가 필요한 함수 :   time,request, matplotlib.....
#   - import가 필요 없는 함수 : builtin 함수(len, print ... )

#파이썬에 내장되어있는 함수가 모여있는 builtins 모듈을 확인하는 코드
#print(dir(__builtins__))
#dir() : 작성한 값이 어떤 변수와 함수(메소드)를 가지고 있는지 나열하는 기능을 가진 함수
#help() : ()안에 작성한 함수에 대한 설명이 출력되는 함수
#help(list)


#이번 파트에서 진행할 과정은 위에 있는 내장 함수가 아닌 사용자가 직접 만드는 사용자 정의 함수에 대한 내용입니다.
'''
def 함수명(매개변수) :
    함수 호출 시 실행할 명령문
    특정 값을 내보낼 경우 return문을 작성합니다.
'''

#매개변수(paramater) : 함수 호출 시 입력할 값에 대한 표현, 따로 정의되는 값이 아닌 표현하기 위한 것
#                     받아온 인자의 값을 복사합니다.

#인자(Argument) : 함수 호출 시 입력할 값 그 자체

#다음은 문장을 넣으면 그 문장이 출력되는 함수 MyPrint(String)을 만들어보겠습니다.

#함수 영역 : 함수를 만들 위치
def MyPrint(String) :
    print(String)

def MyPlus(Number,Number2) :
    Number += Number2
       
def MyPlus2(Number,Number2) :
    return Number + Number2
#분기문 return은 앞에 값을 작성하면 해당 함수를 종료하고 그 값을 반환합니다.
# >> 값 전달 용으로 사용합니다.
#분기문 return 앞에 값을 안적을 경우 함수 종료만 진행됩니다. 

#메인 영역 : 함수를 사용할 위치
MyPrint("솔의 눈")
print(MyPlus(10,5))#함수 실행 후 함수에서 사용한 값들은 다 사라집니다.(데이터 구조 상 스택 영역에 존재합니다.)
print(MyPlus2(10,5))#함수 실행 후 값들은 사라지지만 return에 의해 함수를 종료한 후 값을 밖으로 내보냈기 때문에 사용 가능


함수 사용 목적

1. 기능을 따로 함수 영역에 만들어줌으로써, 프로그램 전체에서 사용될 공통적인
작업을 재사용할 수 있어서 불필요한 중복 작업을 피할 수 있습니다.

2. 메인에 직접 구현하지 않고 함수를 따로 만들면서 얻는 이득은 특정 기능이 잘못
됬을 때, 함수에 대한 수정을 진행하는 것으로 고칠 수 있어 효율적입니다.

3. 함수 영역 / 메인 영역으로 나눠서 작업을 진행하기 때문에 프로그램의 전체 구성
파악이 더 쉬워집니다.








