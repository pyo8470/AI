## 게임의 타입
> ### 결정론적, 확률적
> ### 플레이어의 숫자
> ### Zero Sum
> > - 한 플레이어가 점수를 획득을 하면, 그만큼 다른 플레이어는 점수를 잃음
> ### Perfect information
> > - 게임의 모든 상황에 대해서 가치에 대한 판단이 가능한 상황

## 결정론적 게임
> ### 많은 정규식
> # ![image](https://user-images.githubusercontent.com/84065357/192198666-4b954fb1-c044-4fbf-ac88-fe351d4fe7a8.png)
> > - State
> > - Players
> > - Actions (플레이어와 상태에 의존)
> > - Transition Function
> > - Terminal Test
> > - terminal Utilities
> ### Play어에 대한 Solution = Policy

## Zero-sum game
> - Agents들이 서로 적임(서로 정반대의 utilities)
> - Adversarial, pure Competition
## General games
> - Agents들이 서로 독립적인 Utilities
> - 협력, 무관심,경쟁 등의 형태로 조내 가능함

## Single-agent trees
> ### 트리로 표현 가능
> # ![image](https://user-images.githubusercontent.com/84065357/192199075-41191a4d-7472-421b-b4c4-45af36c51e18.png)
> > - 각 노드 = State
> > - 게임이 종료시 더이상의 Subtree 전개는 없음
> ## Value of a state
> > - state로부터 가장 좋은 outcome(utility)

## Adversarial games
> ### ![image](https://user-images.githubusercontent.com/84065357/192199430-249f2f2c-5778-4155-b15d-8da09f0b6456.png)
> > - 두 개의 플레이어인 경우
> ## Minimax Values
> > # ![image](https://user-images.githubusercontent.com/84065357/192199808-31fb0381-0dd5-4f79-9cae-d8d01a22c29b.png)
> > - 나는 내가 가장 좋은것, 상대방은 내가 가장 나쁜 State를 고른다.
> ## Tic-tac-toe game Tree
> > # ![image](https://user-images.githubusercontent.com/84065357/192199922-607ea273-c8ae-45b2-a107-71a4d8b21a30.png)
> > > - 같은 기호가 일렬로 서면 승리
> > - 계속 노드들을 확장해 나간다, 이 예시는 모든 경우를 탐색하는 경우이다.
> ## Adversarial Search(minimax)
> # ![image](https://user-images.githubusercontent.com/84065357/192200359-442ecb3d-bdde-42e3-aba9-8ead1cb658d0.png)
> > ### 결정론적, Zero-sum game에서 사용 가능
> > > - 틱택토,체스,체커
> > ### Minimax Search
> > > - 상태 공간트리 존재
> > > - 플레이어가 서로 교대하며 수를 둔다
> > > - 각각의 노드의 minimax value를 계산
> > > > - 적에겐 최악의 나에겐 최선의 값을 도출함.
> > > ### 구현
> > > # ![image](https://user-images.githubusercontent.com/84065357/192200615-d750bde5-d4f6-4901-8509-753264335cf8.png)
> > > > - 재귀적 호출
> > > # ![image](https://user-images.githubusercontent.com/84065357/192200684-03b7a294-e946-4992-b91b-1a7bcf7f49b4.png)
> > > > - Max,Min,종료 여부를 구분

## Minimax Example
> # ![image](https://user-images.githubusercontent.com/84065357/192200973-00a12107-d0b7-46bc-bc2c-cddb79d1d019.png)
> > - 삼각형이 아래 -> Min 노드
> > - 삼각형이 위 -> Max 노드
> ## Minimax Properties
> > # ![image](https://user-images.githubusercontent.com/84065357/192201132-f8768e2d-671c-4ae6-bc0e-617755c15780.png)
> ## Minimax의 효율성
> > - DFS(전부 다보는)
> > - time : O(b^m) Space : O(bm)
> > ### 체스에 관해 b=35 m=100
> > > - 전체 트리를 돌려면 계산이 현실적으로 불가능함
> ## Minimax Pruning(가지치기)
> > # ![image](https://user-images.githubusercontent.com/84065357/192201578-af2fd2bf-10e6-4148-b41e-a22bd7f7c47e.png)
> > > - 탐색할 필요가 없는 영역을 탐색 영역에서 삭제한다.

## Alpha-Beta Pruning
> ## General Configuration (MIN Version)
> > - n번째 노드에서 최소값을 계산한다
> > - n번째 노드의 자식노드에서 loop 한다
> > - n번째 노드의 자식노드의 MIN값은 점점 감소한다
> > - n번쨰 노드의 value는 MAX가 선택할지 말지 고른다
> > - MAX가 root로부터의 현재 path를 통한 모든 선택에서 얻을수 있는 값을 a라고 가정함
> > - N이 a보다 좋지 않아진다면, MAX는 n을 고르지 않을 것이고, n의 다른 자식 노드를 고려할 필요가 사라진다.
> ### MAX에 대해서도 그냥 서로 값만 바꾸면 가능.
> # ![image](https://user-images.githubusercontent.com/84065357/192202454-d4e6a01c-94b5-447e-9097-7e1384c5d158.png)
> ## 특징
> > 
