## Designing rational agents
> ### Agent
> > - 지각하고 행동하는 개체
> ### Rational agent
> > - 기대 효용성을 최대화시키는 행동을 선택하는 agent
> - 지각,환경,행동공간의 특성은 rational action을 선택하기 위한 기술을 명령한다
> # ![image](https://user-images.githubusercontent.com/84065357/190072684-2feefb28-9e8c-4182-94a6-8855fbef2f2b.png)

## Reflex agents(반응적)
> - "현재"의 percept(나 메모리)를 기반으로 행동을 선택
> - 현재 상태의 모델이나, 메모리를 가진다
> - 행동의 미래 결과에 대해 고려하지 않음
> - 지금 상태가 어떤지만 고려한다.
> #### 즉, 현재만 고려한다
> #### rational한가?
> > - 항상 그렇지 않을 수 있다

## Planning agents(계획)
> - 현재 상태만을 근거로 행동하지 않고, 미래의 상태도 고려함
> - 행동의 결과에 대한 변화의 모습을 반드시 보유하고 있어야함.
> - 목표를 반드시 만들어내야함(그 목표가 진짜 goal인지도 확인해야함)

## Search problems
> # ![image](https://user-images.githubusercontent.com/84065357/190074383-5206b6e9-7852-4110-afd2-0897e3024f52.png)
> - Soultion은 시작 상태로부터 목표 상태로 변하는 모든 행동(plan) 시퀀스
> ## 예제 ![image](https://user-images.githubusercontent.com/84065357/190074674-276a6a62-57b4-47f2-be7a-1afdb0edda76.png)
> ## 상태트리에 포함되어야 하는 것.
> > # ![image](https://user-images.githubusercontent.com/84065357/190075431-f89e6a3a-4b49-4249-b730-b37140985aea.png)
> > - World state : 모든 detail
> > - Search state : planning을 위해 필요한 detail들만
> ## State space graph
> > ### 탐색문제의 수학적 표현
> > > - Node들은 world 구성요소
> > > - 화살표는 successor(행동 결과)를 나타냄
> > > - goal test는 goal nodes의 집합(하나 이상)
> > - 각각의 상태들은 한번만 발생함
> > - 메모리에 모든 graph를 저장하기 힘들지만(너무 용량이 큼), 좋은 아이디어
> ## Search tree
> # ![image](https://user-images.githubusercontent.com/84065357/190076804-506144ec-85bf-4983-9aeb-faa94de3ce6f.png)
> > - 자식 노드 == successor
> > - 노드들은 state를 보여준다, 하지만 그 상태를 만족시키는 PLANS에 한해서만
> > - 전체 tree를 만드는 경우는 없다.
## Search Algorithm
> ### DFS
> > - LIFO 스택 이용, 높은 차수의 노드부터 탐색
> > - expansion 하는 노드는 스택에서 제외
> > - 즉,스택에서 가장 높은 곳에 있는 노드부터 확장(확장 tree의 root는 지워줌)
> ### BFS
> > - FIFO QUEUE 이용, 낮은 차수의 노드부터 탐색
