#첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어진다. 이 값은 0보다 크거나 같고 10보다 작거나 같은 정수이다.

#체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

KING = 1
QUEEN = 1
ROOKS = 2
BISHOPS = 2
KNIGHTS = 2
PAWNS = 8

king, queen, rooks, bishops, knights, pawns = input().split()

print("%d %d %d %d %d %d" % (KING - int(king), QUEEN - int(queen), ROOKS - int(rooks), BISHOPS - int(bishops), KNIGHTS - int(knights), PAWNS - int(pawns)))