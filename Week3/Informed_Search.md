## 복기 : Search
> ### Search problem
> > - State (~의 세상의 특징)
> > - Actions and Cost
> > - Successor function
> > - Start state and goal test
> ### Search tree
> > - Nodes: State에 도달하는 plan을 표시
> > - Plan은 cost를 가지고 있다(action cost의 합)
> ### Search Algorithm
> > - 체계적으로 탐색트리를 설계
> > - fringe의 순서를 고른다(탐색되지 않은 노드중)
> > - OPTIMAL : Least-Cost Plan을 찾는 것.

## The one queue
> ### 이 모든 검색 알고리즘은 프린지 전략을 제외하고 동일합니다.
> - 개념적으로 모든 프린지는 우선 순위 대기열(즉, 우선 순위가 연결된 노드의 집합)입니다.
> - 실제로 DFS 및 BFS의 경우 스택 및 대기열을 사용하여 실제 우선 순위 대기열에서 로그(n) 오버헤드를 방지할 수 있습니다.
> - 가변 큐잉 개체를 사용하는 하나의 구현을 코딩할 수도 있습니다.

## Uninformed search : Uniform cost search
> ### 최악의 경우
> > - 모든 방향으로 탐색을 시작한다.
> > # ![image](https://user-images.githubusercontent.com/84065357/190975473-6ea96902-93f8-409e-bed9-1a61a51da214.png)
## Informed Search : Search heuristics
> ### Heuristic
> > - state가 goal에 얼마나 가까운지 평가하는 FUCNTION
> > - 특정 탐색 문제를 위해 Designed(맨해튼 거리, 유클리드 거리 등)
> > ## 예시
> > > ### 여전히 제자리에 있지 않은 가장 큰 팬케이크의 수 
> > > # ![image](https://user-images.githubusercontent.com/84065357/190976962-e0a2123e-f5be-4628-b0b3-037404f6f743.png)
> ## Greedy Search
> > # ![image](https://user-images.githubusercontent.com/84065357/190977966-4d720eb4-7dc2-44fc-b28b-90db88a2b49c.png)
> > # ![image](https://user-images.githubusercontent.com/84065357/190978015-be9a0403-7fe0-4f98-8ce1-84d7d164eef8.png)
## A\* Search
> ### UCS와 GREEDY를 결합
> # ![image](https://user-images.githubusercontent.com/84065357/190978688-d2ed5c4b-8f1c-464d-bdef-76c9e51b87b7.png)
> > - g(n) : path cost
> > - h(n) : 목표 예상 cost(임의로 정한다.)
> > - f(n)을 기준으로 선택한다 (F=g+h)
> ### A\* Search가 종료되어야 할 때
> > # ![image](https://user-images.githubusercontent.com/84065357/190979386-99726935-e511-4cd9-b576-fb219b312c20.png)
> > - B를 먼저 선택해서 최적해가 나오지 않는 경우가 있다
> > > - 따라서 G가 QUEUE에서 빠져 나왔을 때 탐색을 멈춰야 한다.
> ### A\* Seacch가 Optimal한가?
> > # ![image](https://user-images.githubusercontent.com/84065357/190979907-73d27352-f97d-42e2-8cb4-d982e693783e.png)
> > - 골 까지의 에측치인 h가 너무 높은 경우
> > - h값을 선택할 때 잘 선택해야함
> ## Admissibilty
> > - 수용 불가능한 heuristic값은 좋지 않은 값이 먼저 선택 될 가능성이 있게함.
> > - 적절한 h값을 정하려면  예상 도달치 >= 실제 bad goal
> > > # ![image](https://user-images.githubusercontent.com/84065357/191429253-3f8079d3-060a-48e4-9728-df69d0b502a9.png)
> ## Optimality of A\* tree Search
> > - A는 최적해, B는 두 번째로 최적한 해, h는 admissible
> > - 요구조건 : A가 B보다 fringe에서 먼저 튀어나와야한다.(즉 확장을 먼저 해야함 = f(A)<f(B), 부모 노드인 n의 f(n) <=f(A))
> > # ![image](https://user-images.githubusercontent.com/84065357/191430264-2c0defc3-462a-46d7-8a4e-6d63d3fa2126.png)
> > > - B가 fringe에 들어와 있다고 가정
> > > ### 1. f(n) <= f(A)
> > > > - = g(n)+h(n) <= g(A) + h(A)(=0)
> > > > - = f(n) <= g(A)
> > > ### 2. f(A) < f(B)
> > > > - = g(A) < g(B)
> > > ### 3. n이 B이전에 확장한다
> > > > - = f(n) <= f(A) <f(B)
> > > > - f값에 따라서 확장 순서를 정하기 때문이다
> > > ### 이 모든 조건을 만족한다면 A\*는 Optimal하다.
> ## UCS VS A\*
> ## ![image](https://user-images.githubusercontent.com/84065357/191432126-6b39d301-964e-42fe-9a2d-188514e8c8d6.png)
> > - A\* 탐색에서 적절한 h 값을 설정한다면 탐색 범위를 줄일 수 있다.
> > - H값을 이용해 방향성을 좀 더 명확하게 함.
> ## Creating admissible heuristics
> > # ![image](https://user-images.githubusercontent.com/84065357/191432872-95a24903-7001-4433-ad60-ce987bc0e8a6.png)
> > > - 직선거리, 벽 뚫 
> > - 주어진 문제의 제약 조건을 좀 완화(조건을 안 지키더라도)하여 만든다.
> > - Inadmissible heuristics이 항상 좋지 않은 것은 아니다.

## Example : 8 Puzzle
> # ![image](https://user-images.githubusercontent.com/84065357/191433156-55e37737-8531-4f9b-90e8-17a5c6c8b44f.png)
> > - state : 숫자들의 배열
> > - action : 숫자를 움직임
> ### Heuristics
> > ## 1.
> > # ![image](https://user-images.githubusercontent.com/84065357/191433976-f762b558-19c5-4a2c-b9af-131fe094b0e7.png)
> > > - 좌우위아래로만 타일이 움직이는게 아니라, 자유롭다고 가정(relaxed-problem heuristic)
> > > - h(start) = 8 
> > ## 2
> > # ![image](https://user-images.githubusercontent.com/84065357/191434239-d12f878d-722d-43e3-a4c5-7830a2f3d8a0.png)
> > > - 맨해튼 거리 사용
> > > - 좀더 현실에 가까운 h값이 나온다 -> 탐색횟수 감소
> > > - h(start) = 18
> > ## 3
> > > - 실제 값을 h값으로 사용한다면 어떨까?
> > > - admissible? : 0 < actual == h\*(n) 이기 때문
> > > - 확장된 노드를 저장할 수 있는가? : 할 수는 있겠지만 노드당 
> > A\*를 사용하는 경우: 예상 품질과 노드당 작업 간 균형
> > - 휴리스틱이 트리 비용에 가까워질수록 노드 수는 줄어들지만 일반적으로 휴리스틱 자체를 계산하기 위해 노드당 더 많은 작업을 함
