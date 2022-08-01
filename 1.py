def solution(numbers, hand):
    answer = ''
    lastL = 10  # '*의 위치를 10으로 임의 지정'
    lastR = 12  # '#의 위치를 12으로 임의 지정'

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lastL = n
        elif n in [3, 6, 9]:
            answer += 'R'
            lastR = n
        else:
            n = 11 if n == 0 else n  # n==0일 때 11로 값 임의 지정, 나머지는 모두 n으로 설정

            absL = abs(n - lastL)  # 절댓값 함수
            absR = abs(n - lastR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):  # 첫 번째 인수를 2번째 인수로 나눈 값의 몫과 나머지를 합한다.
                print((divmod(absL, 3)))
                print(sum(divmod(absL, 3)))
                answer += 'R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = n
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = n
                else:
                    answer += 'R'
                    lastR = n

    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
print(solution(numbers, hand))