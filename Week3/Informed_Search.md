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
> > 
